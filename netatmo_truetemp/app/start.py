import json
import os
import uvicorn


with open("/data/options.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

os.environ["NETATMO_USERNAME"] = cfg.get("username", "")
os.environ["NETATMO_PASSWORD"] = cfg.get("password", "")
home_id = cfg.get("home_id", "")
if home_id:
    os.environ["NETATMO_HOME_ID"] = home_id

uvicorn.run("main:app", host="0.0.0.0", port=8099, app_dir="/app")

