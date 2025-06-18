import openpyxl
import requests

# Load Excel workbook
file_path = 'data.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb['Sheet1']

# Keyword to search
keyword = "John"

# Loop through rows and search for keyword
for row in ws.iter_rows(min_row=2):  # Skip header
    name_cell = row[0]
    if keyword.lower() in str(name_cell.value).lower():
        # Prepare payload from the row
        payload = {
            "name": row[0].value,
            "field1": row[1].value,
            "field2": row[2].value,
            "field3": row[3].value,
        }

        # Send to API
        response = requests.post("https://your-api-url.com/endpoint", json=payload)

        # Save response in Column E
        row[4].value = response.text
        print(f"Data sent for {row[0].value} | Response: {response.text}")
        break  # Remove break if you want to match multiple rows

# Save updated workbook
wb.save(file_path)
print("Excel file updated.")
