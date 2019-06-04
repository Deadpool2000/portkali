#!/usr/bin/python3
import os
import getpass

os.system('clear')
try:
    # Color code
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    B='\033[95m'    
    print(G+"""

██████╗  ██████╗ ██████╗ ████████╗██╗  ██╗ █████╗ ██╗     ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██║ ██╔╝██╔══██╗██║     ██║
██████╔╝██║   ██║██████╔╝   ██║   █████╔╝ ███████║██║     ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔═██╗ ██╔══██║██║     ██║
██║     ╚██████╔╝██║  ██║   ██║   ██║  ██╗██║  ██║███████╗██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝

                { Code By -> Deadpool2000 }"""+Y+"""
                  
Note: Please remove all old kali repositories before installation to avoid errors"""+W)

    def list1():
        
        print(B+"""
#################################################################################"""+G+"""

>>> Main Menu"""+CY+"""

1) Add Kali Repositories
2) Update System
3) Remove all kali repositories
4) Read sources.list file
5) Install Kali Tools
6) Exit
"""+W)
    def l2():
        print(B+"""
#################################################################################"""+G+"""

>>> Kali Linux Tools"""+Y+"""

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
"""+W)
    def check():
        r=getpass.getuser()
        if r!="root":
            print(B+"#################################################################################\n")
            print(R+"You are not root ! First run 'sudo su' and try again this tool !\n\n"+W)
            exit(0)     
    def sel():
        try:
            ch=int(input(R+"#"+Y+" Enter your choice >> "+W))
            if ch==1:
                try:
                    f=os.path.isfile("/usr/bin/wget")
                    if f==False:
                        os.system("apt-get install wget -y")
                    print(G+"\nBacking up 'sources.list'.........................\n")
                    os.system("cp /etc/apt/sources.list /etc/apt/sources.list.bak")
                    print(B+"\nBackup saved as 'sources.list.bak' \n")
                    print(G+"\nAdding repositories................\n")               
                    os.system("echo '# \ndeb http://kali.cs.nctu.edu.tw/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                    os.system("wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add")    
                    print(Y+"\nKali Repositories added successfully!\n"+W)
                except ConnectionError:
                    print("Error! Please check your internet connection and try again :(")
                list1()
                sel()
            elif ch==2:
                print(CY+"Updating system.................................\n"+W)
                os.system("apt-get update")
                list1()
                sel()
            elif ch==3:
                try:
                    with open("/etc/apt/sources.list","r") as inp:
                        with open("/etc/apt/sources.list.rf","w") as out:
                            for line in inp:
                                if line.strip("\n")!="deb http://kali.cs.nctu.edu.tw/kali kali-rolling main contrib non-free":
                                    out.write(line)
                    out.close()
                    os.remove("/etc/apt/sources.list")
                    os.system("mv /etc/apt/sources.list.rf /etc/apt/sources.list")
                    print(R+"\nAll kali linux repositories have been deleted!\n")    
                    print(CY+"\nUpdating system.................................\n"+W)
                    os.system("sudo apt-get update")
                except FileNotFoundError:
                    print(R+"File not found!"+W)
                list1()
                sel()
            elif ch==4:
                print(Y+"\nsources.list file >>> \n"+W)
                os.system("cat /etc/apt/sources.list")
                list1()
                sel()
            elif ch==5:
                l2()
                def tool():
                    c=int(input(R+"#"+Y+" Enter your choice >> "+W))
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
                        print(R+"Invalid option! Please try again"+W)
                        tool()
                tool()
            elif ch==6:
                print(Y+"\n\nExit...........! Have a nice day :)\n")
                print(R+"[======================"+Y+"  Code By"+B+" -"+CY+" Deadpool2000 "+R+"==========================]\n"+W)      
            else:
                print(R+"\nInvalid option! Please try again :( \n")
                sel()
        except ValueError:
            print(R+"\nInvalid option! Please try again :( \n")
            sel()
    check()
    list1()
    sel()
except KeyboardInterrupt:    
    print(Y+"\n\nExit...........! Have a nice day :)\n")
    print(R+"[======================"+Y+"  Code By"+B+" -"+CY+" Deadpool2000 "+R+"==========================]\n"+W) 

