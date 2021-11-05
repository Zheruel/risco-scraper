from requests import Session
from bs4 import BeautifulSoup
from models.comapny import Company
from utils.csv_exporter import save_company_to_csv


def scrape_cui(cui: str) -> None:
    ses = Session()
    company_page_link = None

    response = ses.get("https://www.risco.ro/verifica-firma/cautare/cui={0}".format(cui))
    soup = BeautifulSoup(response.content, 'html.parser')

    company_page_div = soup.find('div', {'class': 'bb_search'})

    if company_page_div:
        company_page_link = company_page_div.find('a', href=True)['href']

    if company_page_link:
        response = ses.get("https://www.risco.ro{0}".format(company_page_link))
        soup = BeautifulSoup(response.content, 'html.parser')

        legal_name = soup.find('span', {'itemprop': 'legalName'})
        telephone = soup.find('td', {'itemprop': 'telephone'})

        if legal_name and telephone:
            print("Company {0} with cui {1} has been scraped".format(legal_name.text, cui))

            save_company_to_csv(Company(legal_name.text, cui, telephone.text))
        else:
            print("Company with cui {0} has not been scraped".format(cui))