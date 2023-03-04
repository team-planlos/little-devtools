# TODO to tempfile module

class TmpFile():

    hash_name: str
    path: str

    def __init__(self, path="", hash_date=True):
        super().__init__(self)
        self.hash_name = ""
        if not path:
            from os import getcwd
            self.path = getcwd()
        else:
            self.path = path
        if hash_date == True:
            self.hash_date()
        else:
            self.hash_rand()
        with open(self.hash_name, "x") as file:
            pass

    def hash_date(self):
        from datetime import datetime
        hashN = str(datetime.utcnow())
        hashN.replace(".", "-").replace(":", "-").replace(" ", "-")
        self.hash_name = "ownpython-{}.tmp".format(hashN)

    def hash_rand(self):
        from random import randint
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        hashL = []
        hashL.append(characters[randint(0, 52)])
        for _ in range(0, 24):
            hashL.append(characters[randint(0, 62)])
        hashL.append(".tmp")
        self.hashL_name = "".join(hashL)

    def __del__(self):
        from os import path as p, remove, sep, chdir
        chdir(self.path)
        if p.exists(self.hash_name):
            remove(sep.join([self.path, self.hash_name]))