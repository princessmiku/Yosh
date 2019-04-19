"""
Github Link: https://github.com/princessmiku/Yosh
"""
import sys
from colorama import Fore, Back, Style

class file:

    file = ""
    isFile = False
    data = {}

    def __init__(self, file: str = None, string: str = None):
        if file.endswith(".yosh") and file is not None:
            self.file = file
            try:
                op = open(file)
                f = op.read().split("\n")
                op.close()
            except FileNotFoundError:
                fi = open(file, mode="w")
                fi.write("")
                fi.close()
                f = ""
            self.isFile = True
        elif string is not None:
            f = str
        else:
            print(Fore.RED + "Invalid data/string")
            sys.exit()

        d = {}
        for x in f:
            y = x.split("@")[1:]
            key = ""
            t = {}
            for z in y:
                a = z.split("=", 1)
                if a[0].lower() == "key":
                    if a[1].endswith(" "):
                        key = a[1][:-1]
                    else:
                        key = a[1]
                else:
                    if a[1].endswith(" "):
                        t[a[0]] = a[1][:-1]
                    else:
                        t[a[0]] = a[1]



            d[key] = t
        self.data = d

    def add(self, key: str, category: str, value: str):
        try:
            self.data[key][category] = value
        except KeyError:
            self.data[key] = {}
            self.data[key][category] = value

    def write(self, key: str, category: str, value: str):
        if not self.isFile:
            print("load data by string\nuse add")
            return
        self.add(key, category, value)
        self.save()

    def read(self):
        d = self.data
        FINALSTRING = ""
        for x in d:
            if not x == '':
                FINALSTRING += f"@key={x}"
                for y in d[x]:
                    FINALSTRING += f" @{y}={d[x][y]}"

                FINALSTRING += "\n"
        return FINALSTRING

    def getValue(self, key:str, category: str):
        return self.data[key][category]

    def getValueAsInt(self, key:str, category: str):
        return int(self.data[key][category])

    def getValueAsStr(self, key:str, category: str):
        return str(self.data[key][category])

    def getKeyValues(self, key):
        return self.data[key]

    def save(self):
        if not self.isFile:
            print("load data by string\nuse read and save it self")
            return
        FINALSTRING = self.read()
        print(f"save file {self.file}")
        f = open(self.file, mode='w')
        f.write(FINALSTRING)
        f.close()




