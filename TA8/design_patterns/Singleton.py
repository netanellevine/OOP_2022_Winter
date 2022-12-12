class DBConnection(object):
    """
    Create a new singleton by not creating a constructor with __init__, instead use __new__.
    If the class has an instance, it will return it, otherwise it will create it.
    Therefore, we will have only one instance of the class, and each object will have it
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnection, cls).__new__(cls)
        return cls.instance


con = DBConnection()
con2 = DBConnection()
print(con)
print(con2)
print(con == con2)
