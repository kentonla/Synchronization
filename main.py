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
    pass

def philosopher_eating(philosopher_number):
    pass

# To stimulate both thinking and eating, this function will put threads to sleep for a random period of time between 1-3 seconds
def random_thread_sleep():
    delay = random.randint(1,3)
    time.sleep(delay)


if __name__ == "__main__":
    # Create 5 philosophers, identified by a number 0, 1, 2, 3, and 4
    # Each philosopher runs as a seprate thread
    Thread(target=alternate(0)).start()
    Thread(target=alternate(1)).start()
    Thread(target=alternate(2)).start()
    Thread(target=alternate(3)).start()
    Thread(target=alternate(4)).start()
    
    Thread(target=alternate(0)).end()
    Thread(target=alternate(1)).end()
    Thread(target=alternate(2)).end()
    Thread(target=alternate(3)).end()
    Thread(target=alternate(4)).end()
    
    exit