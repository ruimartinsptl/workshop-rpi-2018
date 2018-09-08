
# Updating firmware
sudo rpi-update
# sudo reboot

# ldconfig is a program that is used to maintain the shared library cache. 
# This cache is typically stored in the file /etc/ld.so.cache and is used by 
# the system to map a shared library name to the location of the corresponding 
# shared library file
sudo ldconfig
sudo reboot

sudo raspi-config
sudo apt-get update
sudo apt-get -y upgrade

