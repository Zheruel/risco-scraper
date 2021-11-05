from utils.input_parser import parse_string_input
from services.scraping_service import scrape_cui

cui_list = parse_string_input('input/cui_input.txt')

for cui in cui_list:
    scrape_cui(cui)
