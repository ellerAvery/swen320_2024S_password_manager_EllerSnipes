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

if __name__ == "__main__":
    if not is_docker_running():
        print("Docker is not running. Please start Docker and try again.")
        sys.exit(1)
    
    # Define your Docker image name here instead of as a command-line argument
    docker_image_name = 'flask_app'
    if image_exists(docker_image_name):
        print(f"Docker image {docker_image_name} already exists.")
    else:
        print(f"Docker image {docker_image_name} does not exist. You may want to build it.")
