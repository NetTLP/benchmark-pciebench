#!/bin/bash

CRDIR=`pwd`
PBDIR=~/work/pciebench-netfpga/HOST
NETTLP=1b:00.0 

function run_bench() {

        out=$1
	typ=$2
        dir=$3
        len=$4
        mem=$5

	echo
        echo $len bytes, $mem memory
	echo output is $out

	cd $PBDIR

        sudo sh ./restart.sh
        cmd="sudo ./bin/benchmark \
                -d $dir -t $typ -p RAN 2097152 -n $len -l 1000 \
                -P $mem"
        echo $cmd

        $cmd > $out
}


for len in 8 16 32 64 128 256 512 1024 2048 4096 8192; do
	out="$CRDIR/output/pciebench_lat_read_ptr-random_len-${len}.txt"
	run_bench $out lat W $len $NETTLP
done
