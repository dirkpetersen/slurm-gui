import os, setuptools

pkgname = 'slurm-gui'
appdesc = "GUI/TUI frontends to squeue, sbatch and srun using the fabulous textual TUI framework"
gitrepos = 'dirkpetersen/slurm-gui'
pyreq = '>=3.8'
myscripts = ['bin/tsqueue']

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
    print('os.listdir():', os.listdir())
    for root, dirs, files in os.walk("."):
        file_path = ''
        if "requirements.txt" in files:
            file_path = os.path.join(root, "requirements.txt")
        elif "requires.txt" in files:
            file_path = os.path.join(root, "requires.txt")        
        if file_path:
            print('requirements.txt:', file_path)
            with open(file_path, 'r') as file:
                return file.read().splitlines()
    return []

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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=pyreq,
    install_requires=read_requirements(),
    scripts=myscripts,
)
