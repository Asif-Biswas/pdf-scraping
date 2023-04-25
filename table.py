"""
I have a PDF file with a table in it. I want to extract the table and save it as a JSON file.
The PDF file name is 'table.pdf' and the JSON file name will be 'table.json'.
There are some text before and after the table in the PDF file.
"""

import camelot
import json

# read the pdf file
tables = camelot.read_pdf('table.pdf', pages='all')

for i, table in enumerate(tables):
    # convert the table to JSON
    table_json = table.df.to_json(orient='records')
    # save the JSON to a file
    with open('table{}.json'.format(i), 'w') as f:
        f.write(table_json)

    