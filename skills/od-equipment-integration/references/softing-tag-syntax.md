---
type: Skill Reference
title: Softing tag syntax
description: The identifier written when a tag is defined by hand, per driver family, and what a symbol import produces instead.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [integration, softing, tags]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Softing dataFEED — datapoint (tag) syntax

The identifier you type when defining a tag manually, and what a symbol import produces.
From the **dataFEED OPC Suite V5.70** manual, ch. 9.1.16.5 (p. 657–683), in the bundle at
`_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf`.

Get this right and a symbol import is a formality. Get it wrong and you have a tag that
reads a plausible-looking wrong address, which nothing will flag.

---

## Siemens S7

```text
[Group.]<Area><Data type><Start address>[.Array size][Suffix]
```

For a boolean, a bit number is mandatory:

```text
[Group.]<Area><Data type><Start address><.Bit no.>[.Array size][Suffix]
```

`<>` mandatory · `[]` optional.

### Areas

| Area | Syntax | Orientation | Access |
|---|---|---|---|
| Data block | `DBx.` (`V` is a synonym for `DB1`) | byte | read / write |
| Instance block | `DIx.` | byte | read / write |
| Flag | `M` or `F` | byte | read / write |
| Timer | `T` | word | **read only** |
| Counter | `Z` or `C` | word | read / write |
| Input | `E` or `I` | byte | **read only** |
| Output | `A` or `O` or `Q` | byte | read / write |
| I/O input | `PE` or `PI` | byte | **read only** |
| I/O output | `PA` or `PO` or `PQ` | byte | read / write |

Blocks need a block number **x = 1 to 65535**, and **a dot or a comma must follow it**.
That is why the OESL example `DB15,INT1032` is valid — comma after the block number, `INT`
data type, start address `1032`.

*Byte-oriented* means one byte is addressed per physical address; *word-oriented* means
16 bits.

### Examples

| Identifier | Reads |
|---|---|
| `DB5.X4.3` | DB5, bit 3 of byte 4 |
| `MX1.3` | Flag byte 1, bit 3 |
| `DB15,INT1032` | DB15, integer at 1032 |
| `DB10.DW3.4` | DB10, four consecutive double-words from DW3 (array) |

### Arrays

Append the length after a dot: `DB10.DW3.4`.

**Arrays are not possible for** `BOOL`, `DATE AND TIME`, `DATE`, `TIME`, `TIME OF DAY`,
`STRING` (already a character array), and for any suffix that presents as string or bool to
the client: `BA`, `KA`, `S5T`, `KT`, `D`, `T`, `DT`, `DU`, `TOD`.

### Bit masking

Read or write several bits of a data type as one decimal value. Arrays can be masked too.

```text
db5.w0#2.8      8 bits of word 0 in DB5, starting at bit 2
db5.w0#2#8      equivalent
```

**Does not work with** left/right byte (`DL`, `DR`) or the `BA` suffix. **Do not mask** bits
of `REAL` or `KG`.

### Strings — S5 vs S7

The syntax is identical (`DBxSy.z`), but the encodings differ: **an S7 string carries its
length in the first two bytes; an S5 string carries no length information.** By default a
string is interpreted per the access path (S5 path → S5 string, S7 path → S7 string), and a
global setting can force every string to be read as S5. A string that comes back with two
leading junk characters — or truncated by two — is this setting.

---

## Modbus

```text
[UnitID.][Group.]<Area><Data type><Start address>[.Bit number][.Array size][Suffix]
```

The `[UnitID.]` prefix applies only when the connection uses *UnitID individual with item
syntax*.

### Areas

| Area | Syntax | Numeric | Orientation | Access |
|---|---|---|---|---|
| Discrete inputs | `I` `E` `DI` `DE` | `1xxxxx` | bit | read |
| Discrete outputs | `A` `O` `Q` `DA` `DO` `DQ` | `0xxxxx` | bit | read / write |
| Input register | `ER` `IR` | `3xxxxx` | word | read |
| Holding register | `R` `HR` | `4xxxxx` | word | read / write |
| Discrete inputs, octal | `J` | — | bit | read |
| Discrete outputs, octal | `P` | — | bit | read / write |

Areas can be addressed either by the letter form or by the leading digit — a discrete input
is `E` or `1`. The OESL example `HR300` is a holding register at 300.

### Group and UnitID prefixes

**Group** — combines operand areas. `G` + number, range **0–65535** (reduced to **0–255**
when *UnitID individual with item syntax* is on). Prefixed with a dot:
`G1.40001` · `G2.R2` · `G3.S20.30`.

Groups exist to **skip gaps in the I/O map**: put the ranges either side of a gap into
different groups and the gap need not be read at all.

**UnitID** — `Id` + number, range **0–255**, prefixed with a dot: `Id1.40001` · `Id2.R2` ·
`Id3.S20.30`. Both together: `Id1.G2.R3`. **If the UnitID is omitted from the syntax, the
UnitID configured on the connection is sent to the PLC.**

### Two Modbus traps

**Discrete bits are read-modify-written 8 at a time.** A discrete input or output occupies
one bit on the PLC, but read and write access processes 8-bit values: a write reads 8 bits,
flips the target bit, and writes 8 back. The manual's warning verbatim:

> *If another bit of this byte is changed in the meantime, it is overwritten with the old
> value!*

One more reason to leave write access off unless a use case needs it.

**Octal areas take octal start addresses.** For `J` and `P` the digits **8 and 9 are
invalid**. Internally the address is handled as decimal — which matters when reading log and
status messages, because the number in the log is not the number you typed.

---

## Rockwell PLC-5 / SLC

```text
<Area>[File number]<Start address>[.Array size][Suffix]
```

| File type | Syntax | Orientation | Access | Default file no. | Address base |
|---|---|---|---|---|---|
| Output | `O` | bit | read / write | 0 | **octal** |
| Input | `I` | bit | read | 1 | **octal** |
| Status | `S` | word | read / write | 2 | decimal |
| Binary | `B` | word | read / write | 3 | decimal |
| SFC status | `SC` | word | read / write | 3 | decimal |
| String | `ST` | SLC string | read / write | 3 | decimal |
| Integer | `N` | word | read / write | 7 | decimal |
| Float | `F` | double word | read / write | 8 | decimal |
| Timer | `T` | — | — | — | — |

**Input and output files are octal-addressed** while everything else is decimal. Mixing the
two up produces a valid-looking address that reads the wrong point — the classic PLC-5
mistake.

The file number is optional because each type has a default; state it explicitly anyway
when the program uses non-default files, which most real programs do.

ControlLogix / CompactLogix use symbolic tag names rather than this file syntax, and are
browsed from the controller — see the ControlLogix browsing note in
`softing-datafeed.md`.

---

## Mitsubishi MELSEC-Q

Own syntax section, manual p. 675–679. Needs the `dataFEED OPC Server Mitsubishi` licence
(or Suite Extended). ⟨Detail not transcribed here — read p. 675 when a MELSEC-Q machine is
actually in scope.⟩

## Siemens S5 and Send/Receive

Separate syntax sections at p. 663 (S5) and p. 680 (Send/Receive). S5 differs from S7 mainly
in string handling (above) and in the suffix rules: **in S5 syntax a data type without a
suffix is unsigned**, and a signed type requires an explicit suffix — e.g. `DB10DW3.4BCD`.

---

## Suffixes

A suffix presents a value in a different format. The one worth knowing by name:

| Suffix | Syntax | Applies to | Produces |
|---|---|---|---|
| Bit array | `BA` | Byte, Word, Int, DWord, DInt, DDWord, DDInt | A boolean array — size in bytes × 8, or in words × 16 |

`BA` is already an array, so it cannot be combined with an array length, and it cannot be
bit-masked. The same is true of `KA`, `S5T`, `KT`, `D`, `T`, `DT`, `DU`, `TOD` — all present
to the client as string or bool.

Full suffix table: manual p. 694–698.

---

## Data types and how they map to OPC

PLC types (`BYTE`, `WORD`, `S5TIME`, …) are mapped to OPC **variant** types. Every OPC
datapoint has a canonical type — `DB5W3` in S7 syntax maps to `VT_I4` — and a client may
request a different one, in which case the server converts. Requesting type `EMPTY` gives
the canonical type.

**Unsigned handling is a global setting** with two modes:

- **Standard types only** — converts unsigned types to the next larger signed type. Use when
  the OPC client does not support `VT_UI2` / `VT_UI4`.
- **Unsigned types available** — leaves them unsigned.

Both are described as the default in the manual's own text, which is a documentation bug —
**check which one your configuration actually has** before diagnosing a value that is
correct in magnitude but wrong in sign or width.

---

## Practical rules

1. **Prefer symbol-file import.** You needed the PLC program to pass the breakpoint anyway,
   and an SDFI import gets the syntax right by construction.
2. **Re-export from the deployed program version**, not from an archived project. A symbol
   mismatch produces tags that connect and read nothing.
3. **Name tags to the agreed data model** (recorded as *CT Base*, confirmed current), not to the
   address. The identifier is the address; the *name* is what another plant matches on.
4. **Never type an address you have not seen in the program.** A wrong address in the right
   area reads a real value that means something else, and no layer below the use case will
   notice.
5. **Split mandatory from optional tags** in the Machine CV before acceptance.
