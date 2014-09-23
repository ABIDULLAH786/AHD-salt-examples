#!/bin/sh

cd `dirname $0`
source common.sh

echo "wake up"

python ${SCRIPT_DIR}wake_up.py $HOST01 & \
python ${SCRIPT_DIR}wake_up.py $HOST02 & \
python ${SCRIPT_DIR}wake_up.py $HOST03 & \
python ${SCRIPT_DIR}wake_up.py $HOST04 & \
python ${SCRIPT_DIR}wake_up.py $HOST05


echo "head banging"

python ${SCRIPT_DIR}head_move.py $HOST01 '0.9' & \
python ${SCRIPT_DIR}head_move.py $HOST02 '0.9' & \
python ${SCRIPT_DIR}head_move.py $HOST03 '0.9' & \
python ${SCRIPT_DIR}head_move.py $HOST04 '0.9' & \
python ${SCRIPT_DIR}head_move.py $HOST05 '0.9'

exit 0	
