#!/bin/bash

while [ 1 ]; do
	python generator.py
	mv t.json 1.json
	echo -n "x "
	sleep 0.1
done
