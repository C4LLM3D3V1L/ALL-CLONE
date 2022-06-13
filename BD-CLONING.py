
import os,sys,time

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
        
        
      
        	
logo =("""


\033[97;1m   _____           ____       __ 
\033[96;1m  / ___/___  _____/ __ \___  / /_
\033[94;1m  \__ \/ _ \/ ___/ / / / _ \/ __/
 \033[91;1m___/ /  __/ /__/ /_/ /  __/ /_  
\033[96;1m/____/\___/\___/_____/\___/\__/  


\n\x1b[1;33;40m--------------------------------------------------\n  \x1b[1;36;40mAuthor     \x1b[1;33;40m: \x1b[0;37;40mAdnan Adif Hisham\n  \x1b[1;36;40mGitHub     \x1b[1;33;40m: \x1b[0;37;40mhttps://github.com/C4LLM3D3V1L\n  \x1b[1;36;40mFacebook   \x1b[1;33;40m: \x1b[0;37;40mhttps://Facebook.com/C4LL.M3.D3V1L\n  \x1b[1;36;40mPublic     \x1b[1;33;40m: \x1b[0;37;40m12-06-2022\n\x1b[1;33;40m
\n\x1b[1;33;40m--------------------------------------------------\n
""")
os.system("clear")
print(logo)
psb("\033[0;91m                 BD 6-7-8-11 DIGIT CLONING TOOL")
print("\033[0;90m ><><><><><><><><><><><><><><><><><><>><")
print("\033[0;94m            [1] 6 DIGIT CLONING")
print("\033[0;93m            [2] 7 DIGIT CLONING")
print(" \033[96;1m           [3] 8 DIGIT CLONING")
print(" \033[0;94m           [4] 11 DIGIT CLONING")
print("  \033[1;97m          [5] FOLLOW ON FACEBOOK")
print("\033[0;91m            [E] Exit \n")
Adnan =input(" \033[0;93mChoose : ")
if Adnan in ["1", "01"]:
	os.system("python2 code06.py")
if Adnan in ["2", "02"]:
	os.system("python2 code07.py")
if Adnan in ["3", "03"]:
	os.system("python2 code08.py")
if Adnan in ["4", "04"]:
	os.system("python2 code11.py")
if Adnan in ["5", "05"]:
	os.system('xdg-open https://www.facebook.com/C4LL.M3.D3V1L')
	exit()
else:
		print (" Select Correctly ")
		time.sleep(1)
		sys.exit()