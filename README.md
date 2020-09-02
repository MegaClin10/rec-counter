# rec-counter
Program to track data from TAMU Rec Center capacity Google Sheet. 


With the COVID-19 outbreak, Texas A&M Recreation Center has set patron capacity at 300.
Checking the google sheet where the current patron count is displayed is inconvenient and does not display any trend data.
This simple program uses the google sheets API to retrieve the current patron count listed on the official google sheet and exports this data, along with date and time, to a csv every ~5 minutes.

From the csv, I can easily show trends in this data and plan my visits to the rec center accordingly.
