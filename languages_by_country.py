# languages_by_country.py

import json

# Sample data: Dictionary of countries and their official languages
languages = {
    "United States": ["English"],
    "Canada": ["English", "French"],
    "Germany": ["German"],
    "Spain": ["Spanish"],
    "Switzerland": ["German", "French", "Italian", "Romansh"],
    "India": ["Hindi", "English"],
    "Brazil": ["Portuguese"],
    "Japan": ["Japanese"],
    "Russia": ["Russian"],
    "China": ["Mandarin"],
}

# Function to display official languages by country
def get_languages_by_country(country):
    country = country.title()
    if country in languages:
        print(f"Official language(s) of {country}: {', '.join(languages[country])}")
    else:
        print(f"Sorry, no data available for {country}.")

# Main function to prompt the user for a country
def main():
    print("Languages by Country - Find Official Languages")
    while True:
        country = input("Enter the name of the country (or 'exit' to quit): ")
        if country.lower() == 'exit':
            print("Goodbye!")
            break
        get_languages_by_country(country)

if __name__ == "__main__":
    main()
