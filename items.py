import scrapy
from scrapy import Field

class MovieDataItem(scrapy.Item):
    src_url = Field()
    title = Field()
    genres = Field()
    mpaa_rating = Field()
    directors = Field()
    writers = Field()
    actors = Field()
    release_date = Field()
    duration_in_mins = Field()
    countries = Field()
    languages = Field()
    description = Field()
    cover_file = Field()

