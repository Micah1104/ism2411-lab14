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

print("--exercise 3--")
print(len(df))
before = len(df)
df = df.dropna(subset=['order_id', 'order_date'])
print(f"Dropped {before - len(df)} rows missing order_id or order_date")
#this is done because you can't look up an order without an id or date.

df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
#This is done so that when this data is  used missing values do not cause errors.
print(len(df))

print("--exercise 4--")
df['unit_price']=df['unit_price'].str.replace('$', '', regex=False)
df['unit_price'] = df['unit_price'].str.replace(',', '', regex=False).astype(float)
df['quantity_sold'] = df['quantity_sold'].astype(int)
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
bad_dates = df['order_date'].isnull().sum()
print(f"unparsable dates: {bad_dates}")

print("--exercise 5--")
print(f"duplicated rows: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(df.shape)

print("--exercise 6--")
print(df.describe())
#Some odd values are the max being 9999.0 and the std being 252 for quantity sold. I think that 9999 is a place holder and 252 is just being skewed by the 9999 value.
df.drop(df[df['quantity_sold'] == 9999.000000].index, inplace=True)
#i dropped the rows with 9999 because it skewed the data and would mess up any analysis done as is iseen with the max and std.
print(df.describe())
print('--exercise 7--')
df.to_csv("data/clean_sales.csv", index=False)
print("\nSaved clean_sales.csv")

pd.read_csv("data/clean_sales.csv").info()