import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("kc_house_data.csv")

train, test = train_test_split(data, test_size=0.2)

train.to_csv(r'train_data.csv', index=False)
test.to_csv(r'test_data.csv', index=False)
