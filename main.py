# writing to csv dictionaries

import csv

mydict =[{'Journal title': 'Oncology', 'ISSN': '1234-4321', 'Year': '2021', 'Total pdf downloads': '999'},
        {'Journal title': 'Lung cancer', 'ISSN': '3333-4444', 'Year': '2021', 'Total pdf downloads': '657'},
        {'Journal title': 'Palliative care', 'ISSN': '4532-7896', 'Year': '2021', 'Total pdf downloads': '345'},
        {'Journal title': 'Ovarian cancer', 'ISSN': '9854-3765', 'Year': '2021', 'Total pdf downloads': '475'}]

fields = ['Journal title', 'ISSN', 'Year', 'Total pdf downloads']

filename = "journalusage.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)
