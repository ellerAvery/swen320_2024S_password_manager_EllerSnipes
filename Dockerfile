# Use the Python 3.9 image from the Docker Hub as the base image
FROM python:3.9-bullseye

# Install requirements
# Copy the requirements.txt file from your host to the container's /tmp directory
COPY requirements.txt /tmp/requirements.txt
# Install the Python dependencies defined in requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# (Optional) Create and set the working directory. Uncomment if needed.
# RUN mkdir -p /app
WORKDIR /app

# Copy your Flask application files into the container's working directory
# Use $PWD in your docker run command to correctly map volumes if needed
COPY app/*.py /app/
COPY app/ulib /app/ulib
COPY app/run_flask.sh /app/

# (Optional) If you prefer to copy everything from the app directory, uncomment the following line
# COPY app/* /app/

# Specify the command to run within the container
CMD [ "./run_flask.sh"]
