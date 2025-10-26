import pandas as pd

print("Extract Data")
data = {
    'Id': [101, 102, 103],
    'Name': ['Ram', 'Raj', 'Raja'],
    'Age': [29, 34, 560]
}
df = pd.DataFrame(data)
print(df)
