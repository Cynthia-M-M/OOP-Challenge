class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} is already full and content.")
        else:
            self.hunger = max(0, self.hunger - 3)  # Reduces hunger by 3, but not below 0
            self.happiness = min(10, self.happiness + 1)  # Increases happiness by 1, but not above 10
            print(f"{self.name} ate and looks happier! 🍖")

    def sleep(self):
        if self.energy >= 10:
            print(f"{self.name} is already fully rested, energized, and ready to do things! 🎉")
        else:
            self.energy = min(10, self.energy + 5)  # Increases energy by 5, but not above 10
            print(f"{self.name} had a refreshing nap! 💤")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play. Let them sleep! 😓")
        elif self.hunger >= 8:
            print(f"{self.name} is too hungry to play. Please feed them! 🍽️")
        else:
            self.energy = max(0, self.energy - 2)  # Decreases energy by 2, but not below 0
            self.hunger = min(10, self.hunger + 1)  # Increases hunger by 1, but not above 10
            self.happiness = min(10, self.happiness + 2)  # Increases happiness by 2, but not above 10
            print(f"{self.name} played and had fun! 🎾")

    def train(self, trick):
        if self.energy < 3:
            print(f"{self.name} is too tired to learn new tricks. 😴")
        elif self.hunger >= 8:
            print(f"{self.name} is too hungry to concentrate on training. 🍽️")
        elif trick.lower() in [t.lower() for t in self.tricks]:  # Case-insensitive check
            print(f"{self.name} already knows the trick '{trick}'! 🐶")
        else:
            self.tricks.append(trick)  # Adds the new trick to the list
            self.energy = max(0, self.energy - 3)  # Decreases energy by 3, but not below 0
            self.happiness = min(10, self.happiness + 1)  # Increases happiness by 1, but not above 10
            print(f"{self.name} learned a new trick: {trick}! 🧠")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f" - {trick}")
        else:
            print(f"{self.name} has not learned any tricks yet.")

    def get_status(self):
        print(f"\n📋 Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

        # Mood feedback based on hunger
        if self.hunger >= 8:
            print(f"⚠️ {self.name} is starving! Please feed them.")
        elif self.hunger >= 5:
            print(f"{self.name} seems a bit hungry. 🍽️")
        elif self.hunger <= 2:
            print(f"{self.name} is well-fed and satisfied. 😊")

        # Feedback based on energy
        if self.energy <= 2:
            print(f"⚠️ {self.name} is very tired. 😴")

        # Feedback based on happiness
        if self.happiness <= 3:
            print(f"😢 {self.name} looks sad. Play with them!")

        # Mood check for boredom
        if self.happiness >= 7 and self.energy >= 5 and self.hunger <= 5:
            print(f"😊 {self.name} is feeling great today!")
        elif self.happiness <= 5 and self.energy >= 5:
            print(f"{self.name} might be getting bored... try playing with them! 🎾")
