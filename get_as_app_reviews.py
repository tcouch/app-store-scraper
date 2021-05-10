import csv

from app_store_scraper import AppStore

# Change this to the name of the csv file containing your app metadata
# requires "url_name" and "id" fields
IN_FILE = 'as_eating_disorder_apps.csv'

# read app name and id from csv file
apps = []
with open(IN_FILE,newline='',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
    apps.append({'app_name':row['url_name'],'app_id':row['id']})

# for each app, use the AppStore scraper to fetch all reviews
for app in apps:
    app_temp = AppStore(country='gb', app_name=app['app_name'], app_id=app['app_id']) 
    app_temp.review()
    app['reviews'] = app_temp.reviews # save list of reviews to existing dictionary

# save reviews to separate csv files for each app
for app in apps:
    if app.get('reviews'): # Not all apps have reviews
        outfile = app['app_name'] + '_reviews.csv' # use the app_name to name the output file
        with open(outfile,'w',encoding='utf-8',newline='') as file:
            # Needed to add developerResponse by hand as only some reviews have this field
            dict_writer = csv.DictWriter(file, list(app['reviews'][0].keys()) + ['developerResponse'])
            dict_writer.writeheader()
            dict_writer.writerows(app['reviews'])