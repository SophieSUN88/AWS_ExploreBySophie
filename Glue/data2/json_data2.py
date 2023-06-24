from faker import Faker
import json
import pandas as pd

f = Faker()

data = {
    "firstname" : [],
    "lastname" : [],
    "address":[]
}
for i in range(5):
    data["firstname"].append(f.unique.first_name())
    data["lastname"].append(f.unique.last_name())
    data["address"].append(
        {
            "state":f.unique.state(),
            "city":f.unique.city(),
            "zipcode":f.unique.zipcode()
        }
    )

df = pd.DataFrame.from_dict(data)

df.to_json("json_data2.json",orient='records', lines=True)

df.to_csv("csv_data2.csv",index=False)