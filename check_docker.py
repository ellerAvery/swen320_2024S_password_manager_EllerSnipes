import subprocess
import sys

def is_docker_running():
    try:
        subprocess.check_output(['docker', 'info'])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def image_exists(name):
    try:
        subprocess.check_output(['docker', 'image', 'inspect', name])
        return True
    except subprocess.CalledProcessError:
        return False

if not is_docker_running():
    print("Docker is not running. Please start Docker and try again.")
    sys.exit(1)

if image_exists('flask_app'):
    print("Docker image flask_app already exists. No need to rebuild.")
else:
    print("Docker image flask_app does not exist. Proceeding to build...")
    try:
        subprocess.check_call(['docker', 'build', '-t', 'flask_app', '.'])
        print("Docker image flask_app built successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to build Docker image flask_app.")
        sys.exit(1)
