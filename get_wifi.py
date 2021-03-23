# library
import subprocess
# constant
profile = "All User Profile"
keyContent = "Key Content"
resWifi = subprocess.check_output(['netsh', 'wlan', 'show',
                                   'profiles']).decode('utf-8').split('\n')
resWifi = [i.split(":")[1][1:-1] for i in resWifi if profile in i]
for i in resWifi:
    res = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i,
         'key=clear']).decode('utf-8').split('\n')
    res = [wifi.split(":")[1][1:-1] for wifi in res if keyContent in wifi]
    try:
        print("{:<30}|  {:<}".format(i, res[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
resWifi = input("")