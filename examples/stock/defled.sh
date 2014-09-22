#!/bin/sh

python defled.py '192.168.3.9' '1,0,0' & python defled.py '192.168.3.8' '0,1,0'
# python defled.py '192.168.3.9' '1,0,0' & python defled.py '192.168.3.8' '0,1,0' & python defled.py '192.168.3.6' '0,0,1'
