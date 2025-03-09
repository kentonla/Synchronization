import time
import random
from threading import Thread
# https://docs.python.org/3/library/threading.html


# Uses philosopher_number to identify how many philosphers wishing to eat.
# When a philosopher finishes eating, a call is made to return_forks(philosopher_number)
def pickup_forks(philosopher_number):
    pass

def return_forks(philosopher_number):
    pass

# Alternates philosopher between thinking and eating
# Handles all of the actions a philosopher does
# A philosopher has to think to pickup fork, then eat, and then put down the fork
def alternate(philosopher_number):
    philosopher_thinking(philosopher_number)
    pickup_forks(philosopher_number)
    philosopher_eating(philosopher_number)
    return_forks(philosopher_number)
    

def philosopher_thinking(philosopher_number):
    think_time = random_thread_sleep()
    print(f"Philosopher #{philosopher_number} took {think_time}ms thinking")

def philosopher_eating(philosopher_number):
    eat_time = random_thread_sleep()
    print(f"Philosopher #{philosopher_number} took {eat_time}ms eating")

# To stimulate both thinking and eating, this function will put threads to sleep for a random period of time between 1-3 seconds
def random_thread_sleep():
    delay = random.randint(1,3)
    time.sleep(delay)


if __name__ == "__main__":
    # Create 5 philosophers, identified by a number 0, 1, 2, 3, and 4
    # Each philosopher runs as a seprate thread
    philosophers = [
    Thread(target=alternate(0)),
    Thread(target=alternate(1)),
    Thread(target=alternate(2)),
    Thread(target=alternate(3)),
    Thread(target=alternate(4))
    ]
   
    for philosopher in philosophers:
        philosopher.start()
       
    for philosopher in philosophers:
        philosopher.join()
    
    exit