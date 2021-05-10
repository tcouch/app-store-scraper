from csv import DictReader, DictWriter

from google_play_scraper import reviews_all

IN_FILE = 'gps_app_review_test_data.csv'

# read app name and id from csv file
apps = []
with open(IN_FILE,newline='',encoding='utf-8') as file:
    reader = DictReader(file)
    for row in reader:
        apps.append({'app_id':row['app_id']})

# for each app, use the fetch all reviews and save to separate csv file
for app in apps:
    reviews = reviews_all(app['app_id'])    
    app['reviews'] = reviews # save list of reviews to existing dictionary
    if app.get('reviews'): # Not all apps have reviews
        # use the app_name to name the output file
        outfile = app['app_id'].replace('.','_') + '_reviews.csv'
        with open(outfile,'w',encoding='utf-8',newline='') as file:
            dict_writer = DictWriter(file, app['reviews'][0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(app['reviews'])
