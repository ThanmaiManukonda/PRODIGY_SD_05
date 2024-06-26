import requests
from bs4 import BeautifulSoup
import csv

def scrape_walmart_products():
    url = "https://www.walmart.com/browse/shop-grocery/pet-food/5438_426265"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []

    for product in soup.find_all("div", class_="search-result-gridview-item"):
        name = product.find("a", class_="product-title-link").text.strip()
        price = product.find("span", class_="price-group").text.strip()
        rating = product.find("span", class_="visuallyhidden").text.strip() if product.find("span", class_="visuallyhidden") else "N/A"

        products.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })

    return products

def save_to_csv(products):
    with open("walmart_products.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name", "Price", "Rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == "__main__":
    print("Scraping Walmart Products...")
    products = scrape_walmart_products()
    print(f"Found {len(products)} products.")
    print("Saving data to CSV file...")
    save_to_csv(products)
    print("Data saved successfully.")
