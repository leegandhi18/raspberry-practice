import threading
import time

flag_exit = False
def t1_main():
  while True:
    print("\tt1")
    time.sleep(0.5)
    if flag_exit: break
    
def t2_main():
  while True:
    print("\tt2")
    time.sleep(0.2)
    if flag_exit: break

t1 = threading.Thread(target=t1_main)
t1.start()

t2 = threading.Thread(target=t2_main)
t2.start()

try:
  while True:
    userInput = Input()
    print(userInput)

except KeyboardInterrupt:
  pass

flag_exit = True
t1.join()
t2.join()