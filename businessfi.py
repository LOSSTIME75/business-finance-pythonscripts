
#this program is to help me automate my salestax calculations. by the time I am done I will probably have spent more time on this than the actual assignment.#

def salestax():
    print('price before tax')
    pbt = input()
    print('what is the tax? as a decimal please')
    tax = input()
    ttax = float(tax) + 1 #this is how I made it work because I am a pepega#
    
    pat = ttax * float(pbt)
    taxpaid = float(pbt) * float(tax)
    pricebeforest = 'price before sales tax is {}'
    print(pricebeforest.format(pbt))
    priceafterst = 'price after sales tax is {}'
    print(priceafterst.format(pat))
    taxby = 'tax by itself is {}'
    print(taxby.format(taxpaid))

salestax()
