from csv import DictWriter
# pip install google-play-scraper
# pip install play-scraper
from google_play_scraper import app as app_scraper
from play_scraper import search

# CONFIGURATION VARIABLES
SEARCH_TERM = 'eating disorder'

# Use play_scraper.search to get list of apps matching SEARCH_TERM
found_apps = search(SEARCH_TERM, page=12)

# Use app_id to get more details for each app using app_scraper
found_app_data_list = []
for found_app in found_apps:
    app_id = found_app['app_id']
    app_details = app_scraper(app_id)
    app_data = {
        'app_id': app_id,
        'title': app_details['title'],
        'description': app_details['description'],
        'installs': app_details['installs'],
        'score': app_details['score'],
        'ratings': app_details['ratings'],
        'number_of_reviews': app_details['reviews'],
        'genre': app_details['genre']
    }
    found_app_data_list.append(app_data)

# Full list of data fields available:
# 'title', 'description', 'descriptionHTML', 'summary', 'summaryHTML', 
# 'installs', 'minInstalls', 'score', 'ratings', 'reviews', 'histogram', 
# 'price', 'free', 'currency', 'sale', 'saleTime', 'originalPrice', 
# 'saleText', 'offersIAP', 'inAppProductPrice', 'size', 'androidVersion', 
# 'androidVersionText', 'developer', 'developerId', 'developerEmail', 
# 'developerWebsite', 'developerAddress', 'privacyPolicy', 
# 'developerInternalID', 'genre', 'genreId', 'icon', 'headerImage', 
# 'screenshots', 'video', 'videoImage', 'contentRating', 
# 'contentRatingDescription', 'adSupported', 'containsAds', 'released', 
# 'updated', 'version', 'recentChanges', 'recentChangesHTML', 'comments', 
# 'editorsChoice', 'appId', 'url'

# Use search term to name output file
output_file = 'gps_' + SEARCH_TERM.replace(' ','_') + '_apps.csv'

# Save results to output file
with open(output_file,'w',encoding='utf-8',newline='') as file:
    dict_writer = DictWriter(file, found_app_data_list[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(found_app_data_list)
