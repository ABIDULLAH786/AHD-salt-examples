#!/bin/sh
cd `dirname $0`
source common.sh

# host, moveX, moveY, rotate, delay
python ${SCRIPT_DIR}moveTo.py $HOST01 '-0.34' '0.5' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST02 '-0.24' '0.42' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST03 '0' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST04 '-0.85' '-0.5' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST05 '-0.91' '-0.3' '0' '0.0'