from faker import Faker
import pandas as pd

f = Faker()

data = {
    "firstname" : [],
    "lastname" : [],
    "ssn" : []
}
for i in range(5):
    data["firstname"].append(f.unique.first_name())
    data["lastname"].append(f.unique.last_name())
    data["ssn"].append(f.unique.ssn())

df = pd.DataFrame.from_dict(data)

df.to_csv("csv_data1.csv", index=False)
df.to_json("json_data1.json",orient='records', lines=True)
