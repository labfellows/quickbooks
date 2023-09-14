# LabFellows QuickBooks

This repository provides scripting files in python for Barcode integration through Fusion API

Our Fusion API documentation can be accessed here: https://apidocs.labfellows.com


Find the steps below to setup a local python virtual environment using PyCharm and run this project

Step 1: Install Pycharm IDE community edition

Step 2: Install Python 3.8

Step 3: Open your project from Pycharm

Step 4: Create a new directory venv_qb (virtual environment) under your project folder and make sure that you have requirements.txt file

Step 5: Go to Pycharm Preferences => Project Interpreter => Click on the setting icon in the top right corner => Add (A new window will be shown) => New Environment => Location > choose the venv_qb file path => base Interpreter > choose python 3.8

Step 6: create .env file with appropriate values from .env.example. Labfellows members can use the values from below link
https://drive.google.com/drive/folders/1a9oVEhuGGkw9jf-XvMRXrUWCZcBj4_EA?usp=sharing

Step 7: Open terminal, go to your project folder > venv_qb > bin and run the following command.

command: source activate

Step 8: Go to project folder where you can see requirements.txt file and run the following command

command: pip3 install -r requirements.txt  (This will install the required python libraries for the project mentioned in the reqiuirements.txt file)
