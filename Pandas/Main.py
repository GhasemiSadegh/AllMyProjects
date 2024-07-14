import pandas as pd

title_column = {
    'name': ['ali', 'reza', 'mehdi'],
    'height': [180, 190, 160],
    'weight': [90, 88, 67]
}

data = pd.DataFrame(title_column)
print(data)

select_column = data['weight'][0]
# print(select_column)

select_row = data.iloc[1]['weight']
print(select_row)

# doing a research