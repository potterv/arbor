import os
import subprocess
from arbor.app.models.dbModel import Employee
tables=['Employee']

def dbUpgrade(*tables):
    proc = subprocess.Popen("export FLASK_APP=mainArbor.py", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()
    print(out)

    for table in tables:

        proc = subprocess.Popen("flask db migrate -m  \""+str(table)+" table\"", shell=True, stdout=subprocess.PIPE)
        out = proc.stdout.readlines()
        print(out)

if __name__=="__main__":

    u = Employee(login='susan', email='susan@example.com')
    print(u)
    dbUpgrade(tables)
