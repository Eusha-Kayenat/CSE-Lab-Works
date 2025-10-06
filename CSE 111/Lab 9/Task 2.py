class Player:
  total=0
  lst=[]
  index=0
  @classmethod
  def info(cls):
    print(f"Total number of players: {cls.total}")
    print(f"Players enlisted so far: {','.join(Player.lst)}")
  def __init__(self,name=None,jearsy="10",team=None):
    self.name=name
    self.number=jearsy
    self.team=team
    Player.total+=1
    Player.lst.append(self.name)
    self.index=Player.index
    Player.index+=1
  def set_name(self,name):
    self.name=name
    Player.lst[self.index]=name
  def set_team(self,team):
    self.team=team
  def set_number(self,num):
    self.number=num
  def player_detail(self):
    return (f"Player Name: {self.name}\nJersey Number: {self.number}\nCountry: {self.team}")

print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()
