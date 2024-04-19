class Country():
    Continent='Asia'
    def __init__(self,Name,Capital):
        self.Name=Name
        self.Capital=Capital
    def Greet(self,Message):
        print(f'{Message} {self.Name}')
My_country=Country("India",'Delhi')
print(My_country.Greet('Namestay'))