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


#professor
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0


    # 생성자
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        # 클래스 변수는 인스턴스로도 접근할 수 있고 클래스로도 접근할 수 있음
        # 하지만 클래스 변수는 클래스로 접근하는게 좋다

        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    

    # 소멸자
    def __del__(self):
        Doggy.num_of_dogs -= 1


    # 클래스 변수를 사용하면 클래스 메서드 사용하는게 좋다
    # 클래스 메서드 사용하면 cls 사용해서 접근할 수 있음
    @classmethod
    def get_status(cls):
        # 줄바꿈 파이썬에서는 \ 
        return f'Birth: {cls.birth_of_dogs} current: {cls.num_of_dogs}'


    def bark(self):
        return '멍'

d1 = Doggy('a', '진돗개')
d2 = Doggy('b', '시츄')
print(d1.bark())
del d2
print(Doggy.get_status())


# ![image](https://user-images.githubusercontent.com/83294376/215648186-108a9481-4931-4ffc-8bda-6361ddf45fb4.png)
