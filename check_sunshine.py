
import subprocess
import os

def check():
    try:
        out = subprocess.check_output(['/usr/sbin/sunshine', '--version'], stderr=subprocess.STDOUT, text=True)
        with open('sunshine_version.txt', 'w') as f:
            f.write(out)
    except subprocess.CalledProcessError as e:
        with open('sunshine_version.txt', 'w') as f:
            f.write(f"Error: {e.output}")
    except Exception as e:
        with open('sunshine_version.txt', 'w') as f:
            f.write(f"Exception: {str(e)}")

check()
