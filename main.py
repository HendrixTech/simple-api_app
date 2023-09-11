from fastapi import FastAPI, Query
from datetime import datetime
from pytz import utc

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Hendrix's app. Type in your name and track as a parameter"}


@app.get("/api")
async def get_data(
        slack_name: str = Query(..., title="Slack Name"),
        track: str = Query(..., title="Track"),
):
    current_time = datetime.now(utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = datetime.now(utc).strftime("%A")

    github_repo_url = "https://github.com/HendrixTech/simple-api_app"
    github_file_url = "https://github.com/HendrixTech/simple-api_app/blob/main/main.py"

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }
    return response

# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
