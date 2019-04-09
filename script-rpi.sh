
echo 'alias ll="ls -la"' >> .bash_rc
source .bash_rc

# Updating firmware
sudo rpi-update -y
sudo reboot

sudo apt-get -y update
sudo apt-get -y dist-upgrade

# ldconfig is a program that is used to maintain the shared library cache. 
# This cache is typically stored in the file /etc/ld.so.cache and is used by 
# the system to map a shared library name to the location of the corresponding 
# shared library file
sudo ldconfig
sudo reboot

sudo raspi-config

sudo apt-get -y update
sudo apt-get -y upgrade


sudo apt-get purge -y wolfram-engine
sudo apt-get purge -y libreoffice*
sudo apt-get clean
sudo apt-get autoremove


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


