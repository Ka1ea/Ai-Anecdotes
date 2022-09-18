# crayon.py
# functions that open crayon and get the html for parsing
# Kalea Gin
# 9/17/22 
#ver 1

from os import link
from time import sleep
import webbrowser
from selenium import webdriver
from randomPhrase import rand_int
from selenium.webdriver.common.keys import Keys


def open_crayon(line):
    linesX = line.split("/n")
    chosenline = linesX[rand_int(linesX)]
    link = get_link(chosenline)
    driver = webdriver.Firefox()
    driver.get(link)
    button = driver.find_element("xpath","//*[@id=\"app\"]/div/div/div[1]/button")
    button.click()
    
    #two min for the ai to load
    sleep(120)
    
    html = driver.page_source
    imgs = get_image_links(html, chosenline)
    return imgs
    #after 2 mins run
    



def get_link(line):
    root = "https://www.craiyon.com/?prompt="
    line = line.strip().replace(" ", "+")
    return root+line
