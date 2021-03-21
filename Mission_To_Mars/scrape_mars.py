#!/usr/bin/env python
# coding: utf-8

# In[161]:


# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[162]:


def initialize_browser():
    # Returns a "browser" object that will be used for scraping sites. 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser


# In[163]:


def scrape_mars_info():

    mars_url1 = "https://mars.nasa.gov/news"
    mars_url2 = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    mars_url3 = "http://space-facts.com/mars/"
    mars_url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    mars_data = {}
    
    #init the browser
    browser = initialize_browser()
    
    #Visit the first site and get the HTML
    browser.visit(mars_url1)
    
    #Parse the HTML with BS
    time.sleep(2) # Allow time for scraping and updating html variable
    html = browser.html
    soup = bs(html, "html.parser")
    
    # First list item with class=slide is the latest news
    mars_news = soup.find_all("div", attrs={"class":"list_text"})[0]
    news_title = mars_news.find('a').text
    news_p = mars_news.find("div", attrs={"class":"article_teaser_body"}).text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    
    #Scrape the second URL
    browser.visit(mars_url2)
    time.sleep(2)
    html = browser.html
    soup = bs(html,"html.parser")
    mars_img = soup.find("div", attrs={"class":"floating_text_area"})
    mars_img = mars_img.find("a")['href']
    featured_image_url = mars_url2.replace('index.html','') + mars_img
    mars_data['featured_image_url'] = featured_image_url
    
    #Scrape the third URL with Pandas
    print('Before read-html')
    mars_df = pd.read_html(mars_url3, match="Equatorial Diameter")[0]
    #Rename the column labes in dataFrame
    mars_df.rename(columns = {0 : 'Fact', 1 : 'Value'}, inplace = True)
    mars_data['fact_table_html'] = mars_df.to_html()
    
    #Scrape the fourth URL
    browser.visit(mars_url4)
    time.sleep(2)
    html = browser.html
    soup = bs(html, "html.parser")
    title_links = soup.find_all("a", class_="itemLink")
    results_list = []
    for theLink in title_links:
        link_title = theLink.find("h3")
        if (not link_title):
            continue
        #get the link
        a_link = theLink['href']
        url = "https://astrogeology.usgs.gov" + a_link
        browser.visit(url)
        time.sleep(2)
        html = browser.html
        soup = bs(html, "html.parser")
        download_div = soup.find("div", class_ = "downloads")
        full_img = download_div.find_all("li")[0].find('a')['href']
        results_list.append(dict({"title": link_title.text.replace(' Enhanced',''),"img_url":full_img}))

        
    browser.quit()
    mars_data['himispheres'] = results_list
    return(mars_data)


# In[160]:


if __name__ == "__main__":
    results = scrape_mars_info()
    print(results)


# In[ ]:




