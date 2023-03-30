#Class to objectify each item
class ItemObj:
    """
    A DataObject representing an item

    Properties:
        name(str): Name of the item
        price(float): Price of the item
        img(str): Link to the image of the item
        hlink(str): Hyperlink to the items page
        error(bool): Exception object if error occurs
    """
    def __init__(
            self,
            name:str=None,
            price:float=None,
            img:str=None,
            hlink:str=None,
            error:Exception=None,
            ) -> None:
        self.name=name
        self.price=price
        self.img=img
        self.hlink=hlink
        self.error=error
    
    def __str__(self):
        if self.error:
            empty=""
            return f'{empty:-<60}\n{self.error}' 
        
        empty=""
        s=f'{empty:-<60}\n\
        Name:{self.name[:50]}\n\
        Price:{self.price}\n\
        Image:{self.img}\n\
        HyperLink:{self.hlink[:50]}\n'

        return s
