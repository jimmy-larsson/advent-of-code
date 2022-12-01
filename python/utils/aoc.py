import json
import os
import sys
import re

import requests

from bs4 import BeautifulSoup


def log(message, *args):
    sys.stdout.write(message.format(*args) + "\n")
    sys.stdout.flush()


def log_error(message, *args):
    sys.stderr.write(message.format(*args) + "\n")
    sys.stderr.flush()


def has_been_setup():
    if YEAR == -1 and DAY == -1:
        log_error("The setup has not been performed yet. Exiting.")
        sys.exit(1)


def setup(year, day):
    global YEAR
    global DAY
    global SESSION
    global SESSION_COOKIE
    global USER_AGENT

    if not (year >= 2021 and 1 <= day <= 25):
        log_error("Invalid year or date specified.")
        sys.exit(1)

    YEAR = year
    DAY = day

    variables_path = '../../config/variables.json'
    if os.path.isfile(variables_path):
        with open(variables_path) as file:
            config = json.load(file)
            SESSION_COOKIE = config["session-cookie"]
            SESSION.cookies.set("session", SESSION_COOKIE)

            USER_AGENT = config["user-agent"]
            SESSION.headers = {"User-Agent": USER_AGENT}


def validate_response(response):
    if response.status_code != 200:
        log_error(
            "An error occurred when attempting to download the file from the server. Response code for url {} is {} "
            "and response text is: \n{}", response.url, response.status_code, response.text)
        log_error("")
        sys.exit(1)
    if 'please identify yourself' in response.text.lower():
        log('An error occurred when attempting to download the file. Please verify that the session-cookie has been '
            'set and updated.\n')
        sys.exit(1)


def get_input(filename=None, mode='r'):
    has_been_setup()

    if filename is not None:
        return open(filename, mode)

    if not os.path.isdir(CACHE_DIR):
        try:
            log("Cache directory '{}' does not exist. Creating...", CACHE_DIR)
            os.makedirs(CACHE_DIR)
        except Exception as e:
            log_error("Unable to create cache directory '{}'", CACHE_DIR)
            log_error("Actual message: {}", str(e))
            sys.exit(1)

    log("Getting input for year {} and day {}...", YEAR, DAY)
    filename = os.path.join(CACHE_DIR, '{}_{:02d}.txt'.format(YEAR, DAY))
    try:
        file = open(filename, mode)
        log("Done. File downloaded from cache.")
        return file
    except FileNotFoundError:
        log("Input for the specified year and day not found in cache directory. Attempting to download from server...")
        pass

    r = SESSION.get(URL.format(YEAR, DAY, 'input'))
    validate_response(r)

    with open(filename, 'wb') as file:
        file.write(r.content)

    file = open(filename, mode)
    log("Done. File downloaded from server.")

    return file


def print_answer(part, answer):
    print("\nPart {}:".format(part), answer)


def submit_answer(part, answer):
    has_been_setup()

    log('Submitting solution for day {} part {}, answer: {}\n', DAY, part, answer)

    r = SESSION.post(URL.format(YEAR, DAY, 'answer'), data={'level': part, 'answer': answer})
    validate_response(r)

    response = r.text.lower()

    if "that's the right answer" in response:
        log("Good job, that's the right answer!")
        print_response_from_html(response)

        return True

    if "you don't seem to be solving the right level" in response:
        log("You don't seem to be solving the right level.  Did you already complete it?")
        print_response_from_html(response)

        return False

    if "answer too recently" in response:
        matches = re.compile(r'you have ([\w ]+) left to wait').findall(response)

        if matches:
            log('You are submitting too fast. Wait for another {} seconds.\n', matches[0])
        else:
            log('You are submitting too fast!\n')
        print_response_from_html(response)

        return False

    log("That's not the right answer!")
    print_response_from_html(response)


def print_response_from_html(response):
    try:
        soup = BeautifulSoup(response, 'html.parser')
        log("Actual message: {}", soup.article.get_text())
    except Exception as e:
        log_error("Failed to parse html for response.")
        log_error("Actual message {}", str(e))


URL = 'https://adventofcode.com/{:d}/day/{:d}/{:s}'
CACHE_DIR = '../cache/inputs'
USER_AGENT = ''
SESSION = requests.Session()
SESSION_COOKIE = ''
YEAR = -1
DAY = -1
