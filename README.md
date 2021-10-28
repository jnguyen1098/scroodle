# Scroodle

Selenium script to scrape scrambles from csTimer.net

csTimer runs locally in your browser, so this doesn't strain the servers
any more than if you just loaded the webpage; this is entirely to your
own device's discretion.

## Features

- Supports any two-option configuration of csTimer

- Outputs scrambles as an array so it's easy for integration into other scripts

- Bypasses the 999 scramble limit originally imposed by csTimer

- Runs headless for better performance (in theory . . .)

- Only has to use one instance of WebDriver (good for consecutive requests)

## Installation

```text
pip3 install -r requirements.txt
```

## Running

If you run `scroodle.py` as a standalone script, then you can freely change
the `tests` array in the mainline to fit your need. The setup required for
the function is already done there and as long as Selenium is working properly,
there shouldn't be any issue. The below, however, will explain the interface.

The function `get_scrambles()` polls an instance csTimer.net and retrieves
a list of scrambles (array of strings). It takes in four parameters:

- `driver` - an instance of WebDriver

- `puzzle` - the puzzle/event to be solved

- `option` - any optional, secondary parameters

- `scramble_count` - the number of scrambles to create

In order to generate scrambles to the following screenshot (4x4x4,
SiGN notation, 67 scrambles), you'd call the function as:

```py
get_scrambles(driver, "4x4x4", "SiGN", "67")
```

![screenshot of csTimer](https://i.imgur.com/9xAwdGw.png)

The function `get_driver()` creates a headless instance of csTimer.net at
800x480 resolution (in order to ensure the UI elements stay consistent).
Because the driver and scramble generator modal are only instantiated once,
calling `get_scrambles()` multiple times does not reload the page; only
re-create the scramble parameters. This makes it much faster than the original
script I made (also included in this repo) that continously refreshes qqTimer.

I also chose to switch to csTimer because it allows you to generate scrambles
for any event supported by the timer (qqTimer, on the other hand, only supports
a few).
