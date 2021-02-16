
class TravelPackage:

    DESTINATIONS = [
        ("Japan", 1500),
        ("Columbia", 1100),
        ("France", 1300)
    ]

    def __init__(self):
        self.user_budget = None
        self.user_destination = None

    def get_user_budget(self):
        self.user_budget = int(input("How much can you spend? "))

    def get_possible_destinations(self):
        possibles = []
        for dest in self.DESTINATIONS:
            if dest[1] <= self.user_budget:
                possibles.append(dest[0])
        return possibles

    def display_possible_destinations(self):
        print(f"Here are your options: {self.get_possible_destinations()}")

    def get_user_destination(self):
        possible_dest = input("Where do you want to go? ")
        if possible_dest in self.get_possible_destinations():
            self.user_destination = possible_dest
        else:
            raise Exception()
        
    def display_final_confirmation_message(self):
        print(f"Thanks, you are headed to {self.user_destination}")


tp = TravelPackage()
tp.get_user_budget()
tp.get_possible_destinations()
tp.display_possible_destinations()
tp.get_user_destination()
tp.display_final_confirmation_message()
