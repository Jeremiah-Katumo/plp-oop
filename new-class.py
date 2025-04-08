# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
        self.is_cape_on = False

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I have the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their {self.power} power!")

    def toggle_cape(self):
        self.is_cape_on = not self.is_cape_on
        state = "on" if self.is_cape_on else "off"
        print(f"{self.name}'s cape is now {state}.")

# Subclass with inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} takes off and flies at {self.flight_speed} km/h!")

    # Polymorphism example
    def use_power(self):
        print(f"{self.name} takes to the sky and uses their flying power with speed {self.flight_speed} km/h!")

hero1 = Superhero("Shadow Blade", "Invisibility", "Dark Realm")
hero1.introduce()
hero1.use_power()
hero1.toggle_cape()

hero2 = FlyingHero("Sky Streak", "Flight", "Sky Kingdom", 1200)
hero2.introduce()
hero2.use_power()
hero2.fly()
