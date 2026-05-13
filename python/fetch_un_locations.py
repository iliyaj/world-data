import requests
import csv
import json

# API endpoint
base_url = "https://population.un.org/dataportalapi/api/v1/locations"

all_locations = []
page = 1

print("Fetching all UN locations...")

while True:
    # Fetch current page
    url = f"{base_url}?pageNumber={page}&pageSize=100&sort=id"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract locations from this page
        locations = data.get('data', [])
        all_locations.extend(locations)

        print(f"Page {page}: Fetched {len(locations)} locations (Total: {len(all_locations)})")

        # Check if there are more pages
        if data.get('pageNumber') >= data.get('pages'):
            break

        page += 1

    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        break

# Write to CSV
output_file = "data/un_locations.csv"
print(f"\nWriting {len(all_locations)} locations to {output_file}...")

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'parentId', 'iso3', 'iso2', 'name', 'locationType', 'locationTypeId', 'longitude', 'latitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for location in all_locations:
        writer.writerow({
            'id': location.get('id', ''),
            'parentId': location.get('parentId', ''),
            'iso3': location.get('iso3', ''),
            'iso2': location.get('iso2', ''),
            'name': location.get('name', ''),
            'locationType': location.get('locationType', ''),
            'locationTypeId': location.get('locationTypeId', ''),
            'longitude': location.get('longitude', ''),
            'latitude': location.get('latitude', '')
        })

print(f"Done! Saved to {output_file}")
print(f"Total locations: {len(all_locations)}")
