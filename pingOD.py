import subprocess
import time

def pingerOD(location,pingcount):
    if(pingcount < 1000 and pingcount >0 and pingcount):
        for i in range(pingcount):
            subprocess.call(["ping",str(location)])
        return 0

pingerOD("martinchildrensbooks.com", 5)