import pygame
import random
import math
from variables import *

class Main_Character():
  
  def __init__(self):
    set_values(self)
    country_city = random_choice(Countries)
    self.country = country_city[0]
    self.city = country_city[1]
    self.age = 0                 #age is automatically set to 0
    self.health = random.randint(40,100) # attributes are set randomly
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
    health_check(self)
    
    
    
    
class Npc(): 
  def __init__(self,player):
    set_values(self)
    self.country = player.country
    self.city = player.city
    self.age = random.randint(player.age-5,player.age+5)
    self.age = check_values(self.age,player.age+5,0)
    self.health = random.randint(0,100)
    self.relationship_level = random.randint(0,100)
    self.life = True
    self.money_ask = -1
    self.conversate_ask = -1
    self.extra_ask = -1
    self.end_ask=-1
    self.married = bool(random.getrandbits(1))
    self.relationship_level = 10
    self.relationship_type = None
    self.money = random.randint(100,10000)
    
  def have_conversation(self,player):
    if player.age>self.conversate_ask:
      conversation= random_choice(conversation_topics)
      self.relationship_level += random.randint(-10,10)
      self.change_relationship()
      self.conversate_ask=player.age
      return f'You and your {self.relationship_type}, {self.name} had a conversation about {conversation}'
    else:
      return ''
      
  def ask_for_money(self,player):
    if player.age>self.money_ask:
      if self.relationship_level >60:
          money = random.randint(1,1000)
          self.money -= money
          player.money += money 
          self.relationship_level += random.randint(-10,1)
          random_comment = (f'Your {self.relationship_type} gave you £{money}')
          self.change_relationship()
          self.money_ask=player.age
          return random_comment
      else:
        self.relationship_level += random.randint(-30,1)
        self.change_relationship()
        self.money_ask=player.age
        return (f'Your {self.relationship_type} says "stop asking for money"')
    else:
      return ''
      
  def to_date(self,player):
    if player.age>self.extra_ask:
      if self.married ==False:
        if player.significant_other == None:
          if bool(random.getrandbits(1)) == True:
            self.relationship_level = 40
            self.relationship_type = 'Significant Other'
            player.relationships.append(self)
            player.significant_other = self
            self.extra_ask=player.age
            return f'{self.name} {self.surname} has agreed to be your {self.relationship_type}'
        elif bool(random.getrandbits(1)) == True:
          self.relationship_type = 'Significant Other'
          player.relationships.append(self)
          self.relationship_level = 40
          ex = player.significant_other.name+ ' ' +player.significant_other.surname
          text = f' You ended things with {ex} to get with {self.name} {self.surname}'
          player.relationships.remove(player.significant_other)
          player.significant_other = self
          self.extra_ask=player.age
          return text
      else:
        self.extra_ask=player.age
        return f'{self.name} {self.surname} doesn\'t want to date you'
  
    return ''

  def be_friends(self,player):
    if player.age>self.extra_ask:
      if bool(random.getrandbits(1)) == True:
          self.relationship_type = 'Friend'
          player.relationships.append(self)
          self.extra_ask=player.age
          return f'{self.name} {self.surname} has agreed to be your {self.relationship_type}'
      else:
        self.extra_ask=player.age
        return f'{self.name} {self.surname} doesn\'t want to be your friend'
    else:
        return ''
        
  def end_friendship(self,player):
    if player.age>self.end_ask:
      player.relationships.remove(self)
      self.end_ask=player.age
      return f'{self.name} {self.surname} has stopped being your friend'
    return ''
  def break_up(self,player):
    if player.age>self.end_ask:
      player.relationships.remove(self)
      self.end_ask=player.age
      return f'{self.name} {self.surname} has stopped being your significant other'
    return ''


  def check_health(self):
    health_check(self)
    
       
  
  def start_fight(self,player):
    if player.age>self.extra_ask:
      if bool(random.getrandbits(1)) is True:
        self.health += random.randint(-50,0)
        player.health+=random.randint(-50,0)
        self.extra_ask=player.age
        return (f'You and {self.name} tussled')
      else:
        self.extra_ask=player.age
        return (f'{self.name} doesn\'t want to fight you')
    else:
      return ''
  
      
  def change_relationship(self):
    self.relationship_level=check_values (self.relationship_level,100,0)
    
  

class Parent(Npc):
  def __init__(self,player):
    super().__init__(player)
    set_values(self)
    self.surname = player.surname
    self.country = player.country
    self.city = player.city
    self.married = True
    self.age = random.randint(17,75)
    self.health = random.randint(0,100)
    self.relationship_level = random.randint(50,100)
    self.money = random.randint(100,10000)
    self.life = True
    self.last_asked = -1
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

    
  



class Job():
  def __init__(self):
    self.salary = 26000 #default salary for someone starting level in a job without a degree
    self.experience_required = 20
    create_job(self,'')
    self.promote_asked = -1
    self.work_hard=-1
    if self.education[0] != None:
      self.salary = random.randint(35000,40000)# sets random salary of the job
      self.skill_required = random.randint(20,60)
        
  def promote(self,player):
    if player.age> self.promote_asked:

      if self.work_ethic>60:
        
        if 'Junior' or 'Apprentice' in self.title:

          self.salary += random.randint(1000,9000)
          player.experience+=20
          self.work_life_balance = random.randint(1,10)
          self.title=self.title.replace('Junior ','')
          self.title=self.title.replace('Apprentice ','')
          return f'You were promoted to a {self.title}'
        
        elif 'Senior' or 'Expert' in self.title:

          self.salary += random.randint(5000,13000)

        else :

          self.salary += random.randint(1000,20000)
          self.work_life_balance = random.randint(1,10)
          player.experience+=40

          if self.education[0]== None:
            self.title='Expert ' + self.title
            return f'You were promoted to a {self.title}'
          
          else:
             
             self.title='Senior ' + self.title
             return f'You were promoted to a {self.title}'
      else:
         f'You don\'t quailfy for a promotion'
      
    else:
       return ''

  def work(self,player):
    self.work_ethic+=random.randint(1,7)
    self.work_ethic=check_values(self.work_ethic,100,0)
    player.mood += random.randint(-10,5)
    player.intelligence += random.randint(-5,5)
    player.health+= self.work_life_balance*random.randint(-5,0)
    
  def quit_job(self,player):
    text = f'You quit working as a {self.title} at {self.work_place}'
    player.job= None
    return text
    
  def apply_for_job(self,player):
    if self.asked is False:
      if (player.education in self.education):
        if player.experience >=self.experience_required:
          if player.job is not None:
            text = f'You quit working at {player.job.work_place} to work as a {self.title} at {self.work_place}'
            player.job= self
            self.asked = True
            return text
          else:
            player.job= self
            self.asked = True
            return f'You got the {self.title} job at {self.work_place}'
      else:
        self.asked = True
        return f'You did not get the {self.title} job'

    return ''
  
  def check_maxxed(self):
    if self.work_ethic>100:
      self.work_ethic = 100

class Junior_Job(Job):
  def __init__(self):
    super().__init__()
    self.salary = 13000 #default salary for someone starting level in a job without a degree
    self.experience_required = -1
    create_job(self,'Junior')
    if self.education[0] !=  None :
      self.salary = random.randint(24000,29000)# sets random salary of the job
      self.skill_required = random.randint(0,40)
      
      
class Senior_Job(Job):
  def __init__(self):
    super().__init__()
    starting_salary = 35000 #default salary for someone starting level in a job without a degree
    self.experience_required = 40
    create_job(self,'Senior')
    if self.education[0] != None :
      self.salary = random.randint(55000,80000)# sets random salary of the job
      self.skill_required = random.randint(60,80)


class Property():
  def __init__(self):
    random_value= random.choice(list(property_names.items()))
    x= random_value[0]
    self.condition = random.randint(1,100)
    self.price =round(15850000 * (0.6309 ** x) + self.condition, 2 - len(str(int(15850000 * (0.6309 ** x))))) *(self.condition/100)
    self.type = random_value[1]
    self.location = str(random.randint(1,270))+' '+random_choice(street_names)+' '+random_choice(location_names)
    self.price_paid = 0
    self.years_left =25
    self.strikes = 3
    self.bought = False
    self.yearly_payments = (self.price*0.9)/25
    self.mortgage = False
    self.asked = False

  def buy(self,player,mortgage):
    if self.asked is False:
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
      

class School:
  def __init__(self,dict):
    self.attendance = 100
    self.behaviour = random.randint(80,100)
    self.grades = random.randint(60,100)
    self.name = random_choice(school_prefixes)+' '+random_choice(dict)
    self.clubs = [random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs)]
    self.bunked=-1
    self.studied=-1
    self.joined_club=-1
    self.degrees =[random_list_choice(Degree_List),random_list_choice(Degree_List),random_list_choice(Degree_List),random_list_choice(Degree_List)]
  def change_attendance(self,player):
    if player.health < 70:
      self.attendance = check_values((self.attendance - random.randint(0,5)*(70/player.health)),100,0)
      player.mood = check_values((player.mood - random.randint(0,20)),100,0)
      
  def join_club(self,player,club):
    if player.age>self.joined_club:
      player.club = club
      self.behaviour = check_values((self.behaviour +random.randint(0,10)),100,0)
      self.grades = check_values((self.grades +random.randint(-5,10)),100,0)
      player.mood = check_values((player.mood +random.randint(0,20)),100,0)
      self.joined_club = player.age
      print(club)
  def study(self,player):
    if player.age>self.studied:
      self.grades = check_values((self.grades +random.randint(2,10)),100,0)
      player.intelligence =check_values((player.intelligence +random.randint(1,7)),100,0)
      self.studied = player.age
    
  def bunk_class(self,player):
    if player.age>self.bunked:
      self.behaviour = check_values((self.behaviour +random.randint(-20,0)),100,0)
      self.grades = check_values((self.grades +random.randint(-20,0)),100,0)
      player.mood = check_values((player.mood +random.randint(0,20)),100,0)
      self.bunked = player.age
    




class game():
  def __init__(self):
    self.player= Main_Character()
    self.running = True
    self.colour_1 = (105,146,248) 
    self.colour_2 = (77,238,125) 
    self.colour_3 = (245,179,234)
    self.fonts= [pygame.font.Font(None, 30), pygame.font.Font(None, 24),pygame.font.Font(None, 18)]
    self.jobs = generate_jobList()
    self.properties = generate_propertiesList()
    self.schools = generate_schools()
    self.npcs=generate_npcs(self.player)
    self.player.relationships=generate_family(self.player)
    self.player.school= self.schools[0]
    self.history = []
  
  def Change_Colour_Style_1(self,new_colour):
    self.colour_1=new_colour
    
  def Change_Colour_Style_2(self,new_colour):
    self.colour_2=new_colour
    
  def Change_Colour_Style_3(self,new_colour):
    self.colour_3=new_colour

  def random_yearly_actions(self):
    check_history(self.history)
    self.player.relationships= increment_npcs(self.player)
    self.jobs = generate_jobList()
    self.properties = generate_propertiesList()
    self.history.append(remove_dead_npc(self.player.relationships))
    self.npcs=generate_npcs(self.player)
    check_school_level(self)
    for property in self.player.properties:
      if property.mortgage is True:
        property.pay_mortgage(self.player)
        self.history.append(property.check_if_defaulted(self.player))
    if self.player.job is not None:
       self.player.money+= tax(self.player.job.salary)
    if self.player.significant_other is not None:
       if self.player.significant_other.life is False:
        self.player.significant_other =None
  
  def go_back_year(self):
    length = len(self.history)
    for i in range(length):
          if f'Age {self.player.age-1}:' in self.history[i]:
                removing= i
    self.player.age-=1

    del self.history[removing:length]

    
class Button():
    def __init__(self,image,x,y,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
      
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
   
class Colour_Button:
    def __init__(self, x, y, width, height,color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.x = x
        self.y = y
        self.hover_color =  hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect,border_radius=8)
        else:
            pygame.draw.rect(screen, self.color, self.rect,border_radius=8)
    

class Text_Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = None
        self.x = x
        self.y = y
        self.hover_color =  None

    def draw(self, screen,color, hover_color):
        self.color = color
        self.hover_color = hover_color
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect,border_radius=8)
        else:
            pygame.draw.rect(screen, self.color, self.rect,border_radius=8)

#---------------------------------------



def check_school_level(self):
  if self.player.age >= 18:
    self.player.school = self.schools[2]
    self.schools[1].behaviour = self.schools[2].behaviour
    self.schools[1].attendance = self.schools[2].attendance
    self.schools[1].grades=self.schools[2].grades
  elif self.player.age >= 13:
    self.player.school = self.schools[1]
    self.schools[0].behaviour = self.schools[1].behaviour
    self.schools[0].attendance = self.schools[1].attendance
    self.schools[0].grades=self.schools[1].grades

def create_job(self,Type):
  random_job = random_choice(Jobs_Dict)
  self.title=Type + ' ' + random_job[0]
  self.education = random_job[1:len(random_job)]# sets the education required for the job
  self.work_ethic = random.randint(1,100)
  self.work_place = random_choice(last_names) +' '+ random_choice(business_suffixes)
  self.asked = False
  self.work_life_balance = random.randint(1,10)
  if self.education[0] == None and Type == 'Junior':
    self.title='Apprentice' + ' ' + random_job[0]
  elif self.education[0] == None and Type == 'Senior':
    self.title='Expert' + ' ' + random_job[0]
    
def generate_propertiesList():
  list = []
  for i in range(0,6):
    list.append(Property())
  return(list)
def generate_jobList():
  list = []
  for i in range(0,3):
    list.append(Job())
    list.append(Junior_Job())
    list.append(Senior_Job())
  return(list)

def generate_schools():
  return [School(primary_school_names),School(secondary_school_names),School(univeristy_names)]

def generate_family(player):
  npc_list = [Parent(player),Parent(player)]
  if bool(random.getrandbits(1)) == True:
        sibling1= Sibling(player)
        npc_list.append(sibling1)
  return npc_list
#game subprograms
def sort_and_change(colour):
    for x,y in colours:
        if colour == x:
          return y
        
#choice subprograms
def check_available_choices(P):
  if P.age >=55:
    return elder_choices
  elif P.age >=30:
    return adult_choices
  elif P.age >=19:
    return young_adult_choices
  elif P.age >=12:
      return teen_choices
  elif P.age >=4:
    return child_choices
  else:
    return baby_choices
  
def tax(money):
    taxed_amount1= 0
    taxed_amount2 = 0
    if (money - 13000) >0:
        taxed_amount1 = (money - 13000)*0.125
        if (money-30000)> 0:
            taxed_amount2 = (money - 30000)* 0.35

    return ( money -taxed_amount1-taxed_amount2)

      

def random_choice(d):
    random_value= random.choice(list(d.items()))
    return random_value[1]

def random_list_choice(l):
      return(random.choice(l))
def random_choices_for_game(d):
    random_value= random.choice(list(d.items()))
    del d[random_value[0]]
    return random_value[1]
    
def show_choices_and_option(choice_dict):
  choice = random_choices_for_game(choice_dict)
  return([choice[0],choice[1],choice[2],choice[3],choice[4][0][0],choice[4][1][0],choice[4][2][0],choice[4][0][1],choice[4][1][1],choice[4][2][1],choice[4][0][2],choice[4][1][2],choice[4][2][2]])
  
  
#character subprograms
def set_values(self):
  isFemale = bool(random.getrandbits(1)) # randomly generates the gender of the character
  
  if isFemale is True:
    self.gender = 'female'
    self.name = random_choice(female_names)
  
  elif not isFemale :
    self.gender ='male'
    self.name = random_choice(male_names)
          
  self.surname =  random_choice(last_names)
def check_values(value,maxival,minival):
  if value > maxival:
    return maxival
  elif value < minival:
    return minival
  else:
    return value
  
def remove_dead_npc(npc_list):
  for npc in npc_list:
    if npc.life is False:
      death_announcment= f'{npc.name} {npc.surname} your {npc.relationship_type} has passed'
      npc_list.remove(npc)
      return death_announcment
  return ''
  
            
def increment_npcs(player):
  for npc in player.relationships:
    npc.age+=1
    if npc.age>50:
      npc.health=round(npc.health*(random.uniform(0.5,0.99)))
    else:
      npc.health=round(npc.health*(random.uniform(0.7,1.4)))
    npc.check_health()
  if random.randint(0,12)==7:
    player.relationships.append(Sibling(player))
  return player.relationships
    
    

    
def aging_cycle(player):
   if player.age>38:
      player.health=round(player.health*(random.uniform(0.73,1)))
     
#game implementation subprograms

def generate_npcs(player):
    npc_list=[Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player),Npc(player)]
      
    return npc_list
    
      
def generate_new_npc(player,npc_list):
  return(npc_list.append(Npc(player)))

def generate_sibling(player,parent1,parent2,npc_list):
    if random.randint(0,3)==2:
      if parent1.age+parent2.age<75 and random.randint(1,9)==3:
          npc_list.append(Sibling(player))


def health_check(self):
  self.health= check_values(self.health,100,0)
  if self.health< 5:
    self.life = False
    

  
def check_history(lst):
  result = []
  previous_empty = False

  for item in lst:
      if item != '':
          result.append(item)
          previous_empty = False
      elif not previous_empty:
          result.append(item)
          previous_empty = True
  return result
      
      
        

#found on github
def wrap_text(text, font, width):
    text_lines = text.replace('\t', '    ').split('\n')
    if width is None or width == 0:
        return text_lines

    wrapped_lines = []
    for line in text_lines:
        line = line.rstrip() + ' '
        if line == ' ':
            wrapped_lines.append(line)
            continue

        # Get the leftmost space ignoring leading whitespace
        start = len(line) - len(line.lstrip())
        start = line.index(' ', start)
        while start + 1 < len(line):
            # Get the next potential splitting point
            next = line.index(' ', start + 1)
            if font.size(line[:next])[0] <= width:
                start = next
            else:
                wrapped_lines.append(line[:start])
                line = line[start+1:]
                start = line.index(' ')
        line = line[:-1]
        if line:
            wrapped_lines.append(line)
    return wrapped_lines


def render_text_list(lines, font, colour=(255, 255, 255)):
    rendered = [font.render(line, True, colour).convert_alpha()
                for line in lines]

    line_height = font.get_linesize()
    width = max(line.get_width() for line in rendered)
    tops = [int(round(i * line_height)) for i in range(len(rendered))]
    height = tops[-1] + font.get_height()

    surface = pygame.Surface((width, height)).convert_alpha()
    surface.fill((0, 0, 0, 0))
    for y, line in zip(tops, rendered):
        surface.blit(line, (0, y))

    return surface
#..........................................
