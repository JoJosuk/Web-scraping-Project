from Extensions.ItemObj import ItemObj
import pandas as pd

class Analyser:
    def __init__(self,itemList:list[ItemObj]):
        self.df=self.toDF(itemList)
        self.json={}

        #Functions to add to json
        self.MainThree()

        print(self.json)

    def toDF(self,itemList:list[ItemObj]):
        df=pd.DataFrame(columns=['name','price','img','hlink'])
        for item in itemList:
            if not item.error:
                df=df.append(pd.DataFrame(
                    data=[[item.name,item.price,item.img,item.hlink]],
                    columns=df.columns
                ),ignore_index=True)
        df=df.sort_values(by='price')
        return df

    def MainThree(self):
        dict={
        'max':self.df[self.df['price']==self.df['price'].max()].to_dict('records')[0],
        'min':self.df[self.df['price']==self.df['price'].min()].to_dict('records')[0],
        'median':self.df.iloc[len(self.df)//2].to_dict()
        }          
        self.json['MainThree']=dict