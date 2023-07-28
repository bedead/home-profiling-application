from gotrue import Session
import eel
from supabase import Client, create_client
from web.security.chaos_generator.triple_pendulum import decode_key, get_encoded_key
from web.security.diffi_hellman_EC import get_Shared_Key


SUPABASE_URL: str = "https://dvywdtjzuqgctliqaoix.supabase.co"
SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2eXdkdGp6dXFnY3RsaXFhb2l4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODUwODk4OTYsImV4cCI6MjAwMDY2NTg5Nn0.Tz0qflBoehtTWSFKgbVyczAwvvepQGQNBgxof4M-nFQ"
supabase: Client = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)


@eel.expose
def signInUser(email: str, password: str, verified: bool):
    # print(email, password)
    # gotrue.errors.AuthRetryableError (no internet)
    data = supabase.auth.sign_in_with_password({"email": email, "password": password})
    user = data.user
    user_session = data.session
    metadata = user.user_metadata

    # print("access token : ", user_session.access_token)
    print("Current user :", user.id)

    if verified == False:
        # getting user's aggregator's id
        table_name = "private_data"
        response = (
            supabase.table(table_name=table_name)
            .select("aggregator_id", "utility_public_key")
            .eq("user_id", user.id)
            .execute()
        )
        # print(response.data)
        aggregator_id = response.data[0]["aggregator_id"]
        utility_public_key = response.data[0]["utility_public_key"]

        # getting user's aggregator public key
        response1 = (
            supabase.table(table_name=table_name)
            .select("public_key")
            .eq("user_id", aggregator_id)
            .execute()
        )
        aggregator_public_key = response1.data[0]["public_key"]
        user_private_key = metadata["private-key"]
        shared_key_hex = get_Shared_Key(user_private_key, aggregator_public_key)
        encoded_key = get_encoded_key(shared_key_hex)
        generate_keys_list = decode_key(encoded_key[0])

        if user.id != None:
            return (
                user.id,
                user.email,
                user_private_key,
                metadata["user-type"],
                aggregator_public_key,
                aggregator_id,
                user_session.access_token,
                generate_keys_list,
                metadata["username"],
                utility_public_key,
            )
        else:
            return "unknown_error"
    else:
        return "success"


@eel.expose
def signOutUser():
    res = supabase.auth.sign_out()
    print("Current user :", res)
    return res


@eel.expose
def getUserSession():
    res: Session | None = supabase.auth.get_session()
    # user = supabase.auth.get_user()
    # print(res.access_token)
    return res


@eel.expose
def forgotPassword(email: str):
    pass
