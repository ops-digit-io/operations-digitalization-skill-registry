"""
dashboard_builder.py — helpers for generating Grafana 8.5 (schema 36) panel JSON.

Designed for PostgreSQL/TimescaleDB datasources, the bilibala-echarts-panel plugin,
and operations dashboards. Supports both relational and timeseries archetypes —
the panel helpers don't care which one your SQL uses.

Conventions:
- panel_id is caller-controlled (use a counter, increment manually)
- gridPos uses a 24-column grid; standard heights: stat=4, table=7-12, echarts=10-14
- datasource UID is referenced as ${DS_NAME} — adapt the placeholder if needed

Quick start:

    from dashboard_builder import (
        stat, table_panel, echarts, timeseries, row, text,
        traffic_light, gradient_gauge_override, color_cell_override,
        var_query, var_custom, var_textbox, var_uuid_signal,
        build_dashboard,
    )

    panels = []; pid = 100
    panels.append(row(pid, "🎯 KPIs", 0)); pid += 1
    panels.append(stat(pid, "Total downtime", 0, 1, 4, 4, sql, unit="m",
                       thresholds=traffic_light(yellow=20, red=50))); pid += 1

    dashboard = build_dashboard("My Dashboard", panels, variables=[...])
    json.dump(dashboard, open("out.json","w"), indent=2)
"""

import json

# --- Datasource reference. Adapt to user's UID/placeholder. ---
DS = {"type": "postgres", "uid": "${DS_NAME}"}


# =============================================================================
# Threshold helpers
# =============================================================================

def traffic_light(yellow=None, red=None, base="green"):
    """Build threshold steps for traffic-light Stat coloring (low=green, high=red).

    >>> traffic_light(yellow=20, red=50)
    {'mode': 'absolute', 'steps': [
        {'color': 'green', 'value': None},
        {'color': 'yellow', 'value': 20},
        {'color': 'red', 'value': 50}]}
    """
    steps = [{"color": base, "value": None}]
    if yellow is not None:
        steps.append({"color": "yellow", "value": yellow})
    if red is not None:
        steps.append({"color": "red", "value": red})
    return {"mode": "absolute", "steps": steps}


def reverse_traffic_light(yellow=None, green=None):
    """Inverted thresholds — red below, green above. For "higher is better" metrics
    like uptime %, OEE, OK rate."""
    steps = [{"color": "red", "value": None}]
    if yellow is not None:
        steps.append({"color": "yellow", "value": yellow})
    if green is not None:
        steps.append({"color": "green", "value": green})
    return {"mode": "absolute", "steps": steps}


def diverging_thresholds(red_below=0, yellow_below=0.01, green_above=None):
    """Diverging palette for delta columns — green if better, red if worse."""
    steps = [{"color": "green", "value": None}]
    if yellow_below is not None:
        steps.append({"color": "yellow", "value": yellow_below})
    if green_above is not None:
        steps.append({"color": "red", "value": green_above})
    else:
        steps.append({"color": "red", "value": 1})
    return {"mode": "absolute", "steps": steps}


# =============================================================================
# Target builder. Used by every panel helper.
# =============================================================================

def _target(sql, fmt="table"):
    return {
        "datasource": DS,
        "format": fmt,
        "group": [], "metricColumn": "none",
        "rawQuery": True, "rawSql": sql, "refId": "A",
        "select": [[{"params": ["value"], "type": "column"}]],
        "timeColumn": "time", "timeColumnType": "timestamptz",
        "where": [{"name": "$__timeFilter", "params": [], "type": "macro"}],
    }


# =============================================================================
# Stat panel
# =============================================================================

def stat(panel_id, title, x, y, w, h, sql, *, unit="m", description="",
         thresholds=None, color_mode="value", text_mode="value_and_name",
         graph_mode="none"):
    """Single-value stat panel with optional threshold-based coloring.

    Set graph_mode='area' for a sparkline (analyst tier),
    'none' for a flat number (manager tier).
    """
    if thresholds is None:
        thresholds = {"mode": "absolute", "steps": [{"color": "text", "value": None}]}
    return {
        "datasource": DS,
        "description": description,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "thresholds": thresholds,
                "unit": unit,
            },
            "overrides": [],
        },
        "gridPos": {"h": h, "w": w, "x": x, "y": y},
        "id": panel_id,
        "options": {
            "colorMode": color_mode,
            "graphMode": graph_mode,
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": text_mode,
        },
        "pluginVersion": "8.5.22",
        "targets": [_target(sql, fmt="table")],
        "title": title,
        "type": "stat",
    }


# =============================================================================
# Table panel
# =============================================================================

def table_panel(panel_id, title, x, y, w, h, sql, *, overrides=None, description=""):
    """Standard Grafana table panel. Use width_override(), unit_override(),
    color_cell_override(), gradient_gauge_override() to build the overrides list.
    """
    return {
        "datasource": DS,
        "description": description,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {"align": "auto", "displayMode": "auto", "inspect": False},
                "mappings": [],
                "thresholds": {"mode": "absolute", "steps": [{"color": "text", "value": None}]},
                "unit": "none",
            },
            "overrides": overrides or [],
        },
        "gridPos": {"h": h, "w": w, "x": x, "y": y},
        "id": panel_id,
        "options": {
            "footer": {"fields": "", "reducer": ["sum"], "show": False},
            "showHeader": True,
            "sortBy": [],
        },
        "pluginVersion": "8.5.22",
        "targets": [_target(sql, fmt="table")],
        "title": title,
        "type": "table",
    }


# Override helpers — table cell formatting

def width_override(column, width):
    return {"matcher": {"id": "byName", "options": column},
            "properties": [{"id": "custom.width", "value": width}]}


def unit_override(column, unit):
    return {"matcher": {"id": "byName", "options": column},
            "properties": [{"id": "unit", "value": unit}]}


def color_cell_override(column, thresholds, *, unit=None, width=None):
    """Color the entire cell background based on value thresholds. Good for delta columns."""
    props = [
        {"id": "custom.displayMode", "value": "color-background"},
        {"id": "thresholds", "value": thresholds},
    ]
    if unit:  props.append({"id": "unit", "value": unit})
    if width: props.append({"id": "custom.width", "value": width})
    return {"matcher": {"id": "byName", "options": column}, "properties": props}


def gradient_gauge_override(column, *, unit=None, width=None,
                            color_mode="continuous-BlYlRd"):
    """Render the column as a horizontal gradient gauge — good for ranking columns."""
    props = [
        {"id": "custom.displayMode", "value": "gradient-gauge"},
        {"id": "color", "value": {"mode": color_mode}},
    ]
    if unit:  props.append({"id": "unit", "value": unit})
    if width: props.append({"id": "custom.width", "value": width})
    return {"matcher": {"id": "byName", "options": column}, "properties": props}


# =============================================================================
# Time series panel
# =============================================================================

def timeseries(panel_id, title, x, y, w, h, sql, *, unit="m", description="",
               draw_style="bars", stack=True, fill_opacity=70, show_legend=True):
    """Standard time series panel. SQL must return columns: time, metric, value.
    Format is set to time_series automatically.
    """
    return {
        "datasource": DS,
        "description": description,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "axisCenteredZero": False, "axisColorMode": "text", "axisLabel": "",
                    "axisPlacement": "auto", "barAlignment": 0,
                    "drawStyle": draw_style,
                    "fillOpacity": fill_opacity,
                    "gradientMode": "none",
                    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                    "lineInterpolation": "linear", "lineWidth": 1, "pointSize": 5,
                    "scaleDistribution": {"type": "linear"},
                    "showPoints": "never", "spanNulls": False,
                    "stacking": {"group": "A", "mode": "normal" if stack else "none"},
                    "thresholdsStyle": {"mode": "off"},
                },
                "mappings": [],
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": None}]},
                "unit": unit,
            },
            "overrides": [],
        },
        "gridPos": {"h": h, "w": w, "x": x, "y": y},
        "id": panel_id,
        "options": {
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom",
                       "showLegend": show_legend},
            "tooltip": {"mode": "multi", "sort": "desc"},
        },
        "pluginVersion": "8.5.22",
        "targets": [_target(sql, fmt="time_series")],
        "title": title,
        "type": "timeseries",
    }


# =============================================================================
# ECharts panel (bilibala plugin)
# =============================================================================

def echarts(panel_id, title, x, y, w, h, sql, get_option_js, *, description=""):
    """ECharts panel via the bilibala-echarts-panel plugin.

    SQL must use format=table and return columns whose names the JS reads by name.
    See references/echarts_templates.js for ready-to-use getOption JS.
    """
    return {
        "datasource": DS,
        "description": description,
        "gridPos": {"h": h, "w": w, "x": x, "y": y},
        "id": panel_id,
        "options": {"followTheme": False, "getOption": get_option_js},
        "pluginVersion": "8.5.22",
        "targets": [_target(sql, fmt="table")],
        "title": title,
        "type": "bilibala-echarts-panel",
    }


# =============================================================================
# Text and row panels
# =============================================================================

def text(panel_id, title, x, y, w, h, content, *, mode="markdown", transparent=True):
    """Markdown text panel — for "how to read this dashboard" guidance."""
    return {
        "datasource": None,
        "gridPos": {"h": h, "w": w, "x": x, "y": y},
        "id": panel_id,
        "options": {"content": content, "mode": mode},
        "pluginVersion": "8.5.22",
        "title": title,
        "type": "text",
        "transparent": transparent,
    }


def row(panel_id, title, y, *, collapsed=False):
    """Section divider. Always full-width, height 1."""
    return {
        "collapsed": collapsed,
        "datasource": None,
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": y},
        "id": panel_id,
        "panels": [],
        "title": title,
        "type": "row",
    }


# =============================================================================
# Variable builders — generic factories. Compose your own variable set.
# =============================================================================

def var_query(name, label, sql, *, multi=True, include_all=True, sort=5,
              description=""):
    """SQL-driven dashboard variable. SQL must return columns named __text and __value.

    Example for a relational entity dropdown:
        var_query("machine", "MACHINE",
                  "SELECT name AS __text, id AS __value FROM machines "
                  "WHERE is_ignored = false ORDER BY name;")
    """
    return {
        "current": {}, "datasource": DS,
        "definition": sql,
        "description": description,
        "hide": 0, "includeAll": include_all,
        "label": label, "multi": multi, "name": name,
        "options": [],
        "query": sql,
        "refresh": 1, "regex": "", "skipUrlSync": False,
        "sort": sort, "type": "query",
    }


def var_uuid_signal(name, label, *, signal_table="signal_metadata",
                    name_col="name", uuid_col="uuid", where_clause="",
                    description=""):
    """Variable for a single UUID-keyed signal (timeseries archetype).

    The variable returns name → uuid mapping. In SQL, use:
        uuid = (${signal_var:raw})
    The :raw modifier prevents Grafana from quoting the UUID as a string.

    Example:
        var_uuid_signal("speed_signal", "SPEED SIGNAL",
                        signal_table="tags",
                        where_clause="AND tag_type = 'speed'")
    """
    sql = (f"SELECT {name_col} AS __text, {uuid_col} AS __value\n"
           f"FROM {signal_table}\n"
           f"WHERE 1=1\n"
           f"  {where_clause}\n"
           f"ORDER BY {name_col};")
    return {
        "current": {}, "datasource": DS,
        "definition": sql,
        "description": description or
            f"UUID for the {label} signal. Use as: uuid = (${{{name}:raw}})",
        "hide": 0, "includeAll": False,
        "label": label, "multi": False, "name": name,
        "options": [],
        "query": sql,
        "refresh": 1, "regex": "", "skipUrlSync": False,
        "sort": 5, "type": "query",
    }


def var_custom(name, label, options, *, default=None, multi=False):
    """Custom (hardcoded) variable. options is list of (text, value) tuples or strings.

    Examples:
        var_custom("severity", "SEVERITY",
                   [("all","all"), ("info","info"), ("warning","warning"), ("critical","critical")],
                   default="all")
        var_custom("auto_detected", "AUTO DETECTED",
                   [("all","-1"), ("manual","0"), ("auto","1")], default="all")
        var_custom("bucket", "BUCKET",
                   [("1m","1m"), ("5m","5m"), ("15m","15m"), ("1h","1h")], default="5m")
    """
    # Normalize options — accept either strings or (text, value) tuples
    norm = []
    for o in options:
        if isinstance(o, str):
            norm.append((o, o))
        else:
            norm.append((o[0], str(o[1])))
    if default is None:
        default = norm[0][0]
    opts = [{"selected": (text == default), "text": text, "value": value}
            for text, value in norm]
    selected = next(o for o in opts if o["selected"])
    return {
        "current": {"selected": True, "text": selected["text"], "value": selected["value"]},
        "hide": 0, "includeAll": False,
        "label": label, "multi": multi, "name": name,
        "options": opts,
        "query": ", ".join(f"{t} : {v}" if v != t else t for t, v in norm),
        "queryValue": "", "skipUrlSync": False, "type": "custom",
    }


def var_textbox(name, label, default="0"):
    """Free-text input variable — typically for numeric thresholds."""
    return {
        "current": {"selected": False, "text": default, "value": default},
        "hide": 0, "label": label, "name": name,
        "options": [{"selected": True, "text": default, "value": default}],
        "query": default, "skipUrlSync": False, "type": "textbox",
    }


def var_interval(name, label, options=None, *, default="5m"):
    """Time-bucket interval variable — for $__timeGroup (the portable choice; never use time_bucket in dashboard SQL)."""
    if options is None:
        options = ["1m", "5m", "15m", "1h", "6h", "12h", "1d"]
    opts = [{"selected": (o == default), "text": o, "value": o} for o in options]
    return {
        "auto": False, "auto_count": 30, "auto_min": "10s",
        "current": {"selected": True, "text": default, "value": default},
        "hide": 0, "label": label, "name": name,
        "options": opts,
        "query": ",".join(options),
        "queryValue": "", "refresh": 2,
        "skipUrlSync": False, "type": "interval",
    }


# =============================================================================
# Dashboard wrapper
# =============================================================================

def build_dashboard(title, panels, variables, *, refresh="30s",
                    time_from="now-7d", time_to="now",
                    hide_timepicker=False, tags=None,
                    ds_input_name="DS_NAME", ds_input_label="Data Source"):
    """Wrap panels and variables into a complete importable Grafana dashboard."""
    return {
        "__inputs": [{
            "name": ds_input_name, "label": ds_input_label,
            "description": "", "type": "datasource",
            "pluginId": "postgres", "pluginName": "PostgreSQL",
        }],
        "__elements": [],
        "__requires": [
            {"type": "panel", "id": "bilibala-echarts-panel",
             "name": "Echarts", "version": "2.2.4"},
            {"type": "grafana", "id": "grafana", "name": "Grafana", "version": "8.5.22"},
            {"type": "datasource", "id": "postgres", "name": "PostgreSQL", "version": "1.0.0"},
            {"type": "panel", "id": "stat", "name": "Stat", "version": ""},
            {"type": "panel", "id": "table", "name": "Table", "version": ""},
            {"type": "panel", "id": "timeseries", "name": "Time series", "version": ""},
            {"type": "panel", "id": "text", "name": "Text", "version": ""},
        ],
        "annotations": {"list": [{
            "builtIn": 1,
            "datasource": {"type": "grafana", "uid": "-- Grafana --"},
            "enable": True, "hide": True,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "target": {"limit": 100, "matchAny": False, "tags": [], "type": "dashboard"},
            "type": "dashboard",
        }]},
        "editable": True, "fiscalYearStartMonth": 0, "graphTooltip": 0, "id": None,
        "iteration": 1, "links": [], "liveNow": False,
        "panels": panels,
        "refresh": refresh,
        "schemaVersion": 36, "style": "dark",
        "tags": tags or ["operations"],
        "templating": {"list": variables},
        "time": {"from": time_from, "to": time_to},
        "timepicker": {"hidden": True} if hide_timepicker else {},
        "timezone": "", "title": title, "uid": None, "version": 1, "weekStart": "",
    }


# =============================================================================
# Audit helper — verify variables are wired correctly
# =============================================================================

def audit_panels(panels, expected_vars):
    """Print a report of which panels reference which variables.
    Use before delivering — every defined variable should appear in every panel
    where it is logically relevant.
    """
    import re
    print(f"{'Title':<55} " + " ".join(f"{v[:6]:<7}" for v in expected_vars))
    for p in panels:
        if p.get("type") in ("row", "text"):
            continue
        targets = p.get("targets") or [{}]
        sql = targets[0].get("rawSql", "")
        flags = ["Y" if re.search(r"\$\{?" + v + r"(?![\w])", sql) else "·"
                 for v in expected_vars]
        print(f"{p['title'][:54]:<55} " + " ".join(f"{f:<7}" for f in flags))
