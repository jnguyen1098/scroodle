#!/usr/bin/env python3
"""Gather scrambles from csTimer.net."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

DEFAULT_IMPLICIT_WAIT = 10

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=800,480")

    # Open the driver and webpage
    driver = webdriver.Chrome(options=options)
    driver.get("https://cstimer.net")

    # Click on the 'Tools' menu
    tools_button = driver.find_element_by_xpath("//div[@class='mybutton c6']")
    tools_button.click()

    # Choose ScrambleGenerator
    tool_select_dropdown = Select(driver.find_element_by_xpath(
            "(//span[text()='Function']/select)[1]"
        )
    )

    tool_select_dropdown.select_by_visible_text("ScrambleGenerator")
    return driver

def get_scrambles(driver, puzzle, option, scramble_count):
    # Select puzzle/contest
    puzzle_selector = Select(
        driver.find_element_by_xpath("(//div[@class='title']/nobr/select)[1]")
    )
    puzzle_selector.select_by_visible_text(puzzle)

    # Select sub-option if need be
    option_selector = Select(
        driver.find_element_by_xpath("(//div[@class='title']/nobr/select)[2]")
    )
    option_selector.select_by_visible_text(option)

    # Raise the number limit
    driver.execute_script(
        """
            document.getElementByXPath = function(sValue) { var a = this.evaluate(sValue, this, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null); if (a.snapshotLength > 0) { return a.snapshotItem(0); } };
        """
    )
    driver.execute_script(
        """
            document.getElementByXPath("//div[text()='Number of scrambles']/input").setAttribute("maxlength", "10");
        """
    )

    # Specify number of scrambles
    scramble_count_selector = driver.find_element_by_xpath(
        "//div[text()='Number of scrambles']/input"
    )
    scramble_count_selector.clear()
    scramble_count_selector.send_keys(scramble_count)

    # Remove the numbering prefix lmao
    prefix_selector = Select(
        driver.find_element_by_xpath("//div[text()='Number of scrambles']/select")
    )
    prefix_selector.select_by_value("")

    # Click 'Generate Scrambles!'
    generate_button = driver.find_element_by_xpath("//span[text()='Generate Scrambles!']")
    generate_button.click()

    # Extract the text
    text_area = driver.find_element_by_xpath("//textarea[@readonly='']")

    return [line for line in text_area.text.split("\n")]

if __name__ == "__main__":
    tests = [
        ["10 2x2x2 optimal scrambles", "2x2x2", "optimal", "10"],
        ["10 7x7x7 prefix scrambles", "7x7x7", "prefix", "10"],
        ["100 3x3x3 scrambles", "3x3x3", "random state (WCA)", "100"],
        ["10 4x4x4", "4x4x4", "WCA", "10"],
        ["80 skewb", "Skewb", "random state (WCA)", "80"],
        ["10 megaminx", "Megaminx", "WCA", "10"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
        ["999", "3x3x3", "random state (WCA)", "999"],
    ]
    with get_driver() as driver:
        for test in tests:
            print(f"testing {test[0]}: {get_scrambles(driver, test[1], test[2], test[3])}\n\n")
