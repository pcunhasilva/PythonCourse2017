from abc import ABCMeta, abstractmethod
from random import uniform, seed

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
        self.stock = {} # to store stocks
        self.mutualFund = {} # to store Mutual Funds
        self.bond = {} # to store bonds
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

    def addInvestment(self, share, investment):
        """ Add an investment to the portfolio"""

        new_asset = {investment.name : [float(share), \
        float(investment.sale_price)]}
        if investment.investment_type() == 'MutualFund':
            self.mutualFund.update(new_asset)
        elif investment.investment_type() == 'Stock':
            self.stock.update(new_asset)
        else:
            self.bond.update(new_asset)

    def buyInvestment(self, share, investment):
        if self.cash < (share * investment.purchase_price):
            raise RuntimeError('Not enough cash available')
        name = investment.name
        if investment.investment_type() == 'MutualFund':
            self.addInvestment(share, investment)
            self.withdrawCash(share)
        elif investment.investment_type() == 'Stock':
            if (share - int(share)) != 0:
                print 'Only whole units can be bought'
            self.addInvestment(share, investment)
            self.withdrawCash(share * investment.purchase_price)
        else:
            self.addInvestment(share, investment)
            self.withdrawCash(share * investment.purchase_price)
        if share in (1, 1.0):
            self.hist.extend([str(1) + " share of " + name + " purchased"])
        else:
            self.hist.extend([str(share) + " shares of " + name + " purchased"])

    def remInvestment(self, share, name, investmenttype):
        """ Remove an investment from the portfolio"""
        if investmenttype == 'MutualFund':
            if self.mutualFund[name][0] == share:
                del self.mutualFund[name]
            else:
                self.mutualFund[name][0] = self.mutualFund[name][0] - share
        elif investmenttype == 'Stock':
            if self.stock[name][0] == share:
                del self.stock[name]
            else:
                self.stock[name][0] = self.stock[name][0] - share
        else:
            if self.bond[name][0] == share:
                del self.bond[name]
            else:
                self.bond[name][0] = self.bond[name][0] - share

    def sellInvestment(self, share, name):
        # Find if there are more than one investment with
        # the same name in different cathegories:
        find = name in self.stock
        find += name in self.mutualFund
        find += name in self.bond

        if find == 0:
            print 'Investment does not exist.'

        elif find == 1:
            if name in self.mutualFund:
                if share > self.mutualFund[name][0]:
                    print 'Not enought shares available'
                self.remInvestment(share, name, "MutualFund")
                price = self.mutualFund[name][1]
                self.addCash(round(share * price, 2))
            elif name in self.stock:
                if share > self.stock[name][0]:
                    print 'Not enought shares available'
                if (share - int(share)) != 0:
                    print 'Only units can be bought'
                self.remInvestment(share, name, "Stock")
                price = self.stock[name][1]
                self.addCash(round(share * price, 2))
            else:
                if share > self.bond[name][0]:
                    print 'Not enought shares available'
                self.remInvestment(share, name, "Bond")
                price = self.bond[name][1]
                self.addCash(round(share * price, 2))

        elif find > 1:
            print "There is more than one investment with this name.",
            print "Please, inform the type of investment:"
            investtype = raw_input("> ")
            if investtype in ('Mutual Fund', 'MutualFund',
            'mutualfund', 'mutual fund'):
                if share > self.mutualFund[name][0]:
                    print 'Not enought shares available'
                self.remInvestment(share, name, "MutualFund")
                price = self.mutualFund[name][1]
                self.addCash(round(share * price, 2))
            elif investtype in ('Stock', 'stock', 'Stocks', 'stocks'):
                if share > self.stock[name][0]:
                    print 'Not enought shares available'
                if (share - int(share)) != 0:
                    print 'Only whole units can be sold'
                self.remInvestment(share, name, "Stock")
                price = self.stock[name][1]
                self.addCash(round(share * price, 2))
            elif investtype in ('Bond', 'bond', 'Bonds', 'bonds'):
                if share > self.bond[name][0]:
                    print 'Not enought shares available'
                self.remInvestment(share, name, "Bond")
                price = self.bond[name][1]
                self.addCash(round(share * price, 2))
            else:
                print "Type of investment does not exist."

    def __str__(self):
        stocksstring = "Stocks: "
        for key,value in self.stock.items():
            stocksstring += ('\n' + key + " " + str(value[0]))
        mfstring = "\nMutual Fund: "
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

        if self.investment_type() == 'MutualFund':
            self.purchase_price = 1
            self.sale_price = round(uniform(0.9, 1.2), 2)

        elif self.investment_type() == 'Stock':
            if purchase_price <= 0 or purchase_price == None:
                raise RuntimeError('Negative purchase price or invalid price.')
            self.purchase_price = purchase_price
            self.sale_price = round(uniform(0.5 * purchase_price, \
            1.5 * purchase_price), 2)

        else:# This part is used to generate other products, as Bonds.
            if purchase_price <= 0 or purchase_price == None:
                raise RuntimeError('Negative purchase price or invalid price.')
            self.purchase_price = purchase_price
            self.sale_price = round(uniform(1 ** purchase_price, \
            1.5 ** purchase_price), 2)

    @abstractmethod
    def investment_type(self):
        """Return a string representing the type of investiment this is."""
        pass

# Generate Class MutualFund
class MutualFund(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'MutualFund'

# Generate Class Stock
class Stock(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'Stock'

# Generate Class Bond
class Bond(Investment):

    def __str__(self):
        return self.name

    def investment_type(self):
        """ Return a string representing the type of investiment this is."""
        return 'Bond'

# Test the functions using the examples in the HW.
# Set a seed to always have the same values
seed(1)
print "Creates a new portfolio"
portfolio =  Portfolio()
print "Adds cash to the portfolio"
portfolio.addCash(300.50)
print "Create a Stock with price 20"
s = Stock("HFH", 20)
print "Buys 5 share of stock s"
portfolio.buyInvestment(5, s)
print "Creates MF with symbol 'BRT'"
mf1 = MutualFund("BRT")
print "Creates MF with symbol 'GHT'"
mf2 = MutualFund("GHT")
print "Buys 10.3 shares of 'BRT'"
portfolio.buyInvestment(10.3, mf1)
print "Buys 2 shares of 'GHT'"
portfolio.buyInvestment(2, mf2)
print "Prints portfolio"
print portfolio
print "Sells 3 shares of 'BRT'"
portfolio.sellInvestment(3, "BRT")
print "Sells 1 share of HFH"
portfolio.sellInvestment(1, "HFH")
print "Removes $ 50"
portfolio.withdrawCash(50)
print "Prints a list of all transactions"
portfolio.history()
print portfolio




#
# portfolio = Portfolio()
# portfolio.addCash(5000)
# s = MutualFund("s", 3)
# print s.sale_price
# print s.purchase_price
# print s.investment_type()
# portfolio.buyInvestment(50.0, s)
# f = Stock("f", 3)
# print f.sale_price
# print f.purchase_price
# print f.investment_type()
# portfolio.buyInvestment(50.0, f)
# d = Bond("d", 30)
# print d.sale_price
# print d.purchase_price
# print d.investment_type()
# dd = Stock("d", 50)
# portfolio.buyInvestment(5.0, dd)
# portfolio.buyInvestment(5.0, d)
# print "Prints portfolio"
# print portfolio
# portfolio.history()
# portfolio.sellInvestment(3, "d")
# portfolio.history()
# print "Prints portfolio"
# print portfolio
