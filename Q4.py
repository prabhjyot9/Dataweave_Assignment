url_list = input("Enter URLs separated by commas: ").split(", ")
zipcode_list = input("Enter Zip Codes separated by commas: ").split(", ")

for zip_code in zipcode_list:
    filename = f"{zip_code}_input"
    
    with open(filename, 'w') as file:
        for url in url_list:
            url_with_zip = f"{url}#{zip_code}"
            entry = {"url": url_with_zip, "zip": zip_code}
            file.write(str(entry) + '\n'),