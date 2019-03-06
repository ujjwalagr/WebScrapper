import scrapy
from project_1_scrapy.items import ScrapeNaukriDotComItems
from scrapy.loader import ItemLoader


class DataAnalyticsJob(scrapy.Spider):

    # spider name
    name = 'spider_naukri_dot_com'

    # crawl url
    start_urls = ['https://www.naukri.com/data-analytics-jobs-in-delhi-ncr']

    # response parser function
    def parse(self, response):

        all_jobs = response.css('.row')

        # Keys of the fields required
        job_title = "job_title"
        exp_req = "exp_req"
        location = "location"
        company_name = 'company_name'
        links_detail = 'links_detail'
        keyskills = 'keyskills'
        job_desc = 'job_desc'
        salary = 'salary'
        posted_by = 'posted_by'
        posted_on = 'posted_on'

        # Fetching the rows
        for jobs in all_jobs:
            get_job_loader = ItemLoader(
                ScrapeNaukriDotComItems(), selector=jobs)
            try:
                # Scraping the fields using their HTML attributes
                get_job_loader.add_css(job_title, '.desig::text')
                get_job_loader.add_css(exp_req, 'span.exp::text')
                get_job_loader.add_css(location, 'span.loc span::text')
                get_job_loader.add_css(company_name, 'span.org::text')
                get_job_loader.add_css(links_detail, '.content::attr(href)')
                get_job_loader.add_css(keyskills, 'span.skill::text')
                get_job_loader.add_css(job_desc, 'span.desc::text')
                get_job_loader.add_css(salary, 'span.salary::text')
                get_job_loader.add_css(posted_by, 'a.rec_name.active::text')
                get_job_loader.add_css(
                    posted_on, 'div.rec_details span.date::text')
            except:
                continue
            yield get_job_loader.load_item()
