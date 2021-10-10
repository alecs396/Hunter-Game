"""The hunter guesses the prey's location and the prey provides a hint - that's confidence! Guessing continues until the prey is found."""

import random

class Prey:
    """prey is an animal that is hunted. The responsibility of Prey is to know their position and hint about it. That's confidence!"""

    def __init__(self):
        self.location = random.randint(1,1000)
        self.last_guess = 0

    def give_hint(self, guess):
        """
        Accepts a parameter called guess (an integer) and compares the value to its location. The method should return a hint.
        """
        new_distance = abs(self.location - guess)
        old_distance = abs(self.location - self.last_guess)

        hint = ""
        if new_distance == 0:
            hint = "You found me! (;_;)"
        elif new_distance > old_distance:
            hint = "Definately farther! (^_^)"
        elif new_distance < old_distance:
            hint = "Definately closer! (>_<)"
        else:
            hint = "Same as before. (-_-)"
        
        self.last_guess = guess
        return hint

    def is_found(self):
        """
        Returns True if the last guess is the same as the prey's location.
        """
        return self.last_guess == self.location


class Hunter:
    """A hunter is a person who searches. The responsibility of Hunter is to stalk prey when requested."""

    def stalk(self, prey):
        """
        prompt the user for a guess, invoke the give_hint method on the prey, and print the hint.
        """
        guess = int(input("\nGuess a number: "))
        proximity = prey.give_hint(guess)
        print(proximity)

class Guide:
    """ A guide is a person who advises or shows the way to others. The responsibility of Guide is to control the sequence of the hunt."""

    def start_hunt(self):
        hunter = Hunter()
        prey = Prey()
        while not prey.is_found():
            hunter.stalk(prey)

if __name__ == "__main__":
    guide = Guide()
    guide.start_hunt()