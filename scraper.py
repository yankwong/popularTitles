import requests


def generate_url(search_keyword: str, page) -> str:
    return f"""https://www.ebay.com/sch/i.html?_from=R40
            &_trksid=p2380057.m570.l1313
            &_sacat=0
            &_nkw={search_keyword.replace(' ', '+')}
            &_pgn={page}"""


def scrape(keyword, page=1) -> [str]:
    listings = []

    for index in range(page):
        url = generate_url(keyword, index+1)
        listing = requests.get(url)
        listings.append(listing.content)

    return listings
