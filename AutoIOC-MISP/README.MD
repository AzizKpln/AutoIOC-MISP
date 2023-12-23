
<h2 align="center" width="100%">AutoIOC-MISP</h2>

# Installation
````
git clone https://github.com/AzizKpln/AutoIOC-MISP.git
cd AutoIOC-MISP
chmod +x *
bash install.sh
````
# Available Services:
* ThreatFox
* URLHaus
* PhishHunt
* OpenPhish
* CinsScore
* AbuseIPDB
* Emerging Threats
* HoneyDB
* KillNet
* Maliverse
* MalwareBazaar
* VirusShare
* RescureME
* SSLbl
* VXVault

# Usage
* Run The Main File
  ````
  python3 main.py
  ````
* Select the upload type (Manual or Auto)
   <p align="left" width="100%">
    <img width="75%" src="https://i.ibb.co/ryzSJxH/ss1.png">
  </p>
* Give your MISP server URL, MISP API KEY and MISP EVENT ID
* If you selected Manual, Upload the IOC list you have line by line
      <p align="left" width="100%">
      <img width="75%" src="https://i.ibb.co/D4vdtKS/SS2.png">
      </p>
    
* If you selected Auto, Select the service you wanna use and submit
    <p align="left" width="100%">
    <img width="75%" src="https://i.ibb.co/nP8cZ3P/ss3.png">
    </p>
    
# Crontab
* After using the tool, run the crontab.sh file;
    ````
    bash crontab.sh
    ````
* Select the time for per minutes (1440) is suggested
  