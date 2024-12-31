from selenium.webdriver.common.by import By
from page_objects.LoginPage import LoginPage
from keywords.keywords import buttonId

class ShoppingPage(LoginPage):
    cart = (By.CLASS_NAME, "shopping_cart_link")
    checkoutButton = (By.ID, "checkout")
        
    def addItem(self, item):
        buttonField = (By.XPATH, "//button[@id='add-to-cart-"+buttonId(item)+"']")
        if not self.isElementPresent(buttonField):
            return 
        self.clickElement(buttonField)
    
    def proceedToCart(self):
        self.clickElement(self.cart)
        
    def removeItem(self, item):
        buttonField = (By.XPATH, "//button[@id='remove-"+buttonId(item)+"']")
        if not self.isElementPresent(buttonField):
            return 
        self.clickElement(buttonField)
    
    def proceedToCheckout(self):
        self.clickElement(self.checkoutButton)