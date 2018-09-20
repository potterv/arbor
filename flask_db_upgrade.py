import os
import subprocess

if __name__=="__main__":
    proc = subprocess.Popen("flask db upgrade",shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()
    print(out)


