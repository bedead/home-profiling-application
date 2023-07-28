from __auth__ import supabase
import eel

@eel.expose
def getAllAppliancesList():
    table = "electric_appliance"
    query = supabase.table(table_name=table).select('*').execute() 
    
    return query.data
