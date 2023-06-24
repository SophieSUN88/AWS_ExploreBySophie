from faker import Faker
import json
import pandas as pd

f = Faker()
n = 10

for i in range(n):
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

    csv_filename = "csv_data" + str(i+1) + ".csv"
    json_filename = "json_data" + str(i+1) + ".json"
    df.to_csv(csv_filename, index=False)
    df.to_json(json_filename,orient='records', lines=True)