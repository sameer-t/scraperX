scraperX
========

A scraper script in Python to get LinkedIn profiles of all people employed at a company

This repository contains the scripts required to scrape profile data from LinkedIn for feeding it into the Rexsys back-end. As, in future, we will be working with companies like Uber, please use that branch and modify it as required for other companies.

System Configuration: Ubuntu 14.04

External python modules required:

* Selenium + chrome web-driver
* openpyxl
* Beautiful Soup 4

Deployment instructions:


1. Begin by running 'scraper_link.py'. This will give us a list of all the profile links for people employed at Uber. Modify the links on line #30 and #59 w.r.t the company.
2. Then run the 'scraper_html.py' to save all the profiles in the local machine as html files, as well as to create a spreadsheet with the name in 1st column and profile url in the 2nd column(this file has the name uber_lookup.xlsx. Use it with the function 'vlookup' in excel to get the urls for those people who do not have a public profile)
3. Finally, run the 'scraper_data.py' to generate a raw spreadhseet, which, after formatting, will be fed into the rexsys server.

Formatting the raw spreadsheet:

1. Delete unnecessary columns and re-arrange them to match the 'DB_template' file
2. Use the formulas in the template file to get the position, school and company data
3. Sort the data by name and use the lookup file created by scraper_html and VLOOKUP function to get the LinkedIn urls for those without public profile
4. Use the TRIM function on the Data column to remove any extra spaces
5. Use the 'Remove Duplicates' feature in Excel based on the data column to remove any repetitions(might happen sometimes)

NOTE: 

* LinkedIn blocks an account after you have used it to see around 700-800 profiles. You'll then need to use another account to continue scraping. Need to code this in.
* The scraper_analysis.py script is used to generate a spreadsheet to be used for analysis. It need to be updated to use BeautifulSoup
