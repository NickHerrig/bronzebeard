import os
import sys

from peachpy import *
from peachpy.x86_64 import *

sys.path[0:0] = ['.', '..']
from bronzebeard.elf import ELF

# User-level applications use as integer registers for passing the sequence:
# %rdi, %rsi, %rdx, %rcx, %r8 and %r9

with Function("_start", tuple()) as start:
    # exit
    MOV(rax, 60)
    MOV(rdi, 42)
    SYSCALL()

    # unreachable return to make Function happy
    RETURN()

code = start.finalize(abi.detect()).encode().load().code_segment
elf = ELF(code)
with open('output.elf', 'wb') as f:
    f.write(elf.build())

os.chmod('output.elf', 0o775)