#!d:\PycharmProjects\arbor\venv\Scripts\python
import subprocess
from arbor.app.models.dbModel import Employee
from arbor.app import Config

import os



tables=['Employee']



def dbUpgrade(*tables):

 '''
    proc = subprocess.Popen("cmd \"set FLASK_APP\"", shell=True, stdout=subprocess.PIPE)
    out = proc.stdout.readlines()
    print(out)
 '''


 for table in tables:
        proc = subprocess.Popen("flask db migrate -m  \""+str(table)+" table\"", shell=True, stdout=subprocess.PIPE)
        out = proc.stdout.readlines()
        print(out)

if __name__=="__main__":

    u = Employee(login='susan', email='susan@example.com')
    print(u)
    dbUpgrade(tables)
