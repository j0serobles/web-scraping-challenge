# web-scraping-challenge
UCF Data Analytics And Visualization Bootcamp Homework 12 - Web Scraping and Document Databases


# Web Scraping Homework - Mission to Mars

In this assignment, we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# The Process
The process begins by scraping 4 websites and extracting information about Mars, and several image URL's that are compiled into a Python dictionary and later saved as a document in a MongoDB collection.  The collection is later used as the data source of a web page built with Flask. 

# Step 1 - Scraping
The process begins by scraping the websites using a function.  The function uses calls to the BeautifulSoup library to extract the elements of the web pages from 4 sites dedicated to Mars information. This is a section of the scraping program, that extracts the elements of one of the web pages:


The Pandas library is also used to scrape information off one of the websites, using the ```read_html()``` function call.

# Step 2 - Save to MongoDB
The information is saved in memory to a python dictionary structure, and this is later saved to a MongoDB collection.  The data in the MongoDB collection will be used later to construct the new web site. 

# Step 3 - Flask web site
The last step uses Flask to create a website that populates an HTML template with the information saved from the previous step.  The template variables are updated with the information scraped off the websites and saved into the MongoDB collection.
