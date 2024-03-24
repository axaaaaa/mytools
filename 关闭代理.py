import winreg

def set_proxy(state):
    """
    Turn on or off Windows proxy server.
    Args:
        state: bool. True for turning on the proxy, False for turning it off.
    """
    # open the registry editor and navigate to the Internet Settings key
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    internet_settings_key = winreg.OpenKey(registry, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_WRITE)

    # set the ProxyEnable value to 1 (on) or 0 (off)
    if state:
        winreg.SetValueEx(internet_settings_key, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
    else:
        winreg.SetValueEx(internet_settings_key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)

    # close the key and the registry
    winreg.CloseKey(internet_settings_key)
    winreg.CloseKey(registry)

# turn on the proxy server
#set_proxy(True)

# turn off the proxy server
set_proxy(False)
