#!/bin/sh

cd `dirname $0`
source common.sh

echo "slow random"

python ${SCRIPT_DIR}insane_move.py $HOST01 '0.01' & \
python ${SCRIPT_DIR}insane_move.py $HOST02 '0.01' & \
python ${SCRIPT_DIR}insane_move.py $HOST03 '0.01' & \
python ${SCRIPT_DIR}insane_move.py $HOST04 '0.01' & \
python ${SCRIPT_DIR}insane_move.py $HOST05 '0.01' 


exit 0	
