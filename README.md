# Goal
The programming challenge is to find a circle that encompasses a 
given cloud of points X in two dimensions. There is two algorithms in 
this repository, both with linear runtime `O(n)`. The method(s) used 
are described in the jupyter notebooks.

## Set up your virtual environment
Let's assume you have python3.7 and the package `venv` installed. You can create 
a virtual environment in the folder `env/` with the following command:
```bash
python3.7 -m venv env
```
Then activate your environment and install the requirements with:
```bash
source env/bin/activate
python -m pip install -r requirements.txt
```
## Run
The program will run and draw the calculated circle around the point cloud. 
```bash
python start.py
```
## Testing
```bash
python -m pytest
```
