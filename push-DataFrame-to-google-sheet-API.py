import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import requests 
import traceback

def main(data):
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive']

    # Reading Credentails from ServiceAccount Keys file
    credentials = ServiceAccountCredentials.from_json_keyfile_name('project-indeed.json', scope)

    # intitialize the authorization object            
    gc = gspread.authorize(credentials)

    # Open Google Sheets file
    spreadsheet = gc.open('Indeed')

    # Select the desired worksheet
    worksheet = spreadsheet.sheet1  # or specify the worksheet index

    # Clear existing content in the sheet (optional)
    worksheet.clear()

    #Update the worksheet with the data
    worksheet.update('A1', data)

    # Define the new row of data to append
    new_row = ['title', 'link', 'company','search_term','date','location','city','province']

    # Append the new row at the top of the sheet
    worksheet.insert_row(new_row, 1)