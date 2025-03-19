#original setting of the character class
class Character:
    def __init__(self, name, surname,gender,age, health,hygiene, mood, money,life): # everthing needs to be passed in manually from the running code
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.health = health
        self.hygiene = hygiene
        self.mood = mood
        self.money = money
        self.life = life

  #second version
import random
  class Character:
    def __init__(self):
      isFemale = bool(random.getrandbits(1)) # randomly generates the gender of the character
      country_num = random.randint(0,195) # randomly generates the country of the character
      Fname_num= random.randint(0,2742) # randomly generates the first name of the character
      Lname_num = random.randint(1,1000) # rnadomly generates the last name of the character
      for x,y in Countries.items():
        if x == country_num:
          self.country = y[0]
          self.city = y[1]      #sets the country and city of the character
      if isFemale:
        for x,y in female_names.items():
          if x == Fname_num:
            self.name = y
            self.gender = 'female'
      elif not isFemale:
        for x,y in male_names.items(): #sets the gender and name of the character
          if x == Fname_num:
            self.name = y
            self.gender = 'male'
      for x,y in last_names.items():
        if x == Lname_num:
          self.surname = y
        self.age = 0 #age is automatically set to 0
        self.health = random.randint(0,100)
        self.hygiene = random.randint(0,100) # attributes are set randomly
        self.mood = random.randint(0,100)
        self.money = random.randint(0,100)
        self.intelligence=random.randint(0,100)
        self.life = True
#clunky many factors are repeated but is much more effecient as it sets itself, however attributes are irrelevant for other characters such as npcs in the game


#third version
import random
def random_choice(dict):
    random_value= random.choice(list(d.items()))
    del dict[random_value[0]]                     #removes the values retrived from the dictionary so there are no repeats 
    return random_value[1]

  def set_values(self):
    isFemale = bool(random.getrandbits(1)) # randomly generates the gender of the character
    if isFemale:
        self.name = random_choice(female_names)
        
    elif not isFemale:
        self.name = random_choice(male_names)
            
    for x,y in last_names.items():
        self.surname =  random_choice(last_names)
      
#doesnt set everthing, allow for it to be more reusable for other character classes

  class Main_Character:
    def __init__(self):
      set_values(self)
      country_city = random_choice(Countries)
      self.country = country_city[0]
      self.city = country_city[1]
      self.age = 0                #age is automatically set to 0
      self.health = random.randint(40,100) # attributes are set randomly
      self.mood = 100
      self.life_stage = 'Baby'
      self.money = 0
      self.intelligence=random.randint(0,100)
      self.life = True
  # neat and understandable. complexity is reduced by using subprograms, much much better

#final version 

class Main_Character():
  def __init__(self):
    set_values(self)
    country_city = random_choice(Countries)
    self.country = country_city[0]
    self.city = country_city[1]
    self.age = 0                    #age is automatically set to 0
    self.health = random.randint(40,100)    # attributes are set randomly
    self.mood = random.randint(90,100) 
    self.money = 0
    self.intelligence=random.randint(0,100)
    self.life = True
    self.grades = round(self.intelligence/0.85)
    self.attendance = 100
    self.experience=100
    self.properties =[]
    self.relationships = []
    self.education = None                      
    self.significant_other = None
    self.married =False
    self.job= None
    self.club = None
    self.school = None

def choice_results(self,choice,choice_list):
    if choice == 'a':
       i=choice_list[4]
       m=choice_list[5]
       h=choice_list[6]
    elif choice == 'b':
       i=choice_list[7]
       m=choice_list[8]
       h=choice_list[9]
    else:
       i=choice_list[10]
       m=choice_list[11]
       h=choice_list[12]
    self.intelligence=check_values(self.intelligence+random.randint(i[0],i[1]),100,0) 
    self.mood=check_values(self.mood+random.randint(m[0],m[1]),100,0) 
    self.health=check_values(self.health+random.randint(h[0],h[1]),100,0) 

def check_health(self):    
    health_check(self)

