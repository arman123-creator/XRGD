import requests
from bs4 import BeautifulSoup

def scrape_brown_dwarfs():
    url = 'https://en.wikipedia.org/wiki/Brown_dwarf'  # URL of the Wikipedia page for Brown Dwarf stars
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the table for Field brown dwarfs (the third table on the Wikipedia page)
            tables = soup.find_all('table', {'class': 'wikitable'})
            if len(tables) >= 3:
                field_brown_dwarfs_table = tables[2]
                rows = field_brown_dwarfs_table.find_all('tr')

                brown_dwarf_data = []

                # Assuming the table structure has the header row (th) and data rows (td)
                header_row = rows[0].find_all('th')
                column_names = [header.text.strip() for header in header_row]

                for row in rows[1:]:
                    columns = row.find_all('td')
                    if len(columns) >= len(column_names):
                        name = columns[0].text.strip()
                        distance = columns[1].text.strip()
                        mass = columns[2].text.strip()
                        radius = columns[3].text.strip()
                        temperature = columns[4].text.strip()
                        luminosity = columns[5].text.strip()

                        brown_dwarf_data.append({
                            'Name': name,
                            'Distance': distance,
                            'Mass': mass,
                            'Radius': radius,
                            'Temperature': temperature,
                            'Luminosity': luminosity,
                        })

                return brown_dwarf_data

            else:
                print("Table not found on the Wikipedia page.")
                return None

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    brown_dwarfs = scrape_brown_dwarfs()
    if brown_dwarfs:
        for star in brown_dwarfs:
            print(star)
    else:
        print("No data retrieved.")
