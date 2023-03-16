import requests
import bs4
from bs4 import BeautifulSoup
from ItemObj import ItemObj

class Amazon:
    def __init__(self,itemName:str) -> None:
        #Predefine params for souping tags
        self.datacomptype='s-search-result'
        self.span_price='a-price-whole'
        
        self.itemName=itemName
        self.itemPage:BeautifulSoup=BeautifulSoup(
            self.getPage(self.getSearchLink()),'html.parser'
            )
        self.itemList=self.getList()

    def __str__(self):
        s="\n".join([str(x) for x in self.itemList])
        return s

    def getSearchLink(self):
        return f'https://www.amazon.in/s?k={self.itemName}'
    
    def getPage(self,link:str):
        return requests.get(link).content
    
    def getList(self):
        item_cards=self.itemPage.find_all(
            'div',
            attrs={'data-component-type':self.datacomptype}
            )
        
        #First div is not an item card
        item_cards=item_cards[1:]

        itemList=[self.cardtoItemObj(item) for item in item_cards]
        return itemList

    def cardtoItemObj(self,card:bs4.element.Tag):
        try:
            name=card.h2.text
            
            price=card.find('span',class_=self.span_price).text
            #Remove commas and convert to float
            price=float(price.replace(',',''))

            img=card.img['src']

            hlink=card.a['href']
            return ItemObj(
                name,
                price,
                img,
                hlink
            )
        except Exception as err:
            print(err)
            return ItemObj(error=err)


    




if __name__=='__main__':
    print(Amazon('car'))