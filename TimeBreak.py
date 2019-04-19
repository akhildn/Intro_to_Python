import webbrowser
import time


numberOfBreaks = 3
print("break taken at:" + time.ctime())


for i in range(numberOfBreaks):
    time.sleep(2)
    webbrowser.open("https://www.google.com")