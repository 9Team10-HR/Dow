import os 
from pytube import YouTube 
logo = """ \033[0;36m
 /$$                           /$$          
| $$                          |__/          
| $$        /$$$$$$   /$$$$$$  /$$ /$$$$$$$ 
| $$       /$$__  $$ /$$__  $$| $$| $$__  $$
| $$      | $$  \ $$| $$  \ $$| $$| $$  \ $$
| $$      | $$  | $$| $$  | $$| $$| $$  | $$
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$| $$  | $$
|________/ \______/  \____  $$|__/|__/  |__/
                     /$$  \ $$              
                    |  $$$$$$/              
                     \______/               
"""
print(logo)
username = "Grandpa"
password = '69'

givenusername = input ("\033[0;36mEnter Username : ")
if givenusername == username : 
 print("\033[0;32mCORRECT")
else : 
   print("\033[0;31mWORNG")
givenpassword = input("\033[0;34mEnter  Password : ")
if givenpassword == password : 
 print("\033[0;32mCORRECT")
else : 
 print ("\033[0;31mWRONG")
    
logo = ("""\033[0;31m 
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╭╯╰╯┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
-------------------------------------------
\033[0;32mAuthor :Md HR 👑
\033[0;32mtelegram:TEAM→°X°
------------------------------------------- 
    """) 
print(logo)
print( '''\033[0;32mThis script is download all youtube videos in 720p 
if not available in 720p it try 480p/360p''')
link = input("Enter Your link :")
yt = YouTube(link)

video = yt.streams.filter(progressive = true,
file_extension = 'mp4').order_by('resolution').desc().first().download

os.system("clear")
print(""" 

      \033[38;5;46m____  ____  _  ________
     \033[38;5;46m/ __ \/ __ \/ | / / ____/
    \033[38;5;46m/ / / / / / /  |/ / __/   
   \033[38;5;46m/ /_/ / /_/ / /|  / /___   
  \033[38;5;46m/_____/\____/_/ |_/_____/   
                            
 TNQ FOR USING OUR TOOLS 🖤
