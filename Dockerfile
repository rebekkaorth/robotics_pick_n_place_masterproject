FROM rebor94/robotic_grip_grab_shadow_robotics:v1

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# pip install numpy scipy opencv-python matplotlib
# pip install torch==0.3.1 torchvision==0.2.0

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
# app.py file needs to be run with a set of tags
# python main.py --is_sim --method 'reactive' --experience_replay --grasp_only --save_visualizations