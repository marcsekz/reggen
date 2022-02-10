# YAML register description language
This RDL enables the description of registers in YAML, which can be later compiled into Markdown (technically HTML, but with .md extension, so it will be displayed correctly on github).

## Requirements
- Python 3.6 or newer (I think)

## Installation
Just clone the repo.

## Usage
```bash
python3 reggen.py input_file [output_file]
```
When no output filename is specified, the output will have the same name as the input, but the extension will be changed to `.md`.

## Syntax
Top level:
- `register-width`: sets the width of the registers. All registers must have the same width, and all bits must be specified in each register. Bit ranges are allowed, as seen in the example.
- `registers`: all registers go here

Register syntax:
```yaml
REG_NAME:
  address: [address in hex]
  reset: [value of the register on reset]
  desc: [description of the register, as long as needed]
  access: [allowed access, typically R, W, or RW]
  [bit descriptions]
```

Bit description syntax:
```yaml
[bit number or range]:
  name: [short name of the bit, this appears in the summary]
  desc: [longer description of the function]
  values: # Optional, may be omitted (for example for reserved bits)
    [value]: [function]
    [other value]: other function
```

## Example
### Input:
```yaml
register-width: 8
registers:
  CTRL:
    address: 0A
    reset: 00
    desc: Configuration register
    access: RW
    7-6:
      name: RES
      desc: Reserved, reads 0
    5:
      name: AID
      desc: Automatic address pointer increment disable
      values:
        0: Address auto increment enabled
        1: Address auto increment disabled
    4-3:
      name: RES
      desc: Reserved, reads 0
    2:
      name: ITOD
      desc: Interrupt pin open-drain
      values:
        0: Push-pull interrupt output
        1: Open-drain interrupt output (ITP ignored, active-low)
    1:
      name: ITP
      desc: Interrupt output polarity, ignored if ITOD=1
      values:
        0: Active-low
        1: Active-high
    0:
      name: RES
      desc: Reserved, reads 0
```
### Output:
See [example.md](./example.md)