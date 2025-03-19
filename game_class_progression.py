#first version

class Game:
    def __init__(self):
        self.Game_Cont = True

    def Game_Save(self,char):
        file = open('file.txt','w')
        file.write(char.name+'\n'+char.surname+'\n'+str(char.age)+'\n'+str(char.health)+'\n'+str(char.hygiene)+'\n'+str(char.intelligence)+'\n'+str(char.mood)+'\n'+str(char.money)+'\n')
        file.close()

    def Game_Import(self,char):
        file = open('file.txt','r')
        f=file.readlines()
        for i in range(len(f)):
            f[i]=f[i].strip('\n')
        char.set_vals(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7])

  #second version

  class Game:
    def __init__(self):
        self.Game_Cont = True
        self.main1 = (255,0,0) #red
        self.main2 = (0,255,0) #green
        self.main3 = (0,0,255) # blue

    def Game_Save(self,char):
        file = open('file.txt','w')
        file.write(char.name+'\n'+char.surname+'\n'+str(char.age)+'\n'+str(char.health)+'\n'+str(char.hygiene)+'\n'+str(char.intelligence)+'\n'+str(char.mood)+'\n'+str(char.money)+'\n')
        file.close()

    def Game_Import(self,char):
        file = open('file.txt','r')
        f=file.readlines()
        for i in range(len(f)):
            f[i]=f[i].strip('\n')
        char.set_vals(f[0],f[1],f[2],f[3],f[4],f[5],f[6],f[7])
    #settings
    def Change_Colour_Style_main1(self,new_colour):
        self.main1=sort_and_change(new_colour)
    def Change_Colour_Style_main2(self,new_colour)
        self.main2=sort_and_change(new_colour):
    def Change_Colour_Style_main(self,new_colour):
        self.main3=sort_and_change(new_colour)


#third version

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

