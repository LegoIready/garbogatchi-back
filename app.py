from flask import Flask, request
app = Flask(__name__)

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

import prompt
import user
import search

# Homepage
@app.route("/")
def index():
    return "Backend host for Garbagotchi!"

# Get specified number of prompts from Supabase.
# @params:
#   num_prompts: the number of prompts to get.
# @return:
#   num_prompts prompts with URL and bin ID.
# 
#   {
#       "prompts": [
#           {
#               "url": "https://SUPABASE_URL.supabase.co/storage/v1/object/public/BUCKET_NAME/IMAGE_NAME",
#               "bin": BIN_ID
#           }
#       ]
#   }
@app.route("/get_prompts", methods = ["GET", "POST"])
@cross_origin()
def get_prompts():
    return {
        "prompts": prompt.get_prompts(int(request.args.get("num_prompts")))
    }

# eg.
# {
#   "results": [
#     {
#       "County": "Los Angeles",
#       "Enforcement Agency (LEA-EA)": "Los Angeles County",
#       "SWISNumber": "19-AA-5547",
#       "Site Name": "Goldring Dump Landfill",
#       "Site Operational Status": "Clean Closed",
#       "Site Regulatory Status": "Not Currently Regulated",
#       "id": 2346
#     },
#     {
#       "County": "Riverside",
#       "Enforcement Agency (LEA-EA)": "Riverside County",
#       "SWISNumber": "33-AA-0007",
#       "Site Name": "Lamb Canyon Sanitary Landfill",
#       "Site Operational Status": "Active",
#       "Site Regulatory Status": "Permitted",
#       "id": 2630
#     }
#   ]
# }
@app.route("/get_results", methods = ["GET", "POST"])
@cross_origin()
def get_results():
    return {
        "results": search.get_prompts(int(request.args.get("num_prompts")))
    }

# Check registration credentials and add them to the user database if valid.
# @params:
#   username: username.
#   password: password.
# @returns:
#   User ID and exit code.
#       0: user registered successfully.
#       1: username already exists.
#   {
#       "id": USER_ID,
#       "status": EXIT_CODE
#   }
@app.route("/register", methods = ["GET", "POST"])
def register():
    return user.register(
        request.args.get("username"),
        request.args.get("password")
    )

# Check login credentials against the user database.
# @params:
#   username: username.
#   password: password.
# @returns:
#   User ID and exit code.
#       0: user logged in successfully.
#       1: invalid credentials.
#   {
#       "id": USER_ID,
#       "status": EXIT_CODE
#   }
@app.route("/login", methods = ["GET", "POST"])
def login():
    return user.login(
        request.args.get("username"),
        request.args.get("password")
    )

# Adds the score from one round to the user record.
# @params:
#   id: user ID.
#   score: score to add to user record.
@app.route("/save_score", methods = ["GET", "POST"])
def save_score():
    user.save_score(
        int(request.args.get("id")),
        int(request.args.get("score"))
    )
