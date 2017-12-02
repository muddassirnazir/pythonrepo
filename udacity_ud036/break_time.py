import webbrowser
import time

count = 0
print ("This program started on "+time.ctime())
while (count < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=Tm8LGxTLtQk")
    count = count + 1
