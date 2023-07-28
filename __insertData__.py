import httpx
from __auth__ import supabase


def insert_Many_into_Monitor(data, type):
    table_name = None
    if type == "Producer":
        table_name = "producer_monitor"
    elif type == "Consumer":
        table_name = "consumer_monitor"
    try:
        response = supabase.table(table_name=table_name).insert(data).execute()
    except httpx.ConnectTimeout as e:
        print(e.args)
    except httpx.WriteTimeout as e:
        print(e.args)
