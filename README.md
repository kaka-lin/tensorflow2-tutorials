# Tensorflow 2.0 - Tutorials

This repository is `TensorFlow 2.0` tutorial and examples.

## Docker image

We have already made a docker image for this repository.

If you want to build yourself docker image or get information about this image, you can refer [here](https://github.com/kaka-lin/docker-image).

### Download docker image

```bash
$ docker pull kakalin/kimage:cpu-mconda-py36-tf200
```

### Running a container

```bash
$ docker run -it --rm kakalin/kimage:cpu-mconda-py36-tf200
```

### Running Jupyter Notebook in container

```bash
$ docker run -it -p 8888:8888 --rm kakalin/kimage:cpu-mconda-py36-tf200
```

- In container

```bash
$ jupyter notebook --allow-root --no-browser --ip="*"
```
