# Smart Campus Helpdesk

Beginner-friendly Cloud Computing Assignment 7 project: PaaS using Google App Engine.

## Run locally on Windows
1. Install Python 3.12 and open PowerShell in this folder.
2. Create a virtual environment: `py -m venv .venv`
3. Activate it: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then `.\.venv\Scripts\Activate.ps1`
4. Install packages: `python -m pip install -r requirements.txt`
5. Run: `python main.py`
6. Open `http://127.0.0.1:5000` in a browser.

## Deploy to Google App Engine
1. Install Google Cloud CLI and sign in using `gcloud auth login`.
2. Select your project: `gcloud config set project YOUR_PROJECT_ID`.
3. In Google Cloud Console, enable App Engine Admin API and Cloud Build API.
4. If App Engine is not initialized, create it with `gcloud app create --region=YOUR_REGION`.
5. From this folder run `gcloud app deploy app.yaml`, then `gcloud app browse`.

Replace placeholders with your own project and region. Cloud billing/permissions may be required. Optional GitHub automation can use `cloudbuild.yaml` after you configure a Cloud Build trigger and permissions.

The announcements are sample data. This demo has no student login or database, and the cards are informational rather than links to official college systems. Do not claim deployment succeeded until you have opened the deployed URL.
