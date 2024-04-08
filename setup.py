from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read_requirements(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()    

setup(
    name="slurm-gui",
    version="0.1.0",
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
