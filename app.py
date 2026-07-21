import os, sys, time
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
if os.getenv("CRASH_ON_START") == "true": sys.exit("Crashing!")

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "ok"}

# @app.route("/load")
# def load():
#     start_time = time.time()
#     while time.time() - start_time < 10:
#         _ = 12345 * 54321
#     return {"status": "load complete"}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)