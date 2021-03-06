from abc import ABCMeta, abstractmethod
from random import uniform, seed

class Portfolio():
    """A client's portfolio of a financial institution.

    Attributes:
        cash: A float representing the total of cash available.
        stock: A dictionary representing each type of stocks.
               The first element of the dictionary represets the
               total amount of shares in the portfolio and the
               second represets the sales price per share.
        mutual funds: A dictionary representing each mutual fund.
               The first element of the dictionary represets the
               total amount of shares in the portfolio and the
               second represets the sales price per share.
        bond: A dictionary representing each bond.
               The first element of the dictionary represets the
               total amount of shares in the portfolio and the
               second represets the sales price per share.
        hist: A list representing each action in the portfolio.
    """

    def __init__(self, cash = 0.00):
        self.cash = float(cash)
        self.stock = {} # to store stocks
        self.mutualFund = {} # to store mutual funds
        self.bond = {} # to store bonds
        self.hist = [] # to store the log of operations

    def history(self):
        """Print the portfolio's log."""
        print self.hist

    def addCash(self, amount):
        """Add a amount of cash to client's portifolio"""
        self.cash += float(round(amount, 2))
        self.hist.extend(["$"+str(round(amount, 2))+" added"])
        return self.cash

    def withdrawCash(self, amount):
        """Remove a amount of cash from client's portifolio"""
        if amount > self.cash: raise ValueError('Not enough cash available')
        self.cash -= float(round(amount, 2))
        self.hist.extend(["$"+str(round(amount, 2))+" withdrawn"])
        return self.cash

    def addInvestment(self, share, investment):
        """ Add an investment to the portfolio"""

        new_asset = {investment.name : [round(float(share), 2), \
        float(investment.sale_price)]}
        getattr(self, investment.investment_type()).update(new_asset)


    def buyInvestment(self, share, investment):
        """Add an asset to the portfolio"""

        if share <= 0: raise ValueError ("Please insert a positive number.")

        if investment.investment_type() == 'stock' and \
        (share - int(share)) != 0:
            raise ValueError ('Stocks can only be bought as whole units')

        self.addInvestment(share, investment)
        self.withdrawCash(share * investment.purchase_price)

        if share in (1, 1.0):
            self.hist.extend([str(1) + " share of " + investment.name + \
            " purchased"])
        else:
            self.hist.extend([str(share) + " shares of " + investment.name \
            + " purchased"])

    def remInvestment(self, share, name, investmenttype):
        """ Remove an asset from the portfolio"""

        if getattr(self, investmenttype)[name][0] == share:
            del getattr(self, investmenttype)[name]
        else:
            getattr(self, investmenttype)[name][0] = \
            round(getattr(self, investmenttype)[name][0] - share, 2)


    def InvestmentUnique(self, name):
        """ Find if two items of different types of assets
        have the same name """
        investtype = []
        if name in self.stock: investtype.append("stock")
        if name in self.mutualFund: investtype.append("mutualFund")
        if name in self.bond: investtype.append("bond")
        return investtype

    def sellInvestment(self, share, name):
        """ Sell an assets in a portfolio """

        if share <= 0: raise ValueError ("Please insert a positive number.")

        investtype = self.InvestmentUnique(name)

        if len(investtype) == 0:
             raise ValueError ('Investment does not exist.')
        elif len(investtype) == 1:

            if share > getattr(self, investtype[0])[name][0]:
                raise ValueError ('Not enought shares available')

            self.remInvestment(share, name, investtype[0])
            price = getattr(self, investtype[0])[name][1]
            self.addCash(round(share * price, 2))
        else:
            print "There is more than one investment with this name.",
            print "Please, inform the type of investment %s" % investtype
            investtype = raw_input("> ")

            if share > getattr(self, investtype):
                raise ValueError ('Not enought shares available')

            self.remInvestment(share, name, investtype)
            price = getattr(self, investtype)[name][1]
            self.addCash(round(share * price, 2))
        if share == 1: self.hist.extend([str(1) + " share of " + name + " sold"])
        else:self.hist.extend([str(share) + " shares of " + name + " sold"])

    def __str__(self):
        """ Define the print method to Portfolio() """

        stocksstring = "stocks: "
        for key,value in self.stock.items():
            stocksstring += ('\n' + key + " " + str(value[0]))

        mfstring = "\nmutual Fund: "
        for key,value in self.mutualFund.items():
            mfstring += ('\n' + key + " " + str(value[0]))

        bondstring = "\nBonds: "
        for key,value in self.bond.items():
            bondstring += ('\n' + key + " " + str(value[0]))

        cashstring = "Cash: \n" + "$" + str(round(self.cash, 2)) + "\n"

        return cashstring + stocksstring  + mfstring + bondstring


##################################
###### Generate Investments ######
##################################

# Generate Abstract Class Investments
class Investment(object):

    """Attibute:
            name: A string representing the name of the product.
            purchase_price: A float representing the purchase price.
            sale_price: A float representing the sales price.
    """

    __metaclass__ = ABCMeta

    def __init__(self, name, purchase_price = None):
        self.name = name

        if self.investment_type() == 'mutualFund':
            self.purchase_price = 1.0
            self.sale_price = round(uniform(0.9, 1.2), 2)

        else:
            if purchase_price <= 0 or purchase_price == None:
                raise RuntimeError("""Negative purchase price or invalid
                purchase price.""")
            self.purchase_price = purchase_price
            if self.investment_type() == 'stock':
                self.sale_price = round(uniform(0.5 * purchase_price, \
                1.5 * purchase_price), 2)
            else:# This part is used to generate other products, loke Bonds.
                self.sale_price = round(uniform(0.2 * purchase_price, \
                7 * purchase_price), 2)

    @abstractmethod
    def investment_type(self):
        """Return a string representing the type of investiment this is."""
        pass

# Generate Class mutualFund
class mutualFund(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'mutualFund'

# Generate Class stock
class stock(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'stock'

# Generate Class Bond
class bond(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'bond'

# Test the functions using the examples in the HW.
# Set a seed to always have the same values
seed(1)
print "Creates a new portfolio"
portfolio =  Portfolio()
print "Adds cash to the portfolio"
portfolio.addCash(300.50)
print "Create a stock with price 20"
s = stock("HFH", 20)
print "Buys 5 share of stock s"
portfolio.buyInvestment(5, s)
print "Creates MF with symbol 'BRT'"
mf1 = mutualFund("BRT")
print "Creates MF with symbol 'GHT'"
mf2 = mutualFund("GHT")
print "Buys 10.3 shares of 'BRT'"
portfolio.buyInvestment(10.3, mf1)
print "Buys 2 shares of 'GHT'"
portfolio.buyInvestment(5, mf2)
print "Prints portfolio"
print portfolio
print "Sells 3 shares of 'BRT'"
print portfolio.sellInvestment(3, "BRT")
print "Sells 1 share of HFH"
portfolio.sellInvestment(1, "HFH")
print "Removes $ 50"
portfolio.withdrawCash(50)
print "Prints a list of all transactions"
portfolio.history()
print portfolio
print "Create a bond named 'BRT'"
b1 = bond("BRT", 3)
print "Buys 10.3 shares of 'BRT' (bond)"
portfolio.buyInvestment(10.3, b1)
print "Sells 1 shares of 'BRT' (bond)"
print portfolio.sellInvestment(1, "BRT")
portfolio.history()
print portfolio
