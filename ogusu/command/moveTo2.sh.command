#!/bin/sh
cd `dirname $0`
source common.sh

# host, moveX, moveY, rotate, delay
python ${SCRIPT_DIR}moveTo.py $HOST01 '0.45' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST02 '1.65' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST03 '0.20' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST04 '2.55' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST05 '1.05' '0' '0' '0.0'