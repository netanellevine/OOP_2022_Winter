# example of using a thread timer object
from threading import Timer


# target task function
def task(message):
    # report the custom message
    print(message)


# create a thread timer object
timer = Timer(interval=3, function=task, args=('Hello world',))
# start the timer object
timer.start()
# wait for the timer to finish
print('Waiting for the timer...')