
#!//Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
import subprocess
import webbrowser
from googlesearch import search


option= '''

Press 1 to start your vlc media player:
Press 2 to play your fav song on youtube:
Press 3 to search something on google:
Press 4 to start your vlc media playe:
Press 5 to send message to your favourite number:
Press 6 to check current time and date:
Press 7 to reboot your machine:
'''

print(option)


choice= int(input())


if choice ==6:
    current_time = time.ctime()
    print(current_time)

elif choice ==3 :
   web=input("plz enter topic: ")
   url=[]
   for i in search(web,stop=3):
        print(i)
        webbrowser.open_new_tab(i)
        time.sleep(1)
        url.append(i)

   print(url)



else :
	print("hiiiiii")
