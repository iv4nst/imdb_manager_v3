# =================
# URLS
# =================

# sign in
SIGN_IN_PAGE = 'https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com' \
               '%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth' \
               '%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState' \
               '=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_' \
               'cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select' \
               '&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20 '

# watchlist
WATCHLIST_URL = 'https://www.imdb.com/list/watchlist'

# ratings
RATINGS_URL = 'https://www.imdb.com/list/ratings'

# =================
# SELECTORS
# =================

# sign_in()
EMAIL_CSS_SELECTOR = '#ap_email'
PASS_CSS_SELECTOR = '#ap_password'
SIGN_IN_SUBMIT_CSS_SELECTOR = '#signInSubmit'

# -------------------------------------------------------------

# search_term()
CHOOSE_TYPE_CSS_SELECTOR = '#nav-search-form > div.search-category-selector.sc-htoDjs.jAJuqP > div > label'
TITLE_TYPE_CSS_SELECTOR = '#navbar-search-category-select-contents > ul > a:nth-child(2)'
SEARCH_BOX_CSS_SELECTOR = '#suggestion-search'
SEARCH_TERM_CSS_SELECTOR = '#react-autowhatever-1--item-0 > a'
TERM_TITLE_CSS_SELECTOR = '#ratingWidget > p:nth-child(2) > strong'

# -------------------------------------------------------------

# compare_in_watchlist()
ADD_TO_WATCHLIST_CSS_SELECTOR = '#title-overview-widget > div.plot_summary_wrapper > ' \
                                'div.uc-add-wl-button.uc-add-wl--not-in-wl.uc-add-wl > ' \
                                'button.ipc-button.uc-add-wl-button-icon--add.watchlist--title-main-desktop' \
                                '-standalone.ipc-button--core-base.ipc-button--single-padding.ipc-button--default' \
                                '-height '

# -------------------------------------------------------------

# download_watchlist()
EXPORT_CSS_SELECTOR = '#center-1-react > div > div.export > a'

# -------------------------------------------------------------

# rate()
RATE_THIS_CSS_SELECTOR = '#star-rating-widget > div > button'

# stars
ONE_STAR = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(1)'
TWO_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(2)'
THREE_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(3)'
FOUR_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(4)'
FIVE_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(5)'
SIX_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(6)'
SEVEN_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(7)'
EIGHT_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(8)'
NINE_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(9)'
TEN_STARS = '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(10)'

# -------------------------------------------------------------

# remove()
REMOVE_BUTTON_XPATH_SELECTOR = '//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div'

# =================
# ERRORS
# =================
INVALID_EMAIL = 'We cannot find an account with that email address'
TRY_AGAIN_EMAIL = 'Invalid email!\nTry again.'
INVALID_PASSWORD = 'Your password is incorrect'
TRY_AGAIN_PASSWORD = 'Invalid password!\nTry again.'

# =================
# TEXT
# =================

# Files
WATCHLIST = 'WATCHLIST.csv'
RATINGS = 'ratings.csv'

# File not found
WATCHLIST_NOT_FOUND = '[File] WATCHLIST.csv not found.'
RATINGS_NOT_FOUND = '[File] ratings.csv not found.'

WELCOME = 'Welcome to IMDb Manager v3'
ACCESSING_WATCHLIST = 'Accessing watchlist...'
QUITTING = 'Quitting...'
SIGNING_IN = 'Signing in to IMDb...'

SIGNED_IN = 'Signed in.'

ENTER_EMAIL = 'Enter your IMDb email address: '
ENTER_PASSWORD = 'Enter your IMDb password: '

SEARCH_FOR = 'Search for a movie or tv show: '
SEARCHING = 'Searching...'

INVALID_INPUT = 'Invalid input!'
ENTER_A_VALID_OPTION = 'Please enter a valid option!'

CHOOSE_AN_OPTION = 'Choose an option: '

MAIN_OPTIONS = '''
What would you like to do?

1. Choose random movie/tv show from the watchlist
2. Search for a movie or tv show
3. Quit'''

IN_WATCHLIST = '"{Title}" is already in watchlist.'
NOT_IN_WATCHLIST = '"{}" is not in watchlist.'
ADD_TO_WATCHLIST_PROMPT = 'Would you like to add "{}" to watchlist? (y/n) '
CHECK_IF_RATED = 'Checking to see if "{}" is already rated...'
RATED = '"{}" is already rated.'
NOT_RATED = '"{}" is not rated. You can add it to watchlist if you want.'
SUCCESSFULLY_ADDED = '"{}" successfully added to watchlist.'
NOT_ADDED = 'You chose not to add "{}" to watchlist.'
ENTER_RATING = 'Enter the rating for "{Title}": '
TITLE_RATED = '"{Title}" rated.'
REMOVING_FROM_WATCHLIST = 'Removing "{Title}" from your watchlist...'
REMOVED_FROM_WATCHLIST = '"{Title}" removed from your watchlist.'
CHOOSE_RATE = 'You chose to rate "{Title}".'
CHOOSE_REMOVE = 'You chose to remove "{Title}" from your watchlist.'
GOODBYE = 'Goodbye.'
LOCATING = 'Locating "{Title}"...'
NOT_FOUND_WITHIN_TIME = '{} not found within time.'

TWO_OPTIONS = '''
Would you like me to choose for you a random Movie or TV Show?

1. Movie
2. TV Show'''

THREE_OPTIONS = '''
You have three options:
1 - Rate "{Title}" (also removes it from the watchlist)
2 - Remove "{Title}" from your watchlist
3 - Quit'''

TEXT = """
There are {num} feature films in your watchlist.

    I have chosen the following movie for you:

    ===========================================

        {Title} ({Year})

        IMDb Rating:    {IMDb Rating}
        Genres:         {Genres}
        Runtime:        {Runtime (mins)}min
        Link:           {URL}

    ===========================================

    You have two options:
    1 - Rate "{Title}" (also removes it from the watchlist)
    2 - Remove "{Title}" from your watchlist
    3 - Quit
        """
