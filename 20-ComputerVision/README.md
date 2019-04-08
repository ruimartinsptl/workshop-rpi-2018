
# conda install notebook ipykernel
conda install nb_conda # https://stackoverflow.com/questions/37085665/in-which-conda-environment-is-jupyter-executing
conda install --channel=conda-forge nb_conda_kernels # https://github.com/jupyter/jupyter/issues/245

conda create -n workshop-rpi-python27 python=2.7

source activate workshop-rpi-python27

pip install opencv-contrib-python

source deactivate


