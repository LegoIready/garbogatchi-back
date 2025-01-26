from os import getenv
from dotenv import load_dotenv
load_dotenv()
supabase_url = getenv('S_URL')
supabase_key = getenv("S_KEY")

from supabase import create_client
supabase = create_client(supabase_url, supabase_key)
table = supabase.table("users")

from hashlib import sha256
from datetime import datetime

def register(username, password):
    if(table.select("id").eq("username", username).execute().data):
        return {
            "id": -1,
            "status": 1
        }
    return {
        "id": table.insert({
            "username": username,
            "passhash": sha256(password.encode()).digest()
        }).execute(),
        "status": 0
    }

def login(username, password):
    user = table.select("id, username, passhash").eq("username", username).execute().data
    if(not user or not user["passhash"] == sha256(password.encode()).hexdigest()):
        return {
            "id": -1,
            "status": 1
        }
    return {
        "id": user["id"],
        "status": 0
    }

def save_score(id, score):
    table.insert({
        "user": id,
        "score_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score
    }).execute()

