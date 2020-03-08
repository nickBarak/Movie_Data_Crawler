from scrapy.exceptions import DropItem
import psycopg2
import os

class MovieDataPipeline(object):
    def __init__(self):
        self.checked_titles = set()

    def open_spider(self, spider):
        hostname = 'localhost'
        username = os.environ.get('PG_USERNAME')
        password = os.environ.get('PG_PASSWORD')
        database = 'Choosie'
        
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if (item['src_url'] in self.checked_titles):
            raise DropItem(f'Dropped duplicate \"{item["title"]}\"')

        else:
            self.checked_titles.add(item['src_url'])
            try:
                query = 'INSERT INTO movie_data (src_url, title, genres, mpaa_rating, directors, writers, actors, release_date, duration_in_mins, countries, languages, description, cover_file) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                
                data = (item["src_url"], item["title"], item["genres"], item["mpaa_rating"], item["directors"], item["writers"], item["actors"], item["release_date"], item["duration_in_mins"], item["countries"], item["languages"], item["description"], item["cover_file"])

                # self.cur.mogrify(query, data)
                self.cur.execute(query, data)
                self.connection.commit()
            except:
                self.connection.rollback()

            return item