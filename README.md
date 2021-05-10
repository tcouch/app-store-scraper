# App Store Scraping Tools
A collection of scripts which can be used to search for apps on the Apple and Google Play stores and retrieve further details.

Combining existing scrapers where possible and some new code.

## Setup
1. [Create a new virtual environment](https://docs.python.org/3/tutorial/venv.html) and activate it
2. Install the required packages: `pip install -r requirements.txt`

## Searching for apps on google play store

1. Edit *gp_app_search.py* and change the **SEARCH_TERM** variable to your liking
2. Run the script: `python gp_app_search.py`
3. Metadata for all found apps is saved to an output file called; e.g. *gps_SEARCH_TERM_apps.csv*

## Get reviews for google play store apps

1. Edit *get_gp_app_reviews.py* and change **IN_FILE** to the name of a csv file containing metadata for the apps you want to get reviews for. <br>**Must contain a column titled app_id**
2. Run the script: `python get_gp_app_reviews.py`
3. Reviews are saved to separate csv files named according to app_id for each app; e.g., *com_target_app_reviews.csv*

