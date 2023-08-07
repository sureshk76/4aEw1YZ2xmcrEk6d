import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

src_path = r"data/raw/happinessSurvey2020.csv"
dst_path = r"data/processed/happinessSurvey2020Processed.csv"
shutil.copy(src_path, dst_path)
print('Copied')

df = pd.read_csv(r'../data/processed/happinessSurvey2020Processed.csv')
# Split Data:
def split_data(df, testSize, randomState):
    X = df.drop('Y', axis=1)
    y = df['Y']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testSize, random_state=randomState)
    data = {"train": {"X": X_train, "y": y_train}, "test": {"X": X_test, "y": y_test}}
    return data