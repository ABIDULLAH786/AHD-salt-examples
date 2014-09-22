#!/bin/sh

source common.sh

# host, moveX, moveY, rotate, delay
python ${SCRIPT_DIR}moveTo.py $HOST01 '0' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST02 '1.55' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST03 '2.1' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST04 '1.1' '0' '0' '0.0' & \
python ${SCRIPT_DIR}moveTo.py $HOST05 '0' '0' '0' '0.0'