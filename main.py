import time
import random
from threading import Thread, Lock, Condition
# https://docs.python.org/3/library/threading.html

mutex = Lock()
cond = [
    Condition(mutex),
    Condition(mutex),
    Condition(mutex),
    Condition(mutex),
    Condition(mutex)
]

# Helps know which philosopher is next to who at a circular table
LEFT_OF = lambda i: (i - 1 + 5) % 5
RIGHT_OF = lambda i: (i + 1) % 5

# Lets us know what each philosopher is doing
# Used for directing a philosopher to wait for neighboring philosopher to finish, in order to pickup fork
# or put a fork down when finished eating
philosopher_status = ['eating', 'eating', 'eating', 'eating', 'eating']

# Uses philosopher_number to identify how many philosphers wishing to eat.
# When a philosopher finishes eating, a call is made to return_forks(philosopher_number)
def pickup_forks(philosopher_number):
    l = LEFT_OF(philosopher_number)
    r = RIGHT_OF(philosopher_number)
    
    with mutex:
        philosopher_status[philosopher_number] = 'thinking'
        
        # Waits for threads of neighboring philosophers who are currently eating to finish
        while philosopher_status[l] == 'eating' or philosopher_status[r] == 'eating':
            if philosopher_status[l] == 'eating':
                print(f"Forks are with Philosopher #{l}")
            elif philosopher_status[r] == 'eating':
                print(f"Forks are with Philosopher #{r}")
            cond[philosopher_number].wait()
            
        # Once all neighboring philosophers finish eating, allow the current philosopher to pickup fork
        philosopher_status[philosopher_number] = 'eating'
        print(f"Philosopher #{philosopher_number} picked up fork")
        

def return_forks(philosopher_number):
    l = LEFT_OF(philosopher_number)
    r = RIGHT_OF(philosopher_number)
    
    with mutex:
        philosopher_status[philosopher_number] = 'thinking'
        
        print(f"Philosopher #{philosopher_number} put down their fork")
        cond[l].notify()
        cond[r].notify()
        

# Alternates philosopher between thinking and eating
# Handles all of the actions a philosopher does
# When a philosopher is not eating they are thinking and vice versa
def alternate(philosopher_number):
    while True:
        philosopher_thinking(philosopher_number)
        pickup_forks(philosopher_number)
        philosopher_eating(philosopher_number)
        return_forks(philosopher_number)
    

def philosopher_thinking(philosopher_number):
    time = random_thread_sleep()
    print(f"Philosopher #{philosopher_number} took {time}ms thinking")

def philosopher_eating(philosopher_number):
    time = random_thread_sleep()
    print(f"Philosopher #{philosopher_number} took {time}ms eating")

# To stimulate both thinking and eating, this function will put threads to sleep for a random period of time between 1-3 seconds
def random_thread_sleep():
    delay = random.randint(1,3)
    time.sleep(delay)
    return delay*1000


if __name__ == "__main__":
    # Create 5 philosophers, identified by a number 0, 1, 2, 3, and 4
    # Each philosopher runs as a seprate thread
    philosophers = [
    Thread(target=alternate, args=(0,)),
    Thread(target=alternate, args=(1,)),
    Thread(target=alternate, args=(2,)),
    Thread(target=alternate, args=(3,)),
    Thread(target=alternate, args=(4,))
    ]
   
    for philosopher in philosophers:
        philosopher.start()
       
    for philosopher in philosophers:
        philosopher.join()
    
    exit