# Don't forget to schedule the task on system startup
import time
from pathlib import Path
from datetime import datetime as dt

#C:/Windows/System32/drivers/etc/hosts

hosts_path = Path('etc/hosts')
localhost_ip = '127.0.0.1'

websites_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(localhost_ip + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()

        print('Fun hours...')
    time.sleep(5)
