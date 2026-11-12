import json
from sqlmesh import ExecutionContext, model
from sqlglot import exp

@model(    
"ror.json_raw",   
columns={       
"json": "text",    
},
)

def execute(context, **kwargs):
    with open('v2.15-2026-10-20-ror-data.json') as f:
        table = json.load(f)
    select_query = exp.select("*").from_(table)
    return context.fetchdf(select_query)
