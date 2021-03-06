import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import csv
from login import login
from goto_job_details import goto_job_details
from goto_performance import goto_performance
from start_post_job import start_post_job

if __name__ == '__main__':
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    login()
    with open("restart.csv") as f:
        for list in csv.reader(f):
            process_name = list[0]
            goto_job_details(process_name)
            goto_performance()
            start_post_job(process_name)