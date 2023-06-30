from gotrue import Session
import eel
# import os
# import requests
from supabase import Client, create_client

# SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
# SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
# print(SUPABASE_URL)
# print(SUPABASE_KEY)

SUPABASE_URL: str = "https://dvywdtjzuqgctliqaoix.supabase.co"
SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2eXdkdGp6dXFnY3RsaXFhb2l4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODUwODk4OTYsImV4cCI6MjAwMDY2NTg5Nn0.Tz0qflBoehtTWSFKgbVyczAwvvepQGQNBgxof4M-nFQ"
supabase : Client = create_client(supabase_url=SUPABASE_URL,supabase_key=SUPABASE_KEY)

@eel.expose
def signInUser(email: str, password: str):
    # print(email, password)
    # gotrue.errors.AuthRetryableError (no internet)
    data = supabase.auth.sign_in_with_password({"email": email, "password": password})
    user = data.user
    user_session = data.session
    metadata = user.user_metadata
    
    print("access token : ", user_session.access_token)
    print("Current user :", user.id)
    
    # getting user's aggregator's id
    table_name = 'private_data'
    response = supabase.table(table_name=table_name).select('aggregator_id').eq('user_id',user.id).execute()
    print(response.data)
    aggregator_id = response.data[0]['aggregator_id']

    # getting user's aggregator public key
    response1= supabase.table(table_name=table_name).select('public_key').eq('user_id',aggregator_id).execute()
    aggregator_public_key = response1.data[0]['public_key']

    if (user.id != None):
        return user.id, user.email , metadata['private-key'], metadata['user-type'], aggregator_public_key, aggregator_id
    else:
        return 'unknown_error'

@eel.expose
def signOutUser():
    res = supabase.auth.sign_out()

    print("Current user :", res)

    return res

@eel.expose
def getUserSession():
    res : Session | None = supabase.auth.get_session()
    # user = supabase.auth.get_user()
    # print(res.access_token)
    return res

@eel.expose
def forgotPassword(email: str):
    pass