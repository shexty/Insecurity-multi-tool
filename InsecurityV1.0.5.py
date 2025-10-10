# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import base64
import cloudscraper
import concurrent
import csv
import datetime
import discord
import io
import json
import logging
import os
import pandas as pd
import pathlib
import re
import requests
import shutil
import ssl
import subprocess
import sys
import threading
import time
import traceback
import urllib3
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from discord import SyncWebhook
from logging import ERROR, INFO, basicConfig, error, info
from PIL import Image
from pypresence import Presence
from requests.structures import CaseInsensitiveDict
from requests_toolbelt.multipart.encoder import MultipartEncoder
from rich.console import Console
from rich.prompt import IntPrompt
from rich.table import Table
from rich.text import Text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from struct import pack
from typing import List, Tuple, Union
import uuid
import random
thread_pool_ref = concurrent.futures.ThreadPoolExecutor
init(convert=True)
RESET = "\033[0m"
inputting = False
input_lock = threading.Lock()
rpc = False
b_solved = 0
p_solved = 0
b_ready = 0
b_total = 0
p_ready = 0
p_total = 0
def b_readywait():
    while True:
        if b_ready == b_total:
            break
        time.sleep(1)
def p_readywait():
    while True:
        if p_ready == p_total:
            break
        time.sleep(1)
sent = 0
def ebay():
    print("Enter the Ebay product url without url parameters: ",end = '')
    url = input()
    print("How much views shall we send? Input: ", end = '')
    amount = input()
    try:
        amount = int(amount)
    except:
        print("Not a valid number! Please try again")
        ebay()
    print("Sending views...")
    def send(amount,url):
        global sent
        item = url.split("/")[-1]
        headers = {
                "authority": "www.ebay.co.uk",
                "method": "GET",
                "path": f"/itm/{item}",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        for i in range(amount):
            time.sleep(0.5)
            resp = requests.get(url,verify=True,headers=headers)
            if resp.status_code == 200:
                sent += 1
                if sent%50 == 0:
                    print(sent)
            else:
                print(resp.status_code)
    for i in range(10):
        thread = threading.Thread(target=send,args=(amount,url,))
        thread.start()
        time.sleep(0.5)
    print(f"Successfully sent {sent} views!")
    sent = 0
    main_menu()

def main_menu():
    global rpc
    def custom_rpc():
        RPC.update(
            large_image = "icon", #name of your asset
            small_image = "icon",
            state='Exploring the world of code',
            details= f"V{current_version} - Username: {username}",
            large_text = "Insecurity",
            start = time.time()
        )
    if not rpc:
        client_id = "INSERT ID" #your application's client id
        try:
            RPC = Presence(client_id)
            RPC.connect()
            custom_rpc()
        except:
            pass
    rpc = True

    #timestamp = get_timestamp()
    #print(f"\033[38;5;94m[{timestamp}]{RESET} {e}")
    time.sleep(0.1)
    global username
    os.system("cls")
    os.system(f"title Insecurity [V{current_version}] ^| Main Menu ^| Username: {username}")
    text = f"""
\033[38;5;94m██▓ ███▄    █   ██████ ▓█████  ▄████▄   █    ██  ██▀███   ██▓▄▄▄█████▓▓██   ██▓
\033[38;5;94m▓██▒ ██ ▀█   █ ▒██    ▒ ▓█   ▀ ▒██▀ ▀█   ██  ▓██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
\033[38;5;94m▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒███   ▒▓█    ▄ ▓██  ▒██░▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
\033[38;5;94m░██░▓██▒  ▐▌██▒  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░
\033[38;5;94m░██░▒██░   ▓██░▒██████▒▒░▒████▒▒ ▓███▀ ░▒▒█████▓ ░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
\033[38;5;94m░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒ 
\033[38;5;94m ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
\033[38;5;94m ▒ ░   ░   ░ ░ ░  ░  ░     ░   ░         ░░░ ░ ░   ░░   ░  ▒ ░  ░       ▒ ▒ ░░  
\033[38;5;94m ░           ░       ░     ░  ░░ ░         ░        ░      ░            ░ ░     
                            ░                                        ░ ░     """
    lines = text.split("\n")
    console_width = shutil.get_terminal_size().columns
    max_line_length = max(len(line) for line in lines)
    spaces = (console_width - max_line_length) // 2
    for line in lines:
        print(' ' * spaces + line)
    print("\033[0m")
    text = f"""
    \033[38;5;94mChoose an option:
    \033[38;5;94m[1] Parcel tracker
    \033[38;5;94m[2] Revolut Business CC Export
    \033[38;5;94m[3] Revolut Business CC Gen
    \033[38;5;94m[4] Icloud generator
    \033[38;5;94m[5] 3DS Solver Personal
    \033[38;5;94m[6] 3DS Solver Business
    \033[38;5;94m[7] Ebay View Sender
    \033[38;5;94m[8] Exit
    \033[38;5;94mOption: {RESET}"""

    lines = text.split("\n")
    console_width = shutil.get_terminal_size().columns
    max_line_length = max(len(line) for line in lines)
    spaces = (console_width - max_line_length) // 2
    prompt_length = len("[1] ")
    for line in lines[:-1]:
        print(' ' * (spaces - prompt_length) + line)
    print(' ' * (spaces-prompt_length) + lines[-1],end='')
    try:
        choice = int(input())
    except:
        timestamp = get_timestamp()
        
        print(f"\n\033[38;5;94m[{timestamp}]{RESET}{Fore.RED}[X] ERROR: Invalid option! Please try again!{Fore.RESET}")
        main_menu()
    choices = [1,2,3,4,5,6,7,8]
    if choice not in choices:
        timestamp = get_timestamp()
        
        print(f"\n\033[38;5;94m[{timestamp}]{RESET}{Fore.RED}[X] ERROR: {choice} is not an option! Please try again!{Fore.RESET}")
        main_menu()
    if choice == 1:
        os.system("cls")
        parcel_tracker()
    if choice == 2:
        os.system("cls")
        business_card_genyes()
    if choice == 3:
        os.system("cls")
        business_card_genno()
    if choice == 4:
        os.system("cls")
        icloud_gen()
    if choice == 5:
        os.system("cls")
        personal_3DS()
    if choice == 6:
        os.system("cls")
        business_3DS()
    if choice == 7:
        ebay()
    if choice == 8:
        os.system("cls")
        exit()

try:
    def get_timestamp() -> str:
        timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4]
        return timestamp
    

    postcodes = []
    numbers = []
    checked = {}
    color = f'{Fore.CYAN}{Style.BRIGHT}'
    red = f'{Fore.RED}{Style.BRIGHT}'
    green = f'{Fore.GREEN}{Style.BRIGHT}'
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    # Check for updates
    iframe_url = "https://insecuritytools.com/version.txt" #insert here your url where you will store your version number to allow the auto dector to work
    headers = {
    'authority': 'www.insecuritytools.com',
    'method': 'GET',
    'path': '/version.txt',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-modified-since': 'Mon, 03 Apr 2023 21:34:29 GMT',
    'if-none-match': '"0e6fff72d488f27cdc7c8316fa67319a"',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
    iframe_response = requests.get(iframe_url,headers=headers)
    iframe_soup = BeautifulSoup(iframe_response.content, "html.parser")
    latest_version = iframe_soup.text.strip()
    current_version = '1.0.5' # Change this to the version number of your bot
    if latest_version != current_version:
        yesno = input("There is a new update would you like to install it? y/n: ")
        if yesno == "y":
            os.system("cls")
            timestamp = get_timestamp()
            
            print(f"\033[38;5;94m[{timestamp}]{RESET}downloading newest version please wait")
            # Download the latest version of the bot
            download_url = 'https://www.insecuritytools.com' #/download/Insecuirty[V1.0.5].exe'
            # Define the filename for the downloaded file
            filename = 'Insecurity[V1.0.6].exe'
            # Download the latest version of the program
            response = requests.get(download_url, stream=True)
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            # Install the latest version of the program
            subprocess.call(['msiexec', '/i', filename, '/quiet'])
            time.sleep(2)
            new = os.path.join(exe_dir, "/Insecuirty[V1.0.6].exe")
            if os.path.exists(new):
                timestamp = get_timestamp()
                print(f"\033[38;5;94m[{timestamp}]{RESET} Successfully installed press any key to exit")
                start_time = time.time()
                input()
                timestamp = get_timestamp()
                print(f"\033[38;5;94m[{timestamp}]{RESET} Exiting...")
                os.exit(0)
            else: 
                timestamp = get_timestamp()
                
                print(f"\033[38;5;94m[{timestamp}]{RESET} Successfully installed!\nPress any key to exit")
                start_time = time.time()
                while True:
                    if input() != "":
                        break
                    if time.time() - start_time >= 3:
                        break
                timestamp = get_timestamp()
                
                print(f"\033[38;5;94m[{timestamp}]{RESET} Exiting...")
    def get_hwid():
        if sys.platform == "darwin": #mac
            proc1 = subprocess.Popen(['ioreg', '-rd1', '-c', 'IOPlatformExpertDevice'], stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(['grep', 'IOPlatformUUID'], stdin=proc1.stdout, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            proc1.stdout.close()
            out, err = proc2.communicate()
            hwid = out.decode('utf-8').split()[-1].strip('"')

        elif "win" in sys.platform: #windows
            try:
                hwid = str(subprocess.check_output('wmic csproduct get UUID')).split()[1].strip('\\r\\n')
            except:
                from uuid import getnode as get_mac
                hwid = str(get_mac)

        elif sys.platform == "linux" or sys.platform == "linux2": #linux
            hwid = os.popen('cat /etc/machine-id').read().strip()

        else:
            hwid = "idk"

        return hwid
    
    def start():
    
        if not os.path.exists("config.json"):
            key = input("please input your license key: ")
            open("config.json","w")
            settings_setup = {"Delivered_webhook":"Enter webhook url for delivered parcels here!","Error_webhook":"Enter webhook url for error logs here!","Revolut_webhook":"Enter webhook url for Revolut 3DS solves here!","delay":500,"Key":""+key+""}
            json.dump(settings_setup,open("config.json","w",encoding = 'utf-8'),indent = 4)
            timestamp = get_timestamp()
                
            print(f"\033[38;5;94m[{timestamp}]{RESET} Checking license key please wait")
            url = "https://api.whop.com/api/v2/memberships/"+key+""
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer yj1RkkxE8WMblcZy0lgz5GbCMpXpXe1oXKbvZ-0EeaM"
            }
            response = requests.get(url, headers=headers).json()
            test = response['valid']
            global username
            username = response["discord"]["username"]
            metadata=  response["metadata"]
            hwid = get_hwid()
            if len(metadata) != 0:
                if metadata["HWID"] != hwid and metadata["HWID"] != None :
                    print("Your HWID does not match! Exiting in 5s...")
                    time.sleep(5)
                    exit()
            time.sleep(10)
            if test == True:
                url = f"https://api.whop.com/api/v2/memberships/{key}?expand="
                payload = {"metadata": {"HWID": f"{hwid}"}}
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "Authorization": "Bearer yj1RkkxE8WMblcZy0lgz5GbCMpXpXe1oXKbvZ-0EeaM"
                }

                response = requests.post(url, json=payload, headers=headers)
                print(response.json())
                time.sleep(10)
                timestamp = get_timestamp()
                
                print(f"\033[38;5;94m[{timestamp}]{RESET} Key has been authenticated redirecting to program")
                #os.system("cls")
                main_menu()
        else:
            print("here")
            timestamp = get_timestamp()
            
            print(f"\033[38;5;94m[{timestamp}]{RESET} Checking license key please wait")
            keycheck = json.load(open("config.json"))
            key = keycheck["Key"]
            if key == "":
                print("No license key found! Please enter your key here:", end = ' ')
                key = input()
                keycheck["Key"] = key
                json.dump(keycheck,open("config.json","w",encoding = 'utf-8'),indent = 4)
            url = "https://api.whop.com/api/v2/memberships/"+key+""
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer yj1RkkxE8WMblcZy0lgz5GbCMpXpXe1oXKbvZ-0EeaM"
            }
            response = requests.get(url, headers=headers).json()
            test = response['valid']
            username = response["discord"]["username"]
            metadata = response["metadata"]
            hwid = get_hwid()
            if len(metadata) != 0:
                if metadata["HWID"] != hwid and metadata["HWID"] != None :
                    print("Your HWID does not match! Exiting in 5s...")
                    time.sleep(5)
                    exit()
            if test == True:
                url = f"https://api.whop.com/api/v2/memberships/{key}?expand="
                payload = {"metadata": {"HWID": f"{hwid}"}}
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "Authorization": "Bearer yj1RkkxE8WMblcZy0lgz5GbCMpXpXe1oXKbvZ-0EeaM"
                }

                response = requests.post(url, json=payload, headers=headers)
                timestamp = get_timestamp()
                
                print(f"\033[38;5;94m[{timestamp}]{RESET} Key has been authenticated redirecting to program")
                #os.system("cls")
                main_menu()
    
    def start_console():
        thr = threading.Thread(target=console_title)
        thr.start()


    def personal_3DS():
        global p_total
        
        os.system(f"title Insecurity [V{current_version}] ^| Personal 3DS Solver ^| Username: {username}")
        text = f"""
\033[38;5;94m ██▀███  ▓█████ ██▒   █▓    ██▓███  ▓█████  ██▀███    ██████  ▒█████   ███▄    █  ▄▄▄       ██▓         ██████  ▒█████   ██▓  ██▒   █▓▓█████  ██▀███  
\033[38;5;94m▓██ ▒ ██▒▓█   ▀▓██░   █▒   ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒████▄    ▓██▒       ▒██    ▒ ▒██▒  ██▒▓██▒ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
\033[38;5;94m▓██ ░▄█ ▒▒███   ▓██  █▒░   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒██░       ░ ▓██▄   ▒██░  ██▒▒██░  ▓██  █▒░▒███   ▓██ ░▄█ ▒
\033[38;5;94m▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░   ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░         ▒   ██▒▒██   ██░▒██░   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
\033[38;5;94m░██▓ ▒██▒░▒████▒  ▒▀█░     ▒██▒ ░  ░░▒████▒░██▓ ▒██▒▒██████▒▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒░██████▒   ▒██████▒▒░ ████▓▒░░██████▒▒▀█░  ░▒████▒░██▓ ▒██▒
\033[38;5;94m░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░     ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[38;5;94m  ░▒ ░ ▒░ ░ ░  ░  ░ ░░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
\033[38;5;94m  ░░   ░    ░       ░░     ░░          ░     ░░   ░ ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░   ░   ▒     ░ ░      ░  ░  ░  ░ ░ ░ ▒    ░ ░     ░░     ░     ░░   ░ 
\033[38;5;94m   ░        ░  ░     ░                 ░  ░   ░           ░      ░ ░           ░       ░  ░    ░  ░         ░      ░ ░      ░  ░   ░     ░  ░   ░     
\033[38;5;94m                    ░                                                                                                             ░                   {RESET}"""
        lines = text.split("\n")
        console_width = shutil.get_terminal_size().columns
        max_line_length = max(len(line) for line in lines)
        spaces = (console_width - max_line_length) // 2
        print(color)
        for line in lines:
            print(' ' * spaces + line)
        if getattr(sys, 'frozen', False):
                application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        if not os.path.exists(f"{application_path}./Personal"):
            os.makedirs(f'{application_path}./Personal', exist_ok=True)
        if not os.path.exists(f"{application_path}./Personal/revolut_info.csv"):
            with open(f"{application_path}./Personal/revolut_info.csv","w") as f:
                headerList = ['Phonenumber', 'Pin', 'SelfieLocation','Nickname']
                writer = csv.DictWriter(f, fieldnames = headerList)
                writer.writeheader()
            input("Please fill in Personal/revolut_info.csv! Press enter when done!")
        if not os.path.exists(f"{application_path}./Personal/personal_sessions.csv"):
            with open(f"{application_path}./Personal/personal_sessions.csv","w") as f:
                data = ["phone","token","deviceid"]
                writer = csv.DictWriter(f, fieldnames = data)
                writer.writeheader()
                f.close()
        webhooks = json.load(open(f"{application_path}/config.json"))
        global p_webhook
        p_webhook = webhooks["Revolut_webhook"]
        if p_webhook == "Enter webhook url for Revolut 3DS solves here!":
            p_webhook = None
        with open(f"{application_path}./Personal/revolut_info.csv", 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            rev_info = {}
            i = 0
            for row in reader:
                if len(row) == 0:
                    continue
                if row[0] == "Phonenumber" and row[1] == "Pin":
                    continue
                current_list = []
                phonenumber = row[0]
                current_list.append(phonenumber)
                pin = row[1]
                current_list.append(pin)
                selfieLocation = row[2]
                current_list.append(selfieLocation)
                name = row[3]
                current_list.append(name)
                rev_info[i] = current_list
                i += 1
                p_total += 1
        with open(f"{application_path}./Personal/personal_sessions.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)
            pers_sess = {}
            i = 0
            for row in reader:
                if len(row) == 0:
                    continue
                if row[0] == "mail" and row[1] == "token":
                    continue
                current_list = []
                phoneuser = row[0]
                current_list.append(phoneuser)
                tokenuser = row[1]
                current_list.append(tokenuser)
                deviceiduser = row[2]
                current_list.append(deviceiduser)
                pers_sess[i] = current_list
                i += 1
            f.close()

        def clearConsole():
            command = 'clear'
            if os.name in ('nt', 'dos'):
                command = 'cls'
            os.system(command)


        def json_parser(body, post, pre):
            trimmed_body = body.split(post)[1]
            result = trimmed_body.split(pre)[0]
            return result


        def m54958c(i: int) -> List[int]:
            return pack('!i', i)


        def randBytes(n: int) -> List[int]:
            randbArr = [random.randint(0, 255) for _ in range(n)]
            return randbArr


        def m71692d(i: int, uuid: uuid.UUID, s: str = None) -> str:
            mo27057c = random.randint(0, 2147483647)
            j = i * mo27057c
            i3 = 0
            length = 0 if s is None else len(s.encode()) + 4
            allocate = bytearray(length + 64)

            array = bytearray(16)
            array[0:8] = pack('!Q', uuid.int >> 64)
            array[8:16] = pack('!Q', uuid.int & (2 ** 64 - 1))

            c = m54958c(mo27057c)
            if len(c) == 0:
                i3 = 8
            else:
                bArr = bytearray(len(array))
                for i5 in range(len(array)):
                    if len(array) <= len(c):
                        bArr[i5] = c[i5] ^ (array[i5] & 255)
                    else:
                        bArr[i5] = c[i5 % len(c)] ^ (array[i5] & 255)
                array = bArr

            allocate[0:8] = pack('!Q', j)
            allocate[8:12] = randBytes(4)
            allocate[12:16] = c
            allocate[16:20] = randBytes(4)
            allocate[20:28] = randBytes(8)
            allocate[28:44] = array
            allocate[44:52] = randBytes(8)
            allocate[52:56] = randBytes(4)
            allocate[56:58] = (s.encode() if s is not None else b'')
            allocate[58:] = randBytes(12)

            return base64.urlsafe_b64encode(allocate).decode()


        def gen_deviceid():
            while True:
                uuid_ = uuid.uuid4()
                bArr = m71692d(3, uuid_, None)
                if "-" in str(bArr) or "_" in str(bArr) or "==" not in str(bArr):
                    continue
                else:
                    return str(bArr)
                    break

        def post_3ds(id, cardholder_id, auth_token):
            req_url = "https://api.revolut.com/transaction/3ds"

            req_payload = {
                "cardholder_id": cardholder_id,
                "proceed": True,
                "id": id
            }

            headers = {
                "Authorization": auth_token,
                "Accept": "*/*",
                "X-Client-Version": "8.97",
                "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                "X-Timezone": "Europe/London",
                "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                "User-Agent": "Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)",
                "X-Device-Id": deviceid,
                "X-Device-Model": "iPhone9,3"
            }

            try:
                res = requests.post(req_url, json=req_payload, headers=headers)
            except requests.RequestException as e:
                print(e)
                return None

            return res.status_code

        def post_3dssession(id, cardholder_id, auth_token,deviceiduser):
            req_url = "https://api.revolut.com/transaction/3ds"
            req_payload = {
                "cardholder_id": cardholder_id,
                "proceed": True,
                "id": id
            }

            headers = {
                "Authorization": auth_token,
                "Accept": "*/*",
                "X-Client-Version": "8.97",
                "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                "X-Timezone": "Europe/London",
                "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                "User-Agent": "Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)",
                "X-Device-Id": deviceiduser,
                "X-Device-Model": "iPhone9,3"
            }

            try:
                res = requests.post(req_url, json=req_payload, headers=headers)
            except requests.RequestException as e:
                print(e)
                return None

            return res.status_code
        deviceid = gen_deviceid()
        def start_personal(index):
            global p_ready
            with open(f"{application_path}/config.json", 'r') as f:
                data = json.load(f)
                Delay = int(data["delay"])
            nickname = rev_info[index][3]
            deviceiduser = pers_sess[index][2]
            tokenuser = pers_sess[index][1]
            phoneuser = pers_sess[index][0]
            phonenumber = rev_info[index][0]
            pin = rev_info[index][1]
            if phoneuser == phonenumber:
                print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {name} ] " + "Session found ! Waiting to start 3ds..." + RESET)
                p_ready += 1
                p_readywait()
                print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {name} ] " + "Starting 3ds !" + RESET)
                at = tokenuser

                if at == "":
                    time.sleep(3)
                    exit(1)

                auth_token = "Basic " + at

                while True:
                    global p_solved
                    Delay = json.load(open(f"{application_path}/config.json"))["delay"]
                    os.system(f"title Insecurity [V{current_version}] ^| Personal 3DS Solver ^| Username: {username} ^| Delay: {Delay} ^| Solved: {p_solved}")
                    req_url = "https://api.revolut.com/transaction/3ds"

                    headers = {
                        "Authorization": auth_token,
                        "X-Client-Version": "8.97",
                        "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                        "X-Timezone": "Europe/London",
                        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                        "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                        "Accept": "*/*",
                        "User-Agent": "Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)",
                        "X-Device-Id": deviceiduser,
                        "X-Device-Model": "iPhone9,3"
                    }

                    res = requests.get(req_url, headers=headers)

                    body = res.text

                    if "cardholder" in body:

                        id = json_parser(body, '"id":"', '",')
                        cardholder_id = json_parser(body, '"cardholder_id":"', '",')
                        amount = json_parser(body, 'amount":-', ',"currency')
                        manufacturer = json_parser(body, '"name":"', '"}')

                        charged_amount = float(amount) / 100

                        accept_challenge = post_3dssession(id, cardholder_id, auth_token, deviceiduser)

                        if accept_challenge == 200:
                            print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + str(charged_amount) + "€ & " + manufacturer + " -> Accepted !")
                            webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1089319630679584850/dRnfCGsc8drjw8jbKudWzHr9GNASqAbablM98CKuQyRQ16iPFSNWl9Ux5OGBv2dpHQ9_")
                            embed = discord.Embed(
                                title = "[Insecurity] 3DS Challenge Completed",
                                color = 0x7c25ff
                            )
                            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            #embed.add_field(name = "Bank",value = "Revolut Personal",inline=False)
                            embed.add_field(name="Merchant",value=manufacturer,inline=False)
                            embed.add_field(name="Amount",value=f'£{str(charged_amount)}',inline=False)
                            #embed.add_field(name="Account Nickname",value=nickname,inline=False)
                            embed.set_footer(text = "3DS Solved!")
                            p_solved += 1
                            os.system(f"title Insecurity [V{current_version}] ^| Business 3DS Solver ^| Username: {username} ^| Solved: {p_solved}")
                            webhook.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            if p_webhook != None:
                                webhook2 = SyncWebhook.from_url(p_webhook)
                                embed = discord.Embed(
                                    title = "[Insecurity] 3DS Challenge Completed",
                                    color = 0x7c25ff
                                )
                                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                embed.add_field(name = "Bank",value = "Revolut Personal",inline=False)
                                embed.add_field(name="Merchant",value=manufacturer,inline=False)
                                embed.add_field(name="Amount",value=f'£{str(charged_amount)}',inline=False)
                                embed.add_field(name="Account Nickname",value=nickname,inline=False)
                                embed.set_footer(text = "3DS Solved!")
                                webhook2.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            continue

                        else:
                            print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "3ds Failed, Retry !")
                            webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1089319630679584850/dRnfCGsc8drjw8jbKudWzHr9GNASqAbablM98CKuQyRQ16iPFSNWl9Ux5OGBv2dpHQ9_")
                            embed = discord.Embed(
                                title = "[Insecurity] 3DS Challenge Failed",
                                description  = "Please retry.",
                                color = 0x7c25ff
                            )
                            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            embed.set_footer(text = "3DS Failed!")
                            webhook.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            if p_webhook != None:
                                webhook2 = SyncWebhook.from_url(p_webhook)
                                webhook2.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                            continue

                    else:
                        time.sleep(Delay/1000)
                        print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "No 3ds Found, retrying...")
                        continue
            else: 
                signinheaders = {
                    'Host': 'api.revolut.com',
                    'Accept': '/',
                    'X-Client-Version': '8.97',
                    'X-Timezone': 'Europe/London',
                    'Accept-Language': 'en-GB;q=1.0, en-US;q=0.9',
                    'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
                    'Content-Type': 'application/json',
                    'User-Agent': 'Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)',
                    'X-Device-Id': deviceid,
                    'Connection': 'keep-alive',
                    'X-Device-Model': 'iPhone9,3'}

                loginstep1 = {
                    'phone': phonenumber,
                    'password': pin,
                }

                requests.post("https://api.revolut.com/signin",headers=signinheaders, json=loginstep1) #signin
                smscode = input(
                    color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Input SMS Code -> " + RESET)
                time.sleep(1)
                payload = {
                    'phone': phonenumber,
                    'password': pin,
                        'code': smscode}
                sms = requests.post("https://api.revolut.com/signin",
                                    headers=signinheaders, json=payload)
                accessToken = sms.json()['token']['accessCode']
                userId = sms.json()['user']['id']

                idencode = f"{userId}:{accessToken}"
                basicid = base64.b64encode(idencode.encode('utf-8'))
                authbasic = str(basicid, 'utf-8')

                print(color +
                    f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Uploading Selfie" + RESET)
                selfieLocation = rev_info[index][2]
                selfiepath = f'f"{application_path}./Personal/{selfieLocation}'

                file = open(selfiepath, "rb")
                files = {
                    'selfie': file,
                }

                #file_size = os.path.getsize(f'{selfiepath}')
                headers = {
                    'Host': 'api.revolut.com',
                    'authorization': f'Basic {authbasic}',
                    'accept': '/',
                    'x-client-version': "8.97",
                    'x-timezone': 'Europe/London',
                    'Accept-Language': 'en-GB;q=1.0, en-US;q=0.9',
                    'cache-control': 'no-cache',
                    'User-Agent': 'Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)',
                    'X-Device-Id': deviceid,
                    'Connection': 'keep-alive',
                    'X-Device-Model': 'iPhone9,3'
                }
                headers = headers
                body = file
                selfiepost = requests.post(
                    'https://api.revolut.com/biometric-signin/selfie', files=files, headers=headers)
                selfiejson = selfiepost.json()
                selfietoken = selfiejson["id"]
                if selfiepost.status_code != 200:
                    print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Failed To Send Selfie, Exiting In 10 Seconds..." + RESET)
                    time.sleep(10)
                    sys.exit()
                else:
                    print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Successfully Submitted Selfie. Waiting For Approval..." + RESET)
                selfieapproval = requests.post(
                    f"https://api.revolut.com/biometric-signin/confirm/{selfietoken}", headers=headers)
                wait = selfieapproval.json()["estimatedTimeToComplete"].replace(
                    "PT", "").replace("S", "")
                wait = float(wait)
                time.sleep(wait)
                time.sleep(2)
                selfie2 = requests.post(
                    f"https://api.revolut.com/biometric-signin/confirm/{selfietoken}", headers=headers)

                try:
                    dstoken = selfie2.json()['token']['accessCode']
                    dsid = selfie2.json()['user']['id']
                    dsmain = f"{dsid}:{dstoken}"
                    dsmain = base64.b64encode(dsmain.encode('utf-8'))
                    dsbasic = str(dsmain, 'utf-8')
                except:
                    print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Revolut Cooldown. Please Wait and Try Again Later" + RESET)

                if selfie2.status_code != 200:
                    print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Revolut Has Declined The Selfie ! Exiting in 10 Seconds..." + RESET)
                    time.sleep(10)
                    sys.exit()
                else:
                    print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Revolut Has Accepted The Selfie ! Proceeding..." + RESET)
                    data = {
                            "phone": f"{phonenumber}",
                            "token": f"{dsbasic}",
                            "deviceid": f"{deviceid}"
                    }
                    with open(f'{application_path}/Personal/personal_sessions.csv', 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([phonenumber, auth_token, deviceid])
                print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {name} ] " + "Generated Session ! Waiting to start 3ds..." + RESET)
                p_ready += 1
                p_readywait()
                print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {name} ] " + "Starting 3ds !" + RESET)

                at = dsbasic

                if at == "":
                    time.sleep(3)
                    exit(1)

                auth_token = "Basic " + at

                print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "Start Monitoring 3ds...")

                while True:

                    req_url = "https://api.revolut.com/transaction/3ds"

                    headers = {
                        "Authorization": auth_token,
                        "X-Client-Version": "8.97",
                        "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                        "X-Timezone": "Europe/London",
                        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                        "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                        "Accept": "*/*",
                        "User-Agent": "Revolut/com.revolut.revolut 8.97 16733 (iPhone; iOS 14.8.1; sp:AAS)",
                        "X-Device-Id": deviceid,
                        "X-Device-Model": "iPhone9,3"
                    }

                    res = requests.get(req_url, headers=headers)

                    body = res.text

                    if "cardholder" in body:

                        id = json_parser(body, '"id":"', '",')
                        cardholder_id = json_parser(body, '"cardholder_id":"', '",')
                        amount = json_parser(body, 'amount":-', ',"currency')
                        manufacturer = json_parser(body, '"name":"', '"}')

                        charged_amount = float(amount) / 100

                        accept_challenge = post_3ds(id, cardholder_id, auth_token)

                        if accept_challenge == 200:
                            print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + str(charged_amount) + "£ & " + manufacturer + " -> Accepted !")
                            p_solved += 1
                            
                            continue

                        else:
                            print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "3ds Failed, Retry !")
                            continue

                    else:
                        time.sleep(Delay/1000)
                        print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ {nickname} ] " + "No 3ds Found, retrying...")
                        continue
        if len(rev_info) == 0:
            print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Personal Solver ] | [ERROR] "+ "No info filled in revolut_info.csv! Returning to main menu...")
            time.sleep(1)
            main_menu()
        for i in range(len(rev_info)):
            thread = threading.Thread(target=start_personal,args=[i])
            time.sleep(0.5)
            thread.start()
    def business_3DS():
        global b_total
        os.system(f"title Insecurity [V{current_version}] ^| Business 3DS Solver ^| Username: {username} ^| Solved: {b_solved}")
        text = f"""
\033[38;5;94m ██▀███  ▓█████ ██▒   █▓    ▄▄▄▄    █    ██   ██████  ██▓ ███▄    █ ▓█████   ██████   ██████      ██████  ▒█████   ██▓  ██▒   █▓▓█████  ██▀███  
\033[38;5;94m▓██ ▒ ██▒▓█   ▀▓██░   █▒   ▓█████▄  ██  ▓██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▒██    ▒    ▒██    ▒ ▒██▒  ██▒▓██▒ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
\033[38;5;94m▓██ ░▄█ ▒▒███   ▓██  █▒░   ▒██▒ ▄██▓██  ▒██░░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒███   ░ ▓██▄   ░ ▓██▄      ░ ▓██▄   ▒██░  ██▒▒██░  ▓██  █▒░▒███   ▓██ ░▄█ ▒
\033[38;5;94m▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░   ▒██░█▀  ▓▓█  ░██░  ▒   ██▒░██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒     ▒   ██▒▒██   ██░▒██░   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
\033[38;5;94m░██▓ ▒██▒░▒████▒  ▒▀█░     ░▓█  ▀█▓▒▒█████▓ ▒██████▒▒░██░▒██░   ▓██░░▒████▒▒██████▒▒▒██████▒▒   ▒██████▒▒░ ████▓▒░░██████▒▒▀█░  ░▒████▒░██▓ ▒██▒
\033[38;5;94m░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░     ░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
\033[38;5;94m  ░▒ ░ ▒░ ░ ░  ░  ░ ░░     ▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░   ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
\033[38;5;94m  ░░   ░    ░       ░░      ░    ░  ░░░ ░ ░ ░  ░  ░   ▒ ░   ░   ░ ░    ░   ░  ░  ░  ░  ░  ░     ░  ░  ░  ░ ░ ░ ▒    ░ ░     ░░     ░     ░░   ░ 
\033[38;5;94m   ░        ░  ░     ░      ░         ░           ░   ░           ░    ░  ░      ░        ░           ░      ░ ░      ░  ░   ░     ░  ░   ░     
\033[38;5;94m                    ░            ░                                                                                          ░                   {RESET}"""
        lines = text.split("\n")
        console_width = shutil.get_terminal_size().columns
        max_line_length = max(len(line) for line in lines)
        spaces = (console_width - max_line_length) // 2
        print(color)
        for line in lines:
            print(' ' * spaces + line)
        if not os.path.exists("./Business"):
            os.makedirs('./Business', exist_ok=True)
        if not os.path.exists("./Business/revolut_info.csv"):
            with open("./Business/revolut_info.csv","w") as f:
                headerList = ['Email', 'Pin', 'SelfieLocation','Nickname']
                writer = csv.DictWriter(f, fieldnames = headerList)
                writer.writeheader()
            input("Please fill in Business/revolut_info.csv! Press enter once done!")
        if not os.path.exists("./Business/business_sessions.csv"):
            with open("./Business/business_sessions.csv","w") as f:
                data = ["mail","token","deviceid"]
                writer = csv.DictWriter(f, fieldnames = data)
                writer.writeheader()
                f.close()
        webhooks = json.load(open("config.json"))
        p_webhook = webhooks["Revolut_webhook"]
        if p_webhook == "Enter webhook url for Revolut 3DS solves here!":
            p_webhook == None
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        with open(f"{application_path}./Business/revolut_info.csv", 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            rev_info = {}
            i = 0
            for row in reader:
                if len(row) == 0:
                    continue
                if row[0] == "Email" and row[1] == "Pin":
                    continue
                current_list = []
                email = row[0]
                current_list.append(email)
                pin = row[1]
                current_list.append(pin)
                selfieLocation = row[2]
                current_list.append(selfieLocation)
                name = row[3]
                current_list.append(name)
                rev_info[i] = current_list
                i += 1
                b_total += 1 
        with open(f"{application_path}./Business/business_sessions.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)
            bus_sess = {}
            i = 0
            for row in reader:
                if len(row) == 0:
                    continue
                if row[0] == "mail" and row[1] == "token":
                    continue
                current_list = []
                mailuser = row[0]
                current_list.append(mailuser)
                tokenuser = row[1]
                current_list.append(tokenuser)
                deviceiduser = row[2]
                current_list.append(deviceiduser)
                bus_sess[i] = current_list
                i += 1
            f.close()
        with open("config.json", 'r') as f:
            global Delay
            data = json.load(f)
            Delay = int(data["delay"])
        def clearConsole():
            command = 'clear'
            if os.name in ('nt', 'dos'):
                command = 'cls'
            os.system(command)

        def selfie_to_bytes(path: str) -> Tuple[bytes, str]:
            with open(path, "rb") as file:
                multipart_data = MultipartEncoder(
                    fields={"selfie": (path, file, "image/jpg")}
                )

                return multipart_data.to_string(), multipart_data.content_type

        def m54958c(i: int) -> List[int]:
            return pack('!i', i)

        def randBytes(n: int) -> List[int]:
            randbArr = [random.randint(0, 255) for _ in range(n)]
            return randbArr

        def m71692d(i: int, uuid: uuid.UUID, s: str = None) -> str:
            mo27057c = random.randint(0, 2147483647)
            j = i * mo27057c
            i3 = 0
            length = 0 if s is None else len(s.encode()) + 4
            allocate = bytearray(length + 64)

            array = bytearray(16)
            array[0:8] = pack('!Q', uuid.int >> 64)
            array[8:16] = pack('!Q', uuid.int & (2 ** 64 - 1))

            c = m54958c(mo27057c)
            if len(c) == 0:
                i3 = 8
            else:
                bArr = bytearray(len(array))
                for i5 in range(len(array)):
                    if len(array) <= len(c):
                        bArr[i5] = c[i5] ^ (array[i5] & 255)
                    else:
                        bArr[i5] = c[i5 % len(c)] ^ (array[i5] & 255)
                array = bArr

            allocate[0:8] = pack('!Q', j)
            allocate[8:12] = randBytes(4)
            allocate[12:16] = c
            allocate[16:20] = randBytes(4)
            allocate[20:28] = randBytes(8)
            allocate[28:44] = array
            allocate[44:52] = randBytes(8)
            allocate[52:56] = randBytes(4)
            allocate[56:58] = (s.encode() if s is not None else b'')
            allocate[58:] = randBytes(12)

            return base64.urlsafe_b64encode(allocate).decode()

        def gen_deviceid():
            while True:
                uuid_ = uuid.uuid4()
                bArr = m71692d(3, uuid_, None)
                if "-" in str(bArr) or "_" in str(bArr) or "==" not in str(bArr):
                    continue
                else:
                    return str(bArr)
                    break

        business_device_id = gen_deviceid()


        def json_parser(body, post, pre):
            trimmed_body = body.split(post)[1]
            result = trimmed_body.split(pre)[0]
            return result

        


        def post_3ds(id, auth_token1):
            req_url = "https://business-mobile.revolut.com/transaction/3ds"

            req_payload = {
                "cardholder_id": id,
                "proceed": True,
                "id": id
            }

            headers = {
                "Authorization": auth_token1,
                "Accept": "*/*",
                "X-Client-Version": "3.58.1",
                "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                "X-Timezone": "Europe/London",
                "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                "User-Agent": "Revolut/com.revolut.revolut 8.79 16014 (iPhone; iOS 14.4.2; sp:AAS)",
                "X-Device-Id": business_device_id,
                "X-Device-Model": "iPhone9,3"
            }

            try:
                res = requests.post(req_url, json=req_payload, headers=headers)
            except requests.RequestException as e:
                print(e)
                return None

            return res.status_code

        def post_3dssession(id, auth_token1, deviceiduser):
            req_url = "https://business-mobile.revolut.com/transaction/3ds"

            req_payload = {
                "cardholder_id": id,
                "proceed": True,
                "id": id
            }

            headers = {
                "Authorization": auth_token1,
                "Accept": "*/*",
                "X-Client-Version": "3.58.1",
                "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                "X-Timezone": "Europe/London",
                "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                "User-Agent": "Revolut/com.revolut.revolut 8.79 16014 (iPhone; iOS 14.4.2; sp:AAS)",
                "X-Device-Id": deviceiduser,
                "X-Device-Model": "iPhone9,3"
            }

            try:
                res = requests.post(req_url, json=req_payload, headers=headers)
            except requests.RequestException as e:
                print(e)
                return None

            return res.status_code

        def inputwait():
            global inputting
            while inputting:
                time.sleep(0.1)
        
        def business_login(index: int):
            global b_ready, b_solved
            #clearConsole()
            email = rev_info[index][0]
            try:
                mailuser = bus_sess[index][0]
            except:
                mailuser = "None"
            name = rev_info[index][3]
            if email == mailuser :
                    print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "Session Found... Waiting to start 3DS" + RESET)
                    b_ready += 1
                    b_readywait()
                    print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "Starting 3ds !" + RESET)
                    at = bus_sess[index][1]
                    auth_token1 = "Basic " + at
                    deviceiduser = bus_sess[index][2]
                    while True:
                        Delay = json.load(open("config.json"))["delay"]
                        os.system(f"title Insecurity [V{current_version}] ^| Business 3DS Solver ^| Username: {username} ^| Delay: {Delay} ^| Solved: {b_solved}")
                        req_url = "https://business-mobile.revolut.com/transaction/3ds"

                        headers = {
                            "Authorization": auth_token1,
                            "X-Client-Version": "3.58.1",
                            "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                            "X-Timezone": "Europe/London",
                            "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                            "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                            "Accept": "*/*",
                            "User-Agent": "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)",
                            "X-Device-Id": deviceiduser,
                            "X-Device-Model": "iPhone9,3"
                        }

                        res = requests.get(req_url, headers=headers)

                        body = res.text

                        if "currency" in body:
                            
                            id = json_parser(body, '"id":"', '",')
                            amount = json_parser(body, 'amount":-', ',"currency')
                            manufacturer = json_parser(body, '"name":"', '"}')

                            charged_amount = float(amount) / 100

                            accept_challenge = post_3dssession(id, auth_token1, deviceiduser)

                            if accept_challenge == 204:
                                print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  str(charged_amount) + "€ & " + manufacturer + " -> Accepted !")
                                webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1089319630679584850/dRnfCGsc8drjw8jbKudWzHr9GNASqAbablM98CKuQyRQ16iPFSNWl9Ux5OGBv2dpHQ9_")
                                embed = discord.Embed(
                                    title = "[Insecurity] 3DS Challenge Completed",
                                    color = 0x7c25ff
                                )
                                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                #embed.add_field(name = "Bank",value = "Revolut Business",inline=False)
                                embed.add_field(name="Merchant",value=manufacturer,inline=False)
                                embed.add_field(name="Amount",value=f'£{str(charged_amount)}',inline=False)
                                #embed.add_field(name="Account Nickname",value=nickname,inline=False)
                                embed.set_footer(text = "3DS Solved!")
                                webhook.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                b_solved += 1
                                os.system(f"title Insecurity [V{current_version}] ^| Business 3DS Solver ^| Username: {username} ^| Solved: {b_solved}")
                                if p_webhook != None:
                                    webhook2 = SyncWebhook.from_url(p_webhook)
                                    embed = discord.Embed(
                                    title = "[Insecurity] 3DS Challenge Completed",
                                    color = 0x7c25ff
                                    )
                                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                    embed.add_field(name = "Bank",value = "Revolut Business",inline=False)
                                    embed.add_field(name="Merchant",value=manufacturer,inline=False)
                                    embed.add_field(name="Amount",value=f'£{str(charged_amount)}',inline=False)
                                    embed.add_field(name="Account Nickname",value=name,inline=False)
                                    embed.set_footer(text = "3DS Solved!")
                                    webhook2.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                continue
                            else:
                                print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "3ds Failed, Retry !")
                                webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1089319630679584850/dRnfCGsc8drjw8jbKudWzHr9GNASqAbablM98CKuQyRQ16iPFSNWl9Ux5OGBv2dpHQ9_")
                                embed = discord.Embed(
                                    title = "[Insecurity] 3DS Challenge Failed",
                                    description  = "Please retry.",
                                    color = 0x7c25ff
                                )
                                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                embed.set_footer(text = "3DS Failed!")
                                webhook.send(embed=embed,username = 'Insecurity 3DS',avatar_url = "https://media.discordapp.net/attachments/1076443692023414795/1083715344524398623/insecurity-logo.png?width=675&height=675")
                                if p_webhook != None:
                                    webhook2 = SyncWebhook.from_url(p_webhook)
                                    webhook2.send(embed=embed)
                                continue
                        else:
                            time.sleep(Delay/1000)
                            print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "No 3ds Found, retrying...")
                            continue
            else:
                while True:
                    verify = auth_verify(email)

                    if "true" in verify:
                        inputwait()
                        global inputting
                        inputting = True
                        print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Email URl -> "+ RESET)
                        while True:
                            with input_lock:
                                link = input()
                            get_code = confirm_link(link)

                            if any(str(x) in get_code for x in range(10)):
                                confirm = auth_confirm(email, get_code)

                                if "EMPLOYEE_AUTH" in confirm:

                                    access_token = json_parser(confirm, 'accessToken":"', '","isUser')
                                    employee_id = json_parser(confirm, 'employeeId":"', '","userId')
                                    auth_token = base64.standard_b64encode(f"{employee_id}:{access_token}".encode()).decode()
                                    pin = rev_info[index][1]
                                    auth_sign = sign_in_auth(pin, auth_token)

                                    if "SELFIE" in auth_sign:
                                        selfie_access_token = json_parser(auth_sign, 'biometricAccessToken":"', '","last')
                                        auth_token = base64.standard_b64encode(f"{employee_id}:{selfie_access_token}".encode()).decode()

                                        filename = "raptuneselfie"

                                        print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Uploading Selfie"+ RESET)
                                        print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Successfully Submitted Selfie. Waiting For Approval..."+ RESET)

                                        selfie_post = post_selfie(index, auth_token, pin, selfie_to_bytes)

                                        if "firstName" in selfie_post:
                                            print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "Revolut Has Accepted The Selfie ! Proceeding..." + RESET)
                                            access_token = json_parser(selfie_post, 'accessToken":"', '","refresh')
                                            auth_token = base64.standard_b64encode(f"{employee_id}:{access_token}".encode()).decode()
                                            if getattr(sys, 'frozen', False):
                                                application_path = os.path.dirname(sys.executable)
                                            elif __file__:
                                                application_path = os.path.dirname(__file__)
                                            with open(f'{application_path}/Business/business_sessions.csv', 'a+', newline='') as file:
                                                writer = csv.writer(file)
                                                writer.writerow([email, auth_token, business_device_id])
                                            print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "Generated Session ! Waiting to start 3ds..." + RESET)
                                            inputting = False
                                            b_readywait()
                                            print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "Starting 3ds !" + RESET)
                                            b_ready += 1
                                            ds_solve(index,auth_token)
                                        else:
                                            print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Revolut Has Declined The Selfie ! Exiting in 1 Seconds..."+ RESET)
                                            inputting = False
                                            break

                                    elif "firstName" in auth_sign:
                                        print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Generated Session !"+ RESET)

                                        access_token = json_parser(auth_sign, 'accessToken":"', '","refresh')
                                        auth_token = base64.standard_b64encode(f"{employee_id}:{access_token}".encode()).decode()
                                        inputting = False
                                        return auth_token

                                    break

                            else:
                                print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  "Incorrect email or not associated with any Revolut Business account, try again!"+ RESET)
                                continue

                    return None


        def auth_verify(email):
            req_url = "https://business-mobile.revolut.com/auth/verify"
            login_payload = json.dumps({"email": email})

            revolut_client_profile = build_revolut_client_profile()

            headers = CaseInsensitiveDict()
            headers["Accept"] = "*/*"
            headers["Authorization"] = "Basic YXBwOk44R3dTaW1yS0JMUFJQd1U="
            headers["X-Client-Version"] = "3.58.1"
            headers["X-Timezone"] = "Europe/London"
            headers["Accept-Language"] = "en-GB;q=1, en;q=0.9"
            headers["Accept-Encoding"] = "gzip, deflate, br"
            headers["User-Agent"] = "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)"
            headers["X-device-id"] = business_device_id
            headers["X-device-model"] = "iPhone9,3"

            response = requests.post(req_url, headers=headers, data=login_payload)

            if response.status_code not in [200, 401]:
                print(response.status_code)
                print(response.text)

            return response.text


        def confirm_link(link):
            req_url = link
            revolut_client_profile = build_revolut_client_profile()

            headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
                "Accept-Language": "en-GB;q=1, en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br"
            }

            try:
                response = requests.get(req_url, headers=headers, timeout=5)
            except requests.exceptions.RequestException as e:
                print(e)
                return None

            to_be_decoded = json_parser(link, "SIGNIN&q=", "&isMagic")
            decoded = base64.b64decode(to_be_decoded).decode("utf-8")
            improvised_test = decoded + ")"
            final = json_parser(improvised_test, "|", ")")
            code = final

            return code



        def auth_confirm(email, code):
            req_url = "https://business-mobile.revolut.com/auth/confirm"
            login_payload = json.dumps({"email": email, "code": code})

            revolut_client_profile = build_revolut_client_profile()

            headers = {
                "Accept": "*/*",
                "Authorization": "Basic YXBwOk44R3dTaW1yS0JMUFJQd1U=",
                "X-Client-Version": "3.58.1",
                "X-Timezone": "Europe/London",
                "Accept-Language": "en-GB;q=1, en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "User-Agent": "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)",
                "X-device-id": business_device_id, 
                "X-device-model": "iPhone9,3"
            }

            try:
                response = requests.post(req_url, headers=headers, data=login_payload, timeout=5)
            except requests.exceptions.RequestException as e:
                print(e)
                return None

            response_body = response.text

            if response.status_code != 200 and response.status_code != 401:
                print(response.status_code)
                print(response_body)

            return response_body


        def sign_in_auth(pin, authtoken):
            req_url = "https://business-mobile.revolut.com/signin/auth"
            login_payload = json.dumps({})

            revolut_client_profile = build_revolut_client_profile()

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Basic {authtoken}",
                "Accept": "*/*",
                "X-Client-Version": "3.58.1",
                "X-Timezone": "Europe/London",
                "X-Verify-Password": pin,
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-GB;q=1, en;q=0.9",
                "User-Agent": "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)",
                "X-device-id": business_device_id,  
                "X-device-model": "iPhone9,3"
            }

            try:
                response = requests.post(req_url, headers=headers, data=login_payload, timeout=5)
            except requests.exceptions.RequestException as e:
                print(e)
                return None

            response_body = response.text

            if response.status_code != 200 and response.status_code != 422:
                print(response.status_code)
                print(response_body)

            return response_body


        def post_selfie(index, auth_token, pin, selfie_to_bytes_function):
            req_url = "/biometric/selfie/signin"
            selfieLocation = rev_info[index][2]
            selfiepath = f'./Business/{selfieLocation}'
            selfie_bytes, content_type = selfie_to_bytes_function(selfiepath)
            headers = {
                "Content-Type": content_type,
                "Authorization": "Basic " + auth_token,
                "Accept": "*/*",
                "X-Client-Version": "3.58.1",
                "X-Timezone": "Europe/Madrid",
                "X-Verify-Password": pin,
                "Accept-Language": "es-ES;q=1.0, en-ES;q=0.9",
                "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                "user-agent": "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)",
                "X-Device-Id": business_device_id,
                "X-Device-Model": "iPhone9,3",
            }

            response = revolut_pool.urlopen("POST", req_url, body=selfie_bytes, headers=headers)

            return response.data.decode("utf-8")


        def build_revolut_client_profile():
            ssl_context = ssl.create_default_context()
            ssl_context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
            ssl_context.set_ciphers("TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:"
                                    "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:"
                                    "ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-GCM-SHA256:"
                                    "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-CHACHA20-POLY1305:"
                                    "ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:"
                                    "AES256-GCM-SHA384:AES128-SHA:AES256-SHA")

            ssl_context.set_ecdh_curve("prime256v1")
            ssl_context.set_alpn_protocols(["h2", "http/1.1"])

            revolut_pool = urllib3.HTTPSConnectionPool(
                "business-mobile.revolut.com",
                port=443,
                ssl_context=ssl_context,
                block=True,
                maxsize=10,
                timeout=5,
                retries=False,
            )

            return revolut_pool

        revolut_pool = build_revolut_client_profile()

        def ds_solve(index,auth_token):
            at = auth_token

            if at == "":
                time.sleep(3)
                exit(1)

            auth_token1 = "Basic " + at

            while True:

                req_url = "https://business-mobile.revolut.com/transaction/3ds"

                headers = {
                    "Authorization": auth_token1,
                    "X-Client-Version": "3.58.1",
                    "X-Push-Id": "5e32a4cbd3d0b209be30e7c659fcf73651a4d5134be80d9157e9f9c421664282",
                    "X-Timezone": "Europe/London",
                    "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
                    "Accept-Language": "en-GB;q=1.0, en-US;q=0.9",
                    "Accept": "*/*",
                    "User-Agent": "Revolut/com.revolut.business 3646 (iPhone; iOS 14.4.2; sp:AAS)",
                    "X-Device-Id": business_device_id,
                    "X-Device-Model": "iPhone9,3"
                }

                res = requests.get(req_url, headers=headers)

                body = res.text
                name = rev_info[index][3]
                if "currency" in body:
                    id = json_parser(body, '"id":"', '",')
                    amount = json_parser(body, 'amount":-', ',"currency')
                    manufacturer = json_parser(body, '"name":"', '"}')

                    charged_amount = float(amount) / 100

                    accept_challenge = post_3ds(id, auth_token1)

                    if accept_challenge == 204:
                        print(green + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " +  str(charged_amount) + "£ & " + manufacturer + " -> Accepted !")
                        continue

                    else:
                        print(red + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "3ds Failed, Retry !")
                        continue

                else:
                    time.sleep(Delay/1000)
                    print(color + f"   [ {time.strftime('%H:%M:%S', time.localtime())} ] | [ Revolut Business Solver ] | [ {name} ] " + "No 3ds Found, retrying...")
                    continue
        for i in range(len(rev_info)):
            thread = threading.Thread(target=business_login,args=[i])
            time.sleep(0.5)
            thread.start()

    def parcel_tracker():
        os.system("cls")
        thread2 = threading.Thread(target=start_console)
        thread2.start()
        text = f"""
\033[38;5;94m██▓███   ▄▄▄       ██▀███   ▄████▄  ▓█████  ██▓       ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
\033[38;5;94m▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ ▓██▒       ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
\033[38;5;94m▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒███   ▒██░       ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
\033[38;5;94m▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██░       ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
\033[38;5;94m▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▒████▒░██████▒     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
\033[38;5;94m▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░░ ▒░▓  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
\033[38;5;94m░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ░ ░  ░░ ░ ▒  ░       ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
\033[38;5;94m░░         ░   ▒     ░░   ░ ░           ░     ░ ░        ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
\033[38;5;94m               ░  ░   ░     ░ ░         ░  ░    ░  ░               ░           ░  ░░ ░      ░  ░      ░  ░   ░     
\033[38;5;94m                            ░                                                      ░                              {RESET}"""
        lines = text.split("\n")
        console_width = shutil.get_terminal_size().columns
        max_line_length = max(len(line) for line in lines)
        spaces = (console_width - max_line_length) // 2
        print(color)
        for line in lines:
            print(' ' * spaces + line)
        print(Fore.RESET)

        if not os.path.exists("Trackings.txt"):
            open("Trackings.txt","w")
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added Trackings.txt file!{Fore.RESET}')

        if not os.path.exists("Errors.txt"):
            open("Errors.txt","w")
            datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added File For Failed Parcels!{Fore.RESET}')

        if not os.path.exists("Delivered.txt"):
            open("Delivered.txt","w")
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added File For Delivered Parcels!{Fore.RESET}')

        webhooks = json.load(open("config.json"))
        error_url = webhooks["Error_webhook"]
        delivered_url = webhooks["Delivered_webhook"]
        if delivered_url == "Enter webhook url for delivered parcels here!":
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {Fore.RED}Error: please enter a valid webhook url in config.json!\nPress Enter to Exit...{Fore.RESET}')
            input()
            exit()
        if error_url == "Enter webhook url for error logs here!":
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {Fore.RED}Error: please enter a valid error webhook url in config.json!{Fore.RESET}\nPress Enter to Exit...')
            input()
            exit()
        track(delivered_url, error_url)
    info = [0,0]

    def console_title():
        started = time.time()
        while True:
            seconds = time.time() - started  
            seconds = round(seconds)
            days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
            months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
            s_day = time.strftime("%d")
            month = int(time.strftime("%m"))
            year = time.strftime("%Y")
            day = datetime.datetime.weekday(datetime.datetime.now())
            checked = info[0]
            completed = info[1]
            os.system(f'title Insecurity [V{current_version}] ^|Username: {username} ^| Date: {days[day]} {s_day} {months[month-1]} {year} ^| Time running: {str(datetime.timedelta(seconds=seconds))} ^| Parcels Checked: {str(checked)} ^| Parcels Delivered: {str(completed)}')
            time.sleep(1)

    def track(delivered_url,error_url):
        while True:
            with open("Trackings.txt","r") as f:
                lines = f.read().split("\n")
                for line in lines:
                    if str(line) != '':
                        line_list = line.split(":")
                        postcode = line_list[1].replace(" ","%20")
                        postcodes.append(postcode)
                        number = line_list[0].replace(" ","")
                        numbers.append(number)
                total_parcels = len(postcodes)
            for d in range(len(postcodes)):
                info[0] += 1
                url = f"https://apis.track.dpd.co.uk/v1/reference?origin=PRTK&postcode={postcodes[0]}&referenceNumber={numbers[0]}"
                timestamp = get_timestamp()
                
                print(f"\033[38;5;94m[{timestamp}]{RESET} Checking status of order...")
                getStatus = requests.get(url).json()
                try:
                    statusText = getStatus["data"][0]["parcelStatus"]
                except:
                    error_webhook = SyncWebhook.from_url(error_url)
                    error = getStatus["error"]["message"]
                    timestamp = get_timestamp()
                    
                    print(f"{Fore.RED}{Style.BRIGHT}\033[38;5;94m[{timestamp}]{RESET} Error: {error}{Fore.RESET}")
                    with open("Errors.txt","a") as f:
                        to_join = f'{numbers[0]}:{postcodes[0].replace("%20"," ")}'
                        f.write(to_join+'\n')
                        number = numbers[0][:4] + " " + numbers[0][4:9] + " " + numbers[0][9:14] + " " + numbers[0][14:17]
                        embed = discord.Embed(
                        title = f'An Error Occured While Checking `{number}`',
                        description=f'Error: {error}',
                        color = 0xFF0000
                        )
                        error_webhook.send(embed=embed, username='DPD',avatar_url="https://assets.stickpng.com/images/62b30a4eb223544c209f5e49.png")
                        numbers.pop(0)
                        postcodes.pop(0)      
                        total_parcels -= 1 
                        if len(postcodes) != 0:        
                            for i in range(len(postcodes)): 
                                to_join = f'{numbers[0]}:{postcodes[0]}'                   
                                newlist = []
                                newlist.append(to_join)
                            open("Trackings.txt", "w").write("\n".join(newlist)) 
                        else:
                            open("Trackings.txt","w")
                    time.sleep(300)
                    continue
                if statusText == 'Your parcel is ready for you to collect at your DPD Pickup Shop':
                    parcelcode = getStatus["data"][0]["parcelCode"]
                    pickcode_headers = {
                        "authority": "apis.track.dpd.co.uk",
                        "method": "GET",
                        "path": f"/v1/parcels/{parcelcode}?_=1676719275002",
                        "scheme": "https",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                        "cache-control": "max-age=0",
                        "cookie": "sessionId=s%3Af87nUsKTjJjOHN8LL8HYOA2lMaX1k5LC.HweQaCrPKHPcH%2FiDIyq31nnQDPUK9m5MoeyG%2BZdQ3dQ",
                        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                        "sec-ch-ua-arch": "",
                        "sec-ch-ua-bitness": "64",
                        "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.96", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.96"',
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-ua-model": '"Nexus 5"',
                        "sec-ch-ua-platform": '"Android"',
                        "sec-ch-ua-platform-version": '"6.0"',
                        "sec-ch-ua-wow64": "?0",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "none",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
                    }
                    getLocCode = requests.get(f"https://apis.track.dpd.co.uk/v1/parcels/{parcelcode}?_=1677701947218", headers = pickcode_headers).json()
                    try:
                        loc_code = getLocCode["data"]["pickupLocationCode"]
                    except:
                        webhook = SyncWebhook.from_url(delivered_url) # Your webhook
                        info[1] += 1
                        completed_parcels = info[1]
                        embed = discord.Embed(
                        title = f"Parcel arrived! ({completed_parcels}/{total_parcels})",
                        description=f'Your parcel with tracking id `{numbers[0]}` has arrived! Due to an error we cannot display the qr!',
                        color = 0x0000FF
                    )
                        webhook.send(embed=embed, username='DPD',avatar_url="https://assets.stickpng.com/images/62b30a4eb223544c209f5e49.png")
                        timestamp = get_timestamp()
                        
                        print(f"\033[38;5;94m[{timestamp}]{RESET} Parcel arrived! Tracking number: {numbers[0]}")
                        with open("Delivered.txt","a") as f:
                            to_write = f'{numbers[0]}:{postcodes[0]}\n'
                            f.write(to_write)
                        try:
                            del checked[numbers[0]]
                        except:
                            pass
                        numbers.pop(0)
                        postcodes.pop(0)
                        if len(postcodes) != 0:
                            newlist = []
                            for r in range(len(postcodes)): 
                                to_join = f'{numbers[r]}:{postcodes[r]}'                   
                                newlist.append(to_join)
                            open("Trackings.txt", "w").write("\n".join(newlist))
                        else:
                            open("Trackings.txt", "w")
                        time.sleep(300)
                        continue
                    parcel_name = getLocCode["data"]["deliveryDetails"]["address"]["organisation"]
                    original_street = getLocCode["data"]["deliveryDetails"]["address"]["street"]
                    original_property = getLocCode["data"]["deliveryDetails"]["address"]["property"]
                    getAddress = requests.get(f"https://apis.track.dpd.co.uk/v1/pickupLocations/{loc_code}", headers=pickcode_headers).json()
                    business = getAddress["data"]["address"]["organisation"]
                    street = getAddress["data"]["address"]["street"]
                    getPickupDate = requests.get(f"https://apis.track.dpd.co.uk/v1/parcels/{parcelcode}/parcelevents",headers=pickcode_headers).json()
                    date = getPickupDate["data"][0]["eventDate"]
                    QR_headers = {
                        "authority": "apis.track.dpd.co.uk",
                        "method": "GET",
                        "path": f"/v1/pickupLocations/{loc_code}/parcels/{parcelcode}?scale=3",
                        "scheme": "https",
                        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                        "cookie": "sessionId=s%3Af87nUsKTjJjOHN8LL8HYOA2lMaX1k5LC.HweQaCrPKHPcH%2FiDIyq31nnQDPUK9m5MoeyG%2BZdQ3dQ",
                        "referer": "https://track.dpd.co.uk/",
                        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-ua-platform": "Android",
                        "sec-fetch-dest": "image",
                        "sec-fetch-mode": "no-cors",
                        "sec-fetch-site": "same-site",
                        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
                    }
                    getQR = requests.get(f"https://apis.track.dpd.co.uk/v1/pickupLocations/{loc_code}/parcels/{parcelcode}?scale=3", headers = QR_headers)
                    qr_data = getQR.content
                    discord_file_bytes = io.BytesIO()
                    with Image.open(io.BytesIO(qr_data)).convert("RGBA") as image:
                        background = Image.new("RGBA", image.size, "WHITE")
                        background.paste(image,(0,0), image)
                        background.convert('RGB').save(discord_file_bytes, "PNG")
                        image.close()
                    discord_file_bytes.seek(0)
                    file = discord.File(discord_file_bytes,filename = f"parcel_{numbers[0]}.png")
                    webhook = SyncWebhook.from_url(delivered_url) # Your webhook
                    info[1] += 1
                    completed_parcels = info[1]
                    embed = discord.Embed(
                        title = f"Parcel arrived! ({completed_parcels}/{total_parcels})",
                        description=f'Your parcel with tracking id `{numbers[0]}` has arrived!',
                        color = 0x0000FF
                    )
                    embed.add_field(name=f"Name On Parcel:",value=parcel_name)
                    embed.add_field(name=f"Parcel Shop Address:", value=f"{business}, {street}", inline=False)
                    embed.add_field(name=f'Please Collect Your Parcel Before:', value=date, inline=False)
                    embed.add_field(name="Original Address:",value=f"{original_street}, {original_property}", inline=False)
                    embed.set_image(url=f"attachment://parcel_{numbers[0]}.png")
                    webhook.send(embed=embed,file=file, username='DPD',avatar_url="https://assets.stickpng.com/images/62b30a4eb223544c209f5e49.png")
                    timestamp = get_timestamp()
                    
                    print(f"\033[38;5;94m[{timestamp}]{RESET} Parcel arrived! Tracking number: {numbers[0]}")
                    with open("Delivered.txt","a") as f:
                            to_write = f'{numbers[0]}:{postcodes[0]}\n'
                            f.write(to_write)
                    try:
                        del checked[numbers[0]]
                    except:
                        pass
                    numbers.pop(0)
                    postcodes.pop(0)
                    if len(postcodes) != 0:
                        newlist = []
                        for r in range(len(postcodes)): 
                            to_join = f'{numbers[r]}:{postcodes[r]}'                   
                            newlist.append(to_join)
                        open("Trackings.txt", "w").write("\n".join(newlist))
                    else:
                        open("Trackings.txt", "w")
                    time.sleep(300)
                else:
                    if numbers[0] not in checked:
                        webhook = SyncWebhook.from_url(delivered_url) # Your webhook
                        embed = discord.Embed(
                            title = f"Parcel Status",
                            description=f'Status of parcel with tracking id `{numbers[0]}`:\n ``{statusText}``',
                            color = 0x0000FF
                        )
                        webhook.send(embed=embed, username='DPD',avatar_url="https://assets.stickpng.com/images/62b30a4eb223544c209f5e49.png")
                        timestamp = get_timestamp()
                        
                        print(f"\033[38;5;94m[{timestamp}]{RESET} Parcel arrived! Tracking number: {numbers[0]}")
                        checked[numbers[0]] = statusText
                    elif checked[numbers[0]] != statusText:
                        timestamp = get_timestamp()
                        
                        print(f"\033[38;5;94m[{timestamp}]{RESET} Status of parcel (changed)! Tracking id: {numbers[0]} | Status: {statusText}")
                        webhook = SyncWebhook.from_url(delivered_url) # Your webhook
                        embed = discord.Embed(
                            title = f"Parcel Status",
                            description=f'Status of parcel with tracking id `{numbers[0]}`:\n ``{statusText}``',
                            color = 0x0000FF
                        )
                        webhook.send(embed=embed, username='DPD',avatar_url="https://assets.stickpng.com/images/62b30a4eb223544c209f5e49.png")
                        timestamp = get_timestamp()
                        
                        checked[numbers[0]] = statusText
                    number = numbers[0]
                    post = postcodes[0]
                    numbers.pop(0)
                    postcodes.pop(0)
                    numbers.append(number)
                    postcodes.append(post)
                    time.sleep(300)
                    continue


    def business_card_genyes():
        exported = []
        os.system(f"title Insecurity [V{current_version}] ^| Business Card Generator ^| Username: {username}")
        text = f"""
\033[38;5;94m ▄████▄   ▄████▄     ▓█████ ▒██   ██▒ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓
\033[38;5;94m▒██▀ ▀█  ▒██▀ ▀█     ▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒
\033[38;5;94m▒▓█    ▄ ▒▓█    ▄    ▒███   ░░  █   ░▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░
\033[38;5;94m▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ 
\033[38;5;94m▒ ▓███▀ ░▒ ▓███▀ ░   ░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ 
\033[38;5;94m░ ░▒ ▒  ░░ ░▒ ▒  ░   ░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   
\033[38;5;94m  ░  ▒     ░  ▒       ░ ░  ░░░   ░▒ ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    
\033[38;5;94m░        ░              ░    ░    ░  ░░       ░ ░ ░ ▒    ░░   ░   ░      
\033[38;5;94m░ ░      ░ ░            ░  ░ ░    ░               ░ ░     ░              
\033[38;5;94m░        ░                                                                {RESET}"""
        lines = text.split("\n")
        console_width = shutil.get_terminal_size().columns
        max_line_length = max(len(line) for line in lines)
        spaces = (console_width - max_line_length) // 2
        for line in lines:
            print(' ' * spaces + line)
        if not os.path.exists("cards.csv"):
            with open("cards.csv","w") as f:
                timestamp = get_timestamp()
                data = ['NAME', 'NUMBER','MONTH','YEAR','CVV']
                writer = csv.DictWriter(f, fieldnames = data)
                writer.writeheader()
                print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added File For Card Output!{Fore.RESET}')

        if not os.path.exists("cardconfig.json"):
            open("cardconfig.json","w")
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added Config For Card Generator!{Fore.RESET}')
            settings_setup = {"Email":"","Password":"","Rev_Token":"","Device_Id":"","Employee_Email":"","Card_Prefix":"CARD_","Index":0,"Sms_Verification":False,"Base_Url":"https://business.revolut.com/api/","Current_User":"https://business.revolut.com/api/user/current"}
            json.dump(settings_setup,open("cardconfig.json","w",encoding = 'utf-8'),indent = 4)   
        config = json.load(open("cardconfig.json"))
        class RevGen:
            def __init__(self) -> None:
                
                
                self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
                if config["Device_Id"] == "":
                    config["Device_Id"] = str(uuid.uuid4())
                
                self.headers_post =  {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'accept': 'application/json, text/plain, /',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'content-type': 'application/json;charset=UTF-8',
                    'origin': 'https://business.revolut.com/',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                }
                
                self.headers_get = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'accept': 'application/json, text/plain, */*',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                }

                self.s = cloudscraper.create_scraper(requestPreHook=self.pre_hook)
                config_name = "cards.csv"
                if getattr(sys, 'frozen', False):
                    application_path = os.path.dirname(sys.executable)
                elif __file__:
                    application_path = os.path.dirname(__file__)

                config_path = os.path.join(application_path, config_name)
                self.csv_location = config_path
                #if    
                with open(self.csv_location, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader)
                    for row in reader:
                        if len(row) == 0:
                            continue
                        card_name = row[0]
                        card_num = row[1]
                        card_exp_month = row[2]
                        card_exp_year = row[3]
                        card_cvv = row[4]
                        exported.append(str(card_name))
                if config["Email"] == "" or config["Password"] == "" and config["Rev_Token"] == "":
                    raise RuntimeError("Email and Password or Rev Token are empty, supply at least one")
                
                if config["Email"] != "" and config["Password"] != "":
                    self.login()  
                        
                self.business_id = self.get_business()
                if not self.business_id:
                    raise RuntimeError("Cannot Get Business API")
                if self.kyc_status != "PASSED":
                    raise RuntimeError("Account Unverified")
                
                self.BASE_URL = config["Base_Url"] + f"business/{self.business_id}"
                
                self.get_members()
                

                self.get_all_cards()
                for key,value in self.cards.items():
                    self.card_id = key
                    self.card_name = value["name"]
                    self.card_exp_month = value["expiryDate"].split("/")[0]
                    self.card_exp_year = value["expiryDate"].split("/")[1]
                    self.log_info(f"Retrieved Card {self.card_name}")
                    #if config["Sms_Verification"]:
                    if str(self.card_name) in exported:
                        print(f"{red}Didn't export {str(self.card_name)}: Already in file!{RESET}")
                        continue
                    self.get_card_details()
            def pre_hook(self, request, method, url, *args, **kwargs):
                if hasattr(self,"expires"):
                    if self.expires < time.time():
                        self.login()
                if not self.s.cookies.get("token", domain="business.revolut.com") and config["Rev_Token"] != "":
                    self.s.cookies.set("token", config["Rev_Token"], domain="business.revolut.com")
                    
                return method, url, args, kwargs
                
                        
            @staticmethod
            def log_info(*args, **kwargs):
                os.system("")
                timestamp = get_timestamp()
                
                st,en = '\033[92m','\033[0m '
                output =  f"{st}[{str(timestamp)}] {args[0]}{en}"
                logging.basicConfig(format="%(message)s", level=INFO)
                logging.info(output)  
                
                
            @staticmethod
            def log_error(*args, **kwargs):
                os.system("")
                st,en = '\033[91m','\033[0m '
                timestamp = get_timestamp()
                
                output =  f"{st}[{str(timestamp)}] {args[0]}{en}"
                basicConfig(format="%(message)s", level=ERROR)
                error(output)  
                print("An error occured! Going back to main menu in 5 seconds...")
                time.sleep(5)
                main_menu() 
                            
            def login(self):
                
                self.log_info(f"Logging in")
                
                json_data = {
                    'email': config["Email"],
                    'password': config["Password"]
                }

                response = self.s.post(
                    'https://business.revolut.com/api/signin',
                    headers=self.headers_post,
                    json=json_data
                )        
                try:
                    parsed = response.json()
                    config["Rev_Token"] = self.s.cookies["token"]
                except:
                    RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")
                            
                if "userId" not in parsed:
                    raise RuntimeError(f"Cannot Login: {parsed}")
                
                response = self.s.post('https://business.revolut.com/api/2fa/signin/verify', headers=self.headers_post)
                try:
                    parsed = response.json()
                    verification_token = parsed["verificationTokenId"]
                except:
                    raise RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")
                
                response = self.s.get(f'https://business.revolut.com/api/verification/{verification_token}/status', headers=self.headers_get)
                parsed = response.json() 
                
                while parsed["state"] != "VERIFIED":
                    self.log_info(f"Waiting for App confirmation")
                    time.sleep(2)
                    response = self.s.get(f'https://business.revolut.com/api/verification/{verification_token}/status', headers=self.headers_get)
                    parsed = response.json() 
                    
                code = parsed["code"]
                headers = self.headers_post.copy()
                headers["x-verify-code"] = code
                
                verify = self.s.post('https://business.revolut.com/api/2fa/signin/verify', headers=headers)
                try:
                    parsed = verify.json()
                    self.expires = parsed["expireAt"]
                    config["Rev_Token"] = self.s.cookies["token"]
                except:
                    raise RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")        

                
            def get_business(self):
                self.log_info("Getting Business")
                
                response = self.s.get(
                    config["Current_User"],
                    headers=self.headers_get
                    )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    parsed = response.json()

                    self.kyc_status = parsed["kyc"]
                    business_id = parsed["businessId"]
                    return business_id
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")
                    
            
            def get_members(self):

                self.log_info("Getting Team Members")
                
                response = self.s.get(
                    f"{self.BASE_URL}/team/members",
                    headers=self.headers_get
                )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    parsed = response.json()
                    self.current_member = [m for m in parsed if m["email"] == config["Employee_Email"]][0]
                    try:
                        self.employee_id = self.current_member["employee"]["id"]
                    except:
                        self.employee_id = ""
                        
                    self.user_id = self.current_member["user"]["id"]

                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")   
                    
            def get_all_cards(self):
                
                response = self.s.get(
                    f'{self.BASE_URL}/team/members/current-member/cards',
                    headers=self.headers_get
                )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    self.cards = {}
                    parsed = response.json()
                    for x in parsed:
                        self.cards[x["payload"]["id"]] = {
                            "name": x["payload"]["name"], 
                            "expiryDate": x["payload"]["expiryDate"],
                        }
                    self.user_id = self.current_member["user"]["id"]
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")           
            
            def gen_cards(self):
                
                payload = {
                    "includedToExpenseManagement":True,
                    "linkAllAccounts":True,
                    "email": config["Employee_Email"],
                    "employeeId": self.employee_id,
                    "userId": self.user_id,
                    "personal":True
                }
                
                response = self.s.post(
                    f'{self.BASE_URL}/card/virtual/order',
                    headers=self.headers_post,
                    json=payload
                )
                
                if "This action is forbidden" in response.text:

                    raise RuntimeError("Token Expired")
                
                
                try:
                    self.card_id = response.json()["id"]
                except:
                    if response.status_code == 422:
                        self.log_error(f"Error Parsing API: You are being ratelimited!")

                    else:
                        self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}") 
                
            
            def label_cards(self, prefix):
                
                self.log_info("Labeling Card")   
                label = config["Card_Prefix"]
                payload = {"label": f"{label} {prefix}"} 

                self.card_name = f"{label}{prefix}"

                response = self.s.patch(
                    f'{self.BASE_URL}/card/{self.card_id}/label',
                    headers=self.headers_post,
                    json=payload
                    )
                
                try:
                    return response.json()["state"] == "ACTIVE"
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}") 
                    
                    
            def send_sms(self):
                resp_code = 'resp'
                timestamp = get_timestamp()
                
                print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] Sending SMS...')
                while not '"Verification required","code":9014,"factor":"SMS"' in resp_code:
                    response = self.s.get(
                        f"{self.BASE_URL}/card/{self.card_id}/image/unmasked?encrypt=false",
                        headers=self.headers_get
                    )
                    resp_code = response.text
                    if '"Cannot create a new verification code at that moment","code":9015' in resp_code:
                        timestamp = get_timestamp()
                        
                        print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] Error sending SMS waiting 5 seconds...')
                        time.sleep(5)
                timestamp = get_timestamp()
                
                print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] SMS code sent')


            def get_card_details(self):
                self.send_sms()
                Resend = True
                while Resend:
                    timestamp = get_timestamp()
                    self.sms_code = input(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] Enter sms code (type "1" to send sms again): ') 
                    if self.sms_code == "1":
                        self.send_sms()  
                    else:
                        Resend = False

                self.verify_headers = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                    'accept': 'application/json, text/plain, */*',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                    'cookie': f'token={config["Rev_Token"]}', 
                    'x-verify-code': f'{self.sms_code}',
                }
                response = self.s.get(
                    f"{self.BASE_URL}/card/{self.card_id}/image/unmasked?encrypt=false",
                    headers=self.verify_headers
                )
                try:
                    self.card_num = response.json()["pan"]
                    self.card_cvv = response.json()["cvv"]
                    self.write_card_details()
                except:
                    choice = input(f'[{self.card_name}] Wrong sms code wanna try again? y/n: ')
                    if choice == "y":
                        self.get_card_details()
                    else:
                        return
                


            def write_card_details(self):
                with open(self.csv_location, 'a+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(self.card_name), str(self.card_num), str(self.card_exp_month),str(self.card_exp_year),str(self.card_cvv)])
                    message = str(self.card_name) + " "+ str(self.card_num) + " "+  str(self.card_exp_month) + " "+ str(self.card_exp_year) + " "+ str(self.card_cvv)
                    exported.append(self.card_name)
        RevGen()

    def business_card_genno():
        os.system(f"title Insecurity [V{current_version}] ^| Business Card Generator ^| Username: {username}")
        text = f"""
\033[38;5;94m ▄████▄   ▄████▄       ▄████ ▓█████  ███▄    █ 
\033[38;5;94m▒██▀ ▀█  ▒██▀ ▀█      ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
\033[38;5;94m▒▓█    ▄ ▒▓█    ▄    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
\033[38;5;94m▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
\033[38;5;94m▒ ▓███▀ ░▒ ▓███▀ ░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
\033[38;5;94m░ ░▒ ▒  ░░ ░▒ ▒  ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
\033[38;5;94m  ░  ▒     ░  ▒        ░   ░  ░ ░  ░░ ░░   ░ ▒░
\033[38;5;94m░        ░           ░ ░   ░    ░      ░   ░ ░ 
\033[38;5;94m░ ░      ░ ░               ░    ░  ░         ░ 
\033[38;5;94m░        ░                                     {RESET}"""

        lines = text.split("\n")
        console_width = shutil.get_terminal_size().columns
        max_line_length = max(len(line) for line in lines)
        spaces = (console_width - max_line_length) // 2
        for line in lines:
            print(' ' * spaces + line)
        if not os.path.exists("cards.csv"):
            with open("cards.csv","w") as f:
                data = ['NAME', 'NUMBER','MONTH','YEAR','CVV']
                writer = csv.DictWriter(f, fieldnames = data)
                writer.writeheader()
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added File For Card Output!{Fore.RESET}')

        if not os.path.exists("cardconfig.json"):
            open("cardconfig.json","w")
            timestamp = get_timestamp()
            
            print(f'\033[38;5;94m[{timestamp}]{RESET} {color}Added Config For Card Generator!{Fore.RESET}')
            settings_setup = {"Email":"","Password":"","Rev_Token":"","Device_Id":"","Gen_Number":0,"Employee_Email":"","Card_Prefix":"CARD_","Index":0,"Sms_Verification":False,"Base_Url":"https://business.revolut.com/api/","Current_User":"https://business.revolut.com/api/user/current"}
            json.dump(settings_setup,open("cardconfig.json","w",encoding = 'utf-8'),indent = 4)   
        config = json.load(open("cardconfig.json"))
        class RevGen:
            def __init__(self) -> None:
                
                
                self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
                if config["Device_Id"] == "":
                    config["Device_Id"] = str(uuid.uuid4())
                
                self.headers_post =  {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'accept': 'application/json, text/plain, /',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'content-type': 'application/json;charset=UTF-8',
                    'origin': 'https://business.revolut.com/',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                }
                
                self.headers_get = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                    'accept': 'application/json, text/plain, */*',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                }

                self.s = cloudscraper.create_scraper(requestPreHook=self.pre_hook)
                config_name = "/Business/cards.csv"
                if getattr(sys, 'frozen', False):
                    application_path = os.path.dirname(sys.executable)
                elif __file__:
                    application_path = os.path.dirname(__file__)

                config_path = os.path.join(application_path, config_name)
                self.csv_location = config_path
                
                if config["Email"] == "" or config["Password"] == "" and config["Rev_Token"] == "":
                    raise RuntimeError("Email and Password or Rev Token are empty, supply at least one")
                
                if config["Email"] != "" and config["Password"] != "":
                    self.login()  
                        
                self.business_id = self.get_business()
                if not self.business_id:
                    raise RuntimeError("Cannot Get Business API")
                if self.kyc_status != "PASSED":
                    raise RuntimeError("Account Unverified")
                
                self.BASE_URL = config["Base_Url"] + f"business/{self.business_id}"
                
                self.get_members()

                def gennumber() -> int:
                    inp = input("How much cards would you like to generate? (max 200)")
                    try:
                        inp = int(inp)
                        if inp > 200:
                            print("Too much cards! Retry!")
                            gennumber()
                        else:
                            return inp
                    except:
                        print(f"{Fore.RED}You must enter a number! Do you want to retry? (y/n){Fore.RESET}")
                        inp = input()
                        if inp == "y":
                            gennumber()
                        if inp == n:
                            main_menu()
                        else:
                            print("Not a valid option!")
                            gennumber()
                        
                number = gennumber()
                for n in range(0, int(number)):
                        index = config["Index"]
                        self.log_info(f"Generating Card {n+index}")
                        self.gen_cards()
                        self.log_info(f"Generated Card {n+index}")
                        labeled = self.label_cards(n+index)
                        if labeled:
                            self.log_info(f"Labeled Card {n+index}")
                            self.card_exp_month = f'0{str(datetime.date.today().month)}'
                            self.card_exp_year = str(datetime.date.today().year + 5)
                        if config["Sms_Verification"]:
                            self.get_card_details()                        
                
            def pre_hook(self, request, method, url, *args, **kwargs):
                if hasattr(self,"expires"):
                    if self.expires < time.time():
                        self.login()
                if not self.s.cookies.get("token", domain="business.revolut.com") and config["Rev_Token"] != "":
                    self.s.cookies.set("token", config["Rev_Token"], domain="business.revolut.com")
                    
                return method, url, args, kwargs
                

                        
            @staticmethod
            def log_info(*args, **kwargs):
                os.system("")
                timestamp = get_timestamp()
                
                st,en = '\033[92m','\033[0m '
                output =  f"{st}[{str(timestamp)}] {args[0]}{en}"
                logging.basicConfig(format="%(message)s", level=INFO)
                logging.info(output)  
                
                
            @staticmethod
            def log_error(*args, **kwargs):
                os.system("")
                st,en = '\033[91m','\033[0m '
                timestamp = get_timestamp()
                
                output =  f"{st}[{str(timestamp)}] {args[0]}{en}"
                basicConfig(format="%(message)s", level=ERROR)
                error(output)
                print("An error occured! Going back to main menu in 5 seconds...")
                time.sleep(5)
                main_menu()  
                            
            def login(self):
                
                self.log_info(f"Logging in")
                
                json_data = {
                    'email': config["Email"],
                    'password': config["Password"]
                }

                response = self.s.post(
                    'https://business.revolut.com/api/signin',
                    headers=self.headers_post,
                    json=json_data
                )        
                try:
                    parsed = response.json()
                    config["Rev_Token"] = self.s.cookies["token"]
                except:
                    RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")
                            
                if "userId" not in parsed:
                    raise RuntimeError(f"Cannot Login: {parsed}")
                
                response = self.s.post('https://business.revolut.com/api/2fa/signin/verify', headers=self.headers_post)
                try:
                    parsed = response.json()
                    verification_token = parsed["verificationTokenId"]
                except:
                    raise RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")
                
                response = self.s.get(f'https://business.revolut.com/api/verification/{verification_token}/status', headers=self.headers_get)
                parsed = response.json() 
                
                while parsed["state"] != "VERIFIED":
                    self.log_info(f"Waiting for App confirmation")
                    time.sleep(2)
                    response = self.s.get(f'https://business.revolut.com/api/verification/{verification_token}/status', headers=self.headers_get)
                    parsed = response.json() 
                    
                code = parsed["code"]
                headers = self.headers_post.copy()
                headers["x-verify-code"] = code
                
                verify = self.s.post('https://business.revolut.com/api/2fa/signin/verify', headers=headers)
                try:
                    parsed = verify.json()
                    self.expires = parsed["expireAt"]
                    config["Rev_Token"] = self.s.cookies["token"]
                except:
                    raise RuntimeError(f"Error Parsing API: {response.status_code} - {response.text}")        

                
            def get_business(self):
                self.log_info("Getting Business")
                
                response = self.s.get(
                    config["Current_User"],
                    headers=self.headers_get
                    )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    parsed = response.json()

                    self.kyc_status = parsed["kyc"]
                    business_id = parsed["businessId"]
                    return business_id
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")
                    
            
            def get_members(self):

                self.log_info("Getting Team Members")
                
                response = self.s.get(
                    f"{self.BASE_URL}/team/members",
                    headers=self.headers_get
                )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    parsed = response.json()
                    self.current_member = [m for m in parsed if m["email"] == config["Employee_Email"]][0]
                    try:
                        self.employee_id = self.current_member["employee"]["id"]
                    except:
                        self.employee_id = ""
                        
                    self.user_id = self.current_member["user"]["id"]

                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")   
                    
            def get_all_cards(self):
                
                response = self.s.get(
                    f'{self.BASE_URL}/team/members/current-member/cards',
                    headers=self.headers_get
                )
                
                if "This action is forbidden" in response.text:
                    raise RuntimeError("Token Expired")
                
                try:
                    self.cards = {}
                    parsed = response.json()
                    for x in parsed:
                        self.cards[x["payload"]["id"]] = {
                            "name": x["payload"]["name"], 
                            "expiryDate": x["payload"]["expiryDate"],
                        }
                    self.user_id = self.current_member["user"]["id"]
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")           
            
            def gen_cards(self):
                
                payload = {
                    "includedToExpenseManagement":True,
                    "linkAllAccounts":True,
                    "email": config["Employee_Email"],
                    "employeeId": self.employee_id,
                    "userId": self.user_id,
                    "personal":True
                }
                
                response = self.s.post(
                    f'{self.BASE_URL}/card/virtual/order',
                    headers=self.headers_post,
                    json=payload
                )
                
                if "This action is forbidden" in response.text:

                    raise RuntimeError("Token Expired")
                
                
                try:
                    self.card_id = response.json()["id"]
                except:
                    if response.status_code == 422:
                        self.log_error(f"Error Parsing API: You are being ratelimited!")
                    else:
                        self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}")
                
            
            def label_cards(self, prefix):
                
                self.log_info("Labeling Card")   
                label = config["Card_Prefix"]
                payload = {"label": f"{label} {prefix}"} 

                self.card_name = f"{label}{prefix}"

                response = self.s.patch(
                    f'{self.BASE_URL}/card/{self.card_id}/label',
                    headers=self.headers_post,
                    json=payload
                    )
                
                try:
                    return response.json()["state"] == "ACTIVE"
                except:
                    self.log_error(f"Error Parsing API: {response.status_code} - {response.text} - {traceback.format_exc()}") 
                    
                    
            def send_sms(self):
                resp_code = 'resp'
                timestamp = get_timestamp()
                
                print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] Sending SMS...')
                while not '"Verification required","code":9014,"factor":"SMS"' in resp_code:
                    response = self.s.get(
                        f"{self.BASE_URL}/card/{self.card_id}/image/unmasked?encrypt=false",
                        headers=self.headers_get
                    )
                    resp_code = response.text
                    if '"Cannot create a new verification code at that moment","code":9015' in resp_code:
                        timestamp = get_timestamp()
                        
                        print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] Error sending SMS waiting 5 seconds...')
                        time.sleep(5)
                timestamp = get_timestamp()
                
                print(f'\033[38;5;94m[{timestamp}]{RESET} [{self.card_name}] SMS code sent')


            def get_card_details(self):
                self.send_sms()
                Resend = True
                while Resend:
                    self.sms_code = input(f'[{self.card_name}] Enter sms code (type "1" to send sms again): ') 
                    if self.sms_code == "1":
                        self.send_sms()  
                    else:
                        Resend = False

                self.verify_headers = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                    'accept': 'application/json, text/plain, */*',
                    'sec-ch-ua-mobile': '?0',
                    'user-agent': self.ua,
                    'x-device-id': config["Device_Id"],
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://business.revolut.com/',
                    'accept-language': 'en-US;q=0.9',
                    'cookie': f'token={config["Rev_Token"]}', 
                    'x-verify-code': f'{self.sms_code}',
                }
                response = self.s.get(
                    f"{self.BASE_URL}/card/{self.card_id}/image/unmasked?encrypt=false",
                    headers=self.verify_headers
                )
                try:
                    self.card_num = response.json()["pan"]
                    self.card_cvv = response.json()["cvv"]
                    self.write_card_details()
                except:
                    choice = input(f'[{self.card_name}] Wrong sms code wanna try again? y/n: ')
                    if choice == "y":
                        self.get_card_details()
                    else:
                        return
                


            def write_card_details(self):
                with open(self.csv_location, 'a') as f:
                    message = str(self.card_name) + " "+ str(self.card_num) + " "+ str(self.card_exp_month) + " " + str(self.card_exp_month) + " "+ str(self.card_exp_year) + " "+ str(self.card_cvv) + "\n"
                    f.write(message)
        RevGen()

    def icloud_gen():
        def log_error(*args, **kwargs):
            os.system("")
            st,en = '\033[91m','\033[0m '
            timestamp = get_timestamp()
            
            output =  f"{st}[{str(timestamp)}] {args[0]}{en}"
            basicConfig(format="%(message)s", level=ERROR)
            error(output)  
            print("An error occured! Going back to main menu in 5 seconds...")
            time.sleep(5)
            main_menu() 
        os.system(f"title Insecurity [V{current_version}] ^| Icloud Generator ^| Username: {username}")
        text = f"""
\033[38;5;94m ██▓ ▄████▄   ██▓     ▒█████   █    ██ ▓█████▄      ▄████ ▓█████  ███▄    █ 
\033[38;5;94m▓██▒▒██▀ ▀█  ▓██▒    ▒██▒  ██▒ ██  ▓██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
\033[38;5;94m▒██▒▒▓█    ▄ ▒██░    ▒██░  ██▒▓██  ▒██░░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
\033[38;5;94m░██░▒▓▓▄ ▄██▒▒██░    ▒██   ██░▓▓█  ░██░░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
\033[38;5;94m░██░▒ ▓███▀ ░░██████▒░ ████▓▒░▒▒█████▓ ░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
\033[38;5;94m░▓  ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒  ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
\033[38;5;94m ▒ ░  ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░░▒░ ░ ░  ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░
\033[38;5;94m ▒ ░░          ░ ░   ░ ░ ░ ▒   ░░░ ░ ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░ 
\033[38;5;94m ░  ░ ░          ░  ░    ░ ░     ░        ░             ░    ░  ░         ░ 
\033[38;5;94m    ░                                   ░                                         {RESET}"""
        try:
            lines = text.split("\n")
            console_width = shutil.get_terminal_size().columns
            max_line_length = max(len(line) for line in lines)
            spaces = (console_width - max_line_length) // 2
            for line in lines:
                print(' ' * spaces + line)
            MAX_CONCURRENT_TASKS = 10
            while True:
                if os.path.isfile('cookie.txt') and os.path.getsize('cookie.txt') > 0:
                    # Run code if the file is not empty
                    class HideMyEmail:
                        base_url = "https://p68-maildomainws.icloud.com/v1/hme"
                        params = {
                            "clientBuildNumber": "2206Hotfix11",
                            "clientMasteringNumber": "2206Hotfix11",
                            "clientId": "",
                            "dsid": "",
                        }

                        def __init__(self, label: str = "insecurity gen", cookies: str = ""):
                            """Initializes the HideMyEmail class.

                            Args:
                                label (str)     Label that will be set for all emails generated, defaults to `insecurity gen`
                                cookies (str)   Cookie string to be used with requests. Required for authorization.
                            """
                            # Label that will be set for all emails generated, defaults to `insecurity gen`
                            self.label = label

                            # Cookie string to be used with requests. Required for authorization.
                            self.cookies = cookies

                        async def __aenter__(self):
                            self.s = aiohttp.ClientSession(
                                headers={
                                    "Connection": "keep-alive",
                                    "Pragma": "no-cache",
                                    "Cache-Control": "no-cache",
                                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
                                    "Content-Type": "text/plain",
                                    "Accept": "*/*",
                                    "Sec-GPC": "1",
                                    "Origin": "https://www.icloud.com",
                                    "Sec-Fetch-Site": "same-site",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Dest": "empty",
                                    "Referer": "https://www.icloud.com/",
                                    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,cs;q=0.7",
                                    "Cookie": self.__cookies.strip(),
                                },
                                timeout=aiohttp.ClientTimeout(total=10),
                            )

                            return self

                        async def __aexit__(self, exc_t, exc_v, exc_tb):
                            await self.s.close()

                        @property
                        def cookies(self) -> str:
                            return self.__cookies

                        @cookies.setter
                        def cookies(self, cookies: str):
                            # remove new lines/whitespace for security reasons
                            self.__cookies = cookies.strip()

                        async def generate_email(self) -> dict:
                            """Generates an email"""
                            try:
                                async with self.s.post(
                                    f"{self.base_url}/generate", params=self.params, timeout=10
                                ) as resp:
                                    res = await resp.json()
                                    return res
                            except asyncio.TimeoutError:
                                raise TimeoutError("Request timed out")

                        async def reserve_email(self, email: str) -> dict:
                            """Reserves an email and registers it for forwarding"""
                            try:
                                payload = {
                                    "hme": email,
                                    "label": self.label,
                                    "note": "Generated by insecurity iCloud email generator",
                                }
                                async with self.s.post(
                                    f"{self.base_url}/reserve", params=self.params, json=payload
                                ) as resp:
                                    res = await resp.json()
                                return res
                            except asyncio.TimeoutError:
                                return {"error": 1, "reason": "Request timed out"}

                        async def list_email(self) -> dict:
                            """List all HME"""
                            try:
                                async with self.s.get(f"{self.base_url}/list", params=self.params) as resp:
                                    res = await resp.json()
                                    return res
                            except asyncio.TimeoutError:
                                return {"error": 1, "reason": "Request timed out"}

                    class RichHideMyEmail(HideMyEmail):
                        _cookie_file = "cookie.txt"

                        def __init__(self):
                            super().__init__()
                            self.console = Console(log_path=False)
                            self.table = Table()

                            if os.path.exists(self._cookie_file):
                                # load in a cookie string from file
                                with open(self._cookie_file, "r") as f:
                                    self.cookies = [line for line in f if not line.startswith("//")][0]
                            else:
                                self.console.log(
                                    '[bold yellow][WARN][/] No "cookie.txt" file found! Generation might not work due to unauthorized access.'
                                )

                        async def _generate_one(self) -> Union[str, None]:
                            # First, generate an email
                            gen_res = await self.generate_email()
                            if not gen_res: 
                                return
                            email = gen_res["result"]["hme"]
                            if "success" not in gen_res or not gen_res["success"]:
                                error = gen_res["error"] if "error" in gen_res else {}
                                err_msg = "Unknown"
                                if type(error) == int and "reason" in gen_res:
                                    err_msg = gen_res["reason"]
                                elif type(error) == dict and "errorMessage" in error:
                                    err_msg = error["errorMessage"]
                                if "You have reached the limit of addresses you can create" in err_msg:
                                    print("Sleeping for 30 minutes due to rate limiting")
                                    time.sleep(30 * 60)  # sleep for 30 minutes
                                elif "Invalid global session" in err_msg or "Missing X-APPLE-WEBAUTH-USER cookie" in err_msg:
                                    filename = "cookie.txt"
                                    for root, dirs, files in os.walk("/"):
                                        if filename in files:
                                            os.remove(os.path.join(root, filename))
                                            print(f"Deleting file because of error: " + err_msg)
                                            sys.exit()
                                self.console.log(
                                    f"[bold red][ERR][/] - Failed to reserve email {email}. Reason: {err_msg}"
                                )
                                return

                            self.console.log(f'[bold green][50%] "{email}" - Successfully generated{Fore.RESET}')

                            # Then, reserve it
                            reserve_res = await self.reserve_email(email)

                            if not reserve_res:
                                return
                            elif "success" not in reserve_res or not reserve_res["success"]:
                                error = reserve_res["error"] if "error" in reserve_res else {}
                                err_msg = "Unknown"
                                if type(error) == int and "reason" in reserve_res:
                                    err_msg = reserve_res["reason"]
                                elif type(error) == dict and "errorMessage" in error:
                                    err_msg = error["errorMessage"]
                                if "You have reached the limit of addresses you can create" in err_msg:
                                    print(f"{color}Sleeping for 30 minutes due to rate limiting{Fore.RESET}")
                                    time.sleep(30 * 60)  # sleep for 30 minutes
                                elif "Invalid global session" or "Missing X-APPLE-WEBAUTH-USER cookie" in err_msg:
                                    filename1 = "cookie.txt"
                                    for root, dirs, files in os.walk("/"):
                                        if filename1 in files:
                                            os.remove(os.path.join(root, filename1))
                                            timestamp = get_timestamp()
                                            print(f"\033[38;5;94m[{timestamp}]{color}Deleting file because of error: {Fore.RESET}" + err_msg)
                                            sys.exit()
                                self.console.log(
                                    f"[bold red][ERR][/] - Failed to reserve email {email}. Reason: {err_msg}"
                                )

                            self.console.log(f'[bold green][100%] "{email}" - [bold green]Successfully reserved')
                            return email

                        async def _generate(self, num: int):
                            tasks = []
                            for _ in range(num):
                                task = asyncio.ensure_future(self._generate_one())
                                tasks.append(task)

                            return filter(lambda e: e is not None, await asyncio.gather(*tasks))

                        async def generate(self) -> List[str]:
                            try:
                                emails = []
                                s = IntPrompt.ask(
                                    Text.assemble((f"{color}How many iCloud emails do you want to generate?{Fore.RESET}")),
                                    console=self.console,
                                )

                                count = int(s)
                                self.console.log(f"[bold green]Generating {count} [bold green]email(s){Fore.RESET}")

                                with self.console.status(f"{color}Generating iCloud email(s)...{Fore.RESET}"):
                                    while count > 0:
                                        batch = await self._generate(
                                            count if count < MAX_CONCURRENT_TASKS else MAX_CONCURRENT_TASKS
                                        )
                                        count -= MAX_CONCURRENT_TASKS
                                        emails += batch

                                if len(emails) > 0:
                                    with open("emails.txt", "a+") as f:
                                        f.write(os.linesep.join(emails) + os.linesep)

                                    self.console.log(
                                        f'[bold green]Emails have been saved into the "emails.txt" file'
                                    )

                                    self.console.log(
                                        f"[bold green]Successfully generated [bold green]{len(emails)} email(s)"
                                    )

                                return emails
                            except KeyboardInterrupt:
                                return []

                        async def list(self, active: bool, search: str) -> None:
                            gen_res = await self.list_email()
                            if not gen_res:
                                return

                            if "success" not in gen_res or not gen_res["success"]:
                                error = gen_res["error"] if "error" in gen_res else {}
                                err_msg = "Unknown"
                                if type(error) == int and "reason" in gen_res:
                                    err_msg = gen_res["reason"]
                                elif type(error) == dict and "errorMessage" in error:
                                    err_msg = error["errorMessage"]
                                self.console.log(
                                    f"[bold red][ERR][/] - Failed to generate email. Reason: {err_msg}"
                                )
                                return

                            self.table.add_column("Label")
                            self.table.add_column("Hide my email")
                            self.table.add_column("Created Date Time")
                            self.table.add_column("IsActive")

                            for row in gen_res["result"]["hmeEmails"]:
                                if row["isActive"] == active:
                                    if search is not None and re.search(search, row["label"]):
                                        self.table.add_row(
                                            row["label"],
                                            row["hme"],
                                            str(
                                                datetime.datetime.fromtimestamp(
                                                    row["createTimestamp"] / 1000
                                                )
                                            ),
                                            str(row["isActive"]),
                                        )
                                    else:
                                        self.table.add_row(
                                            row["label"],
                                            row["hme"],
                                            str(
                                                datetime.datetime.fromtimestamp(
                                                    row["createTimestamp"] / 1000
                                                )
                                            ),
                                            str(row["isActive"]),
                                        )

                            self.console.print(self.table)

                    async def generate() -> None:
                        async with RichHideMyEmail() as hme:
                            await hme.generate()


                    async def list(active: bool, search: str) -> None:
                        async with RichHideMyEmail() as hme:
                            await hme.list(active, search)

                    if __name__ == "__main__":
                        loop = asyncio.new_event_loop()
                        loop.run_until_complete(generate())
                        break

                else:
                    # Run code if the file does not exist or is empty
                    print("The file is either empty or does not exist")
                    # set up the webdriver
                    driver = webdriver.Chrome()
                    driver.get("https://www.icloud.com/")

                    # wait for the sign-in button to become clickable
                    wait = WebDriverWait(driver, 10)
                    sign_in_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//ui-button[@class='push primary sign-in-button']")))

                    # click on the sign-in button
                    sign_in_button.click()

                    # prompt user to enter email and password manually
                    input("Please enter your email and password in the Chrome browser, then press Enter to continue...")

                    # get the cookies
                    cookies = driver.get_cookies()

                    # write the cookies to a file
                    with open('cookie.txt', 'w') as file:
                        for cookie in cookies:
                            file.write(
                                f"{cookie['name']}={cookie['value']}; path={cookie['path']}; domain={cookie['domain']}; secure={cookie['secure']}; HttpOnly={cookie['httpOnly']};")
                    print("Cookies exported")

                    # close the driver
                    driver.quit()

                # Wait for some time before checking again
                time.sleep(2)  # Wait for 1 minute before checking again
        except:
            log_error(f"An Error Occured: {traceback.format_exc()}")
    thread1 = threading.Thread(target=start)
    thread1.start()
    thread1.join()
except Exception as e:
    print(f"{Fore.RED}[x] An error occured: {e}{Fore.RESET}\n{Fore.CYAN}Redirecting to Main Menu in 5 seconds...")
    time.sleep(5)

    main_menu()
