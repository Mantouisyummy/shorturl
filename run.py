import uvicorn
import sys
import subprocess

command = [
    sys.executable,
    '-m',
    'pip',
    'install',
    '--requirement',
    'requirements.txt',
]

subprocess.check_call(command)

uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug",
                workers=1, limit_concurrency=1, limit_max_requests=1)
