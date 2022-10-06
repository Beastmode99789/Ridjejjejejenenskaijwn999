#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import json
import time
import ctypes
import socket
import random
import requests
import threading
from colorama import init
from threading import Thread
import itertools
init()


ctypes.windll.kernel32.SetConsoleTitleW('Xbox Follower Tool')


banner = '''
                                 _____     _ _                          _____           _
                                |  ___|__ | | | _____      _____ _ __  |_   _|__   ___ | |
                                | |_ / _ \| | |/ _ \ \ /\ / / _ \ '__|   | |/ _ \ / _ \| |
                                |  _| (_) | | | (_) \ V  V /  __/ |      | | (_) | (_) | |
                                |_|  \___/|_|_|\___/ \_/\_/ \___|_|      |_|\___/ \___/|_|

                                             
                                             [+] Unban's Follower Tool v.2 [+] 


                                                

'''
swap = '[\033[1;32;40m{}\033[1;37;40m]'.format(socket.gethostname())
error = '[\033[1;31;40mError\033[1;37;40m]'



def Clear():
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        os.system('clear')


class Xbox_Token_Grabber:
    def __init__(self):
        self.Threading()


    with open('data/xbox_user_tokens.txt', 'r') as file:
        xbox_user_tokens = file.read().splitlines()
        if len(xbox_user_tokens) < 1:
            Clear()
            print('{} No Tokens Found In data/xbox_user_tokens.txt'.format(error))
            os._exit(0)



    def Grab_Tokens(self, token):
        global xbox_grabbed

        

        try:
            json = {'RelyingParty': 'http://xboxlive.com', 'TokenType': 'JWT', 'Properties': {'UserTokens': [token], 'SandboxId': 'RETAIL'}}
            response = requests.post('https://xsts.auth.xboxlive.com/xsts/authorize', json=json)


            if response.status_code == 200:

                s = requests.session()
                proxy = set()

                with open('data/xuid.txt', 'r') as file:
                    xuid1 = file.read()

                    token = 'XBL3.0 x={};{}'.format(response.json()['DisplayClaims']['xui'][0]['uhs'], response.json()['Token'])
                    token2 = 'https://social.xboxlive.com/users/xuid({})/people/xuid({})?app_name=xbox_on_windows&app_ctx=user_profile'.format(response.json()['DisplayClaims']['xui'][0]['xid'], xuid1)

                headers = {'Authorization': token}
                response2 = requests.put(token2, headers=headers)

                if '"gamerTag":null' not in response.text:
                    xbox_tokens.append(token)
                    xbox_grabbed += 1
                else:
                    pass
            else:
                pass
        except:
            pass

        ctypes.windll.kernel32.SetConsoleTitleW('Xbox Account(s) added xuid - ({:,})'.format(xbox_grabbed))

      


    def Threading(self):
        while True:
            for token in self.xbox_user_tokens:
                for i in range(1):
                    thread = Thread(target=self.Grab_Tokens, args=(token,))
                    thread.setDaemon(True)
                    threads.append(thread)
                    thread.start()
                    time.sleep(0.1)
               


            for thread in threads:
                thread.join()

            



if __name__ == '__main__':
    Clear()
    print(banner)

    threads = []
    xbox_tokens = []
    xbox_grabbed = 0

    Xbox_Token_Grabber();print()

    ctypes.windll.kernel32.SetConsoleTitleW('Xbox Follower Tool')

    print('{} Xbox Token(s) Loaded - ({:,})'.format(swap, xbox_grabbed))

    print('\n{}'.format(swap), end='');choice = input(' All Token(s) added xuid as a friend ')

    time.sleep(5)


