import threading


class SyncList:
    lock = threading.Lock()

    def __init__(self):
        self.__list = []

    def append(self, element):
        SyncList.lock.acquire()
        self.__list.append(element)
        SyncList.lock.release()

    def insert(self, index, element):
        SyncList.lock.acquire()
        self.__list.insert(index, element)
        SyncList.lock.release()

    def pop(self, index=None):
        SyncList.lock.acquire()
        if index is None:
            self.__list.pop()
        else:
            self.__list.pop(index)
        SyncList.lock.release()

    def __getitem__(self, item):
        with SyncList.lock:
            if isinstance(item, int):
                if 0 <= item < len(self.__list):
                    return self.__list[item]
            return None

    def clear(self):
        SyncList.lock.acquire()
        self.__list.clear()
        SyncList.lock.release()

    def extend(self, sync_list):
        SyncList.lock.acquire()
        self.__list.extend(sync_list.__list)
        SyncList.lock.release()


    def __str__(self):
        return str(self.__list)


def f1(sync_list):
    sync_list.append(0)
    sync_list.append(1)
    sync_list.append(2)
    sync_list.insert(0, 3)
    sync_list.pop()


def f2(sync_list):
    sync_list.append(4)
    sync_list.pop(1)
    sync_list.append(9)



sync = SyncList()
t1 = threading.Thread(target=f1, args=(sync,))
t2 = threading.Thread(target=f2, args=(sync,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Both threads are finished")
print(sync)
