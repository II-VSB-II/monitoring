#!/usr/bin/env python3.6
import os
import sys

if __name__ == "__main__":
    
    if sys.argv[1]=="setKey":
       import random
       secretKey=''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
       file=open(os.getcwd()+"/monitoring/settings.py","r")
       data=file.read()
       file.close()
       data=data.replace('{{setKey}}',secretKey)
       file1=open(os.getcwd()+"/monitoring/settings.py","w")
       file1.write(data)
       file1.close()      
       sys.exit() 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoring.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
