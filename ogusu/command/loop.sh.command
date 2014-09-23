#!/bin/sh
cd `dirname $0`
source common.sh

while  :
do
	python ${SCRIPT_DIR}loop01.py $HOST01 & \
	python ${SCRIPT_DIR}loop01.py $HOST02 & \
	python ${SCRIPT_DIR}loop01.py $HOST03 & \
	python ${SCRIPT_DIR}loop01.py $HOST04 & \
	python ${SCRIPT_DIR}loop01.py $HOST05
	sleep 1s
	
	python ${SCRIPT_DIR}loop02.py $HOST01 & \
	python ${SCRIPT_DIR}loop02.py $HOST02 & \
	python ${SCRIPT_DIR}loop02.py $HOST03 & \
	python ${SCRIPT_DIR}loop02.py $HOST04 & \
	python ${SCRIPT_DIR}loop02.py $HOST05
	sleep 1s

	python ${SCRIPT_DIR}loop03.py $HOST01 & \
	python ${SCRIPT_DIR}loop03.py $HOST02 & \
	python ${SCRIPT_DIR}loop03.py $HOST03 & \
	python ${SCRIPT_DIR}loop03.py $HOST04 & \
	python ${SCRIPT_DIR}loop03.py $HOST05
	sleep 1s

	python ${SCRIPT_DIR}loop04.py $HOST01 & \
	python ${SCRIPT_DIR}loop04.py $HOST02 & \
	python ${SCRIPT_DIR}loop04.py $HOST03 & \
	python ${SCRIPT_DIR}loop04.py $HOST04 & \
	python ${SCRIPT_DIR}loop04.py $HOST05
	sleep 1s

	python ${SCRIPT_DIR}loop05.py $HOST01 & \
	python ${SCRIPT_DIR}loop05.py $HOST02 & \
	python ${SCRIPT_DIR}loop05.py $HOST03 & \
	python ${SCRIPT_DIR}loop05.py $HOST04 & \
	python ${SCRIPT_DIR}loop05.py $HOST05
	sleep 1s

done
echo "stopped loop"

exit 0	
