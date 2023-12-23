#!/bin/bash

read -p "Enter the frequency of the cron job (e.g., '*/5 * * * *' for every 5 minutes): " cron_frequency
current_path=$(pwd)
file_path="Selected/sources"

if grep -q "AbuseIPDB" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/abuseipdb.py") | crontab -
    echo "[+]Crontab entry added successfully. [AbuseIPDB]"
fi
if grep -q "CinsScore" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/cinsscore.py") | crontab -
    echo "[+]Crontab entry added successfully. [CinsScore]"
fi
if grep -q "KillNet" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/killnet.py") | crontab -
    echo "[+]Crontab entry added successfully. [KillNet]"
fi
if grep -q "Emerging_Threats" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/emergingthreats.py") | crontab -
    echo "[+]Crontab entry added successfully. [Emerging_Threats]"
fi
if grep -q "HoneyDB" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/honeydb.py") | crontab -
    echo "[+]Crontab entry added successfully. [HoneyDB]"
fi
if grep -q "Maltiverse" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/maltiverse.py") | crontab -
    echo "[+]Crontab entry added successfully. [Maltiverse]"
fi
if grep -q "Malware_Bazaar" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/malware_bazar.py") | crontab -
    echo "[+]Crontab entry added successfully. [Malware_Bazaar]"
fi
if grep -q "OpenPhish" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/openphish.py") | crontab -
    echo "[+]Crontab entry added successfully. [OpenPhish]"
fi
if grep -q "RescureMe" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/rescureme.py") | crontab -
    echo "[+]Crontab entry added successfully. [RescureMe]"
fi
if grep -q "SSLbl" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/sslbl.py") | crontab -
    echo "[+]Crontab entry added successfully. [SSLbl]"
fi
if grep -q "ThreatFox" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/threatfox.py") | crontab -
    echo "[+]Crontab entry added successfully. [ThreatFox]"
fi
if grep -q "URLHaus" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/urlhaus.py") | crontab -
    echo "[+]Crontab entry added successfully. [URLHaus]"
fi
if grep -q "VirusShare" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/virusshare.py") | crontab -
    echo "[+]Crontab entry added successfully. [VirusShare]"
fi
if grep -q "VXVault" "$file_path"; then
    (crontab -l ; echo "*/$cron_frequency * * * * cd $current_path && python3 $current_path/Integrations/vxvault.py") | crontab -
    echo "[+]Crontab entry added successfully. [VXVault]"
fi