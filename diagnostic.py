
import os
import subprocess

def check():
    results = []
    results.append("Diagnostic Report")
    results.append("=================")
    
    sunshine_path = shutil.which('sunshine') or '/usr/sbin/sunshine'
    results.append(f"Sunshine path: {sunshine_path}")
    
    if os.path.exists(sunshine_path):
        try:
            ldd_out = subprocess.check_output(['ldd', sunshine_path], stderr=subprocess.STDOUT, text=True)
            results.append("\nLDD Output:")
            results.append(ldd_out)
        except Exception as e:
            results.append(f"\nError running ldd: {e}")
    else:
        results.append("Sunshine binary not found!")

    results.append("\nICU Libraries in /usr/lib:")
    try:
        libs = [f for f in os.listdir('/usr/lib') if 'libicuuc' in f]
        for lib in sorted(libs):
            path = os.path.join('/usr/lib', lib)
            is_link = os.path.islink(path)
            target = os.readlink(path) if is_link else "regular file"
            results.append(f"  {lib} -> {target}")
    except Exception as e:
        results.append(f"Error listing /usr/lib: {e}")

    with open('diagnostic_results.txt', 'w') as f:
        f.write('\n'.join(results))

import shutil
check()
