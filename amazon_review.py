import scrapy


# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
    # Spider name
    name = 'amazon_reviews'

    # Domain names to scrape
    allowed_domains = ['amazon.in']

    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/Samsung-MicroSDXC-Memory-Adapter-MB-MC128GA/product-reviews/B06Y63ZKLS/ref=cm_cr_arp_d_paging_btm_next_501?ie=UTF8&reviewerType=all_reviews&pageNumber="
    #   myBaseUrl = "https://www.amazon.in/Butterfly-EKN-1-5-Litre-Kettle-Silver/product-reviews/B078V8R9BS/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&amp%3Bamp%3B&pageNumber="
    #   myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;amp;reviewerType=all_reviews&amp;amp;pageNumber="
    start_urls = []

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1, 501):
        start_urls.append(myBaseUrl + str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css('#cm_cr-review_list')

        # Collecting product star ratings
        star_rating = data.css('.review-rating')
        review_title = response.css('.a-text-bold span')
        review_date = response.css('.review-date')


        # Collecting user reviews
        comments = data.css('.review-text-content')
        count = 0

        # Combining the results
        for review in star_rating:
            yield {'stars': ''.join(review.xpath('.//text()').extract()),
                   'comment': ''.join(comments[count].xpath(".//text()").extract()),
                   'title': ''.join(review_title[count].css('::text').extract()),
                   'review_date': ''.join(review_date[count].css('::text').extract())
                   }
            count = count + 1



import pandas as pd
reviews= pd.read_csv("reviews.csv")
reviews=reviews["comment"]

rev=" ".join(reviews)
print(rev)

