#!/bin/sh

cd `dirname $0`
source common.sh


cd `dirname $0`
echo "kill_all"

python ${SCRIPT_DIR}kill_all.py $HOST01 & \
python ${SCRIPT_DIR}kill_all.py $HOST02 & \
python ${SCRIPT_DIR}kill_all.py $HOST03 & \
python ${SCRIPT_DIR}kill_all.py $HOST04 & \
python ${SCRIPT_DIR}kill_all.py $HOST05

exit 0	
