
import subprocess
import os
from pathlib import Path

def test_start():
    config_dir = Path.home() / '.config' / 'big-remoteplay' / 'sunshine'
    config_file = config_dir / 'sunshine.conf'
    log_path = Path.cwd() / 'test_sunshine.log'
    
    env = os.environ.copy()
    if 'DISPLAY' not in env: env['DISPLAY'] = ':0'
    
    cmd = ['/usr/sbin/sunshine', str(config_file)]
    
    print(f"Running: {' '.join(cmd)}")
    print(f"CWD: {config_dir}")
    
    try:
        with open(log_path, 'w') as log_file:
            process = subprocess.Popen(
                cmd,
                text=True,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                env=env,
                cwd=str(config_dir)
            )
            try:
                process.wait(timeout=5)
                return f"Process exited with code {process.returncode}"
            except subprocess.TimeoutExpired:
                process.terminate()
                return "Process started and ran for 5 seconds (success?)"
    except Exception as e:
        return f"Exception: {e}"

result = test_start()
with open('test_start_result.txt', 'w') as f:
    f.write(result)
