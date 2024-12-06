import pandas as pd

data_path = "BME3053C_FinalProject/DASH_-_Global_School-based_Student_Health_Survey__GSHS.csv"
data = pd.read_csv(data_path)
key_columns = ["Year","LocationDesc","QuestionCode","Greater_Risk_Data_Value","Sex","Age"]
data = data[key_columns]

print(data.head(5))
