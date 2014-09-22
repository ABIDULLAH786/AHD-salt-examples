#!/bin/sh

source common.sh

# host, moveX, moveY, rotate, delay
python ${SCRIPT_DIR}moveTo.py $HOST01 '0' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST02 '-0.65' '0.65' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST03 '0' '0' '-180' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST04 '-0.2' '-0.5' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST05 '0' '0' '180' '0.0'