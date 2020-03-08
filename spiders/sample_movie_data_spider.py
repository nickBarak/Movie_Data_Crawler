import scrapy
from movie_data.items import MovieDataItem
from scrapy import Spider, Request
import re

class MovieDataSpider(Spider):
    name = 'sample_movie_data_spider'
    allowed_domains = ['imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=adventure&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=animation&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=biography&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=crime&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=documentary&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=drama&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=family&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=fantasy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=film-noir&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=history&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=music&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=musical&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=mystery&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=romance&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=short&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=sport&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=superhero&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=thriller&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=war&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1',
        'https://www.imdb.com/search/title/?genres=western&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=V1DCQWZTMKDAXM1E3041&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1'
    ]

    def parse(self, response):
        split_url = self.split(response.url)
        genre = self.find_vars(response, split_url)
        linkgen = self.linkgen(response)
        for link in range(50):
            next_title = linkgen.__next__()
            yield response.follow(next_title, callback=self.store_record)

    def split(self, string): return list(string)

    def find_vars(self, response, url):
        checked_chars = []
        genre_chars = []
        start_nums = []
        for char in url:
            checked_chars.insert(0, char)
            if (''.join(reversed(checked_chars[0:7])) == 'genres='):
                for genre_char in url[len(checked_chars):]:
                    if (genre_char is not '&'):
                        genre_chars.append(genre_char)
                    else:
                        for start_num in url[len(checked_chars) + len(genre_chars) + 7:]:
                            if (start_num in self.split('0123456789')):
                                start_nums.append(start_num)
                            else:
                                break
                        break
        if (start_nums):
            return ''.join(genre_chars), int(''.join(start_nums))
        else:
            return ''.join(genre_chars)

    def linkgen(self, response):
        for link in response.css('.lister-list .lister-item .lister-item-content .lister-item-header a::attr(href)').getall():
            yield response.urljoin(link)        

    def store_record(self, response):
        item = MovieDataItem()

        features = [
            'title',
            'genres',
            'mpaa_rating',
            'directors',
            'writers',
            'actors',
            'release_date',
            'duration_in_mins',
            'countries',
            'languages',
            'description',
            'cover_file'
        ]

        controls = {
            'title': response.css('div.title_wrapper h1::text').get(),
            'genres': response.css('#titleStoryLine div.see-more.inline.canwrap a[href*="/search/title?genres="]::text').getall(),
            'mpaa_rating': response.css('div.title_wrapper .subtext::text').get(),
            'directors': response.css('.plot_summary div.credit_summary_item:nth-child(2) a::text').getall(),
            'writers': response.css('.plot_summary div.credit_summary_item:nth-child(3) a::text').getall(),
            'actors': response.css('table.cast_list td.primary_photo img::attr(alt)').getall(),
            'release_date': response.css('.title_wrapper .subtext [title*="release dates"]::text').get(),
            'duration_in_mins': response.css('#titleDetails div.txt-block time[datetime]::text').get(),
            'countries': response.css('#titleDetails .txt-block a[href*="country_of_origin"]::text').getall(),
            'languages': response.css('#titleDetails .txt-block a[href*="primary_language"]::text').getall(),
            'description': response.css('#titleStoryLine div.inline.canwrap p span::text').get(),
            'cover_file': response.css('.title-overview .poster a img:last-child').get()
        }
        
        for feature in features:
            if (not controls[feature]):
                if (feature != 'title' and feature != 'duration_in_mins' and feature != 'release_date'):
                    item[feature] = 'Not available'
                else:
                    if feature == 'duration_in_mins':
                        item[feature] = 0
                    elif feature == 'release_date':
                        item[feature] = '1 January 3000'
                    else: pass
            else:
                if feature == 'title':
                    if re.findall(r'(.*?)\xa0', controls[feature]):
                        item[feature] = re.findall(r'(.*?)\xa0', controls[feature])[0]
                elif feature == 'genres':
                    try:
                        item[feature] = controls[feature]
                        for (i, genre) in enumerate(item[feature]):
                            item[feature][i] = re.findall(r'\s(\w*)', item[feature][i])[0]
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'mpaa_rating':
                    try:
                        item[feature] = re.findall(r'\w\w?-?\w?\w?', controls[feature])[0]
                    except:
                        item[feature] = 'Not available'
                    finally:
                        if not item[feature]:
                            item[feature] = 'Not available'
                elif feature == 'directors':
                    try:
                        item[feature] = controls[feature]
                        for i in item[feature]:
                            if i == 'See full cast & crew':
                                item[feature].pop()
                            elif re.findall(r'\d', i):
                                item[feature].pop()
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'writers':
                    try:
                        item[feature] = controls[feature]
                        for i in item[feature]:
                            if i == 'See full cast & crew':
                                item[feature].pop()
                            elif re.findall(r'\d', i):
                                item[feature].pop()
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'actors':
                    try:
                        item[feature] = controls[feature]
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'release_date':
                    try:
                        item[feature] = ''.join(re.findall(r'(\d\d?\s)(.*?)\s\(', controls[feature])[0])
                    except:
                        item[feature] = controls[feature]
                    finally:
                        if not item[feature]:
                            item[feature] = '1 January 3000'
                        else:
                            if len(self.split(item[feature])) == 4 or re.findall(r'\d\s(\w*?)\s', item[feature]):
                                if len(self.split(item[feature])) == 4 or re.findall(r'\d\s(\w*?)\s', item[feature])[0] not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                                    if re.findall(r'\d\d\d\d', str(item[feature])):
                                        if re.findall(r'\d\d\d\d', str(item[feature])):
                                            item[feature] = '1 January ' + re.findall(r'\d\d\d\d', str(item[feature]))[0]
                                    else:
                                        item[feature] = '1 January 3000'
                elif feature == 'duration_in_mins':
                    try:
                        item[feature] = int(re.findall(r'(\d*?)\s', controls[feature])[0])
                    except:
                        item[feature] = 0
                    finally:
                        if not item[feature]:
                            item[feature] = 0
                elif feature == 'countries':
                    try:
                        item[feature] = controls[feature]
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'languages':
                    try:
                        item[feature] = controls[feature]
                    except:
                        item[feature] = ['Not available']
                    finally:
                        if not item[feature]:
                            item[feature] = ['Not available']
                elif feature == 'description':
                    try:
                        item[feature] = re.findall(r'\s(\w.*)', controls[feature])[0]
                    except:
                        item[feature] = 'Not available'
                    finally:
                        if not item[feature]:
                            item[feature] = 'Not available'
                else:
                    try:
                        item[feature] = re.findall(r'src="(.*)"', controls[feature])[0]
                    except:
                        item[feature] = 'Not available'
                    finally:
                        if not item[feature]:
                            item[feature] = 'Not available'

        item['src_url'] = response.url
        return item