# your code goes here!
import time
def countdown(integer):
    while integer >=1:
        print(f'{integer} SECOND(S)!')
        integer -=1
    print("HAPPY NEW YEAR!")
# countdown(10)

def countdown_with_sleep(num):
    while num >=1:
        print(f'{num} SECOND(S)!')
        time.sleep(1)
        num -=1
    print("HAPPY NEW YEAR!")
countdown_with_sleep(10)
 
