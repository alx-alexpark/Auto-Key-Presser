from pynput.keyboard import Key, Controller
from click import clear
import time
def main():
try:
    keyboard = Controller()
    presskey = input("What Key to Spam Press???\n>")
    times = input("how many times to press?? If infinity type -1\n>")
    try:
        times = float(times)
    except:
        print('Error')
        time.sleep(.5)
        clear()
        main()
main()
    delaytime = input("What delay Between Pressing Keys?(seconds)\n>")
    try:
        delaytime = float(delaytime)
    except:
        print('Error')
        time.sleep(.5)
        clear()
        main()
    input("press enter to continue")


    for count in range(3, 0, -1):
        print(count)
        time.sleep(1)


    if times == -1:
        while True:
            keyboard.press(presskey)
            keyboard.release(presskey)
            #keyboard.send(delaytime)
            time.sleep(delaytime)
    elif times >= 0:
        for number in range(times):
            keyboard.press(presskey)
            keyboard.release(presskey)
            #keyboard.send(presskey)
            time.sleep(delaytime)
    input('done, press enter to exit')
except:
	print("An error occured")
