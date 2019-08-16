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
                -d $dir -t $typ -p FIX 0 -n $len -l 50 \
                -P $mem" > $out
        echo $cmd
        $cmd > $out
}

for len in 8 16 32 64 128 256 512 1024 2048 4096; do
	out="$CRDIR/output/pciebench_bw_read_ptr-fix_len-${len}.txt"
	run_bench $out bw W $len $NETTLP
done
