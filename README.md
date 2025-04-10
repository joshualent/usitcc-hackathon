# hackathon Connection App
This is a group of 4 

## Installation
> Installation steps are different depending on which OS and terminal you are using
> Use Python 3 to run this project, `python3` if on Mac or Linux, might need to use `python` if on windows
1. To run this project, please create a virtual environment using Python's venv library
```
# Windows
python -m venv .venv
# Mac or Linux
python3 -m venv .venv
```
2. Activate your virtual environment
```
# Windows - powershell
.venv/Scripts/Activate.ps1
# Windows - command prompt
.venv/Scripts/Activate/bat
# Mac or Linux
source .venv/bin/activate
```
3. install `requirements.txt` using pip
```
pip install -r requirements.txt
```
4. Run database migrations
```
python3 manage.py migrate
```
5. Run the server and look around
```
python3 manage.py runserver
```
6. Click on the link shown in terminal which will take you to the app! Look around the different URLs

Deployed app url: https://usitcc-hackathon-08637577cb26.herokuapp.com/