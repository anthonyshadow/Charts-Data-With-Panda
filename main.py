import matplotlib.pyplot as plt
import pandas as pd

# data = [{
#         'name': 'Anthony',
#         'jan_ir': 144,
#         'feb_ir': 172,
#         'march_ir': 154,
#     },
#     {
#         'name': 'Panda',
#         'jan_ir': 132,
#         'feb_ir': 182,
#         'march_ir': 104,
#     }]

# Creates same data as above, but will be created simpler/faster with panda in the below format

raw_data = { 'names': ['Anthony', 'Panda', 'Z', 'X', 'Y'],
             'jan_ir': [144, 132, 243, 123, 52],
             'feb_ir': [172, 182, 211, 143, 111],
             'march_ir': [154, 104, 190, 92, 8]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])

# Adds up totals using panada much faster instead of having to create a for loop to get the answers. 
# Creates a new a column with the correct response
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['march_ir']

print(df)