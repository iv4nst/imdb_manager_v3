from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import csv
import random
import os
import time

from constants import *


def main(driver):
    print(WELCOME)
    while True:
        print(MAIN_OPTIONS)
        choice = input(CHOOSE_AN_OPTION)
        try:
            if int(choice) == 1:  # Access the watchlist
                sign_in(driver)
                print(ACCESSING_WATCHLIST)
                download_watchlist(driver)
                choose_from_watchlist(driver)
                break
            elif int(choice) == 2:  # Search for the movie or tv show
                sign_in(driver)
                search_term(driver)
                break
            elif int(choice) == 3:
                print(QUITTING)
                break
            else:
                print(INVALID_INPUT)
                print(ENTER_A_VALID_OPTION)
        except ValueError:
            print(INVALID_INPUT)
            print(ENTER_A_VALID_OPTION)


def sign_in(driver):
    print(SIGNING_IN)
    while True:
        driver.get(SIGN_IN_PAGE)

        imdb_email = input(ENTER_EMAIL)
        imdb_pass = input(ENTER_PASSWORD)

        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)))
        email.send_keys(imdb_email)
        password = driver.find_element_by_css_selector(PASS_CSS_SELECTOR)
        password.send_keys(imdb_pass)

        sign_in_submit = driver.find_element_by_css_selector(SIGN_IN_SUBMIT_CSS_SELECTOR)
        sign_in_submit.click()

        page_source = driver.page_source

        if INVALID_EMAIL in page_source:
            print(TRY_AGAIN_EMAIL)
        elif INVALID_PASSWORD in page_source:
            print(TRY_AGAIN_PASSWORD)
        else:
            print(SIGNED_IN)
            break


def search_term(driver):
    choose_type = driver.find_element_by_css_selector(CHOOSE_TYPE_CSS_SELECTOR)
    choose_type.click()

    title_type = driver.find_element_by_css_selector(TITLE_TYPE_CSS_SELECTOR)
    title_type.click()

    search_term_input = input(SEARCH_FOR)

    search_box = driver.find_element_by_css_selector(SEARCH_BOX_CSS_SELECTOR)
    search_box.send_keys(search_term_input)

    print()

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    term = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, SEARCH_TERM_CSS_SELECTOR)))
    term.click()

    url = driver.current_url[:37]
    term_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, TERM_TITLE_CSS_SELECTOR)))
    title = term_title.text

    compare_in_watchlist(driver, url, title)


def compare_in_watchlist(driver, url, title):
    download_watchlist(driver)

    try:
        is_downloaded(WATCHLIST)
        with open(WATCHLIST) as f:
            rows = csv.DictReader(f, delimiter=',', quotechar='"')
            movie_in_watchlist = [row for row in rows if row['URL'] == url]
        if movie_in_watchlist:
            movie = movie_in_watchlist[0]
            print(IN_WATCHLIST.format(**movie))
            print(THREE_OPTIONS.format(**movie))
            choose_option(driver, movie)
        else:
            print(NOT_IN_WATCHLIST.format(title))
            add_to_watchlist = input(ADD_TO_WATCHLIST_PROMPT.format(title))
            if add_to_watchlist == 'y'.lower():
                print(CHECK_IF_RATED.format(title))
                download_ratings(driver)
                try:
                    with open(RATINGS) as f:
                        rows = csv.DictReader(f, delimiter=',', quotechar='"')
                        already_rated = [row for row in rows if row['URL'] == url]
                    if already_rated:  # already rated
                        print(RATED.format(title))
                    else:
                        print(NOT_RATED.format(title))
                        add_to_watchlist = input(ADD_TO_WATCHLIST_PROMPT.format(title))
                        if add_to_watchlist == 'y'.lower():
                            driver.get(url)
                            add_to_watchlist_btn = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, ADD_TO_WATCHLIST_CSS_SELECTOR)))
                            add_to_watchlist_btn.click()
                            print(SUCCESSFULLY_ADDED.format(title))
                        elif add_to_watchlist == 'n'.lower():
                            print(NOT_ADDED.format(title))
                except FileNotFoundError:
                    print(RATINGS_NOT_FOUND)
    except FileNotFoundError:
        print(WATCHLIST_NOT_FOUND)
    finally:
        remove_watchlist()
        remove_ratings()


def download_watchlist(driver):
    driver.get(WATCHLIST_URL)
    # First remove the watchlist file if there is one
    remove_watchlist()
    # Download the watchlist file
    export = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, EXPORT_CSS_SELECTOR)))
    export.click()


def download_ratings(driver):
    driver.get(RATINGS_URL)
    # First remove the ratings file if there is one
    remove_ratings()
    # Download the ratings file
    url = driver.current_url + '/export'
    driver.get(url)


def choose_from_watchlist(driver):
    while True:
        print(TWO_OPTIONS)
        choice = input(CHOOSE_AN_OPTION)
        try:
            if int(choice) == 1:
                choose_movie(driver)
                break
            elif int(choice) == 2:
                choose_tv_show(driver)
                break
            else:
                print(INVALID_INPUT)
                print(ENTER_A_VALID_OPTION)
        except ValueError:
            print(INVALID_INPUT)
            print(ENTER_A_VALID_OPTION)


def choose_movie(driver):
    try:
        with open(WATCHLIST) as f:
            rows = csv.DictReader(f, delimiter=',', quotechar='"')
            movies = [row for row in rows if row['Title Type'] == 'movie']
        movie = random.choice(movies)

        print(TEXT.format(num=len(movies), **movie))
        choose_option(driver, movie)
        remove_watchlist()
    except FileNotFoundError:
        print(WATCHLIST_NOT_FOUND)


def choose_tv_show(driver):
    try:
        with open(WATCHLIST) as f:
            rows = csv.DictReader(f, delimiter=',', quotechar='"')
            tv_shows = [row for row in rows if
                        row['Title Type'] == 'tvSeries' or row['Title Type'] == 'tvMiniSeries']
        tv_show = random.choice(tv_shows)

        print(TEXT.format(num=len(tv_shows), **tv_show))
        choose_option(driver, tv_show)
        remove_watchlist()
    except FileNotFoundError:
        print(WATCHLIST_NOT_FOUND)


def rate(driver, element):
    rating = int(input(ENTER_RATING.format(**element)))

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    rate_this = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, RATE_THIS_CSS_SELECTOR)))
    rate_this.click()

    if rating == 1:
        rate_star = driver.find_element_by_css_selector(ONE_STAR)
        rate_star.click()
    elif rating == 2:
        rate_star = driver.find_element_by_css_selector(TWO_STARS)
        rate_star.click()
    elif rating == 3:
        rate_star = driver.find_element_by_css_selector(THREE_STARS)
        rate_star.click()
    elif rating == 4:
        rate_star = driver.find_element_by_css_selector(FOUR_STARS)
        rate_star.click()
    elif rating == 5:
        rate_star = driver.find_element_by_css_selector(FIVE_STARS)
        rate_star.click()
    elif rating == 6:
        rate_star = driver.find_element_by_css_selector(SIX_STARS)
        rate_star.click()
    elif rating == 7:
        rate_star = driver.find_element_by_css_selector(SEVEN_STARS)
        rate_star.click()
    elif rating == 8:
        rate_star = driver.find_element_by_css_selector(EIGHT_STARS)
        rate_star.click()
    elif rating == 9:
        rate_star = driver.find_element_by_css_selector(NINE_STARS)
        rate_star.click()
    elif rating == 10:
        rate_star = driver.find_element_by_css_selector(TEN_STARS)
        rate_star.click()

    print(TITLE_RATED.format(**element))


def remove(driver, element):
    print(REMOVING_FROM_WATCHLIST.format(**element))

    remove_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, REMOVE_BUTTON_XPATH_SELECTOR)))
    remove_btn.click()

    print(REMOVED_FROM_WATCHLIST.format(**element))


def choose_option(driver, element):
    while True:
        choice = input(CHOOSE_AN_OPTION)
        try:
            if int(choice) == 1:
                print(CHOOSE_RATE.format(**element))
                locate(driver, element)
                rate(driver, element)
                remove(driver, element)
                print(GOODBYE)
                break
            elif int(choice) == 2:
                print(CHOOSE_REMOVE.format(**element))
                locate(driver, element)
                remove(driver, element)
                print(GOODBYE)
                break
            elif int(choice) == 3:
                print(QUITTING)
                break
            else:
                print(INVALID_INPUT)
                print(ENTER_A_VALID_OPTION)
        except ValueError:
            print(INVALID_INPUT)
            print(ENTER_A_VALID_OPTION)


def remove_watchlist():
    watchlist = os.getcwd() + '\\' + WATCHLIST
    if os.path.isfile(watchlist):
        os.remove(watchlist)
    else:
        pass


def remove_ratings():
    ratings = os.getcwd() + '\\' + RATINGS
    if os.path.isfile(ratings):
        os.remove(ratings)
    else:
        pass


def locate(driver, element):
    print(LOCATING.format(**element))
    movie_url = '{URL}'.format(**element)
    driver.get(movie_url)


def is_downloaded(filename, timeout=60):
    end_time = time.time() + timeout
    while not os.path.exists(filename):
        time.sleep(1)
        if time.time() > end_time:
            print(NOT_FOUND_WITHIN_TIME.format(filename))
            return False
    if os.path.exists(filename):
        return True
