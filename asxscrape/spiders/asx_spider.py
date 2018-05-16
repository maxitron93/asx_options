import scrapy

class AsxSpider(scrapy.Spider):
    name = "asx_spider"
    
    def start_requests(self):

        companies = ["AGL", "ALL", "AM8", "AMC", "AMP", "AN8", "ANN", "ANZ", "AP8", "APA", "AR8", "ASX", "AWC", "AZJ", "BEN", "BH8", "BHP", "BLD", "BOQ", "BSL", "BX8", "BXB", "CB8", "CBA", "CCL", "CIM", "CPU", "CS8", "CSL", "CSR", "CTX", "CU8", "CWN", "CYB", "DX8", "FLT", "FM8", "FMG", "FXJ", "GM8", "GMG", "GP8", "GPT", "HVN", "IA8", "IAG", "IFL", "IL8", "ILU", "IPL", "JH8", "JHX", "LL8", "LLC", "MG8", "MGR", "MPL", "MQ8", "MQG", "MTS", "MYR", "NA8", "NAB", "NC8", "NCM", "OI8", "OR8", "ORG", "ORI", "OS8", "OSH", "OZL", "QA8", "QAN", "QBE", "RH8", "RHC", "RI8", "RIO", "RRL", "S32", "SC8", "SCG", "SEK", "SG8", "SGM", "SGP", "SGR", "SHL", "ST8", "STO", "STW", "SUN", "SY8", "SYD", "TAH", "TC8", "TCL", "TL8", "TLS", "TW8", "TWE", "VC8", "VCX", "WB8", "WBC", "WES", "WF8", "WFD", "WO8", "WOR", "WOW", "WPL", "XJO"]

        for company in companies:
            url = "https://www.asx.com.au/asx/markets/optionPrices.do?by=underlyingCode&underlyingCode=%s&expiryDate=&optionType=" % company
            
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        first_letter = list(response.url)[-27]
        second_letter = list(response.url)[-26]
        third_letter = list(response.url)[-25]
        company_name = (first_letter + second_letter + third_letter)
        filename = "Options-%s.html" % company_name
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log("saved file %s" % filename)

# run python -m scrapy crawl asx_spider from /asxscrape directory