import time
my_time =int(input("Enter Time in Seconds: "))

for x in range(my_time,0,-1):
    seconds =x%60
    minute=int(x/60)%60
    hour=int(x/3600)%24
    print(f"{hour:02}:{minute:02}:{seconds:02}")
    time.sleep(1)




print("hello there")