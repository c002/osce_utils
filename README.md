# osce_utils
Useful scripts and commands for OSCE

### Useful tricks   
The following configurations in bashrc:  
```
function reversestring() {
 v=${1}
 echo ${v:6:2}${v:4:2}${v:2:2}${v:0:2}
}

function complement() {
  gdb -batch -ex "p/x (0 - ${1})" | cut -f2 -d"="
}

function gdbcalc() {
  gdb -batch -ex "p/x  ${1}" | cut -f2 -d"="
}

function checkbads() {
  nasm -f bin ${1}.asm  
  findRightSub.py badchars.txt $1
}  
```  

	#hex2bin:
	perl -e 'print "\x...."'

	# Set space between two character
	cat bin | sed 's/.\{2\}/& /g'

	# bin2hex
	hexdump -C shell | grep -v 00000144 | cut -d" " -f3-19 | sed 's/ //g' | tr -d '\n'

	# bin2hex (\x12\xff\xe3...)
	hexdump -C jmp  | grep -v 00000011 | cut -d" " -f3-19 | sed 's/ //g' | tr -d '\n' | sed 's/.\{2\}/\\x&/g'

    # Separate each 4 bytes
    cat messagebox | sed 's/.\{8\}/&\n/g'
    # SEH JMP = shift+f9 
 
### assembly conversion  
   shellnoob --intel -i --to-opcode
    
 ### Useful scripts  
 ./gen_xor.sh   : Generate the xor encoding code (start address, end address and xor address)  
 ### Check info binary 
 https://github.com/iaraoz/binsecurity
    
