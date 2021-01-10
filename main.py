import scraper
import parser
import user_io
from pprint import pprint


def get_titles(search_word: str, page_total: str):
    page_soups = parser.get_page_soups(scraper.scrape(search_word, int(page_total)))
    pprint(parser.get_item_titles(page_soups))


if __name__ == '__main__':
    keyword = user_io.prompt_for_keyword()
    total_page = user_io.prompt_for_page()
    user_io.print_loading_msg()
    get_titles(keyword, total_page)
    user_io.print_done_msg()
