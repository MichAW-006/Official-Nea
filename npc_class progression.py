#first version
class npcs:
  def __init__(self):
    isFemale = bool(random.getrandbits(1)) 
    i2= random.randint(0,2742)
    i3 = random.randint(1,1000)
    if isFemale is True:
      for x,y in female_names.items():
        if x == i2:
          self.name = y
    elif isFemale is False:
      for x,y in male_names.items():
        if x == i2:
          self.name = y
    for x,y in last_names.items():
      if x == i3:
        self.surname = y
    self.age = random.randint(17,75)
    self.health = random.randint(0,100)
    self.money = random.randint(0,100)
    self.love = random.randint(0,100)
    self.life = True

class parent(npcs):
  def __init__(self,player):
    isFemale = bool(random.getrandbits(1))
    i2= random.randint(0,2742)
    if isFemale == True:
      for x,y in female_names.items():
        if x == i2:
          self.name = y
          self.title = 'mother'
    elif isFemale == False:
      for x,y in male_names.items():
        if x == i2:
          self.name = y
          self.title = 'father'
    self.surname = player.surname
    self.age = random.randint(17,75)
    self.health = random.randint(0,100)
    self.money = random.randint(0,100)
    self.love = random.randint(0,100)
    self.life = True




#final version
class Npc(): 
  def __init__(self,player):
    set_values(self)
    self.age = random.randint(player.age-5,player.age+5)
    self.age = check_values(self.age,player.age+5,0)
    self.health = random.randint(0,100)
    self.relationship_level = random.randint(0,100)
    self.life = True
    self.money_ask = -1 # ask attributes make sure that the user does not abuse the system 
    self.conversate_ask = -1
    self.extra_ask = -1
    self.end_ask=-1
    self.married = bool(random.getrandbits(1))
    self.relationship_level = 10
    self.relationship_type = None
    self.money = random.randint(100,10000)

class Parent(Npc):
  def __init__(self,player):
    super().__init__(player)
    set_values(self)
    self.surname = player.surname
    self.married = True
    self.age = random.randint(17,75)
    self.relationship_level = random.randint(50,100)
    self.money = random.randint(100,10000)
    self.life = True
    if self.gender == 'male':
      self.relationship_type = 'Father'
    else:
      self.relationship_type = 'Mother'
  
    
class Sibling(Npc):
  def __init__(self,player):
    super().__init__(player)
    set_values(self)
    if player.age-1 ==0:
       max_age = 10
    else:
       max_age = 0
    self.surname = player.surname
    self.age = random.randint(0,max_age)
    self.relationship_level = random.randint(0,100)
    self.life = True
    self.money = random.randint(0,1000)
    self.relationship_type = 'Sibling'

  
  def have_conversation(self,player):                                #conversation method
    if player.age>self.conversate_ask: # checks when the user last asked 
      self.relationship_level += random.randint(-10,10)
      self.change_relationship()
      self.conversate_ask=player.age
      return f'You and your {self.relationship_type}, {self.name} had a conversation about {random_choice(conversation_topics)}'
    else:
      return ''  #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
      
  def ask_for_money(self,player):
    if player.age>self.money_ask: # checks if the user has asked before
      if self.relationship_level >60: # checks that the player and the npc have a strong enough relationship to ask fro money
          money = random.randint(1,1000)
          self.money -= money
          player.money += money 
          self.relationship_level += random.randint(-10,1)
          self.change_relationship()
          self.money_ask=player.age #sets the value so the player cannot ask again
          return f'Your{self.relationship_type}, {self.name} gave you £{money} '# appends to the history
      else:
        self.relationship_level += random.randint(-30,1)
        self.change_relationship()
        self.money_ask=player.age #sets the value so the player cannot ask again
        return (f'Your {self.relationship_type}, {self.name} says "stop asking for money"')# appends to the history
    else:
      return ''  #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
  def start_fight(self,player):
    if player.age>self.extra_ask: # checks if the user has asked before
      if bool(random.getrandbits(1)) is True:# gives the user a 1/2 chance that the npc will want to fight them
        self.health += random.randint(-50,0)
        player.health+=random.randint(-50,0)
        self.extra_ask=player.age #sets the value so the player cannot ask again
        return (f'You and {self.name} tussled') # appends to the history
      else:
        self.extra_ask=player.age #sets the value so the player cannot ask again
        return (f'{self.name} doesn\'t want to fight you') # appends to the history
    else:
      return ''  #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
      
  def to_date(self,player): 
    if player.age>self.extra_ask: # checks if the user has asked before
      if self.married == False: # checks if the npc is married
        if player.significant_other == None: # checks if the user already has a partner
          if bool(random.getrandbits(1)) == True:  # gives the user a 1/2 chance that the npc will want to be with them
            self.relationship_level = 40  #sets the new relationship values
            self.relationship_type = 'Significant Other'
            player.relationships.append(self)
            player.significant_other = self
            self.extra_ask=player.age #sets the value so the player cannot ask again
            return f'{self.name} {self.surname} has agreed to be your {self.relationship_type}'# appends to the history
        elif bool(random.getrandbits(1)) == True:  # gives the user a 1/2 chance that the player will want to be with them
          self.relationship_type = 'Significant Other' ##sets the new relationship values
          player.relationships.append(self)
          self.relationship_level = 40
          ex = player.significant_other.name+ ' ' +player.significant_other.surname
          text = f' You ended things with {ex} to get with {self.name} {self.surname}'
          player.relationships.remove(player.significant_other)
          player.significant_other = self
          self.extra_ask=player.age #sets the value so the player cannot ask again
          return text # appends to the history
      else:
        self.extra_ask=player.age
        return f'{self.name} {self.surname} doesn\'t want to date you' # appends to the history
  
    return ''   #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash

  def be_friends(self,player):
    if player.age>self.extra_ask: # checks if the user has asked before
      if bool(random.getrandbits(1)) == True:
          self.relationship_type = 'Friend'
          player.relationships.append(self)
          self.extra_ask=player.age #sets the value so the player cannot ask again
          return f'{self.name} {self.surname} has agreed to be your {self.relationship_type}' # appends to the history 
      else:
        self.extra_ask=player.age #sets the value so the player cannot ask again
        return f'{self.name} {self.surname} doesn\'t want to be your friend' # appends to the history
    else:
        return '' #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
        
  def end_friendship(self,player):
    if player.age>self.end_ask: # checks if the user has asked before
      player.relationships.remove(self)
      self.end_ask=player.age #sets the value so the player cannot ask again
      return f'{self.name} {self.surname} has stopped being your friend'# appends to the history
    return '' #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
    
  def break_up(self,player):
    if player.age>self.end_ask: # checks if the user has asked before
      player.relationships.remove(self) 
      self.end_ask=player.age #sets the value so the player cannot ask again
      return f'{self.name} {self.surname} has stopped being your significant other'# appends to the history
    return ''  #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash


  def check_health(self):
    health_check(self)
    
       
  
  
      
  def change_relationship(self):
    self.relationship_level=check_values (self.relationship_level,100,0)
