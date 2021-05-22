import subprocess, sys, os
p = subprocess.Popen(["powershell.exe", r"C:\Users\nagar\Downloads\bluetooth.ps1"], stdout=sys.stdout)
p.communicate()
