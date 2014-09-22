#!/bin/sh

source common.sh

python ${SCRIPT_DIR}led.py $HOST01 & \
python ${SCRIPT_DIR}led.py $HOST02 & \
python ${SCRIPT_DIR}led.py $HOST03 & \
python ${SCRIPT_DIR}led.py $HOST04 & \
python ${SCRIPT_DIR}led.py $HOST05