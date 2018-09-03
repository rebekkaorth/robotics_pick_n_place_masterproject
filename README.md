# Robotics Pick 'n' Place with a Smart Grasping System 

## Introduction

This project is part of my master's project for my MSc. Software Development at the University of Glasgow (summer 2018). 
It is an approach to enable a robot to classify object poses and grasping them in a 3D simulation environment. 
For the classification the robot uses a convolutional neural network. 

This repository contains the neural network part of the project which was used and adapted. This neural network was originally developed by Andy Zeng, Shuran Song, Stefan Welker, Johnny Lee, Alberto Rodriguez and Thomas Funkhouser. Their paper "Learning Synergies between Pushing and Grasping with Self-supervised Deep Reinforcement Learning" (2018) describes how they implemented a ConvNet to enable a robot to push and grasp simple objects. (paper : https://arxiv.org/pdf/1803.09956.pdf - repository: https://github.com/andyzeng/visual-pushing-grasping). The repository at hand is a state of A. Zeng et al.'s repository from 4th of July 2018.  

To use the above mentioned neural network in this project, the repository of the neural network was taken and its code was adjusted to fit the needs of the project at hand. Originally the code was supposed to be implemented in the below described simulation. However, due to the scope of this project, the implementation of the neural network was put on hold and has not been finished. Therefore, the content of this repository represents the started implementation and adjustment of the described neural network!

## 2nd part of the described project

As indicated above, the project could be split into two parts. One being the neural network adjustment and its implementation and the second one being the programming of the robot to grasp objects in a 3D simulation. 

This 2nd part of the project can be found here: 
https://github.com/rebekkaorth/ros_smart_grasping_pkgs

## Authors
Rebekka Orth - 2312288O - 2312288O@student.gla.ac.uk

## Acknowledgments
The Convolutional Neural Network used in the project is from: 
https://github.com/andyzeng/visual-pushing-grasping

The paper corresponding to that repository can be found here: 
https://arxiv.org/pdf/1803.09956.pdf
