import pandas as pd

title_column = {
    'num': ['ali', 'reza', 'mehdi'],
    'height': [180, 190, 160],
    'weight': [90, 88, 67]
}

data = pd.DataFrame(title_column)
# print(data)

select_column = data['weight'][0]
print(select_column)
