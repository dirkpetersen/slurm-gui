import os, subprocess
from setuptools import setup, find_packages

def get_version():
    try:
        # Get the version from the git tag
        tag = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).decode("utf-8").strip()
        # Remove the "v" prefix if present
        version = tag[1:] if tag.startswith("v") else tag
        return version
    except subprocess.CalledProcessError:
        # If there is no git tag, fallback to a default version
        return "0.0.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read_requirements(file_path):
    requirements_path = os.path.join(os.path.dirname(__file__), file_path)
    try:
        with open(requirements_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'Could not read {requirements_path}')
        return ['textual<0.50']

setup(
    name="slurm-gui",
    version=get_version(),
    author="Dirk Petersen",
    author_email="no-email@no-domain.com",
    description="GUI/TUI frontends to squeue, sbatch and srun using the fabulous textual TUI framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dirkpetersen/slurm-gui",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=read_requirements('requirements.txt'),
    scripts=['bin/tsqueue'],
)
