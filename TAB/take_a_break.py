import webbrowser
import time

total_breaks = 2 
break_count = 0

print("This program started at"+time.ctime())
while(break_count < total_breaks) :
    time.sleep(10)
    webbrowser.open("http://www.youtube.com")
    break_count = break_count + 1