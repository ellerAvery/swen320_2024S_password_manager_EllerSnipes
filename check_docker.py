import subprocess
import sys

image_name = sys.argv[1]

def image_exists(name):
    try:
        subprocess.check_output(['docker', 'image', 'inspect', name])
        return True
    except subprocess.CalledProcessError:
        return False

if not image_exists(image_name):
    print(f"Docker image {image_name} does not exist. Proceeding to build...")
    try:
        subprocess.check_call(['docker', 'build', '-t', image_name, '.'])
        print(f"Docker image {image_name} built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to build Docker image {image_name}.")
        sys.exit(1)
else:
    print(f"Docker image {image_name} already exists. No need to rebuild.")
