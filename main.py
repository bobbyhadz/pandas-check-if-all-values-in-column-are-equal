# Check if all values in a Column are Equal in Pandas

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [3, 3, 3, 3],
    'salary': [175.1, 180.2, 190.3, 205.4],
})


def values_in_column_equal(col):
    arr = col.to_numpy()

    return (arr[0] == arr).all()


# 👇️ True
print(values_in_column_equal(df['experience']))

# 👇️ False
print(values_in_column_equal(df['name']))