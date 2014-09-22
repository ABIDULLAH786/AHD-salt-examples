#!/bin/sh

source common.sh

python ${SCRIPT_DIR}defled.py $HOST01 '1,0,0' & \
python ${SCRIPT_DIR}defled.py $HOST02 '1,1,0' & \
python ${SCRIPT_DIR}defled.py $HOST03 '0,1,0' & \
python ${SCRIPT_DIR}defled.py $HOST04 '0,1,1' & \
python ${SCRIPT_DIR}defled.py $HOST05 '0,0,1'

