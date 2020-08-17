#code by Priyansh (DragonHeart)
#importing the modules
import time
import webbrowser
#ask for the alarm time
set_alarm= str(input("Alarm Time (H:M:S) in 24 hour format: "))
#get the actual time in 24 hour format
actual_time=time.strftime("%H:%M:%S")
#ask for the url user want to access at that alarm time
url= str(input("Enter website you wanna work on: "))
#time will print the actual time till actual time and alarm time is not equal
while(actual_time!=set_alarm):
    print("Actual Time is: "+ actual_time)
    actual_time= time.strftime("%H:%M:%S")
    time.sleep(1)
#condition to check if actual time is equal to alarm time and ask if user wanna access the page
if(actual_time==set_alarm):
    answer_open=str(input("Shall I open your webpage? (y/n) "))
    #if answer is y then open the webpage
    if (answer_open=='y'):
        webbrowser.open(url)
