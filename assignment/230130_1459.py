class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs +=1
    
    def __del__(self):
        Doggy.num_of_dogs -=1
    
    def get_status(self):
        print(f'birth: {self.birth_of_dogs}, num: {self.num_of_dogs}')
    
    def bark(self):
        print("멍")


d1 = Doggy('멍멍이', '치와와')
print(d1.num_of_dogs, d1.birth_of_dogs)
d2 = Doggy('멍', '시추')
print(d2.num_of_dogs, d2.birth_of_dogs)
d3 = Doggy('멍이', '치와와')

