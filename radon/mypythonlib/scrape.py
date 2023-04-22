from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class flipkart_fashion:
    def __init__(self,itemName) -> None:
        self.items=itemName
        self.pageurl=f'https://www.flipkart.com/search?q={self.items}'   
        self.pageurl2=f'https://www.flipkart.com/search?q={self.items}&page='
    cardClass = '_1xHGtK'
    nameCard='_2WkVRV'
    descriptionClass='IRpwTa'
    priceClass="_30jeq3"
    imageClass='_2r_T1I'
    hrefClass='IRpwTa'
    
class amazon:
    def __init__(self,itemName) -> None:
        self.items=itemName
        self.pageurl=f'https://www.amazon.in/s?k={self.items}&ref=nb_sb_noss_2'
        self.pageurl2=f'https://www.amazon.in/s?k={self.items}&ref=nb_sb_noss_2&page='
    cardClass='s-search-result'
    nameCard='a-size-base-plus a-color-base'
    descriptionClass='a-size-base-plus a-color-base a-text-normal'
    priceClass='a-price-whole'
    imageClass='s-image'
    hrefClass='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
class myntra:
    def __init__(self,itemName) -> None:
        self.items=itemName
        self.pageurl=f'https://www.myntra.com/{self.items}'
        self.pageurl2=f'https://www.myntra.com/{self.items}?p='
    cardClass='product-base'
    nameCard='product-brand'
    descriptionClass='product-product'
    priceClass='product-discountedPrice'
    imageClass='img-responsive'
    hrefClass='_blank'
    
    

def getdata(itemname):
    print(itemname)
    itemName='%20'.join(itemname.strip().split())
    keyWords=[]
    itemList=[]
    
    websites = [myntra(itemName),amazon(itemName),flipkart_fashion(itemName)]
    namewebsites=['myntra','amazon','flipkart']
    
    def setlist(item,nameCard,descriptionClass,priceClass,websitewhich,imageClass,hrefClass):
        if str(websitewhich)=='flipkart':
            name=item.find('div',class_=nameCard)
            if name ==None:
                name=item.find('a',class_='IRpwTa').text

            else:
                name=name.text
            dis=item.find('a',class_=descriptionClass)['title']
            price=item.find('div',class_=priceClass).text[1:]
            price=''.join(price.split(','))
            img=item.find('img',class_=imageClass)['src']
            href=item.find('a',class_=hrefClass)['href']

            keyWords.extend(dis.split())
            return [name,dis,float(price),img,'https://www.flipkart.com'+str(href),'FLIPKART']
        elif str(websitewhich)=='amazon':
            name=item.find('span',class_=nameCard).text
            dis=item.find('span',class_=descriptionClass).text
            price=item.find('span',class_=priceClass)
            if price==None:
                price='0'
            else:
                price=price.text
            price=''.join(price.split(','))
            img=item.find('img',class_=imageClass)['src']
            href=item.find('a',class_=hrefClass)['href']
            
            keyWords.extend(dis.split())
            return [name,dis,float(price),img,'https://www.amazon.com'+str(href),'AMAZON']
        elif str(websitewhich)=='myntra':
            name=item.find('h3',class_=nameCard).text
            dis=item.find('h4',class_=descriptionClass).text
            price=item.find('span',class_=priceClass)
            if price==None:
                price=item.find('div',class_='product-price')
                if price==None:
                    price='0'
                else:
                    price=price.text[3:]
            else:
                price=price.text[3:]
            if item.find('img',class_=imageClass)==None:
                img='https://womens-southerngolfassociation.org/wp-content/uploads/2021/10/Image-Not-Available.png'
            else:
                img=item.find('img',class_=imageClass)['src']
            href=item.find('a')['href']
            # if len(price)>3:
            #     price=price[3:]
            # if price==None:
            #     price=0
            print(price)
            keyWords.extend(dis.split())
            return [name,dis,float(price),img,'https://www.myntra.com/'+str(href),'MYNTRA']
        
    # WINDOW_SIZE = "1920,1080"
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    
    for no,i in enumerate(websites):      
        cardClass=i.cardClass
        nameCard=i.nameCard
        descriptionClass=i.descriptionClass
        priceClass=i.priceClass
        imageClass=i.imageClass
        pageurl=i.pageurl
        pageurl2=i.pageurl2
        hrefClass=i.hrefClass
        # itemPage=requests.get(pageurl,headers={'User-Agent': 'Mozilla/5.0'}).content
        for enum in range(1,2):
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument('--disable-dev-shm-usage')     
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(pageurl2+str(enum))
            itemPage=driver.page_source
            idk = BeautifulSoup(itemPage,'html.parser')
            driver.close()
            if namewebsites[no]=='flipkart':
                itemCards=idk.find_all('div',class_=cardClass)[1:]
            elif namewebsites[no]=='amazon':
                itemCards=idk.find_all('div',{'data-component-type': 's-search-result'})
            elif namewebsites[no]=='myntra':
                itemCards=idk.find_all('li',class_=cardClass)
        

            itemList.extend([setlist(item,nameCard,descriptionClass,priceClass,namewebsites[no],imageClass,hrefClass) for item in itemCards])
       
    table=pd.DataFrame(itemList,columns=['Name','Description','Price','Image','Link','Website'])
    table=table.sort_values(by='Price')
    table=table.reset_index(drop=True)
    table.to_excel('data.xlsx')  
 
    return table