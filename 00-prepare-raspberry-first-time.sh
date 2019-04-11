#!/usr/bin/env bash

set -e

echo '' >> .bash_rc
echo 'alias ll="ls -la"' >> .bash_rc
echo '' >> .bash_rc
source .bash_rc

# Updating firmware
sudo rpi-update # Press 'Y'
# sudo reboot

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade

# ldconfig is a program that is used to maintain the shared library cache. 
# This cache is typically stored in the file /etc/ld.so.cache and is used by 
# the system to map a shared library name to the location of the corresponding 
# shared library file
sudo ldconfig
# sudo reboot

# sudo raspi-config
sudo apt-get -y install raspi-config # Update raspi-config
sleep 5
sudo raspi-config nonint do_expand_rootfs
sudo raspi-config nonint do_wifi_country PT
sudo raspi-config nonint do_hostname rpi-demo
sudo raspi-config nonint do_boot_behaviour B3
sudo raspi-config nonint do_vnc 1
sudo raspi-config nonint do_rgpio 1

sudo apt-get -y update && sudo apt-get -y upgrade


sudo apt-get install -y vim
sudo apt-get install -y eog
sudo apt-get install -y screen
sudo apt-get install -y htop

sudo apt-get purge -y wolfram-engine
sudo apt-get purge -y libreoffice*
sudo apt-get clean
sudo apt-get autoremove



# Instalar por repositorio
sudo apt-get install -y libopencv-dev python-dev python-opencv python-numpy

sudo apt-get install -y libcblas-dev
sudo apt-get install -y libhdf5-dev
sudo apt-get install -y libhdf5-serial-dev
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libjasper-dev
sudo apt-get install -y libqtgui4
sudo apt-get install -y libqt4-test

sudo apt-get install -y libjasper1
sudo apt-get install -y libhdf5-100
# sudo apt-get --yes --force-yes install libatlas-base-dev

sudo pip3 install opencv-python  # if you install 'opencv-contrib-python', you don't need to install 'opencv-python'
sudo pip3 install opencv-contrib-python

python -c "import cv2; print cv2.__version__"
python3 -c "import cv2; print(cv2.__version__)"

read -p "Press enter to continue... The system will reboot."

sudo reboot

exit









# Instalar a partir do código fonte

sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk2.0-dev libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran



sudo apt-get install -y python2.7-dev
sudo apt-get install -y python3-dev

wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py


sudo pip3 install numpy scipy

wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
unzip opencv.zip
unzip opencv_contrib.zip

rm opencv.zip
rm opencv_contrib.zip

cd ~/opencv-3.4.1/
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules \
    -D BUILD_EXAMPLES=ON ..

make -j4

sudo make install
sudo ldconfig
