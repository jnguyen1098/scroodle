#!/usr/bin/env python3
"""Gather scrambles from qqtimer.net."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

DEFAULT_IMPLICIT_WAIT = 10

def get_scramble_text(scramble_type, sub_type=None, scramble_length=None):
    options = Options()
    options.add_argument("--headless")
    with webdriver.Chrome(options=options) as driver:
        driver.get("https://www.qqtimer.net/")
        driver.implicitly_wait(DEFAULT_IMPLICIT_WAIT)
        select = Select(driver.find_element_by_xpath("//select[@id='optbox']"))
        select.select_by_visible_text(f"{scramble_type}")
        if sub_type is not None:
            select2 = Select(driver.find_element_by_xpath("//select[@id='optbox2']"))
            select2.select_by_visible_text(f"{sub_type}")
        if scramble_length is not None:
            num_scrambles = driver.find_element_by_xpath("//input[@id='leng']")
            num_scrambles.clear()
            num_scrambles.send_keys(f"{scramble_length}\n")
        scramble_text = driver.find_element_by_xpath("//span[@id='scramble']")
        return scramble_text.text.replace("scramble: ", "")

def get_3x3_relay(num_scrambles):
    text = get_scramble_text("Relays", "lots of 3x3x3s", num_scrambles)
    return [
        line[line.index(") ") + 2:] for line in text.split("\n")[1:]
    ]

if __name__ == "__main__":

    tests = [
        ["3x3x3", "3x3x3", None, None],
        ["3x3x3 old style", "3x3x3", "old style", None],
        ["10x10x10", "10x10x10", None, None],
    ]
    for test in tests:
        print(f"Current test: {test[0]}: {get_scramble_text(test[1], test[2], test[3])}")

    print("Getting 100 relay scrambles")
    for line in get_3x3_relay(100):
        print(line)
