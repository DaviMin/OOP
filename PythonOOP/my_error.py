# objekt na odkazovani vyjimek

class MyCustomError(Exception):

    def __init__(self, message):
        self.message = message
