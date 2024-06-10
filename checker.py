import aiohttp
import asyncio
import requests 
import threading 
import random
import os
import random
import string
from colorama import Fore
from colorama import Style
from colorama import init

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
rst = Fore.RESET

def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass


async def postREQ1(session, url, headers=None, data=None, return_type='status', proxy=None):
    try:
        async with session.post(url, headers=headers, data=data, proxy=proxy) as response:
            if return_type == 'status':
                return response.status
            elif return_type == 'text':
                return await response.text()
    except:
        pass

def generate4user():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    random_string = random.choice(lower)  # Add 1 random lowercase letter
    random_string += random.choice(upper)  # Add 1 random uppercase letter
    random_string += ''.join(random.choices(upper + digits, k=2))  # Add 2 random characters (uppercase or digits)
    
    random_string = ''.join(random.sample(random_string, len(random_string))).lower()  # Shuffle and convert to lowercase
    return random_string


def generate3user():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    random_string = random.choice(lower)  # Add 1 random lowercase letter
    random_string += random.choice(upper)  # Add 1 random uppercase letter
    random_string += ''.join(random.choices(upper + digits, k=1))  # Add 1 random characters (uppercase or digits)
    
    random_string = ''.join(random.sample(random_string, len(random_string))).lower()  # Shuffle and convert to lowercase
    return random_string


async def checkY(username,proxy):
    with open("success.txt","a+") as output :
        try:
            url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
            data1 = '{"username":"'+username+'"}'
            header1 = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/123.0","Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate","Content-Type": "application/json","X-Discord-Locale": "en-US","X-Debug-Options": "bugReporterEnabled","Origin": "https://discord.com","Referer": "https://discord.com/register","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin","Te": "trailers"}

            async with aiohttp.ClientSession() as session:
                result = await postREQ1(session, url, headers=header1, data=data1, return_type='text', proxy=proxy)
                if '"taken":false' in result:
                    print(f"{fg}[*] {gr}{username} {fg}Is Available {rst}")
                    output.write(f"{username}")
                elif '"taken":true' in result:
                    print(f"{fr}[*] {gr}{username} {fr} Is Taken{rst}")
        except:
            pass

async def main():
    try:
        proxyFile = input(f"{fr}[*] Select ProxyList : {rst}")
        threads = input(f"{fr}[*] THREADS  : {rst}")
        fileProxy = open(proxyFile,"r+").readlines()
        option = input(f"{fr}[*] Looking For {gr}4,3 {fr}User ? : {rst}")

        if option == "3":
            while True:
                account_tasks = []
                for _ in range(int(threads)):
                    proxy = f"http://{random.choice(fileProxy).strip()}"
                    username = generate3user()
                    account_tasks.append(checkY(username,proxy))
                await asyncio.gather(*account_tasks)
        if option == "4":
            while True:
                account_tasks = []
                for _ in range(int(threads)):
                    proxy = f"http://{random.choice(fileProxy).strip()}"
                    username = generate4user()
                    account_tasks.append(checkY(username,proxy))
                await asyncio.gather(*account_tasks)
    except:
        pass


if __name__ == "__main__":
    clear()
    print('''
_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██
          [*] Discord CHECKER V1.0 (37)
          [*] Coded By M2NS
 ''')
    asyncio.run(main())
