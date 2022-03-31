import os
from colorama import Fore, init
import discord
import webbrowser
import time
import shutil
center = shutil.get_terminal_size().columns

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
dgreen = Fore.GREEN
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTMAGENTA_EX
dblue = Fore.MAGENTA
gray = Fore.LIGHTBLACK_EX
intents = discord.Intents.all()

def enderhandler():
    os._exit(3)
 
def makenerd():
    print("Step 1.\n" + "learn IT (python, html, css, C++) and Focus In School\n" + "be good at it too\n" + "come back when your a nerd")
    enderhandler()


 
pcname = (os.getenv('COMPUTERNAME'))
 
nerdcheck = input(f"Are You A Nerd y/n?: ")
if nerdcheck == "yes":
    print(f"welcome {pcname}")
 
if nerdcheck == "no":
    print("Nerds Only!")
    makenerd()
 
if nerdcheck == "y":
  print(f"welcome {pcname}")
 
if nerdcheck == "n":
  print("Nerds Only!")
  makenerd()

os.system('cls')
os.system('title Nerd MultiTool - Main Menu')

buh = '''
███╗   ██╗███████╗██████╗ ██████╗ 
████╗  ██║██╔════╝██╔══██╗██╔══██╗
██╔██╗ ██║█████╗  ██████╔╝██║  ██║
██║╚██╗██║██╔══╝  ██╔══██╗██║  ██║
██║ ╚████║███████╗██║  ██║██████╔╝
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═════╝ 
By Shade#3421
'''
print("Ong I Made This At School On Notepad Lmao")
for line in buh.splitlines():
    print(f'\033[35m {line}'.center(center).replace("█",f"\033[0m█\033[35m"))

border = "\033[0m─"*center
print(border.center(center))

print("""
            [1] Teddy Stealer                  [2] Nightmare Tools                  [3] Hazard Nuker


             [4] Hook Stealer                  [5] Site                            [6] Suggest
             

                                               [7] Credits                            
""")
option = input("Option: ")

if option == "1":
    webbrowser.open('https://codeload.github.com/Shade3421/TeddyStealer/zip/refs/heads/main')

if option == "2":
    webbrowser.open('https://codeload.github.com/Shade3421/Nightmare-Tools/zip/refs/heads/main')

if option == "3":
    webbrowser.open('https://codeload.github.com/Rdimo/Hazard-Nuker/zip/refs/heads/master')

if option == "4":
    webbrowser.open('https://codeload.github.com/Shade3421/HookStealer/zip/refs/heads/main')

if option == "5":
    webbrowser.open('https://shade.army')

if option == "6":
    webbrowser.open('https://discord.gg/raid')

if option == "7":
    print(' These Are Just People I love\n' + " dacki#0001\n Rin|#4671\n slimez#3883\n Steffke#0002\n Speaker#1799\n steveSkid#9117\n strxanger#0001\n DeKrypt#7777\n Rdimo#6968\n The Variety Universe#9395\n If Your Name Isnt Here Im Sorry\n")
    input("Press ENTER To Exit!")
    enderhandler()
