import pandas as pd

df = pd.read_csv('data/messy_sales.csv')

print("--exercise 1--")
df.info()
#Unit price should be a float but is a string, so is quantity. 
#8% of customer ids are missing. 
# Quantity is also a float where it should be int.

print("\nMissing values:\n", df.isnull().sum())

print("--exercise 2--")
df.columns = df.columns.str.lower().str.replace(" ", "_")
print("\nCleaned columns:", df.columns.tolist())
