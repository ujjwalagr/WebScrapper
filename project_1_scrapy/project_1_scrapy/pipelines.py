class NullFixPipeline(object):
    def process_item(self, item, spider):
        
        #Processing the field filtering the data properly
        try:
            item['job_title'] = item['job_title'][0].strip().title() 
        except KeyError:
            raise print("No Job Found")
        try:
            item['exp_req'] = item['exp_req'][0].strip().title()
        except KeyError:
            item['exp_req'] = 'N/A'

        try:
            item['company_name'] =  item['company_name'][0].strip().title()
        except KeyError:
            item['company_name'] = 'N/A'

        try:
            item['links_detail'] = item['links_detail'][0].strip()
        except KeyError:
            item['links_detail'] = 'N/A'

        try:
            item['keyskills'] = item['keyskills'][0].title().replace("...","").strip()
        except KeyError:
            item['keyskills'] = 'N/A'

        try:
            item['job_desc'] = item['job_desc'][0].title()
            temp = item['job_desc'].replace("-","",1)
            item['job_desc'] = temp.replace("...","").strip()
        except KeyError:
            item['job_desc'] = 'N/A'

        try:
            item['salary'] = item['salary'][0].strip().title()
        except KeyError:
            item['salary'] = 'N/A'

        try:
            item['posted_by'] = item['posted_by'][0].strip()
        except KeyError:
            item['posted_by'] = 'N/A'

        try:
            item['posted_on'] = item['posted_on'][0].strip()
        except KeyError:
            item['posted_on'] = 'N/A'
        return item
