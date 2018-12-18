#!/usr/bin/python


import subprocess


def mac_address_backup(interface, file="backup.txt"):
    cmd_backup = "ip link show {0} | awk '{1}' ".format(interface,"/ether/ {print $2}")
    print(cmd_backup)
    mac_address = subprocess.check_output(cmd_backup, shell=True)
    with open(file, 'a') as file_handler:
        file_handler.write(mac_address.decode("utf-8"))


def mac_changer(mac_adress, interface):
    cmd_up = "ifconfig {0} up ".format(interface)
    cmd_change = "ifconfig {0} hw ether {1} ".format(interface, mac_adress)
    cmd_down = "ifconfig {0} down ".format(interface)

    subprocess.call(cmd_down, shell=True)
    subprocess.call(cmd_change, shell=True)
    subprocess.call(cmd_up, shell=True)


if __name__ == "__main__":
    print(subprocess.call("ifconfig", shell=True))
    #mac_address_backup("eth0")
    mac_changer("08:00:27:d8:3f:2b", "eth0")
    print(subprocess.call("ifconfig", shell=True))
