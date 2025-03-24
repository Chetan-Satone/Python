import pandas as pd

a = [5, 3, 1]

myvar = pd.Series(a, index = ["chetan", "asus", "nihira"])

"""print(myvar["asus"])"""

print(myvar)

print(myvar["chetan"])