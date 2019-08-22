# Tensorflow 2.0 - Tutorials

This repository is `TensorFlow 2.0` tutorial and examples.

## Requirements

- Tensorflow 2.0
- Jupyter Notebook

You can just install TensorFlow 2.0 with `pip` (as shown below ), or you can use a [docker image](#docker-image) that we already made.

```bash
$ pip install -r requirements.txt
```

## Start

1. clone this repository

    ```bash
    $ git clone https://github.com/kaka-lin/tensorflow2-tutorials.git
    ```

2. Run Jupyter Notebook
    
    In your local directory

    ```bash
    $ jupyter notebook
    ```

---

<span id="docker-image"></span>
## Docker image

We have already made a docker image for this repository.
If you want to build yourself docker image or get information about this image, you can refer [here](https://github.com/kaka-lin/docker-image).

### Download docker image

```bash
$ docker pull kakalin/kimage:cpu-mconda-py36-tf200
```

### Running a container

You need to mount directory into container and publish a container's port to the host.

- mount directory: 

    ```bash
    -v <localhost_directory>:<container_path>
    ```

- publish port:

    ```bash
    -p xxxx:8888 # xxxx can be any port(s), ex: 8888 or 7777 
    ```

#### Example

```bash
$ docker run -it - kakalin/kimage:cpu-mconda-py36-tf200
```

```bash
$ docker run -it -p 8888:8888 -v ~/tensorflow2-tutorials:/root/tensorflow2-tutorials kakalin/kimage:cpu-mconda-py36-tf200
```

#### In container

```bash
$ jupyter notebook --allow-root --no-browser --ip="*"
```
