#!/bin/bash
apt update 
apt upgrade -y
apt install python3 -y
apt install python3-pip -y
python3 -m pip install requirements.txt
clear
echo "[+]Requirements For AutoMISP downloaded successfully!"