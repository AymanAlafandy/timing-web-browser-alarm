import webbrowser
import time

# a small program that open a web browser.
# I can expand it to be like an alarm or timing program.

print ("the program is running: "+ time.ctime())
i = 0
while i<3:
  time.sleep(2*3) # that make the program sleeps for
  #i open a link in web browser
  webbrowser.open('https://www.youtube.com/watch?v=wyx6JDQCslE', new=2)
  i +=1
