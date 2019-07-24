from __future__ import print_function

from flask import Flask
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

@app.route('/')
def hello_world():
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

    results = service.files().list(pageSize=50, fields = 'nextPageToken, files(id, name)').execute()
    items = results.get('files', [])

    if not items:
        print('There aren\'t files')

    else:
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    return file.read() + "йй"


if __name__ == '__main__':
    app.run()
