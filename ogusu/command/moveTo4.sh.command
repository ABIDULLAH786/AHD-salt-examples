#!/bin/sh
cd `dirname $0`
source common.sh

# host, moveX, moveY, rotate, delay
python ${SCRIPT_DIR}moveTo.py $HOST01 '0' '0' '36' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST02 '0' '0' '108' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST03 '0' '0' '-45' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST04 '0' '0' '-108' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST05 '0' '0' '-36' '0.0'