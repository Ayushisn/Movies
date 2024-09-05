import pandas as pd

file_path = 'C:/Users/Atulya Kumar/Downloads/Movies.csv' 
df = pd.read_csv(file_path, encoding='ISO-8859-1')

df = df.dropna(subset=['Rating'])

df = df.dropna(subset=['Votes', 'Duration', 'Genre'])

df = df.assign(
    Director=df['Director'].fillna('Unknown'),
    **{'Actor 1': df['Actor 1'].fillna('Unknown')},
    **{'Actor 2': df['Actor 2'].fillna('Unknown')},
    **{'Actor 3': df['Actor 3'].fillna('Unknown')}
)

df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})').astype(float).astype('Int64')

df['Duration'] = df['Duration'].astype(str).str.extract(r'(\d+)').astype(float).astype('Int64')

print(df.info())
print(df.head())
