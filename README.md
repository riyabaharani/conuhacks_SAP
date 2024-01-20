# Setting up the virtual environment
Download virtualenv with:
`pip install virtualenv`

Setup the virtual environment folder in the root folder using the following command:
`python<version> -m venv .venv`

## Activating the virtual environment
For Windows cmd
`.venv\Scripts\activate.bat`
Powershell
`.venv\Scripts\Activate.ps1`

Linux
`source .venv/bin/activate`

## Installation and venv deactivation
Run `pip install -r requirements.txt`
To deactivate: `deactivate`