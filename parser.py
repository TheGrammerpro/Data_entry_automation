from bs4 import BeautifulSoup


class SoupParser:
    def __init__(self, website_contents):
        self.soup = BeautifulSoup(website_contents, 'html.parser')
        self.addresses = []
        self.prices = []
        self.links = []

    def get_addresses(self):
        address_tags = self.soup.find_all(name="address")
        for tag in address_tags:
            address = tag.get_text().strip()
            self.addresses.append(address)
        return self.addresses

    def get_prices(self):
        price_tags = self.soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        for tag in price_tags:
            if "+" in tag.get_text():
                price_text = tag.get_text().split("+")[0]
            else:
                price_text = tag.get_text().split("/")[0]
            self.prices.append(price_text)
        return self.prices

    def get_links(self):
        link_tags = self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
        for tag in link_tags:
            self.links.append(tag.get("href"))
        return self.links
