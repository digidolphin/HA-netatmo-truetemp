from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class SetReq(BaseModel):
    room_name: str
    temperature: float

def run_cli(args: list[str]) -> str:
    p = subprocess.run(["netatmo-truetemp", *args], capture_output=True, text=True)
    if p.returncode != 0:
        raise HTTPException(status_code=500, detail=(p.stderr or p.stdout).strip() or "CLI failed")
    return p.stdout.strip()

@app.get("/rooms")
def rooms():
    return {"raw": run_cli(["list-rooms"])}

@app.post("/set")
def set_temp(req: SetReq):
    out = run_cli([
        "set-truetemperature",
        "--room-name", req.room_name,
        "--temperature", str(req.temperature),
    ])
    return {"ok": True, "raw": out}
