import os
import sys
os.system("clear")
os.chdir("/data/data/com.termux/files/home/lock")
os.system(" cp motd /data/data/com.termux/files/usr/etc/")

def banner():

   banner = '''
   \033[1;32;40m Welcome to the world of C.S.G lover

   \033[1;36;40m                | |
   \033[1;36;40m                | |
   \033[1;36;40m             ___| |___
   \033[1;36;40m             \       /
   \033[1;36;40m              \     /
   \033[1;36;40m               \   /
   \033[1;36;40m                \ /
   \033[1;36;40m                 •
   \033[1;31;40m       .....           .....
   \033[1;31;40m   ,ad8PPPP88b,     ,d88PPPP8ba,
   \033[1;31;40m  d8P"      "Y8b, ,d8P"      "Y8b
   \033[1;31;40m dP'           "8a8"           `Yd
   \033[1;31;40m 8(              "              )8
   \033[1;31;40m I8                             8I
   \033[1;31;40m  Yb,          \033[1;32;40mC.S.G\033[1;31;40m          ,dP
   \033[1;31;40m   "8a,                     ,a8"
   \033[1;31;40m     "8a,                 ,a8"
   \033[1;31;40m       "Yba             adP"
   \033[1;31;40m         `Y8a         a8P'
   \033[1;31;40m           `88,     ,88'
   \033[1;31;40m             "8b   d8"
   \033[1;31;40m              "8b d8"
   \033[1;31;40m               `888'
   \033[1;31;40m                 "

   '''
   print (banner)
def newloger():

   while True:
     try:
       print ("")
       print ("      .--------.               ")
       print ("     / .------. \              ")
       print ("    / /        \ \             ")
       print ("    | |        | |             ")
       print ("   _| |________| |_            ")
       print (" .' |_|        |_| '.          ")
       print (" '._____ ____ _____.'          ")
       print (" |     .'____'.     |          ")
       print (" '.__.'.'    '.'.__.'          ")
       print (" '.__  | Lock1|  __.'          ")
       print (" |   '.'.____.'.'   |          ")
       print (" '.____'.____.'____.'          ")
       print (" '.________________.'          ")
       print ("")
       lock1 = input("\033[1;36;40mEnter the password that you want to put in lock1 --> \033[1;32;40m")
       relock1 = input("\033[1;36;40mReEnter the password that you want to put in lock1 --> \033[1;32;40m") 
       if lock1 == relock1:
          while True:
            try:
              print ("")
              print ("")
              print ("      .--------.               ")
              print ("     / .------. \              ")
              print ("    / /        \ \             ")
              print ("    | |        | |             ")
              print ("   _| |________| |_            ")
              print (" .' |_|        |_| '.          ")
              print (" '._____ ____ _____.'          ")
              print (" |     .'____'.     |          ")
              print (" '.__.'.'    '.'.__.'          ")
              print (" '.__  | Lock2|  __.'          ")
              print (" |   '.'.____.'.'   |          ")
              print (" '.____'.____.'____.'          ")
              print (" '.________________.'          ")
              print ("")
              lock2 = input("\033[1;36;40mEnter the password that you want to put in lock2 --> \033[1;32;40m")
              relock2 = input("\033[1;36;40mReEnter the password that you want to put in lock2 --> \033[1;32;40m")
              if lock2 == relock2:
                 print ("done")
                 break
              print ("\033[1;31;40m     password did not match     ")
            except Exception as e:
              print (e)
          break
       print ("\033[1;31;40m       password did not match    ")
     except Exception as e:
       print (e)

   os.chdir("/data/data/com.termux/files/home/lock")
   x = (lock1 + os.linesep + lock2)
   os.system ("clear")
   f = open (".show", "w")
   f.write(str(x))
   f.close()

   bashrc(lock1, lock2)
def bashrc(lock1, lock2):

   filename = "/data/data/com.termux/files/usr/etc/bash.bashrc"
   f = open (filename, "w")
   print ("# Command history tweaks:",file = f)
   print ("# - Append history instead of overwriting",file = f)
   print ("",file = f)
   print ("#   when shell exits.",file = f)
   print ("# - When using history substitution, do not",file = f)
   print ("#   exec command immediately.",file = f)
   print ("# - Do not save to history commands starting",file = f)
   print ("#   with space.",file = f)
   print ("# - Do not save duplicated commands.",file = f)
   print ("shopt -s histappend",file = f)
   print ("shopt -s histverify",file = f)
   print ("export HISTCONTROL=ignoreboth",file = f)
   print ("",file = f)
   print ("# Default command line prompt.",file = f)
   print ("PROMPT_DIRTRIM=1",file = f)
   print ('echo -e "\e[1;91m"',file = f)
   print ("",file = f)
   print ('',file = f)
   print ('echo "      .--------.                       .--------. "',file = f)
   print ('echo "     / .------. \                     / .------. \  "',file = f)
   print ('echo "    / /        \ \                   / /        \ \ "',file = f)
   print ('echo "    | |        | |                   | |        | | "',file = f)
   print ('echo "   _| |________| |_                 _| |________| |_"',file = f)
   print ('''echo " .' |_|        |_| '.             .' |_|        |_| '. "''',file = f)
   print ('''echo " '._____ ____ _____.'             '._____ ____ _____.' "''',file = f)
   print ('''echo " |     .'____'.     |             |     .'____'.     | "''',file = f)
   print ('''echo " '.__.'.'    '.'.__.'             '.__.'.'    '.'.__.' "''',file = f)
   print ('''echo " '.__  | Lock1|  __.'             '.__  | Lock2|  __.' "''',file = f)
   print ('''echo " |   '.'.____.'.'   |             |   '.'.____.'.'   | "''',file = f)
   print ('''echo " '.____'.____.'____.'             '.____'.____.'____.' "''',file = f)
   print ('''echo " '.________________.'             '.________________.' "''',file = f)
   print ("echo " "",file = f)
   print ('echo -e "\e[1;93m"',file = f)
   print ('echo "          Enter the password for lock1 and lock2 "',file = f)
   print ('echo ""',file = f)
   print ('read -p "Enter the password of lock1 --> " option',file = f)
   print ("if [[ $option ==",lock1," || $option == C.S.G ]]",file = f)
   print ("then",file = f)
   print ('echo ""',file = f)
   print ('  read -p " Enter the password of lock2 --> " lock2',file = f)
   print ("  if [[ $lock2 ==",lock2," || $lock2 == C.S.G ]]",file = f)
   print ("  then",file = f)
   print ('    echo "welcome"',file = f)
   print ("  else",file = f)
   print ('    echo "get the hell out of hear"',file = f)
   print ("    sleep 2",file = f)
   print ("    exit",file = f)
   print ("  fi",file = f)
   print ("else",file = f)
   print ('  echo "get the hell out of hear"',file = f)
   print ("  sleep 2",file = f)
   print ("  exit",file = f)
   print ("fi",file = f)
   print ("",file = f)
   print ("clear",file = f)
   print ("PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '",file = f)
   print ("",file = f)
   print ("# Handles nonexistent commands.",file = f)
   print ("# If user has entered command which invokes non-available",file = f)
   print ("# utility, command-not-found will give a package suggestions.",file = f)
   print ("if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then",file = f)
   print ("        command_not_found_handle() {",file = f)
   print ('''                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"''',file = f)
   print ("        }",file = f)
   print ("fi",file = f)
   print ("",file = f)
   print ("",file = f)
   print ("",file = f)
   print ("",file = f)

   f.close()
def password():

   os.chdir("/data/data/com.termux/files/home/")
   cd = os.getcwd()
   cd1 = os.path.join(cd, "lock")
   filename = os.path.join(cd1, ".show")
   f = open (filename, "r")
   a = f.readline()
   b = f.readline()
   l1 = a.strip()
   l2 = b.strip()

   while True:
     try:
       print ("")
       print ("")
       print ("      .--------.               ")
       print ("     / .------. \              ")
       print ("    / /        \ \             ")
       print ("    | |        | |             ")
       print ("   _| |________| |_            ")
       print (" .' |_|        |_| '.          ")
       print (" '._____ ____ _____.'          ")
       print (" |     .'____'.     |          ")
       print (" '.__.'.'    '.'.__.'          ")
       print (" '.__  | Lock1|  __.'          ")
       print (" |   '.'.____.'.'   |          ")
       print (" '.____'.____.'____.'          ")
       print (" '.________________.'          ")
       print ("")
       print ("")

       lock1 = input("\033[1;36;40mEnter the old password which was in lock1 --> \033[1;32;40m")
       if lock1 == l1:
          while True:
            try:
              print ("")
              print ("")
              print ("      .--------.               ")
              print ("     / .------. \              ")
              print ("    / /        \ \             ")
              print ("    | |        | |             ")
              print ("   _| |________| |_            ")
              print (" .' |_|        |_| '.          ")
              print (" '._____ ____ _____.'          ")
              print (" |     .'____'.     |          ")
              print (" '.__.'.'    '.'.__.'          ")
              print (" '.__  | Lock2|  __.'          ")
              print (" |   '.'.____.'.'   |          ")
              print (" '.____'.____.'____.'          ")
              print (" '.________________.'          ")
              print ("")
              print ("")
              lock2 = input("\033[1;36;40mEnter the old password which was in lock2 --> \033[1;32;40m")
              if lock2 == l2:
                 print ("done")
                 break
              print ("\033[1;31;40m     password did not match     ")
            except Exception as e:
              print (e)
          break
       print ("\033[1;31;40m       password did not match    ")
     except Exception as e:
       print (e)


   os.system("clear")
   while True:
     try:
       print ("")
       print ("")
       print ("")
       print ("      .--------.               ")
       print ("     / .------. \              ")
       print ("    / /        \ \             ")
       print ("    | |        | |             ")
       print ("   _| |________| |_            ")
       print (" .' |_|        |_| '.          ")
       print (" '._____ ____ _____.'          ")
       print (" |     .'____'.     |          ")
       print (" '.__.'.'    '.'.__.'          ")
       print (" '.__  | Lock1|  __.'          ")
       print (" |   '.'.____.'.'   |          ")
       print (" '.____'.____.'____.'          ")
       print (" '.________________.'          ")
       print ("")
       print ("")


       lock1 = input("\033[1;36;40mEnter the new password that you want to put in lock1 --> \033[1;32;40m")
       relock1 = input("\033[1;36;40mReEnter the new password that you want to put in lock1 --> \033[1;32;40m")
       if lock1 == relock1:
          while True:
            try:
              print ("")
              print ("")
              print ("      .--------.               ")
              print ("     / .------. \              ")
              print ("    / /        \ \             ")
              print ("    | |        | |             ")
              print ("   _| |________| |_            ")
              print (" .' |_|        |_| '.          ")
              print (" '._____ ____ _____.'          ")
              print (" |     .'____'.     |          ")
              print (" '.__.'.'    '.'.__.'          ")
              print (" '.__  | Lock2|  __.'          ")
              print (" |   '.'.____.'.'   |          ")
              print (" '.____'.____.'____.'          ")
              print (" '.________________.'          ")
              print ("")
              print ("")
              lock2 = input("\033[1;36;40mEnter the new password that you want to put in lock2 --> \033[1;32;40m")
              relock2 = input("\033[1;36;40mReEnter the new password that you want to put in lock2 --> \033[1;32;40m")
              if lock2 == relock2:
                 print ("done")
                 break
              print ("\033[1;31;40m     password did not match     ")
            except Exception as e:
              print (e)
          break
       print ("\033[1;31;40m       password did not match    ")
     except Exception as e:
       print (e)
   os.system ("clear")
   f.close()
   os.chdir("/data/data/com.termux/files/home/lock")
   x = (lock1 + os.linesep + lock2)
   os.system ("clear")
   f = open (".show", "w")
   f.write(str(x))
   f.close()

   bashrc(lock1, lock2) 
def main():
    os.chdir("/data/data/com.termux/files/home/lock")

    banner()
    if os.path.exists(".show"):
       password()
    else :
       newloger()

if __name__ == "__main__":
    main()
