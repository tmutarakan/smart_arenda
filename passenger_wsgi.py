import sys
import os


INTERP = os.path.expanduser("/var/www/u2672974/data/smartenv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)


sys.path.append(os.getcwd())


from app import application
