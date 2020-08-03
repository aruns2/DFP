# Data Focused Python
# 95-888-C3
# HW2 Team 3
# Smith_Colton, coltons@andrew.cmu.edu
# Sharma_Arun, aruns2@andrew.cmu.edu

input_file = open(r"C:\Users\sharm\Desktop\CMU\Sem2\Python\cme.20200117.c.pa2\cme.20200117.c.pa2", 'rt', encoding='utf-8')
output_file = open(r"C:\Users\sharm\Desktop\CMU\Sem2\Python\test1.txt", 'wt', encoding='utf-8')
lines_num = 0

# Filter rows and append to table strings
# Create table strings
table_1 = str()
table_2 = str()

# Start Filtering
for line in input_file:
    # Filter B rows
    if 'B' in line[:2] :
        # Create row attributes
        commodity_code = line[5:7] # futures code
        product_type = line[15:18] # contract type
        contract_month = line[18:24] # contract month
        expiration_date = line[91:99] # fut exp date

        # Do not include contract months earlier than 2020-03, or later than 2021-12.
        if 202003 <= int(contract_month) <= 202112:
            # Create 'CL' rows
            if 'CL ' in line[5:8]:
                output_str = "{:8s}{:10s}{:10s}{:12s}{:10s}{:8s}\n".format(commodity_code,
                                                                           contract_month[:4] + '-' + contract_month[4:],
                                                                           product_type.lower().capitalize(),
                                                                           expiration_date[:4] + '-' + expiration_date[4:6] + '-' + expiration_date[6:],
                                                                           '',
                                                                           '')
                table_1 += output_str
                
   
            # Create 'LO' rows
            elif 'LO' in line[5:7]:
                output_str = "{:8s}{:10s}{:10s}{:12s}{:10s}{:8s}\n".format("CL",
                                                                            contract_month[:4] + '-' + contract_month[4:],
                                                                            "Opt",
                                                                            '',
                                                                            commodity_code,
                                                                            expiration_date[:4] + '-' + expiration_date[4:6] + '-' + expiration_date[6:])
                table_1 += output_str

    # Filter 81-type rows
    elif '81' in line[:2] :
        # Create row attributes
        commodity_code = line[5:7]  # futures code
        product_type = line[25:28]  # contract type
        contract_month = line[29:35]  # contract month
        settlement_price = line[108:122]  # settlement price

        # Do not include contract months earlier than 2020-03, or later than 2021-12.
        if 202003 <= int(contract_month) <= 202112:
            if 'CL ' in line[5:8]:
                output_str = "{:8s}{:10s}{:10s}{:8s}{:10.2f}\n".format(commodity_code,
                                                                     contract_month[:4] + '-' + contract_month[4:],
                                                                     product_type.capitalize(),
                                                                     "",
                                                                     int(settlement_price) / 100)
                table_2 += output_str

            elif "LO" in line[5:7] and 'OOFP' in line[25:29]:
                strike_price = line[47:54]
                output_str = "{:8s}{:10s}{:10s}{:8.2f}{:10.2f}\n".format('CL',
                                                                     contract_month[:4] + '-' + contract_month[4:],
                                                                     'Put',
                                                                     int(strike_price) / 100,
                                                                     int(settlement_price) / 100)
                table_2 += output_str

            elif "LO" in line[5:7] and 'OOFC' in line[25:29]:
                strike_price = line[47:54]
                output_str = "{:8s}{:10s}{:10s}{:8.2f}{:10.2f}\n".format('CL',
                                                                     contract_month[:4] + '-' + contract_month[4:],
                                                                     'Call',
                                                                     int(strike_price) / 100,
                                                                     int(settlement_price) / 100)
                table_2 += output_str

# Make table 1 headers
header_1 = "{:8s}{:10s}{:10s}{:12s}{:10s}{:8s}\n".format('Futures', 'Contract', 'Contract', 'Futures', 'Options', 'Options')
header_2 = "{:8s}{:10s}{:10s}{:12s}{:10s}{:8s}\n".format('Code', 'Month', 'Type', 'Exp Date', 'Code', 'Exp Date')
header_3 = "{:8s}{:10s}{:10s}{:12s}{:10s}{:8s}\n".format('-' * 6, '-' * 8, '-' * 6, '-' * 8, '-' * 6, '-' * 8)

# Write table 1 headers to file
output_file.write(header_1 + header_2 + header_3)

# Write table 1 strings to file
output_file.write(table_1)
output_file.write("\n")

# Make table 2 headers
header_1 = "{:8s}{:10s}{:10s}{:8s}{:10s}\n".format('Futures', 'Contract', 'Contract', 'Strike', 'Settlement')
header_2 = "{:8s}{:10s}{:10s}{:8s}{:10s}\n".format('Code', 'Month', 'Type', 'Price', 'Price')
header_3 = "{:8s}{:10s}{:10s}{:8s}{:10s}\n".format('-' * 6, '-' * 8, '-' * 6, '-' * 6, '-' * 10)

# Write table 2 headers to file
output_file.write(header_1 + header_2 + header_3)

# Write table 2 strings to file
output_file.write(table_2)

# Close file writer
output_file.close()
input_file.close()