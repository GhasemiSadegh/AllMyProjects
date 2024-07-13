import pandas as pd


column = ['ali', 'reza', 'mehdi']
title_column = {'num': column,
                'height': [180, 190, 160],
                'weight': [90, 88, 67]
                }

data = pd.DataFrame(title_column)
print(data)
