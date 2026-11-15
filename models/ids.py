import json
import pandas as pd
from sqlmesh import model


@model(
    "ror.ids",
    depends_on=["ror.json_raw"],
     columns={       
         "id": "text",    
     },
)

def execute(context, **kwargs) -> pd.DataFrame:
    table = context.resolve_table("ror.json_raw")
    df = context.fetchdf(f"SELECT * FROM {table}")
    ids = []    
    for json_dict in df["json"]:
        ids.append(json_dict["id"])
    return pd.DataFrame(data = {"id": ids}, columns = ["id"])


