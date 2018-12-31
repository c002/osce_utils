#!/bin/bash
function usage() {
  echo "$1 <start> <end> <xor>"
  exit -1
}
if [ "$#" -ne 3 ];  then
  usage
fi
START_ADDRESS=$1
END_ADDRESS=$2
XOR_ADDRESS=$3
cat <<EOF
MOV EAX, $START_ADDRESS 
XOR BYTE PTR DS:[EAX],0F 
INC EAX 
CMP EAX, $END_ADDRESS 
JLE SHORT $XOR_ADDRESS 
PUSH EBP 
MOV EBP,ESP 
PUSH -1 
JMP $START_ADDRESS 
EOF
