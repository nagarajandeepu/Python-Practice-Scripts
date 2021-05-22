def get_keys(self, path, i=0):
    try:
        yield winreg.EnumValue(winreg.OpenKey(winreg.HKEY_CURRENT_USER, path), i)
        yield from get_keys(path, i+1)
    except WindowsError as err:
        pass


for name, value, type in n get_keys(r"Local Settings\Software\Microsoft\Windows\Shell\MuiCache"):
    print(f"{name} => {value} ({type})")