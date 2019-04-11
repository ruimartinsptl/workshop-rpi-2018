    Rui Martins, rui@martins.pt [Setembro de 2018]

# Instalar OpenCV

## OpenCV 2.x
```
sudo apt-get install -y libopencv-dev python-dev python-opencv python-numpy
python -c "import cv2; print cv2.__version__"
```

## OpenCV 3.x
```
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

sudo pip3 install opencv-contrib-python # OpenCV 3

python -c "import cv2; print cv2.__version__"
python3 -c "import cv2; print(cv2.__version__)"
```

# Processar imagens
## O que é uma imagem
![raspi-config](/img/MatBasicImageForComputer.jpg)

![raspi-config](/img/RGB-matrix.png)











# Configurar conda [opcional] 
```
conda install notebook ipykernel
conda install nb_conda # https://stackoverflow.com/questions/37085665/in-which-conda-environment-is-jupyter-executing
conda install --channel=conda-forge nb_conda_kernels # https://github.com/jupyter/jupyter/issues/245

===============

# USAR PYTHON 2.7
conda create -n workshop-rpi-python27 python=2.7
source activate workshop-rpi-python27

pip install opencv-contrib-python

python -c "import cv2; print cv2.__version__"

source deactivate

---------------

# USAR PYTHON 3.7
conda create -n workshop-rpi-python37 python=3.7
source activate workshop-rpi-python37

pip install opencv-contrib-python

python -c "import cv2; print(cv2.__version__)"

source deactivate

===============

conda env list
```

