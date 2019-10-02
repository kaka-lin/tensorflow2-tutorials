# Install/Uninstall NVIDIA driver, CUDA Toolkit and cuDNN

## Install

- Ubuntu 18.04 (CUDA 10)

### 1. Add NVIDIA package repositories

```bash
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
$ sudo apt-get update

$ wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
$ sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
$ sudo apt-get update
```

### 2. Install NVIDIA driver

```bash
# Search the nvidia-driver version
$ suao apt search nvidia-driver

# Install nvidia-driver-418
$ sudo apt install --no-install-recommends nvidia-driver-418
# Reboot. Check that GPUs are visible using the command: nvidia-smi
```

### 3. Install development and runtime libraries (~4GB)

```bash
sudo apt-get install --no-install-recommends \
    cuda-10-0 \
    libcudnn7=7.6.2.24-1+cuda10.0  \
    libcudnn7-dev=7.6.2.24-1+cuda10.0
```

### 4. check CUDA and cuDNN version

1. CUDA

    ```bash
    $ cat /usr/local/cuda/version.txt

    # or
    
    $ nvcc --version
    ```

2. cuDNN

    ```bash
    $ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2

    # or

    $ cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2
    ```

## Uninstall

### 1. Uninstall NVIDIA driver

```bash
# bash
$ sudo apt remove --purge nvidia*

# zsh
$ sudo apt remove --purge "nvidia*"

# and then
$ sudo apt autoremove 
```

### 2. Uninstall CUDA

```bash
# bash
$ sudo apt --purge remove cuda*

# zsh
$ sudo apt --purge remove "cuda*"

# and then
$ sudo apt autoremove 
```
