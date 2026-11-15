import json
import pandas as pd
from sqlmesh import model


@model(
    "ror.json_raw",
     columns={       
         "json": "jsonb",    
     },
)

def execute(context, **kwargs) -> pd.DataFrame:
    with open('v2.15-2026-10-20-ror-data.json') as json_file:
        records = json.load(json_file)
    json_objs = list(map(json.dumps, records))
    return pd.DataFrame(data = {"json": json_objs}, columns = ["json"])
