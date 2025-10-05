class MangoTree:
    def __init__(self, variety):
        self.variety = variety
        self.height = 1 
        self.number_of_mangoes = 0 

    def grow_and_bear_fruits(self, years):
        self.height += 3 * years
        if self.variety == "Amrapali":
            self.number_of_mangoes = self.height * 15 
        elif self.variety == "Gopalbhog":
            self.number_of_mangoes = self.height * 10  

mangoTree1 = MangoTree("Gopalbhog")
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")

mangoTree2 = MangoTree("Amrapali")
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

mangoTree1.grow_and_bear_fruits(5)
mangoTree2.grow_and_bear_fruits(5)

print("Updated details after 5 years:")
print("=====================================")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
