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
	echo restart pciebench
        sudo sh ./restart.sh

	sleep 0.5

        cmd="sudo ./bin/benchmark \
                -d $dir -t $typ -p RAN 2097152 -n $len -l 30 \
                -P $mem" > $out
        echo $cmd
        $cmd > $out
}

for x in `seq 128`; do

	len=$(( $x * 16 ))

	out="$CRDIR/output/pciebench_bw2_read_ptr-random_len-${len}.txt"
	run_bench $out bw W $len $NETTLP
done
