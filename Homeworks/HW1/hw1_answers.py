from random import uniform

class Portfolio():
    """A client's portfolio of a financial institution.

    Attributes:
        cash: A float representing the total of cash available.
        stock: A dictionary representing each type of stocks.
        mutual funds: A dictionary representing each mutual fund.
        hist: A list representing each action in the portfolio.
    """

    def __init__(self, cash = 0.00):
        self.cash = float(cash)
        self.stock = {}
        self.mutualFund = {}
        self.hist = []

    def history(self):
        print self.hist

    def addCash(self, amount):
        """Add a amount of cash to client's portifolio"""
        self.cash += float(amount)
        self.hist.extend(["$"+str(amount)+" added"])
        return self.cash

    def withdrawCash(self, amount):
        """Remove a amount of cash from client's portifolio"""
        if amount > self.cash:
            raise RuntimeError('Not enough cash available')
        self.cash -= float(amount)
        self.hist.extend(["$"+str(amount)+" withdrawn"])
        return self.cash

    def addProduct(self, share, name, price, producttype):
        """ Add a product to the portfolio"""
        d = {name : [float(share), float(price)]}
        if producttype == "MutualFund":
            self.mutualFund.update(d)
        else:
            self.stock.update(d)

    def remProduct(self, share, name, producttype):
        """ Remove a product from the portfolio"""
        if producttype == "MutualFund":
            if self.mutualFund[name][0] == share:
                del self.mutualFund[name]
            else:
                self.mutualFund[name][0] = self.mutualFund[name][0] - share
        else:
            if self.stock[name][0] == share:
                del self.stock[name]
            else:
                self.stock[name][0] = self.stock[name][0] - share

    def buyMutualFund(self, share, obj):
        name = obj.name
        self.addProduct(share, name, obj.sales_price, "MutualFund")
        self.withdrawCash(share)
        if share == 1:
            self.hist.extend([str(1) + " share of " + name + " purchased"])
        else:
            self.hist.extend([str(share) + " shares of " + name + " purchased"])

    def buyStock(self, share, obj):
        name = obj.name
        self.addProduct(share, name, obj.sales_price, "Stock")
        self.withdrawCash(round(share * obj.purchase_price, 2))
        if share == 1:
            self.hist.extend([str(1) + " share of " + name + " purchased"])
        else:
            self.hist.extend([str(share) + " shares of " + name + " purchased"])

    def sellMutualFund(self, share, name):
        if share > self.mutualFund[name][0]:
            raise RuntimeError('Not enought shares available')
        self.remProduct(share, name, "MutualFund")
        price = self.mutualFund[name][1]
        self.addCash(round(share * price, 2))
        if share == 1:
            self.hist.extend([str(1) + " share of " + name + " sold"])
        else:
            self.hist.extend([str(share) + " shares of " + name + " sold"])

    def sellStock(self, share, name):
        if share > self.stock[name][0]:
            raise RuntimeError('Not enought shares available')
        self.remProduct(share, name, "Stock")
        price = self.stock[name][1]
        self.addCash(round(share * price, 2))
        if share == 1:
            self.hist.extend([str(1) + " share of " + name + " sold"])
        else:
            self.hist.extend([str(share) + " shares of " + name + " sold"])

    def __str__(self):
        stocksstring = "Stocks: "
        for key,value in self.stock.items():
            stocksstring += ('\n' + key + " " + str(value[0]))
        mfstring = "\nMutual Fund: "
        for key,value in self.mutualFund.items():
            mfstring += ('\n' + key + " " + str(value[0]))
        cashstring = "Cash: \n" + "$" + str(round(self.cash, 2)) + "\n"
        return cashstring + stocksstring  + mfstring

# Generate Class Mutual Fund
class MutualFund():

    """Attributes:
        name = A string representing the name of the fund.
        purchase_price = A float representing the purchase price.
        sales_price = A float representing the sales price.
    """

    def __init__(self, name):
        self.name = name
        self.purchase_price = float(1)
        self.sales_price = float(uniform(0.9, 1.2))

    def __str__(self):
        return self.name

# Generate Class Stock
class Stock():

    """Attributes:
        name = A string representing the name of the fund.
        purchase_price = A float representing the purchase price.
        sales_price = A float representing the sales price.
    """
    def __init__(self, name, purchase_price = 1):
        self.name = name
        self.purchase_price = purchase_price
        self.sales_price = float(uniform(0.5 * purchase_price, \
        1.5 * purchase_price))

    def __str__(self):
        return self.name


print "Creates a new portfolio"
portfolio =  Portfolio()
print "Adds cash to the portfolio"
portfolio.addCash(300.50)
print "Create a Stock with price 20"
s = Stock("HFH", 20)
print "Buys 5 share of stock s"
portfolio.buyStock(5, s)
print "Creates MF with symbol 'BRT'"
mf1 = MutualFund("BRT")
print "Creates MF with symbol 'GHT'"
mf2 = MutualFund("GHT")
print "Buys 10.3 shares of 'BRT'"
portfolio.buyMutualFund(10.3, mf1)
print "Buys 2 shares of 'GHT'"
portfolio.buyMutualFund(2, mf2)
print "Prints portfolio"
print portfolio
print "Sells 3 shares of 'BRT'"
portfolio.sellMutualFund(3, "BRT")
print "Removes $ 50"
portfolio.withdrawCash(50)
print "Prints a list of all transactions"
portfolio.history()
# portfolio.sellMutualFund()
#
#
#
# print portfolio.history
# print portfolio
# print "Test to subtract cash to portfolio and print"
# portfolio.withdrawCash(100)
# print portfolio
# print "Generate a Mutual Fund and print"
# mf1 = MutualFund("Test")
# print mf1
# print "Buy 40 shares of a Mutual Fund and print"
# portfolio.buyMutualFund(40, mf1)
# x = portfolio.mutualFund
# print x
# print "Sell 20 shares of a Mutual Fund and print"
# portfolio.sellMutualFund(20, mf1)
# x = portfolio.mutualFund
# print x
# print portfolio
# print "Generate a Stock  and print"
# s1 = Stock("TestStock")
# print s1
# print "Buy 40 shares of Stock and print"
# portfolio.buyStock(40, s1)
# x = portfolio.stock
# print x
# print portfolio
# print "Sell 20 shares of Stock and print"
# portfolio.sellStock(20, s1)
# x = portfolio.stock
# print x
# print portfolio
# print portfolio.history



# Generate Abstract Class Product
# class Product():
#
#     """Attibute:
#             name: A string representing the name of the product.
#             purchase_price: A float representing the purchase price.
#             sale_price: A float representing the sales price.
#
#     """
#     _metaclass_ = ABCMeta
#
#     initial = 0
#     final = 0
#
#     def __init__(self, name, purchase_price = None):
#         self.name = name
#         self.purchase_price = purchase_price
#         self.sale_price = uniform(initial * self.purchase_price, final * self.purchase_price)
#
#     @abstractmethod
#     def product_type(self):
#         """Return a string representing the type of investiment this is."""
#         pass
#
# class MutualFund(Product):
#     """A Mutual Fund available in a financial institution"""
#
#     base_buy = 1
#     initial = 0.9
#     final = 1.2
#
#     def __str__(self):
#         return self.name
#
#     def product_type(self):
#         """ Return a string representing the type of investiment this is."""
#         return 'MutualFund'
#
# p1 = Product("ENM")
# print p1
