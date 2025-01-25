from flask import Flask, request
app = Flask(__name__)

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

import prompt

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

# Check registration credentials and add them to the user database if valid.
# @params:
#   user: username.
#   pass: password.
# @returns:
#   Exit code.
#       0: user registered successfully.
#       1: invalid credentials.
#       2: username already exists.
@app.route("/register", methods = ["POST"])
def register():
    return "Not implemented."

# Check login credentials against the user database.
# @params:
#   user: username.
#   pass: password.
# @returns:
#   Exit code.
#       0: user logged in successfully.
#       1: invalid credentials.
@app.route("/login", methods = ["POST"])
def login():
    return "Not implemented."

# Adds the score from one round to the user record.
# @params:
#   user: username.
#   pass: password.
#   score: score to add to user record.
# @returns:
#   Updated user statistics.
@app.route("/save_score", methods = ["POST"])
def save_score():
    return "Not implemented."
