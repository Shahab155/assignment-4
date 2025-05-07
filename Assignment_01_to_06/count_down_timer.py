import time 

def count_down_timer(seconds):
    while seconds > 0:
        print(f"Time left {seconds} seconds!")
        seconds -= 1
        time.sleep(1)

    print("⏰ Time Up!")             

seconds = int(input("Enter the number of seconds: "))
count_down_timer(seconds)
