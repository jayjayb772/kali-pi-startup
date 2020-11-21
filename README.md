# kali-pi-startup
Portable kali pi setup docs and tools

# setup.sh
Run this file to:
- update the apt sources.list
- update, upgrade, full-upgrade, dist-upgrade, autoremove
- install all tools in the menu, including dependencies
# Touch screen 
## Main Menu
- Wi-Fi Attacks
- Local Network Recon
- Web Recon
- Tools
- Utilities

## Wi-fi Attacks
- Wifite Quick Scan
   - sudo wifite --no-wps --skip-crack
- Wifite Full Scan
   - sudo wifite --skip-crack
- Wireshark
   - sudo wireshark

## Local Network Recon
- _Nmap menu (unfinished)_
    - ~~sudo nmap -sn {IFace IP range}~~
    - ~~sudo nmap {IFace IP Range}~~
    - ~~sudo nmap {IFace IP Range} -A~~
    - sudo nmap -h
- _Netdiscover (unfinished)_
     - sudo netdiscover -h
- Wireshark
    - sudo wireshark
    
## Web Recon
- _Nmap menu (unfinished)_ 
    - sudo nmap -h
- _sqlmap (unfinished)_ 
    - sudo sqlmap -h
- _wpscan (unfinished)_ 
    - sudo wpscan -h
- _dirb (unfinished)_ 
    - sudo dirb -h
- _burp (unfinished)_ 
    - sudo burp
    
## Tools
- Airgeddon
    - sudo ~/Tools/airgeddon/airgeddon.sh
    
- Pret
    - sudo python ~/Tools/PRET/pret.py -h
    - sudo python ~/Tools/PRET/pret.py {Printer IP} [ps | pjl | pcl]
- Routersploit
    - sudo python3 ~/Tools/routersploit/rsf.py 
- Metasploit console
    - sudo msfconsole
- Social Engineering Toolkit
    - sudo setoolkit
- Gqrx
    - gqrx
- RTL-433
    - sudo rtl_433 -h
    - sudo rtl_433 -G 4
    - sudo rtl_433 -A 
    - sudo rtl_433 -w ~/rtl433_output/{output_file}

## Utilities
- ifconfig
    - sudo ifconfig
- _pwnagotchi network bridge (unfinished)_
- _vnc (unfinished)_
- _bluetooth (unfinished)_
- macchange (in progress)
    - sudo ifconfig wlan0 down && sudo macchanger -r wlan0 && sudo ifconfig wlan0 up
- __Shutdown__
- __Reboot__