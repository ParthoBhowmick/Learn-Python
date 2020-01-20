import pandas as pd
import numpy as np

my_dict = {
    'name': ["a", "b", "c", "d", "e", "f", "g"],
    'age': [20, 27, 35, 55, 18, 21, 35],
    'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]
}
# df = pd.DataFrame(
#      my_dict,
#      index=["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]
# )
# df.set_index("name")
# print(df.index)
# print(df.columns)

# use column as row index
df = pd.DataFrame(my_dict)
series_col = []
for col_name in df.columns:
    series_col.append(df[col_name])

print(type(series_col))

# Delete Columns "name" & "age"
df.drop(['name', 'age'], 1)
# Delete Rows with index "2","3", & "4"
df.drop([2, 3, 4], 0)
print(df)

my_list = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]]
df = pd.DataFrame(my_list)

df = pd.DataFrame(
    my_list,
    index=["1->", "2->", "3->", "4->", "5->"],
    columns=["A", "B", "C", "D"]
)

print(df)

np_arr = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 15, 16, 16],
                   [17, 18, 19, 20]])
df = pd.DataFrame(np_arr)

print(df)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s1 = {'Archery': 'Bhu',
          'Golf': 'Sco',
          'Sumo': 'Jap',
          'Taekwondo': 'SK'}
s1 = pd.Series(s1)
df = pd.DataFrame([s,s1])
print(df)
pd.DataFrame(s)

# df.age.mean()
# df.designation.unique()


# s = pd.Series(np.random.randint(0, 20, 10))
# print(s)
# print
# s = {'1l': '34', '2l': '45', '3l': '74', '5l': '101'}
# s = pd.Series(s)
# print(s.loc['1l'])
# print(s.iloc[2])
