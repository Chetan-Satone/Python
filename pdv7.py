import pandas as pd

data = {
    "calories": [500, 700, 1000],
    "duration": [50, 20, 30]
}

myvar = pd.Series(data)

print(myvar)