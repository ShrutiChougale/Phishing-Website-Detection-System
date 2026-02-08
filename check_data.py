import pandas as pd

data = pd.read_csv("dataset/phishing.csv")
print(data)
print("Number of samples:", len(data))
