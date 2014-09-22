#!/bin/sh

source common.sh

python ${SCRIPT_DIR}ledoff.py $HOST01 & \
python ${SCRIPT_DIR}ledoff.py $HOST02 & \
python ${SCRIPT_DIR}ledoff.py $HOST03 & \
python ${SCRIPT_DIR}ledoff.py $HOST04 & \
python ${SCRIPT_DIR}ledoff.py $HOST05
