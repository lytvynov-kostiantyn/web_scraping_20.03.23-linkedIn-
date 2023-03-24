# Web Scraping using Beautiful Soup and Selenium for LinkedIn

### Description:
A training project whose goal is to read a list of links to pages with descriptions of companies from a
Google spreadsheet by reference. After that, with the help of selenium and BeautifulSoup, open data on the
number of employees is extracted from each link. The withdrawn data is subsequently recorded in the target Google
table, also by reference.

### TODO:
- For the script to work, you need to create a ".env" file with the following variables: 
  + LOGIN – login from LinkedIn account;
  + PASSWORD – password from LinkedIn account;
  + INPUT_URL - link to google spreadsheet with list of links and open read access;
  + OUTPUT_URL - link to google spreadsheet to record results;
- Create 'credentials.json' file. It`s a JSON file that contains the credentials for accessing Google APIs,
including Google Sheets API. It is used in conjunction with the Google API Client Library for Python to
authenticate and authorize access to a Google Sheets document. The file contains sensitive information such
as the client ID and client secret, which are used to authenticate the application and obtain an access token
for the Google Sheets API.

### Under the hood:
`main.py` - it`s a main file of the project

`requirements.txt` - it`s a file listing all the dependencies for Python project.