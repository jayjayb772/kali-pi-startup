!#/bin/bash
sudo touch /etc/apt/sources.list
sudo echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6
sudo apt update -y
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt install onboard -y
# Get routersploit
# install requirements

#get pret
#install requirements

#get sdr library
#install requirements

#setup ssh
sudo dpkg-reconfigure openssh-server
sudo update-rc.d -f ssh remove
sudo update-rc.d -f ssh defaults
#EDIT FILE
nano /etc/ssh/sshd_config
sudo update-rc.d -f ssh enable 2 3 4 5

#setup vnc
#install tightvnc


sudo apt-get autoremove

