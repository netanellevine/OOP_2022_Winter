import threading
import time

# thread = threading.Thread(target=func_for_thread, args=(arg1, arg2))
# thread.start()
# thread.run()
# thread.join()
# thread.getname()
# thread.setname()
# thread.setDaemon()
# thread.isDaemon()
# thread.is_alive() and not thread.isAlive()


def example1():
    my_thread = threading.Thread(target=func)

    print(my_thread.is_alive())

    my_thread.start()

    print(my_thread.is_alive())


def func():
    print("Starting...")
    time.sleep(2)
    print("Done.")


def example2():
    threads = []
    for k in range(3):
        t = threading.Thread(target=count, args=(k,))
        threads.append(t)
        t.start()  # what about join?


def count(n):
    for i in range(5):  # different range?
        print(f'Thread number: {n} -->{i}  ')


# Events -> Objects that can communicate with all the threads
# threading_event = threading.Event()  -> create a thread event
#
# threading_event.set()     -> flag the event as True
# threading_event.clear()   -> flag the event as False
# threading_event.is_set()  -> returns the flag of the event True/False
# threading.wait()          -> stops the code as long as the flag is False when it is set to True it continues.


def example3():
    pause_resume_event = threading.Event()
    stop_event = threading.Event()

    my_thread = threading.Thread(target=analyse, args=(pause_resume_event, stop_event))
    my_thread.start()

    print("Enter p to pause/resume the analysing")
    print("Enter x to stop and exit")
    input("Press enter to start analysing...")

    pause_resume_event.set()
    while True:
        user_command = input()
        if user_command == 'x':
            stop_event.set()
            exit(0)
        elif user_command == 'p':
            if pause_resume_event.is_set():
                pause_resume_event.clear()
                time.sleep(0.3)
                print("########")
                print("PAUSED")
                print("########")
            else:
                print("########")
                print("RESUMED")
                print("########")
                time.sleep(0.3)
                pause_resume_event.set()


def analyse(pause_resume_event, stop_event):
    for i in range(1000):
        if stop_event.is_set():
            print("########")
            print("Exiting")
            print("########")
            print()
            return
        else:
            pause_resume_event.wait()
            print(i)
            time.sleep(0.2)


if __name__ == '__main__':
    # example1()
    # example2()
    example3()
