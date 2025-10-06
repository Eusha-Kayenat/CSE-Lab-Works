class Team:
  def __init__(self,name=None):
    self.__name=name
    self.__lst=[]
  def setName(self,name):
    self.__name=name
  def addPlayer(self,player):
    self.__lst.append(player.name)
  def printDetail(self):
    print("=====================")
    print(f"Team: {self.__name}")
    print(f"List of Players:\n{self.__lst}")
    print("=====================")
class Player:
  def __init__(self,name):
    self.name=name

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail() yh
