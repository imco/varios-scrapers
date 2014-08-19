# Scrapy settings for sep_pdf project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
DEPTH_LIMIT = 1
BOT_NAME = 'sep_pdf'

SPIDER_MODULES = ['sep_pdf.spiders']
NEWSPIDER_MODULE = 'sep_pdf.spiders'

ITEM_PIPELINES = ['sep_pdf.pipelines.MongoDBPipeline',]
 
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "sep_pdf_list"
MONGODB_COLLECTION = ""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sep_pdf (+http://www.yourdomain.com)'
