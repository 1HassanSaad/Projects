#!/bin/bash
if [ "$1" == "" ]; then
    echo "invalid"
else
    for i in `seq 1 254` ; do
	ping -c 1 $1.$i | grep "64 bytes" | cut -d " " -f 4 | cut -d : -f 1
    done
fi
