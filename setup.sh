sudo touch /etc/apt/sources.list
sudo echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6
sudo apt update -y
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt install onboard -y
sudo apt-get install cmake build-essential python-pip3 libusb-1.0-0-dev python3-numpy git pandoc isc-dhcp-server dsniff beef-xss mdk4 hostapd lighttpd bettercap hostapd-wpe hcxdumptool hcxtools libtool librtlsdr-dev autoconf pkg-config gnuradio rtl-sdr gr-osmosdr gqrx-sdr -y
sudo mkdir Tools

#region TOOLS
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



#sudo pip install pyrtlsdr


sudo git clone git://git.osmocom.org/rtl-sdr.git
cd rtl-sdr
sudo mkdir build
sudo cd build
sudo cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
sudo make
sudo make install
sudo ldconfig
sudo pip install pyrtlsdr
sudo pip3 install pyrtlsdr

sudo python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#sudo python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

cd $HOME/Tools
sudo git clone https://github.com/Banjopkr/WQ7Tpanadapter.git
sudo cp -r WQ7Tpanadapter/FreqShow_Large FreqShow_Large
sudo cp -r FreqShow_Large/FreqShow.desktop Desktop/FreqShow.desktop

#rtl443 setup

git clone https://github.com/merbanan/rtl_433
cd rtl_433/
sudo mkdir build
sudo cmake . .
sudo make
sudo make install
cd ../

sudo mkdir ~/rtl433_output

cd ~/
#endregion

#setup ssh
sudo dpkg-reconfigure openssh-server
sudo update-rc.d -f ssh remove
sudo update-rc.d -f ssh defaults
#EDIT FILE
#nano /etc/ssh/sshd_config
sudo update-rc.d -f ssh enable 2 3 4 5

#setup vnc
sudo apt-get install tightvnc
#install tightvnc



sudo apt-get autoremove


sudo touch /usr/local/bin/touch-menu
sudo echo "#!/bin/bash" >> /usr/local/bin/touch-menu
sudo echo "sudo python3 ~/kali-pi-startup/ToolMenu/MenuStart.py" >> /usr/local/bin/touch-menu


