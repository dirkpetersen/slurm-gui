import os, setuptools

pkgname = 'slurm-gui'
appdesc = "GUI/TUI frontends to squeue, sbatch and srun using the fabulous textual TUI framework"
gitrepos = 'dirkpetersen/slurm-gui'
pyreq = '>=3.8'

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
    for root, dirs, files in os.walk("."):
        file_path = ''
        if "requirements.txt" in files:
            file_path = os.path.join(root, "requirements.txt")
        elif "requires.txt" in files:
            file_path = os.path.join(root, "requires.txt")
        if file_path:
            with open(file_path, 'r') as file:
                return file.read().splitlines()
    return []

# Create a custom script wrapper
def create_script_wrapper(script_name):
    wrapper_content = f"""#!/usr/bin/env python3
import os, sys
script_path = os.path.join(os.path.dirname(__file__), '{script_name}')
os.execv(sys.executable, [sys.executable, script_path] + sys.argv[1:])
"""
    return wrapper_content

setuptools.setup(
    name=pkgname,
    version=get_version(),
    author="Dirk Petersen",
    author_email="no-email@no-domain.com",
    description=appdesc,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{gitrepos}",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: HPC Users",
        "Topic :: System :: Distributed Computing"
        "Topic :: Utilities"        
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13", 
    ],
    python_requires=pyreq,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'tsqueue = slurm-gui.tsqueue:main',
        ],
    },
    cmdclass={
        'install_scripts': lambda self: [
            (script, create_script_wrapper(script))
            for script in self.distribution.entry_points['console_scripts']
        ]
    }
)