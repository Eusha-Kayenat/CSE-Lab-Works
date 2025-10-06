class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(SportsPerson):
  def __init__(self,team_name,name,role,goal,played):
    super().__init__(team_name,name,role)
    self.goal=goal
    self.played=played
    self.earning_per_match=(goal*1000)+(played*10)
    self.ratio=0
  def calculate_ratio(self):
    self.ratio= self.goal/self.played
  def print_details(self):
    print(super().get_name_team())
    print(f"Team Role: {self.role}")
    print(f"Total Goal: {self.goal}, Total Played: {self.played}")
    print(f"Goal Ratio: {self.ratio}")
    print(f"Match Earning: {self.earning_per_match}K")
class Manager(SportsPerson):
  def __init__(self,team_name,name,role,win):
    super().__init__(team_name,name,role)
    self.win=win
    self.earning_per_match=(win*1000)
  def print_details(self):
    print(super().get_name_team())
    print(f"Team Role: {self.role}")
    print(f"Total Win: {self.win}")
    print(f"Match Earning: {self.earning_per_match}K")
player_one = Player('Al-Nassr', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
