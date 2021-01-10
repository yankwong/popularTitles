from bs4 import BeautifulSoup


def get_page_soups(listings_array: [str]):
    page_soups = []
    for listing in listings_array:
        page_soups.append(BeautifulSoup(listing, 'html.parser'))

    return page_soups


def get_item_titles(page_soups):
    titles = []
    for page_content in page_soups:
        title_elements = page_content.find_all('h3', class_='s-item__title')

        for title_element in title_elements:
            titles.append(title_element.text)

    return titles
