#!/bin/sh
cd `dirname $0`
source common.sh

python ${SCRIPT_DIR}test.py $HOST01 '1' '2' & \
python ${SCRIPT_DIR}test.py $HOST02 '1' '2' & \
python ${SCRIPT_DIR}test.py $HOST03 '1' '2'
