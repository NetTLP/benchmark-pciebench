#!/usr/bin/env bash

BUS_ID=`lspci | grep '3776:8022' | cut -d' ' -f1 | cut -d':' -f1`

if [ -z ${BUS_ID} ]; then
	echo "device not found."
	exit 1
fi

sudo chmod 666 /sys/bus/pci/devices/0000:${BUS_ID}:00.0/remove
sudo echo 1 > /sys/bus/pci/devices/0000:${BUS_ID}:00.0/remove
sudo chmod 666 /sys/bus/pci/rescan
sudo echo "1" > /sys/bus/pci/rescan
