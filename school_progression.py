#first version
def find_school_name(school):
    random_school = random.randint(0,len(school))
    for x,y in school:
        if random_school == x:
           return y
class School:
    def __init__(self,city,level):
        if level == 'Primary':
            self.name=city + find_school_name(primary_school_names)
        elif level == 'Secondary':
            self.name=city + find_school_name(primary_school_names)   
        elif level == 'University':
            self.name=city + find_school_name(primary_school_names)            


#second version
class School:
  def __init__(self,city,player):
    name=find_school_name(player)
    if name  is not False:
       self.name = city +' '+ name

def find_school_name(player):
    if player.age==5:
        school=primary_school_names
        random_school = random.randint(0,len(school))
        for x,y in school:
            if random_school == x:
                return y
    elif player.age == 12:
        school = secondary_school_names
        random_school = random.randint(0,len(school))
        for x,y in school:
            if random_school == x:
                return y
    elif player.age == 18:
        school = univeristy_names
        random_school = random.randint(0,len(school))
        for x,y in school:
            if random_school == x:
                return y
    else:
       return False
#third verison
class School:
  def __init__(self,dict):
    self.attendance = 100
    self.behaviour = 100
    self.grades = 100
    self.name = random_choice(school_prefixes)+' '+random_choice(dict)
    self.clubs = [random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs),random_choice(school_clubs)]
      
  def change_attendance(self,player):
    if player.health < 70:
      self.attendance += -random.randint(0,5)*(70/player.health)
      player.mood += random.randint(-20,0)
      
  def change_behaviour(self, player):
    self.behaviour +=random.randint(-20,0)
    self.grades += random.randint(-20,0)
    player.mood += random.randint(-20,0)
    
  def study(self,player):
    self.grades += random.randint(0,8)
    player.intelligence += random.randint(1,7)

#final version
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
    
  def join_club(self,player,club):
    if player.age>self.joined_club:
      
      if player.club is not None:
        self.joined_club = player.age
        return f'You are already in the {player.club}, you can\'t join the {club}'
        
      else:
        player.club = club
        self.behaviour = check_values((self.behaviour +random.randint(0,10)),100,0)
        self.grades = check_values((self.grades +random.randint(5,10)),100,0)
        player.mood = check_values((player.mood +random.randint(0,20)),100,0)
        self.joined_club = player.age
        return f'You joined the {club} at school'
        
    else:
      return ''
    
  def study(self,player):
    if player.age>self.studied:
      self.grades = check_values((self.grades +random.randint(2,10)),100,0)
      player.intelligence =check_values((player.intelligence +random.randint(1,7)),100,0)
      self.behaviour = check_values((self.behaviour +random.randint(2,7)),100,0)
      player.mood =check_values((player.mood +random.randint(5,12)),100,0)
      self.studied = player.age
      return 'You studied extra hard at school'
    else:
      return ''
    
  def bunk_class(self,player):
    if player.age>self.bunked:
      self.behaviour = check_values((self.behaviour +random.randint(-20,0)),100,0)
      self.grades = check_values((self.grades +random.randint(-20,0)),100,0)
      player.intelligence =check_values((player.intelligence -random.randint(1,7)),100,0)
      player.mood = check_values((player.mood +random.randint(0,20)),100,0)
      self.bunked = player.age
      return 'You decided to skip class'
    else:
      return ''

