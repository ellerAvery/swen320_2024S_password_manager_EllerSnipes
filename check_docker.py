'''# check_docker.py
import subprocess
import sys

def is_docker_running():
    try:
        subprocess.check_output(['docker', 'info'])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def image_exists(image_name):
    try:
        subprocess.check_output(['docker', 'image', 'inspect', image_name])
        return True
    except subprocess.CalledProcessError:
        return False

def container_running(container_name):
    try:
        output = subprocess.check_output(['docker', 'container', 'inspect', container_name])
        return True
    except subprocess.CalledProcessError:
        return False

def run_container(image_name, container_name):
    try:
        subprocess.check_output(['docker', 'run', '-d', '--name', container_name, image_name])
        print(f"Container {container_name} started.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start container {container_name}: {e}")

if __name__ == "__main__":
    docker_image_name = 'flask'
    container_name = 'flask_container'
    
    if not is_docker_running():
        print("Docker is not running. Please start Docker and try again.")
        sys.exit(1)
    
    if not image_exists(docker_image_name):
        print(f"Docker image {docker_image_name} does not exist. Please build the image and try again.")
        sys.exit(1)
    
    if not container_running(container_name):
        print(f"Starting container {container_name}...")
        run_container(docker_image_name, container_name)
    else:
        print(f"Container {container_name} is already running.")
''' 