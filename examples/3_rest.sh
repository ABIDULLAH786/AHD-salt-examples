#! /bin/sh

python ledoff.py '192.168.3.9' & python ledoff.py '192.168.3.8' & python ledoff.py '192.168.3.6'

python sleep.py '192.168.3.6' & python sleep.py '192.168.3.9' & python sleep.py '192.168.3.8'

