def chai_falv(flavor="masala"):
    
    """"Return the flavour of chai.""" #triple string, this is the doc string. It will be printed in __doc__, it needs to be the very first line
    chai="ginger"
    return flavor

print(chai_falv.__doc__)
print(chai_falv.__name__)

def genenrate_bill(chai=0,samosa=0):
    """calcualte the total bill for chai and samosa
        :param chai: no of chai cups
        :oaram samosa: no of samosa 
        : returns: (total amount, than you message)
    """
    total = chai*10+ samosa*15

    return total, "thank your for visiting" 

