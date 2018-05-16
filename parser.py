from bs4 import BeautifulSoup
import csv

all_companies = []
company_codes = ["AGL", "ALL", "AM8", "AMC", "AMP", "AN8", "ANN", "ANZ", "AP8", "APA", "AR8", "ASX", "AWC", "AZJ", "BEN", "BH8", "BHP", "BLD", "BOQ", "BSL", "BX8", "BXB", "CB8", "CBA", "CCL", "CIM", "CPU", "CS8", "CSL", "CSR", "CTX", "CU8", "CWN", "CYB", "DX8", "FLT", "FM8", "FMG", "FXJ", "GM8", "GMG", "GP8", "GPT", "HVN", "IA8", "IAG", "IFL", "IL8", "ILU", "IPL", "JH8", "JHX", "LL8", "LLC", "MG8", "MGR", "MPL", "MQ8", "MQG", "MTS", "MYR", "NA8", "NAB", "NC8", "NCM", "OI8", "OR8", "ORG", "ORI", "OS8", "OSH", "OZL", "QA8", "QAN", "QBE", "RH8", "RHC", "RI8", "RIO", "RRL", "S32", "SC8", "SCG", "SEK", "SG8", "SGM", "SGP", "SGR", "SHL", "ST8", "STO", "STW", "SUN", "SY8", "SYD", "TAH", "TC8", "TCL", "TL8", "TLS", "TW8", "TWE", "VC8", "VCX", "WB8", "WBC", "WES", "WF8", "WFD", "WO8", "WOR", "WOW", "WPL", "XJO"]

for company_code in company_codes:
    with open("Options-%s.html" % company_code) as html_file:
        soup = BeautifulSoup(html_file, "lxml")

    options_table = soup.find(id="optionstable")
    options_data = options_table.find_all("td")

    # Remove the headings from the table
    temp_array = options_table.find_all("th")
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)
    temp_array.pop(0)


    # Creates an array called codes to contain all the options codes
    codes = [] 
    for code in temp_array:
        code = code.text
        codes.append(code)

    # Creates an array of array, with each inner array represnting one row of the table
    temp_table_array = []
    row_array = []
    counter = 1
    for data in options_data:
        data = data.text
        if counter < 9:
            row_array.append(data)
            counter += 1
        else:
            row_array.pop(-2)
            temp_table_array.append(row_array)
            row_array = []
            counter = 1

    # Joins the code array and row_array to create the final array with all the row information on one row
    table_array = []
    counter = 0
    for row in temp_table_array:
        row.insert(0, codes[counter])
        table_array.append(row)
        counter += 1
    
    #Creates an array for all companies
    all_companies.append(table_array)

# Creates the CSV
with open("mycsv.csv", "w", newline="") as f:
    thewriter =csv.writer(f)
    
    thewriter.writerow(["Code", "Expiry Date", "P/C", "Exercise", "Bid", "Offer", "Last", "Open Interest"])

    for company in all_companies:
        for row in company:
            thewriter.writerow(row)