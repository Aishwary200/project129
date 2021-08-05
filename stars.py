import csv
import pandas as pd
df = pd.read_csv("dwarf_stars.csv")
df.columns
df.dtypes
df = df.dropna()
df.dtypes
df["Radius"] = 0.102763*df["Radius"]
df['Mass'] = df['Mass'].apply(lambda x: x.replace(
    '$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.head()
df.columns
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.head()
df.reset_index(drop=True, inplace=True)
df.to_csv("unit_converted_stars.csv")
df.dtypes

file1 = 'bright_stars.csv'
file2 = 'unit_converted_stars.csv'

d1 = []
d2 = []
with open(file1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(file2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d = []

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df = pd.read_csv('total_stars.csv')
df.tail(8)
df = pd.read_csv('total_stars.csv')
df
df.columns
df.drop(['Unnamed: 0', 'Unnamed: 6', 'Star_name.1', 'Distance.1',
        'Mass.1', 'Radius.1', 'Luminosity'], axis=1, inplace=True)
df
final_data = df.dropna()
final_data
final_data.reset_index(drop=True, inplace=True)
final_data
final_data.to_csv('final_data.csv')
final_data.describe()
final_data.head(5)
final_data.dtypes
