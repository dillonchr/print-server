import os
from flask import Flask, request
from dotenv import load_dotenv
from print import process_lines

load_dotenv()

app = Flask(__name__)

def print_lines(req):
    if req.content_length:
        with open(os.environ["PRINT_PATH"], "w") as file:
                process_lines(request.data.decode().splitlines(), file)


@app.route("/pppppprint", methods=["GET", "POST"])
def index():
    if request.data:
        print_lines(request)
    return "ok"

