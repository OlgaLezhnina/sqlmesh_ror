import pandas as pd
from sqlmesh import model


@model(
    "ror.external_ids",
    depends_on=["ror.json_raw"],
    columns={
        "id": "text",
        "type": "text",
        "preferred": "bool",
        "external_id": "text",
    },
)
def execute(context, **kwargs) -> pd.DataFrame:
    table = context.resolve_table("ror.json_raw")
    df = context.fetchdf(f"SELECT * FROM {table}")
    ids = []
    types = []
    preferred = []
    external_ids = []

    for json_dict in df["json"]:
        for external_id_dict in json_dict["external_ids"]:
            id_type = external_id_dict["type"]
            preferred_value = external_id_dict["preferred"]
            for value in external_id_dict["all"]:
                ids.append(json_dict["id"])
                types.append(id_type)
                preferred.append(preferred_value == value)
                external_ids.append(value)

    return pd.DataFrame(
        data={"id": ids, "type": types, "preferred": preferred, "external_id": external_ids},
        columns=["id", "type", "preferred", "external_id"],
    )
