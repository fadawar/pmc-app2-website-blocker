import time
from datetime import datetime as dt

hosts_path = './hosts'
# hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
websites = ["www.facebook.com", "facebook.com"]

while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("Fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
