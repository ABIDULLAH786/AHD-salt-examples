#!/bin/sh

cd `dirname $0`
source common.sh
echo "wake up"

python ${SCRIPT_DIR}wake_up.py $HOST01 & \
python ${SCRIPT_DIR}wake_up.py $HOST02 & \
python ${SCRIPT_DIR}wake_up.py $HOST03 & \
python ${SCRIPT_DIR}wake_up.py $HOST04 & \
python ${SCRIPT_DIR}wake_up.py $HOST05

exit 0	
