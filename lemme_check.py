def tax(money):
    taxed_amount1= 0
    taxed_amount2 = 0
    if (money - 13000) >0:
        taxed_amount1 = (money - 13000)*0.125
        if (money-30000)> 0:
            taxed_amount2 = (money - 30000)* 0.35

    return ( money -taxed_amount1-taxed_amount2)

print(tax(39999))