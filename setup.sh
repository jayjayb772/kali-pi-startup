#!/bin/bash
sudo touch /etc/apt/sources.list
sudo echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6
sudo apt update -y
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt install onboard -y
sudo apt-get install cmake build-essential python-pip libusb-1.0-0-dev python-numpy git pandoc -y
sudo mkdir $HOME/Tools
cd Tools
# Get routersploit
git clone https://github.com/threat9/routersploit
# install requirements
cd routersploit
python3 -m pip install -r requirements.txt
cd ../

# Get pret
git clone https://github.com/RUB-NDS/PRET
#install requirements
sudo pip install colorama pysnmp
sudo pip3 install colorama pysnmp


#Get airrgeddon
git clone https://github.com/v1s1t0r1sh3r3/airgeddon
#install requirements
sudo apt-get install isc-dhcp-server dsniff beef-xss mdk4 hostapd lighttpd bettercap hostapd-wpe hcxdumptool hcxtools -y


#get sdr library
cd ~
git clone git://git.osmocom.org/rtl-sdr.git
cd rtl-sdr
mkdir build
cd build
cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
make
sudo make install
sudo ldconfig
#install requirements
sudo pip install pyrtlsdr
sudo pip3 install pyrtlsdr


#setup ssh
sudo dpkg-reconfigure openssh-server
sudo update-rc.d -f ssh remove
sudo update-rc.d -f ssh defaults
#EDIT FILE
nano /etc/ssh/sshd_config
sudo update-rc.d -f ssh enable 2 3 4 5

#setup vnc
sudo apt-get install tightvnc
#install tightvnc



sudo apt-get autoremove

