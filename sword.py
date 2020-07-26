import sys, time, os, itertools
tname = 'sword.py'
nm = os.name
print"\033[1;96m You Are Using "+ nm
time.sleep(1)
#Colors

rs = '\033[1;0m'
rd = '\033[1;31m'
gn = '\033[1;32m'
yl = '\033[1;33m'
bl = '\033[1;34m'
ul = '\033[1;4m'
vl = '\033[1;35m'
lb = '\033[1;36m'
bg = '\033[1;7m'
cf = '\033[1;9m'


def cl():
	os.system("clear")
fm = gn +"[" + rd +"+" +gn +"]" +rs +" "
fm1 = rd +"[" + yl +"+" +rd +"]" +rs +" "

t = time.asctime()

pwd = os.system("cd /data/data/com.termux/files/home/")

def ls():
	print gn+"                 Installed Successfully"
	print""
	slowly(yl +"Returning To Start Page...")
	os.system("cd ")
	os.system("python2 "+ tname)
cl()

def slowly(s):
	       try:
	               time.sleep (1)
	               for w in s + '\n' :
	                         sys.stdout.write(w)
	                         sys.stdout.flush ()
	                         time.sleep (10. / 100)
	               time.sleep(1.5)
	       except KeyboardInterrupt:
	               time.sleep(1)
	               print""
	               print rd +"speed \033[1;32m- \033[1;33m 3x...."
	               time.sleep(1)
def myinfo():
	         os.system("clear")
	         slowly (yl +"Returning To Main Page...")
	         os.system("cd")
	         os.system("python2 "+ tname)
def stintro():
             slowly(fm + yl +"Starting Framework Console...")
             os.system("clear")
             print""

def enintro():
             slowly(fm1 + bl +"Closing Framework Console...")
             os.system("clear & login")
def relo():
	os.system("clear")
	banner()
	tool()
	input()
	return

def tpackages():
	os.system("pkg install git -y")
	os.system("pkg install python2 -y")
	os.sysem("pkg install python -y")
	os.system("pkg install python3 -y")
	os.system("pkg install clang -y")
	os.system("pkg install php -y")
	os.systen("pkg install ruby -y")
	os.system("pkg install wget -y")
	os.system("pkg install nano")
def banner():
           print""
           print""
           print  rd +"           [\033[1;32m=====================\033[1;31m]"
           print rd +"           [                     ]"
           print rd +"           [\033[1;35m     SWORD Tool\033[1;31m      ]"
           print rd +"           [                     ]"
           print  rd +"           [\033[1;32m=====================\033[1;31m]"
           print gn +"                                            ", t
           
         

def author():
	cl()
	print('\n')
	print('\n')
	print('\n')
	print bl +"             ==========================="
	print""
	print rd +"            Author : \033[1;32m Muhamed Lafeer"
	print""
	print rd +"            Youtube : \033[1;32m PY-Linux"
	print""
	print rd +"            Github : \033[1;32m PY-Linux"
	print""
	print rd +"            Email : \033[1;32m lafir837@gmail.com"
	print""
	print rd+"            Today : \033[1;37m", t
	print""
	print bl +"             ==========================="
######

def tool():
	print gn +"                01. \033[1;33mWeeman"

	print gn +"                02.\033[1;33m Websploit"

	print gn +"                03. \033[1;33mADB-ToolKit"

	print gn +"                04. \033[1;33mA-Rat"

	print gn +"                05. \033[1;33mAndroSpy"
	print gn +"                06. \033[1;33mBrutal"

	print gn +"                07. \033[1;33mBreacher"

	print gn +"                08. \033[1;33mD-Tech"
	
	print gn +"                09. \033[1;33mEasY_HacK"
	
	print gn+"                10. \033[1;33mExploitOnCLI"
	
	print gn +"                11. \033[1;33mEyeWitness"
	
	print gn +"                12. \033[1;33mGoldenEye"
	
	print gn +"                13. \033[1;33mTermux-Packages"
	print""
	print rd +"      # - \033[1;33m Exit     \033[1;31m + -  \033[1;33mHelp \033[1;31m    A - \033[1;33mAuthor\033[1;31m  M - \033[1;33mMy device info"
	print ""



####

def help():
	print yl +"Enter No. To Install Tool Or Other"
	print""
	print yl +"CTRL + d is easy exit method"
	print""
	slowly(gn +"Restarting Tool...")

#####

def input():
	x = raw_input(fm + bl +"Sw06D[ :\033[1;36m ")
	if x=='#':
		print""
		enintro()
		
	elif x=='+':
		print""
		help()
		os.system("python2 "+ tname)
	elif x=='A' or x=='a':
		author()
		slowly(gn +"Restarting Tool...")
		os.system("python2 "+ tname)
	elif x=='m' or x=='M':
		cl()
		os.system("bash screenfetch")
		time.sleep(8)
		print""
		ls()
		
	elif x=='1' or x=='01':
		print""
		cl()
		pwd
		os.system("git clone https://github.com/evait-security/weeman.git")
		ls()
	elif x=='2' or x=='03':
		cl()
		pwd
		os.system("git clone https://github.com/websploit/websploit.git")
		ls()
	elif x =='3' or x=='03':
		cl()
		pwd
		os.system("git clone https://github.com/esc0rtd3w/adb-toolkit")
		ls()
	elif x=='4' or x=='04':		
		cl()
		pwd
		os.system("git clone https://github.com/RexTheGod/A-Rat")
    		ls() 
    	elif x=='5' or x=='05':
    		cl()
    		pwd
    		os.system("git clone https://github.com/TunisianEagles/Androspy.git")
    		ls()
    	elif x=='6' or x=='06':
    		cl()
    		pwd
    		os.system("git clone https://github.com/Screetsec/Brutal.git")
    		ls()
    	elif x=='7' or x=='07':
    		cl()
    		pwd
    		os.system("git clone https://github.com/UltimateHackers/Breacher.git")
    		ls()
    	elif x=='8' or x=='08':
    		cl()
    		pwd
    		os.system("git clone https://github.com/bibortone/D-Tech")
    		ls()
    	elif x=='9' or x=='09':
    		cl()
    		pwd
    		os.system("git clone https://github.com/sabri-zaki/EasY_HaCk.git")
    		ls()
    	elif x=='10':
    		cl()
    		pwd
    		os.system("git clone https://github.com/r00tmars/ExploitOnCLI.git")
    		ls()
    	elif x=='11':
    		cl()
    		pwd
    		os.system("git clone https://github.com/FortyNorthSecurity/EyeWitness.git")
    		ls()
    	elif x=='12':
    		cl()
    		pwd
    		os.system("git clone https://github.com/jseidl/GoldenEye.git")
    		ls()
    	elif x=='13':
    		cl()
    		pwd
    		tpackages()
    		ls()
    	elif x=='':
    		relo()
   
stintro()
banner()
tool()


try:
	input()
except EOFError or KeyboardError:
	enintro()
