import uvicorn
import sys
import subprocess
import gunicorn

command = [
    sys.executable,
    '-m',
    'pip',
    'install',
    '--requirement',
    'requirements.txt',
]

command2 = [
    'gunicorn',
    'main:app',
    '--workers',
    '4',
    '--worker-class',
    'uvicorn.workers.UvicornWorker',
    '--bind',
    '0.0.0.0:80'
]

subprocess.check_call(command)

subprocess.check_call(command2)