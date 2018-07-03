# Use an official Python runtime as a parent image
FROM python:2.7-slim
MAINTAINER Rebkka Orth <2312288O@student.gla.ac.uk>

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip2 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

FROM rebor94/robotic_grip_grab_shadow_robotics:latest
WORKDIR /workspace/src/

COPY  app.py /workspace/src
COPY  logger.py /workspace/src
COPY  model.py /workspace/src
COPY  robot_in_training.py /workspace/src
COPY  trainer.py /workspace/src
COPY  utils.py /workspace/src


RUN entrypoint.sh


# Run app.py when the container launches
CMD ["python", "app.py"]
# app.py file needs to be run with a set of tags
# python main.py --is_sim --method 'reactive' --experience_replay --grasp_only --save_visualizations