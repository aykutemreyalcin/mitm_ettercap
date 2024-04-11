Man-in-the-Middle Attack Tool
=============================

Introduction
------------

This Python script implements a simple Man-in-the-Middle (MITM) attack tool. It leverages ARP spoofing using `ettercap` to intercept network traffic between a target victim and the router, facilitating network sniffing.

Features
--------

*   Discovers the router's IP address and the connected subnet using `netifaces`.
*   Scans the network using `nmap` to identify live hosts.
*   Launches `Wireshark` for packet capture and analysis.
*   Performs ARP spoofing using `ettercap` to intercept traffic between the victim and router.

Requirements
------------

*   This script requires `Python 3.x` to run.
*   Install the necessary Python libraries: `scapy`, `colorama`, and `netifaces`.
*   Ensure `Wireshark`, `nmap`, and `ettercap` are installed on your system.
*   **Note**: The script should be executed with `sudo` privileges to perform network-related operations.

Usage
-----

1.  Run the script with `sudo` privileges: `sudo python3 mitm_attack.py`.
2.  Follow the on-screen instructions:
    *   Enter the IP address of the victim.
    *   Monitor network traffic using `Wireshark`.
3.  The script will perform ARP spoofing and intercept traffic between the victim and router.

Disclaimer
----------

*   This tool is for educational and testing purposes only. Misuse of this tool for unauthorized access to networks is illegal and unethical.
*   Use this tool responsibly and only on networks you are authorized to access.
