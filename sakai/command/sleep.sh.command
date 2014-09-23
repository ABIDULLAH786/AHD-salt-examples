#!/bin/sh

cd `dirname $0`
source common.sh


echo "good night"

python ${SCRIPT_DIR}sleep.py $HOST01 & \
python ${SCRIPT_DIR}sleep.py $HOST02 & \
python ${SCRIPT_DIR}sleep.py $HOST03 & \
python ${SCRIPT_DIR}sleep.py $HOST04 & \
python ${SCRIPT_DIR}sleep.py $HOST05

exit 0	
