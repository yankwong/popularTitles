from bs4 import BeautifulSoup


def get_page_soup(page_content: str):
    return BeautifulSoup(page_content, 'html.parser')


def get_item_titles(page_soup):
    titles = []
    title_elements = page_soup.find_all('h3', class_='s-item__title')

    for title_element in title_elements:
        titles.append(title_element.text)

    return titles
