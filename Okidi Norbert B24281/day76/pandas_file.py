import pandas as pd
import numpy as np


data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180, 90, 200]
}

sales_df = pd.DataFrame(data)

print("Original Sales Dataset:")
print(sales_df)
pivot_df = sales_df.pivot(index='Date', columns='Product', values='Sales')

print("\nPivoted Sales Dataset:")
print(pivot_df)

pivot_df = pivot_df.fillna(0)

print("\nPivoted Sales Dataset with NaN filled:")
print(pivot_df)

