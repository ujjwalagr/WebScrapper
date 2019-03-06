import scrapy

class ScrapeNaukriDotComItems(scrapy.Item):

    #Describing the fields required
    job_title = scrapy.Field()
    exp_req = scrapy.Field()
    location = scrapy.Field()
    company_name = scrapy.Field()
    links_detail = scrapy.Field()
    keyskills = scrapy.Field()
    job_desc = scrapy.Field()
    salary = scrapy.Field()
    posted_by = scrapy.Field()
    posted_on = scrapy.Field()
