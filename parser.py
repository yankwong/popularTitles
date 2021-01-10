import json
from bs4 import BeautifulSoup

rarity_translator = {
    1: '★',
    2: '★★',
    3: '★★★',
    4: '★★★★',
    5: '★★★★★',
}


def get_page_soup(page_content: str):
    return BeautifulSoup(page_content, 'html.parser')


def get_total_rarity(tier_list_json, target_rarity) -> int:
    total = 0
    all_rarities = tier_list_json.find_all('span', class_='star-rarity')

    for rarity in all_rarities:
        if rarity.text == rarity_translator[target_rarity]:
            total += 1
    return total


def get_servant_type(tier_list_json, servant_type) -> int:
    total = 0
    all_servant_types = tier_list_json.select('.FGOTierNPInfo > div')

    for s_type in all_servant_types:
        if s_type.text == servant_type:
            total += 1
    return total
