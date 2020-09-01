"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

import string

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/drive.readonly'
#     'https://www.googleapis.com/auth/spreadsheets'
#     'https://www.googleapis.com/auth/spreadsheets.readonly'
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = '1AV5IqNhVaiFLq9hEDezLs4JYm4OcepfN1uux-E0NzdY'  # TODO: Update placeholder value.

# The A1 notation of the values to retrieve.
range_ = 'A13:A13'  # TODO: Update placeholder value.

# How values should be represented in the output.
# The default render option is ValueRenderOption.FORMATTED_VALUE.
value_render_option = 'FORMATTED_VALUE'  # TODO: Update placeholder value.

# How dates, times, and durations should be represented in the output.
# This is ignored if value_render_option is
# FORMATTED_VALUE.
# The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
date_time_render_option = 'SERIAL_NUMBER'  # TODO: Update placeholder value.

patronRequest = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
response = patronRequest.execute()

# TODO: Change code below to process the `response` dict:
currentPatronCount = str(response.get('values')).strip('[]\'')
print(currentPatronCount)