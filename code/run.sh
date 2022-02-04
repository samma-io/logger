#!/bin/bash
echo "Parsing logs - samma"
python3 -u /code/readLogs.py

echo "Sleep so filebeat can read the logs"
sleep 1m


echo "All done die"
echo "died man die" > /out/die
