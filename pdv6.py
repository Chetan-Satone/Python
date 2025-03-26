import pandas as pd

work = {"day1": 500, "day2": 600, "day3": 1000, "day4": 2300}

myvar = pd.Series(work, index = ["day1", "day2"])

print(myvar)