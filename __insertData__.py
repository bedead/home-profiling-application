import csv
import time
import httpx
from __auth__ import supabase


def insert_Many_into_Monitor(data, type):
    table_name = None
    if type == "Producer":
        table_name = "producer_monitor"
    elif type == "Consumer":
        table_name = "consumer_monitor"
    starttime = time.time()
    try:
        response = supabase.table(table_name=table_name).insert(data).execute()
    except httpx.ConnectTimeout as e:
        print(e.args)
    except httpx.WriteTimeout as e:
        print(e.args)
    endtime = time.time()
    process_time = endtime - starttime

    with open("sending_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # writer.writerow(['Public key exchange time','Private key exchange time'])
        writer.writerow([process_time])
    file.close()