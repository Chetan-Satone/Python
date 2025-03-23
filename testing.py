import pandas as pd

mydataset = {
    'cars': ["BMW", "VOlVO", "TATA"],
    'passings': [2, 4, 7]
}

myvar = pd.DataFrame(mydataset)

print(myvar)