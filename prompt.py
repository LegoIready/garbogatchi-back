from os import getenv
from dotenv import load_dotenv
load_dotenv()
supabase_url = getenv('S_URL')
supabase_key = getenv("S_KEY")

from supabase import create_client
supabase = create_client(supabase_url, supabase_key)

def get_prompt(id):
    return supabase.table("waste").select("*").eq("id", str(id)).execute().data[0]

import random
def get_prompts(num_prompts):
    num_rows = supabase.table("waste").select("id", count = "exact").execute().count
    prompts = []
    ids = [-1]

    for i in range(num_prompts):
        if(len(ids) - 1 == num_rows):
            break
        id = -1
        while(id in ids):
            id = random.randint(0, num_rows - 1)
        prompts.append(get_prompt(id))
        ids.append(id)
    
    return prompts
