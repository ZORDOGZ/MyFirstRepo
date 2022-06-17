import prettytable
from prettytable import PrettyTable
import win32api

x=PrettyTable()

l=["Utility","Price"]
x.field_names=l
x.add_row(["Smoke","$300"])
x.add_column("Duration(in seconds)",["10"])
x.add_row(["Flash","$200","5"])
x.align="l"
print(x)

"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
p={"papaya","xyz"}
print(type(p))
"""
