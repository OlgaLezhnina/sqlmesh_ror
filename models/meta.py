import json
import requests
import pandas as pd
from sqlmesh import model


@model(
    "ror.meta",
    columns={       
         "keys": "text",
         "values": "text",
     },
)

def execute(context, **kwargs) -> pd.DataFrame:
    response = requests.get("https://zenodo.org/api/records/23500708")
    response_dict = response.json()
    keys = []
    values = []
    for key, value in response_dict.items():
        keys.append(json.dumps(key))
        values.append(json.dumps(value))
    return pd.DataFrame(data = {"keys": keys, "values": values}, 
                        columns = ["keys", "values"])


