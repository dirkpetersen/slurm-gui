# Slurm made easy with slurm-gui ! 

**GUI/TUI frontends to squeue, sbatch and srun using the fabulous textual TUI framework**

![PyPI](https://img.shields.io/pypi/v/slurm-gui)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/slurm-gui)
![PyPI - License](https://img.shields.io/pypi/l/slurm-gui)

Install with `python3 -m pip install slurm-gui` and then run `tsqueue` on a node with Slurm installed to get a list of slurm jobs (tsbatch and tsrun are coming...)

![image](https://github.com/dirkpetersen/slurm-gui/assets/1427719/d56d9b88-0ff4-49cf-a563-b21d4aa2d9e0)

use the mouse or keys to scroll up and down and hit enter to get more details (from squeue and sstat or sacct).

If a job is pending,  get a very detailed reason for it: 

![image](https://github.com/dirkpetersen/slurm-gui/assets/1427719/4889ec08-dee6-406d-b914-e8a79690d69c)

Get a long list of information. squeue info comes first but if you scroll down, you will get also all the info provided by sstat

if a job is running, it will offer you to cancel it plus an error message for jobs you cannot kill

![image](https://github.com/dirkpetersen/slurm-gui/assets/1427719/8c27c8c0-8a00-47e9-be9a-1346ff2cbab5)

