from ctypes import Structure, windll, c_uint, sizeof, byref
import subprocess, time
tot_time = 0
#flag = True
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
while True:
    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0
    tot_time = get_idle_duration()
    print(tot_time)
    if int(tot_time) >= 60:
        print("Hi, it's been a minute. Locking the screen for your Safety!")
        time.sleep(1)
        cmd='rundll32.exe user32.dll, LockWorkStation'
        subprocess.call(cmd)
        break