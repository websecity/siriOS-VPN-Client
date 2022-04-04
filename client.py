# -*- coding: utf-8 -*-
from colorama import Fore
import subprocess
import json
import logo
import vpnsettings
from startOS import startup

# For clearing console
startup()

logo.logo_text()
sign = "siriOS-VPN"

# Config file
with open("config.json") as jsonFile:
    jsonRead = json.load(jsonFile)
    jsonWrite = json.dump
    jsonFile.close()


# Selecting OS
def setup():
    if len(jsonRead['OS']) == 0:
        print(sign + "Please select your OS: Linux | Windows | Mac")
        os = input(sign + ":\t")
        with open("config.json", "w") as f:
            jsonRead["OS"] = os
            json.dump(jsonRead, f, indent=4)
            f.close()

        if os == "Linux" or os == "Windows" or os == "MacOS" or os == "Lin" or os == "Win" or os == "Mac":
            print("Your system choice setting has been successfully set to: " + os)

        elif os != "Linux" or "Windows" or "MacOS" or "Win" or "Mac" or "Lin":
            print("Please enter a valid option.")
            return setup()
    else:
        pass


# Menus
def ui():
    # Fow Windows
    if len(jsonRead['OS']) >= 1 and jsonRead['OS'] == "Windows" or "Win":
        print(Fore.CYAN + "1) New VPN connection")
        print("2) Go Windows VPN Settings")
        print("3) Show VPN profiles")
        print("4) Settings")
        inp_win = int(input(sign + " | Please select:\t"))

        # Add VPN Connection Section
        if inp_win == 1:
            print(Fore.CYAN + "Name of connection:")
            name = input(sign + ":  ")
            print(Fore.CYAN + "IP/server address:")
            ip = input(sign + ":  ")
            print(Fore.CYAN + "IPSec PSK:")
            ipsecpsk = input(sign + ":\t")

            subprocess.call(["powershell",
                             "Add-VpnConnection -Name {} -ServerAddress {} -L2tpPsk {} -TunnelType L2tp "
                             "-EncryptionLevel Required -AuthenticationMethod Chap,MSChapv2 -Force "
                             "-RememberCredential -PassThru".format(
                                 name, ip, ipsecpsk)], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            print(Fore.WHITE + "\nSuccesfully added VPN as {}\n {} | IP {}\n {} | PSK{}".format(name, sign, ip, sign,
                                                                                                ipsecpsk))
            print("\n")
            return ui()
        # Windows VPN settings
        elif inp_win == 2:
            vpnsettings.vpn_settings()
            print("\n")
            return ui()
        # Print VPN configurations
        elif inp_win == 3:
            subprocess.call(["powershell", "Get-VpnConnection"], shell=True)
            print("\n")
            return ui()

        # OS Settings
        elif inp_win == 4:

            def option4():

                print(sign + "Select your operating system: [Win | Linux | MacOS]")
                setting_os = input(sign + "\t")

                if setting_os == "Linux" or "Windows" or "MacOS" or "Lin" or "Win" or "Mac":

                    with open("config.json", "w") as f:
                        jsonRead["OS"] = setting_os
                        json.dump(jsonRead, f, indent=4)
                        f.close()
                        print(sign + " | Successfully changed to {}".format(setting_os))
                        return ui()
                elif setting_os != "Linux" or "Windows" or "MacOS" or "Lin" or "Win" or "Mac":
                    print("Please enter a valid option.")
                    return option4()

            option4()
        elif inp_win != 1 or jsonRead['OS'] != "Win" or inp_win != 2 or inp_win != 3 or inp_win != 4:
            print(Fore.RED + sign + " | Please enter a valid option.")
            return ui()


setup()
ui()
