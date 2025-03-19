#first version
class Job:
  def __init__(self):
    starting_salary = 21000 #default salary for someone mid level in a job without a degree
    job_num = random.randint(0,263) #selects random jobs for the user to see
    for x,y in Jobs_Dict.items():   #sorts through the dictionary of jobs
      if x == job_num :
        self.name=y[0] #sets the job title
        self.education = y[1:len(y)] # sets the education required for the job
        if self.education[0] != 'None':
          starting_salary = 29000 # if the job has a required degree it will give you a higher starting salary
        self.salary = random.randint(starting_salary,starting_salary+7000) # sets random salary of the job

  def display_info(self):
    education = (', ').join(self.education)
    print('Name: {}\nEducation: {}\nSalary: {}\n\n'.format(self.name,education,self.salary))

class Junior_Job():
  def __init__(self):
    starting_salary = 13000 #default salary for someone starting level in a job without a degree
    randomx = random.randint(0,263) #selects random jobs for the user to see
    for x,y in Jobs_Dict.items():#sorts through the dictionary of jobs   
      if x == randomx :
        self.name='Junior '+y[0] #sets the job title, if you dont have the expreince required you will only be able to apply for junior jobs
        self.education = y[1:len(y)]# sets the education required for the job
        if self.education[0] != 'None':
          starting_salary = 24000  # if the job has a required degree it will give you a higher starting salary
        self.salary = random.randint(starting_salary,starting_salary+5000)# sets random salary of the job

class Senior_Job():
  def __init__(self):
    starting_salary = 26000 #default salary for someone advanced level in a job without a degree
    randomx = random.randint(0,263) #selects random jobs for the user to see
    for x,y in Jobs_Dict.items(): #sorts through the dictionary of jobs  
      if x == randomx :
        self.name='Senior '+y[0] #sets the job title, if you  have the expreince required you will  be able to apply for senior jobs
        self.education = y[1:len(y)]# sets the education required for the job
        if self.education[0] != 'None':
          starting_salary = 40000  # if the job has a required degree it will give you a higher starting salary
        self.salary = random.randint(starting_salary,starting_salary+20000)# sets random salary of the job




#final version
class Job():
  def __init__(self):
    self.salary = 26000 #default salary for someone starting level in a job without a degree
    self.experience_required = 20 # sets minimum expreience required
    create_job(self,'') #creates the job
    if self.education[0] != None:
      self.salary = random.randint(35000,40000)# sets random salary of the job
        
  def promote(self,player):
    if player.age> self.promote_asked: 

      if self.work_ethic>60:
        
        if 'Junior' or 'Apprentice' in self.title:
          self.salary += random.randint(1000,9000)
          player.experience =player.experience = check_values((player.experience+20),100,0)
          self.work_life_balance = random.randint(1,10)
          self.title=self.title.replace('Junior ','')
          self.title=self.title.replace('Apprentice ','')
          self.promote_asked= player.age
          return f'You were promoted to a {self.title}' # appends to the history
        
        elif 'Senior' or 'Expert' in self.title:
          self.salary += random.randint(5000,13000)

        else :
          self.salary += random.randint(1000,20000)
          self.work_life_balance = random.randint(1,10)
          player.experience+=40

          if self.education[0]== None:
            self.title='Expert ' + self.title
            self.promote_asked= player.age
            return f'You were promoted to a {self.title}'# appends to the history
          
          else:
             self.title='Senior ' + self.title
            self.promote_asked= player.age
             return f'You were promoted to a {self.title}' # appends to the history
      else:
        self.promote_asked= player.age
        return f'You don\'t quailfy for a promotion' # appends to the history
      
    else:
       return '' #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash

  def work(self,player):
    if player.age>   self.work_asked:
      self.work_ethic = check_values((self.work_ethic+random.randint(1,7)),100,0) # changes all values and checks them so they remain in the bounds
      player.mood =  check_values((player.mood+random.randint(-10,5)),100,0)
      player.intelligence  = check_values((player.intelligence+random.randint(1,7)),100,0)
      player.experience = check_values((player.experience+random.randint(1,7)),100,0)
      player.health+= check_values(player.health+(self.work_life_balance*random.randint(-5,0))),100,0
      self.work_asked= player.age
      return f'Your boss noticed you hard at work' # appends to the history
    else:
      return '' #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash
    
  def quit_job(self,player):
    text = f'You quit working as a {self.title} at {self.work_place}' # appends to the history
    player.job= None
    return text
    
  def apply_for_job(self,player):
    if self.apply_asked is False:
      if (player.education in self.education):
        if player.experience >=self.experience_required:
          if player.job is not None:
            text = f'You quit working at {player.job.work_place} to work as a {self.title} at {self.work_place}'# appends to the history
            player.job= self
            self.apply_asked = True
            return text 
          else:
            player.job= self
            self.apply_asked = True
            return f'You got the {self.title} job at {self.work_place}' # appends to the history
      else:
        self.apply_asked = True
        return f'You did not get the {self.title} job' # appends to the history

    return '' #fail safe incase the button is clicked multiple times. if there is nothing to append to history the game will crash

class Junior_Job(Job):
  def __init__(self):
    super().__init__()
    self.salary = 13000 #default salary for someone starting level in a job without a degree
    self.experience_required = -1 #sets minimum expreience
    create_job(self,'Junior')
    if self.education[0] !=  None :
      self.salary = random.randint(24000,29000)# sets random salary of the job
      
      
      
class Senior_Job(Job):
  def __init__(self):
    super().__init__()
    starting_salary = 35000 #default salary for someone starting level in a job without a degree
    self.experience_required = 40 #sets minimum expreience
    create_job(self,'Senior')
    if self.education[0] != None :
      self.salary = random.randint(55000,80000)# sets random salary of the job
      
      
def create_job(self,Type):
  random_job = random_choice(Jobs_Dict) #gets a random job from the job dict
  self.title=Type + ' ' + random_job[0] #sets the title of the job
  self.education = random_job[1:len(random_job)]# sets the education required for the job
  self.work_ethic = random.randint(35,70) #sets the work ethic the player has in this job 
  self.work_place = random_choice(last_names) +' '+ random_choice(business_suffixes) 
  self.apply_asked = False # checks if the player has applied for the job
  self.promote_asked = -1 # check when the player last asked for a promotion
  self.work_asked= -1 # check when the player last used the work function 
  self.work_life_balance = random.randint(1,10)
  if self.education[0] == None and Type == 'Junior':
    self.title='Apprentice' + ' ' + random_job[0]
  elif self.education[0] == None and Type == 'Senior':
    self.title='Expert' + ' ' + random_job[0]
