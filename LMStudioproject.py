#Prompt: can you write python code that takes market data points for stock entry and exit. Take in certain variable such as previous closes and open prices.

import pandas as pd

# Assuming these are our market data points (I'm just using random values here)
data = {
    'Open': [10, 20, 35, 40],
    'High': [12, 21, 36, 48],
    'Low': [9, 18, 34, 42],
    'Close': [11, 21, 37, 45]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Calculate the previous close and open prices
df['Prev_Open'] = df['Open'].shift()
df['Prev_Close'] = df['Close'].shift()

# Here, you can add your logic to determine when to enter or exit based on certain conditions.
# For simplicity, let's just say we buy if the close is higher than open and sell if it's lower
df['Entry'] = 0
df['Exit'] = 0
for index in range(len(df)):
    if df['Close'][index] > df['Open'][index]: # buying condition
        df.loc[index, 'Entry'] = 1
    elif df['Close'][index] < df['Open'][index]:  # selling condition
        df.loc[index, 'Exit'] = -1

# Print out the final DataFrame with our entry and exit signals
print("\nData with Entry and Exit Signals:")
print(df)