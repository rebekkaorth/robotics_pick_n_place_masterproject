# Robotics Pick n' Place with a Smart Grasping System 

The project is part of my master's project for my Master of Science in Information Technology at the University of Glasgow. 
It is an approach to enable a robot classifying poses of objects in a 3D room and grasping them in a 3D simulation environment. 
It uses a Convolutional Neural Network for the classification and the Gazebo simulation environment. 

## Getting started 

Clone this repository:

```
git clone https://github.com/rebekkaorth/robitics_pick_n_place_masterproject
```
Its Dockerfile builds the container from the Shadow Robotics sandbox from which I saved a snapshot. This snapshot can be found here: https://hub.docker.com/r/rebor94/robotic_grip_grab_shadow_robotics/
The snapshot was taken on the 26/08/2018.

## Prerequisites 

Go to the repository directory to install all needed requirements. The following command assumes that you a pip installed. 

```
pip install -r requirements.txt
```

Go to the directory of the cloned repository and build the Docker container: 

```
docker build .
```

## Installing

The original code can be found in the following Github repository: 
https://github.com/shadow-robot/smart_grasping_sandbox

The Docker Hub that this repository refers to, can be found here: 
https://hub.docker.com/r/shadowrobot/shadow-robot/

Run the Docker container: 

```
docker run -it --name sgs -p 8080:8080 -p 8888:8888 -p 8181:8181 -p 7681:7681 <ID of the Docker image>
```

If the code is running, you can call the Gazebo simulation environment by opening your favorite browser and calling: 

```
localhost:8080/
```

The IDE Cloud 9 by AWS can be called like: 

```
localhost:8181/
```

## Training of the Neural Netowork

### Dataset used to train the neural network
The website where the dataset was downloaded from (06/07/2018): 
http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com 

## Examples of How the system works

### Identifying poses of models 

### Grasping identified models

## Authors
Rebekka Orth - 2312288O - 2312288O@student.gla.ac.uk

## Acknowledgments
The Convolutional Neural Network used in the project is from: 
https://github.com/andyzeng/visual-pushing-grasping

The paper corresponding to that repository can be found here: 
https://arxiv.org/pdf/1803.09956.pdf

The code of the simulation and the robot comes from: 
https://github.com/shadow-robot/smart_grasping_sandbox

Shadow robotics website can be found here: 
https://www.shadowrobot.com 
