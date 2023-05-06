import datetime
import requests
import glob
import os
from bs4 import BeautifulSoup

# define the URL to retrieve
url = "https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note"

# send a GET request to retrieve the web page
response = requests.get(url)

# parse the HTML content of the web page
soup = BeautifulSoup(response.content, "html.parser")

# extract the contents of the <main> element
main_content = str(soup.find("main"))

# write the contents to a file called temp.html
with open("temp.html", "w", encoding="utf-8") as f:
    f.write(main_content)

# read the contents of the file
with open("temp.html", "r", encoding="utf-8") as f:
    main_content = f.read()


# find the newest file in the current directory matching the glob "????-??-??.html"
# and compare its contents with the current version
try:
    latest_file = max(glob.glob("????-??-??.html"), key=os.path.getmtime)

except ValueError:
    # create a new latest_file with 
    # the current date and time
    latest_file = "1969-12-31.html"


# create a new file in the format YYYY-MM-DD.html
currentfile = datetime.datetime.now().strftime("%Y-%m-%d") + ".html"


# check if the file exists and compare its contents with the current version
if os.path.isfile(latest_file):
    with open(latest_file, "r", encoding="utf-8") as f:
        last_main_content = f.read()
        # do a binary comparison of the two strings
        if last_main_content == main_content:
            print("The current version is the same as the last saved version.")
        else:
            print(f"The current version is different from the last saved version. Saving {currentfile}.")
            # save the current version
            with open(currentfile, "w", encoding="utf-8") as f:
                f.write(main_content)
else:
    print("The file does not exist. Saving the current version.")
    # save the current version
    with open(currentfile, "w", encoding="utf-8") as f:
        f.write(main_content)
