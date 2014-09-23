#!/bin/sh


cd `dirname $0`
source common.sh

echo "fast random"

python ${SCRIPT_DIR}insane_move_auto.py $HOST01 & \
python ${SCRIPT_DIR}insane_move_auto.py $HOST02 & \
python ${SCRIPT_DIR}insane_move_auto.py $HOST03 & \
python ${SCRIPT_DIR}insane_move_auto.py $HOST04 & \
python ${SCRIPT_DIR}insane_move_auto.py $HOST05 


exit 0	
