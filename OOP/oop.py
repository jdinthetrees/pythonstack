
class User:
    #Attibutes / Properties
    def __init__(self, name_input, height_input, email_input, 
    location_input, fav_fruit_input):
        self.name = name_input
        self.height = height_input
        self.email = email_input
        self.location = location_input
        self.fav_fruit = fav_fruit_input
    #Methods

    def say_hi(self, person):
        print(f"Hi {person}! My name is", self.name)

mary = User("Mary", "Five foot nine inches", "foam_foamerton@foam.com", "Seattle, WA", "lychee")
xavier = User("Xavier", 4, "email@fake.com", "Philly, PA", "dragonfruit")

print(mary.email)
print(xavier.email)

mary.say_hi(xavier)
xavier.say_hi(mary)