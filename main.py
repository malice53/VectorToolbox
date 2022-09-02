import gratient
from colorama import Fore, Style
import os
import subprocess
import time


### Variables ###
blue = Fore.BLUE + Style.BRIGHT
purp = Fore.MAGENTA + Style.DIM
white = Fore.WHITE + Style.BRIGHT


def cls():
    os.system('cls')
    print(gratient_header)
def cls2():
    os.system('cls')
    print(gratient_header2)

info = blue + "[" + white + '*' + blue + ']' + white
error = blue + "[" + white + '!' + blue + ']' + white
inputt = blue + "[" + white + '>' + blue + ']' + white

headertext = f"""

:::     ::: :::::::::: :::::::: ::::::::::: ::::::::  :::::::::  
:+:     :+: :+:       :+:    :+:    :+:    :+:    :+: :+:    :+: 
+:+     +:+ +:+       +:+           +:+    +:+    +:+ +:+    +:+ 
+#+     +:+ +#++:++#  +#+           +#+    +#+    +:+ +#++:++#:  
 +#+   +#+  +#+       +#+           +#+    +#+    +#+ +#+    +#+ 
  #+#+#+#   #+#       #+#    #+#    #+#    #+#    #+# #+#    #+# 
    ###     ########## ########     ###     ########  ###    ### 
[!]----------------------------------------------------------[!]
                         WiFi Toolbox
                           @malice

1: Display WiFi Connections             2: Display WiFi Password 
3: Connect To Wifi                      4: Credits                        
"""
headertext2 = f"""

:::     ::: :::::::::: :::::::: ::::::::::: ::::::::  :::::::::  
:+:     :+: :+:       :+:    :+:    :+:    :+:    :+: :+:    :+: 
+:+     +:+ +:+       +:+           +:+    +:+    +:+ +:+    +:+ 
+#+     +:+ +#++:++#  +#+           +#+    +#+    +:+ +#++:++#:  
 +#+   +#+  +#+       +#+           +#+    +#+    +#+ +#+    +#+ 
  #+#+#+#   #+#       #+#    #+#    #+#    #+#    #+# #+#    #+# 
    ###     ########## ########     ###     ########  ###    ### 
[!]----------------------------------------------------------[!]
                         WiFi Toolbox                               
                           @malice                                                      

1: Get 1 Password                                    2: List All                              
"""

### Setting Up ###
print(Style.BRIGHT + '')
gratient_header = gratient.blue(headertext)
gratient_header2 = gratient.blue(headertext2)
cls()

while True:
    
    choice = input(inputt)

    if choice == "1":
        cls()
        connections = subprocess.check_output(['netsh','wlan','show','network'])
        # Stackoverflow LMFAO
        encoding='utf-8'
        connections = connections.decode('ascii')
        connections = connections.replace("\r","")
        print(connections)
        print(info + "Press enter to return to selection...")
        input()
        cls()
    elif choice == "2":
        cls2()

        class getPassword:
            def __init__(self, name):
                self.name = name

            def getOnePassword(self):
                passw = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', self.name, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                passw = [b.split(":")[1][1:-1] for b in passw if "Key Content" in b]

                print(f'Network: {self.name}    \/     Password: {passw[0]}')
                

        while 1==1:
            cls2()
            choice2 = input(inputt)

            if choice2 == "1":
                cls2()
                print(info + "Network Name")
                netname = input(inputt)
                nettarget = getPassword(netname)
                nettarget.getOnePassword()
                print()
                print(info + "Press enter to return to selection...")
                input()
                cls2()
            elif choice2 == "2":
                connections = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
                profiles = [i.split(":")[1][1:-1] for i in connections if "All User Profile" in i]
                for i in profiles:
                    try:
                        passw = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                        passw = [b.split(":")[1][1:-1] for b in passw if "Key Content" in b]
                        try:
                            print ("{:<20}\/  {:<}".format(i, passw[0]))
                        except IndexError:
                            print ("{:<20}\/  {:<}".format(i, ""))
                    except subprocess.CalledProcessError:
                        print ("{:<20}|  {:<}".format(i, "Error"))

                print()
                print(info + "Press enter to return to selection...")
                input()
                cls()
            else:
                print(error + 'Not an option!')
                time.sleep(0.5)
                cls2()
    elif choice == "3":


        #CREDIT: https://www.geeksforgeeks.org/how-to-connect-wifi-using-python/

        cls()
        def createNewConnection(name, SSID, password):
            config = """<?xml version=\"1.0\"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>"""+name+"""</name>
            <SSIDConfig>
                <SSID>
                    <name>"""+SSID+"""</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>"""+password+"""</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>"""
            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config)
            os.system(command)
          
        def connect(name, SSID):
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
            os.system(command)
        

        def displayAvailableNetworks():
            command = "netsh wlan show networks interface=Wi-Fi"
            os.system(command)
        
        print(info + "Available Networks: ")
        time.sleep(1)
        displayAvailableNetworks()
        

        print(info + "SSID/Name")
        name = input(inputt)
        cls()
        
        print(info + "Password")
        password = input(inputt)
        
        createNewConnection(name, name, password)
        

        connect(name, name)
        print()
        print(info + "Press enter to return to selection...")
        input()
        cls2()
    elif choice == "4":
        cls()
        print(info + "Credits")
        print()
        print(info + "github.com/malice53")
        print(info + "www.geeksforgeeks.org")
        print()
        print()
        print(info + "Press enter to return to selection...")
        input()
        cls()
