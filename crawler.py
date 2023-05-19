from datetime import date
from icrawler.builtin import FlickrImageCrawler

flickr_crawler = FlickrImageCrawler('17d082f450af18012ae480394dbd0883', storage={'root_dir': 'D:\Education\Hacaton\Small'})
flickr_crawler.crawl(max_num=2700, text="""Bewick's swan""", max_size=(4096, 3072))