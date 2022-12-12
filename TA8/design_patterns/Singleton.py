class DBConnection(object):
    """
    Create a new singleton by not creating a constructor with __init__, instead use __new__.
    If the class has an instance, it will return it, otherwise it will create it.
    Therefore, we will have only one instance of the class, and each object will have it
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DBConnection, self).__new__(self)
        return self.instance


con = DBConnection()
con2 = DBConnection()
print(con)
print(con2)
print(con == con2)
