from Scraper import *


#ADD THE TAGS TO SCRAPE HERE
tags = ["data-science"]


#ADD THE DATES TO SCRAPE HERE
yearstart=2018
monthstart=9
yearstop=2018
monthstop=10

#LOOPS THROUGH ALL LISTED-TAGS AND SCRAPES DATA OFF OF MEDIUM/TAG/archive
#SAVES THE FILES TO /TAG_SCRAPES/ IN CSV FORMAT AND
#SAVES THE ENTIRE ARTICLE IN stories.pickle file

for tag in tags:
    scrape_tag(tag, yearstart, monthstart, yearstop, monthstop)
    print("Done with tag: ", tag)

print("Scraping Completed")