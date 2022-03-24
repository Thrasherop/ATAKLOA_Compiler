# Introduction
This repository contains the source code for the ATAKLOA compiler, which compiles assembly into machine code that the BYU-Idaho ECEN 240 MicroProcessor can execute. The compiler is written in Python3.


## Usage
---
To compile, navigate to the root of the project and run:

`$ python ATAKLOA_Compiler.py <assembly_file> <binary_output>`



## Inside this repo
---
This repo contains the following files:
- `ATAKLOA_Compiler.py`: The actual compiler
- `README.md`: This file, which explains the repo
- `test.txt`: an example assembly file, which contains all commands
- `output.txt`: an example output file



## Instruction set: 
---

```
0000 - NOP - No Operation - Does nothing
0001 - LD - Load - LD [destination], [source]
0010 - MOV - Move - MOV [destination], [source]
0011 - DISP - Display - DISP [source1], [source2]
0100 - XOR - Exclusive OR - XOR [destination], [source1], [source2]
0101 - AND - AND - AND [destination], [source1], [source2]
0110 - OR - OR - OR [destination], [source1], [source2]
0111 - ADD - add - ADD [destination], [source1], [source2]
1111 - SUB - subtract - SUB [destination], [source1], [source2]
```