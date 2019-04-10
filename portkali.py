#!/usr/bin/python3
import os

os.system('clear')
try:
    os.system("echo '\e[92m'")
    print("""

██████╗  ██████╗ ██████╗ ████████╗██╗  ██╗ █████╗ ██╗     ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║ ██╔╝██╔══██╗██║     ██║
██████╔╝██║   ██║██████╔╝   ██║   █████╔╝ ███████║██║     ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔═██╗ ██╔══██║██║     ██║
██║     ╚██████╔╝██║  ██║   ██║   ██║  ██╗██║  ██║███████╗██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝

                Code By --> Deadpool2000

        Import Kali Linux Repositories in any Debian distro

#########################################################################
""")

    def list1():
        os.system("echo '\e[96m'")
        print("""
1) Add Kali Repositories
2) Update System
3) Remove all kali repositories
4) Read sources.list file
5) Install Kali Tools
6) Exit
""")
    def l2():
        os.system("echo '\e[93m'")
        print("""

>>> Kali Linux Tools

1] Aircrack-ng
2] Armitage
3] Apktool
4] Burpsuite
5] Dex2jar
6] John the Ripper
7] Kismet
8] Mdk3
9] Metasploit-Framework
10] Nmap
11] PixieWPS
12] RainbowCrack
13] Recon-ng
14] Setoolkit
15] Sqlmap
16] Wifite
17] Wireshark

99] Back to Main Menu
""")
    
    def sel():
        ch=int(input("# Enter your choice >> "))
        if ch==1:
            try:
                os.system('sudo apt-get install wget -y')
                os.system("echo '# \ndeb http://kali.cs.nctu.edu.tw/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                os.system("wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add")
                os.system("echo '\e[93m'")
                print("Kali Repositories successfully added!\n")
            except ConnectionError:
                print("Error! Please check your internet connection and try again :(")
            list1()
            sel()
        elif ch==2:
            os.system("echo '\e[97m'")
            print("Updating system.................................\n")
            os.system("apt-get update")
            list1()
            sel()
        elif ch==3:
            os.system("echo '\e[97m'")
            try:
                with open("/etc/apt/sources.list","r") as inp:
                    with open("/etc/apt/sources.list.rf","w") as out:
                        for line in inp:
                            if line.strip("\n")!="deb http://kali.cs.nctu.edu.tw/kali kali-rolling main contrib non-free":
                                out.write(line)
                out.close()
                os.remove("/etc/apt/sources.list")
                os.system("mv /etc/apt/sources.list.rf /etc/apt/sources.list")
                os.system("echo '\e[91m'")
                print("All kali linux repositories have been deleted!\n")
                os.system("echo")
                os.system("echo '\e[97m'")
                print("Updating system.................................\n")
                os.system("sudo apt-get update")
            except FileNotFoundError:
                os.system("echo '\e[91m'")
                print("File not found!")
            list1()
            sel()
        elif ch==4:
            os.system("echo '\e[97m'")
            os.system("cat /etc/apt/sources.list")
            list1()
            sel()
        elif ch==5:
            l2()
            def tool():
                c=int(input("# Enter your choice >> "))
                os.system("echo '\e[97m'")
                if c==1:
                    os.system("sudo apt-get install aircrack-ng -y")
                    l2()
                    tool()
                elif c==2:
                    os.system("sudo apt-get install armitage -y")
                    l2()
                    tool()
                elif c==3:
                    os.system("sudo apt-get install apktool -y")
                    l2()
                    tool()
                elif c==4:
                    os.system("sudo apt-get install burpsuite -y")
                    l2()
                    tool()
                elif c==5:
                    os.system("sudo apt-get install dex2jar -y")
                    l2()
                    tool()
                elif c==6:
                    os.system("sudo apt-get install john -y")
                    l2()
                    tool()
                elif c==7:
                    os.system("sudo apt-get install kismet -y")
                    l2()
                    tool()
                elif c==8:
                    os.system("sudo apt-get install mdk3 -y")
                    l2()
                    tool()
                elif c==9:
                    os.system("sudo apt-get install metasploit-framework -y")
                    l2()
                    tool()
                elif c==10:
                    os.system("sudo apt-get install nmap -y")
                    l2()
                    tool()
                elif c==11:
                    os.system("sudo apt-get install pixiewps -y")
                    l2()
                    tool()
                elif c==12:
                    os.system("sudo apt-get install rainbowcrack -y")
                    l2()
                    tool()
                elif c==13:
                    os.system("sudo apt-get install recon-ng -y")
                    l2()
                    tool()
                elif c==14:
                    os.system("sudo apt-get install set -y")
                    l2()
                    tool()
                elif c==15:
                    os.system("sudo apt-get install sqlmap -y")
                    l2()
                    tool()
                elif c==16:
                    os.system("sudo apt-get install wifite -y")
                    l2()
                    tool()
                elif c==17:
                    os.system("sudo apt-get install wireshark -y")
                    l2()
                    tool()
                elif c==99:
                    list1()
                    sel()
                else:
                    os.system("echo '\e[91m'")
                    print("Invalid option! Please try again")
                    tool()
            tool()
        elif ch==6:
            os.system("echo '\e[93m'")
            print("\nExit...........! Have a nice day :)\n")
            print("[======================  Code By - Deadpool2000 ==========================]")
            os.system("echo '\e[97m'")            
        else:
            os.system("echo '\e[91m'")
            print("Invalid option! Please try again\n")
            sel()
    list1()
    sel()
except KeyboardInterrupt:
    os.system("echo '\e[93m'")
    print("\nExit...........! Have a nice day :)\n")
    print("[======================  Code By - Deadpool2000 ==========================]")
os.system("echo '\e[97m'")
