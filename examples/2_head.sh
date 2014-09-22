#! /bin/sh

python wake_up.py '192.168.3.9' & python wake_up.py '192.168.3.8' 
python defled.py '192.168.3.9' '1,1,1' & python defled.py '192.168.3.8' '1,1,1'
python head_move.py '192.168.3.9' '0.9' & python head_move.py '192.168.3.8' '0.9'