import os, subprocess
from setuptools import setup, find_packages

currdir = os.path.dirname(__file__)

def get_version():
    github_ref = os.getenv("GITHUB_REF")
    if github_ref and github_ref.startswith("refs/tags/"):
        # Extract the tag name from the reference
        tag = github_ref.split("/")[-1]
        # Remove the "v" prefix if present
        version = tag[1:] if tag.startswith("v") else tag
        return version
    else:
        # If there is no tag reference, fallback to a default version
        return "0.0.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read_requirements():
    requirements_path = os.path.join(currdir, 'requirements.txt')
    if not os.path.exists(requirements_path):
        print(f'Could not find {requirements_path}')
        return ['textual<0.50']
    with open(requirements_path, 'r', encoding="utf-8") as file:
        return file.read().splitlines()


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
    install_requires=read_requirements(),
    scripts=['bin/tsqueue'],
)
