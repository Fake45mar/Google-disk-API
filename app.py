from __future__ import print_function

from flask import Flask, render_template, request
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

@app.route('/')
def home_page():
    file = open('credentials.json', 'r')
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_config('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    service_v2 = build('drive', 'v2', credentials=creds)
    results = service.files().list(pageSize=1000, fields='nextPageToken,files(id,name, createdTime, mimeType)').execute()#files().list(pageSize=150).execute()
    items = results.get("files")
    res = {}
    for e in items:
        res[e["id"]] = e
        # date = service.files().get(fileId=e["id"]).execute()
        if "folder" in e["mimeType"]:
            e["mimeType"] = "folder"

        else:
            e["mimeType"] = "file"
        # print(e)

    # print(service)
    return render_template("base.html")

@app.route('/folder', methods=['GET'])
def get_children_dir(method='GET'):
    file = open('credentials.json', 'r')
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_config('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v2', credentials=creds)
    s = build('drive', 'v3', credentials=creds)
    results = service.children().list(folderId='0B4zkVGWQL6-UfmRUeHpnVzJ3TWZfU2RNMWIyUnEtY01DRTEyTGR5ZmRXdVdsbTdyUFRVTzQ').execute()#list(pageSize=1000).execute()#files().list(pageSize=150).execute()
    items = results["items"]
    res = {}
    for e in items:
        res[e["id"]] = e
        print(service.files().get(fileId=e["id"]).execute())

if __name__ == '__main__':
    app.run()
