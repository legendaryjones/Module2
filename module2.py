



import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(15, 35)
        new_health = self.health + heal_amount

        if new_health > self.max_health:
            heal_amount = self.max_health - self.health  
            self.health = self.max_health
            print(f"{self.name} restored their health fully to their {self.max_health} maximum.")
        else:
            self.health = new_health
            print(f"{self.name} replenished {heal_amount} health points! Current health: {self.health}/{self.max_health}.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class 
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class 
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Berserk Mode')
        print('2. Second Wind')
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            self.attack_power = int(self.attack_power * 1.5)  # Increase attack power by 50%
            print(f"{self.name} enters Berserk Mode! Attack power is now {self.attack_power}.")

        elif action == '2':
           if self.health < self.max_health // 2:  # Only allow if health is low
             self.health = self.max_health
             print(f"{self.name} uses Second Wind! Health fully restored to {self.max_health}.")
           else:
                print(f"{self.name} is still strong and cannot use Second Wind yet!")
        else:
            # Default to Choice 1
            self.attack_power = int(self.attack_power * 1.5)  # Increase attack power by 50%
            print(f"{self.name} enters Berserk Mode! Attack power is now {self.attack_power}.")
        

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.shield_active = False

    def special_ability(self, opponent):
        print('\n Select Special Ability')
        print('1. Double Attack Power')
        print('2. Shield')
        
        action = input("Choose an Ability: ")
        
        if action == '1':
            self.attack_power *= 2
            print(f"{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power}")
        elif action == '2':
             self.shield_active = True
             print(f"{self.name} raises their shield! The next attack will deal half damage.")
        
        else:
            # Default to Choice 1
            self.attack_power *= 2
            print(f"{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power}")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
      return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
