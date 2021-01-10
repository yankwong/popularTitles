
# https://api.ebay.com/buy/browse/v1/item_summary/search?q=drone&limit=3
# api doc: https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search#h2-samples
import scraper
import parser
import language

keyword = ''
total_page = 1

def prompt_for_info() -> None:
    global keyword
    keyword = input(language.ASK_FOR_KEYWORD)
    global total_page
    total_page= input(language.ASK_FOR_TOTAL_PAGE)


def get_titles():
    page_soup = parser.get_page_soup(scraper.scrape(keyword, total_page))
    

if __name__ == '__main__':
    prompt_for_info()
    get_titles()


