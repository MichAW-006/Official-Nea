#first version
class Property():
  def __init__(self):
    random_value= random.choice(list(property_names.items()))
    self.price =round(max(0, min(20*(10**6) / math.exp(0.5*(random_value[0]-1)) * random.uniform(0.5, 1.1), 20*(100**6))))
    self.type = random_value[1]
    self.location = str(random.randint(1,270))+' '+random_choice(street_names)+' '+random_choice(location_names)
    self.price_paid = 0
    self.years_left =25
    self.strikes = 3

  def buy(self,mortgage,player):
    if mortgage is True: 
      if player.money >= (self.price/10):
        self.price_paid=player.money-(self.price/10)
        return True
      else:
        return False
    elif mortagage is False :
      if player.money >= self.price:
        self.price_paid = self.price
        return True 
      else:
        return False
        
def sell(self,player):
  player.money += self.price_payed
  
def pay_mortagage(self,player):
  self.years_left += -1
  left_to_pay =self.price-self.price_payed
  if player.money >= (left_to_pay)/25:
    self.price_payed +=(left_to_pay)/25
    return left_to_pay/25
  else:
    self.strikes+=-1
def check_if_defaulted(self):
  if self.strikes == 0:
    pass


#final version

class Property():
  def __init__(self):
    random_value= random.choice(list(property_names.items()))
    x= random_value[0] # property it ranked from most the leat expensive. x represents this
    self.condition = random.randint(1,100) 
    self.price =round(15850000 * (0.6309 ** x) + self.condition, 2 - len(str(int(15850000 * (0.6309 ** x))))) *(self.condition/100) # asked ai to generate this equation for me
    self.type = random_value[1] # the type of property
    self.location = str(random.randint(1,270))+' '+random_choice(street_names)+' '+random_choice(location_names)
    self.price_paid = 0 # the moutn the player will have played
    self.years_left =25 # years left on the mortgage
    self.strikes = 3 #how many time the user can fail the repay their mortage before their property gets reclaimed
    self.bought = False # checkls if the property is owned
    self.yearly_payments = (self.price*0.9)/25 #how much must be payed yearly on the mortage
    self.mortgage = False # if the propery has a mortgage
    self.asked = False # checks if the player has asked to buy the property

  def buy(self,player,mortgage):
    if self.asked is False: #
      if self.bought is False:
        if mortgage is True: 
          if player.money >= (self.price/10):
            self.price_paid=(self.price/10)
            player.money= player.money- self.price_paid
            self.asked = True
            self.bought= True
            self.mortgage = True
            player.properties.append(self)
            return f'you bought the {self.type} at {self.location}'
          else:
            self.asked = True
            return 'not enough money'
        elif mortgage is False :
          if player.money >= self.price:
            self.price_paid = self.price
            player.money= player.money-self.price_paid
            self.bought = True
            self.asked = True
            self.mortgage = False
            player.properties.append(self)
            return f'you bought the {self.type} at {self.location}' 
          else:
            self.asked = True
            return 'not enough money'
    else:
      return ''
        
  def sell(self,player):
    player.money += self.price_paid
    player.properties.remove(self)
    return( f'You sold your {self.type} on {self.location}')
    
  def pay_mortgage(self,player): 
    if self.price_paid >= self.price:
      self.mortgage = False
 
    if player.money >= self.yearly_payments:
      player.money-=self.yearly_payments
      self.price_paid+=self.yearly_payments
      self.years_left += -1

    else:
      self.strikes+=-1
      
  def check_if_defaulted(self,player):
    if self.strikes <= 0:
      player.properties.remove(self)
      return f'The bank reclaimed your {self.type} on {self.location}'
    else:
      return ''
