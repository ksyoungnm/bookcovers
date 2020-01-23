import scrapy

class DataSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
            "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_72%3A1250224011&s=review-count-rank&dc&fst=as%3Aoff&qid=1579803456&rnid=1250219011&ref=sr_st_review-count-rank",
            ]

    def parse(self, response):
       for cover in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-image", " " ))]/@src'):
           yield {
                   'cover': cover.get(),
                   }

       for rating in response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "aok-align-bottom", " " ))]'):
           processing = rating.get()
           index = processing.index("<span class=\"a-icon-alt\">") + 25
           yield {
                    'rating': rating.get()[index:-11],
                    }

       next_page = response.css('li.a-last a::attr(href)').get()
       if next_page is not None:
           next_page = response.urljoin(next_page)
           yield scrapy.Request(next_page, callback=self.parse)

