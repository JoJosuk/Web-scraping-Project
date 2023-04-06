import requests
import bs4
from bs4 import BeautifulSoup
from Extensions.ItemObj import ItemObj
from Extensions.DataAnalyser import Analyser
from time import sleep

class Flipkart:
    def __init__(self,itemName:str) -> None:
        #Predefine params for souping tags
        self.card_class='_4ddWXP'
        self.name_class='s1Q9rs'
        self.price_class='_30jeq3'
        self.image_class='CXW8mj'
        
        self.error=False
        self.itemName=itemName
        self.itemPage:BeautifulSoup=BeautifulSoup(
            self.getPage(self.getSearchLink()),'html.parser'
            )
        self.json={}
        if not self.error:
            self.itemList=self.getList()
            self.json=Analyser(self.itemList).json

    def __str__(self):
        s="\n".join([str(x) for x in self.itemList])
        return s

    def getSearchLink(self):
        return f'https://www.flipkart.com/search?q={self.itemName}'
    
    def getPage(self,link:str):
        for _ in range(10):
            response=requests.get(link)
            if response.ok:
                return response.content
            else:
                sleep(2)
        self.error=True
        return response.content
    
    def getList(self):
        item_cards=self.itemPage.find_all('div',class_=self.card_class)

        itemList=[self.cardtoItemObj(item) for item in item_cards]
        return itemList

    def cardtoItemObj(self,card:bs4.element.Tag):
        try:
            
            price=card.find('div',class_=self.price_class).text[1:]
            #Remove commas and convert to float
            price=float(price.replace(',',''))

            return ItemObj(
                name=card.find('a',class_=self.name_class).text,
                price=price,
                img=card.find('div',class_=self.image_class).img['src'],
                hlink='https://www.flipkart.com'+card.find('a',class_=self.name_class)['href']
            )
        except Exception as err:
            print(err)
            return ItemObj(error=err)

    




if __name__=='__main__':
    obj=Flipkart('book')