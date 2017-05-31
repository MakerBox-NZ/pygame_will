import random
import time
time.sleep(4)
print('running')
player = random.randint(1,6) #variable-random 
ai = random.randint(1,6) #variable-random
time.sleep(4)
if player > ai:
    print('you did -very well-')
    print( player )
else :

    print('*sarcasm* well done')
    time.sleep(1)
    print('you lost, in case that wasnt clear')
    
