from faker import Faker
import pandas as pd

f = Faker()
n = 10
for i in range(n):
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

    csv_filename = "csv_data_simple" + str(i+1) + ".csv"
    json_filename = "json_data_simple" + str(i+1) + ".json"
    df.to_csv(csv_filename, index=False)
    df.to_json(json_filename,orient='records', lines=True)

for i in range(n):
    data = {
        "firstname" : [],
        "lastname" : [],
        "ssn" : [],
        "date": [],
        "profile":[]
    }
    for i in range(5):
        data["firstname"].append(f.unique.first_name())
        data["lastname"].append(f.unique.last_name())
        data["ssn"].append(f.unique.ssn())
        data["date"].append(f.date())
        data["profile"].append(f.profile())

    df = pd.DataFrame.from_dict(data)

    csv_filename = "csv_data_complex" + str(i+1) + ".csv"
    json_filename = "json_data_complex" + str(i+1) + ".json"
    df.to_csv(csv_filename, index=False)
    df.to_json(json_filename,orient='records', lines=True)
