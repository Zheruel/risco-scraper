from models.comapny import Company
from csv import writer
from pathlib import Path


def save_company_to_csv(company: Company):
    file = Path("output/companies.csv")
    write_header = False

    if not file.exists():
        write_header = True

    with open("output/companies.csv", "a") as file:
        csv_writer = writer(file)

        if write_header:
            csv_writer.writerow(["name", "cui", "phone number"])

        csv_writer.writerow([company.name, company.cui, company.phone_number])
