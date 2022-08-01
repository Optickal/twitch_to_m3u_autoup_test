

#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 twitch_m3ugrabber.py > ../twitch.m3u

echo m3u grabbed
