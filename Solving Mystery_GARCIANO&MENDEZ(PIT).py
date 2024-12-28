import time
import sys

class investigation:
    """Manages the player's investigation."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            slow_print(f"You have added {item} to your investigation as evidence.")
        else:
            slow_print(f"{item} is already in your investigation.")

    def has_item(self, item):
        return item in self.items

    def show_investigation(self):
        if self.items:
            slow_print("Your evidence contains:")
            for item in self.items:
                slow_print(f"- {item}")
        else:
            slow_print("Your evidence is empty.")

investigation = investigation()

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main_menu():
    """Displays the main menu and handles user input."""
    print("\nWelcome to The Enigmatic Case of the Vanishing Heiress\n")
    print("1. Start Game")
    print("2. Quit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            start_game()
            break
        elif choice == "2":
            slow_print("Goodbye, detective.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")

def start_game():
    """Begins the storyline and handles the first interactions."""
    slow_print("Scenario 1: The Disappearance of heir")
    slow_print("Elara Sinclair, the sole heiress of the Sinclair fortune, vanished without a trace on a stormy night in 1999.")
    slow_print("Her disappearance shocked the city of Ravenswood, known for its affluent society and hidden secrets.")
    slow_print("Elara was last seen at the grand Sinclair mansion, a sprawling estate filled with ancient artifacts and hidden passageways.")
    slow_print("Detective Evelyn Hart has been assigned to solve this case.")
    interview_guests()

def interview_guests():
    """Introduces the suspects and begins the investigation."""
    slow_print("\nScenario 2: The Shadow of Suspicion")
    slow_print("Evelyn begins by interviewing the guests who attended the gala on the night of Elara's disappearance.")

    print("\nWho would you like to question first?")
    print("1. Lord Reginald Ashcroft - A family friend with financial troubles.")
    print("2. Lady Isabella Thornton - A socialite with a long-standing rivalry with Elara.")
    print("3. Dr. Charles Whitmore - The family physician with a dark secret.")
    print("4. Marjorie Sinclair - Elara's enigmatic aunt with a mysterious past.")

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                slow_print("Lord Reginald admits he had financial troubles but insists he would never harm Elara.")
                investigation.add_item("Reginald's Statement")
                break
            elif choice == 2:
                slow_print("Lady Isabella, known for her rivalry with Elara, claims she left the gala early.")
                investigation.add_item("Isabella's Statement")
                break
            elif choice == 3:
                slow_print("Dr. Whitmore seems uneasy but provides no useful information.")
                investigation.add_item("Whitmore's Statement")
                break
            elif choice == 4:
                slow_print("Marjorie Sinclair offers vague answers, but her demeanor raises Evelyn's suspicions.")
                investigation.add_item("Marjorie's Statement")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    find_diary()

def find_diary():
    """Discovers Elara's hidden diary, introducing new leads."""
    slow_print("\nScenario 3: The Hidden Diary")
    slow_print("While searching Elara's room, Evelyn discovers a hidden diary.")
    slow_print("The diary reveals that Elara had been receiving threatening letters filled with cryptic warnings.")
    slow_print("It also mentions a secret love affair with a man known as 'A.S.'")
    investigation.add_item("Elara's Diary")
    follow_clues()

def follow_clues():
    """Follows the clues from Elara's letters."""
    slow_print("\nScenario 4: The Cryptic Clues")
    slow_print("Evelyn follows the clues from the threatening letters, leading her to an abandoned warehouse on the outskirts of Ravenswood.")
    slow_print("Inside, she finds an old chest containing more letters, maps, and a photograph of Elara with a man whose face is partially obscured.")
    slow_print("The initials 'A.S.' are scrawled on the back of the photograph.")

    while True:
        choice = input("\nDo you want to investigate 'A.S.' further? (yes/no): ").lower()
        if choice == "yes":
            investigate_as()
            break
        elif choice == "no":
            slow_print("Evelyn decides to focus on other leads, but the mystery deepens. Game over.")
            sys.exit()
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def investigate_as():
    """Investigates Arthur Sterling and uncovers new twists."""
    slow_print("\nScenario 5: A Race Against Time")
    slow_print("Evelyn learns that 'A.S.' is Arthur Sterling, a former Sinclair employee with a grudge against the family.")
    slow_print("Arthur had been meeting Elara to exact revenge, but he is found dead in his apartment, an apparent suicide.")
    slow_print("A note in his apartment confesses to Elara's abduction, but Evelyn suspects foul play.")
    confront_marjorie()

def confront_marjorie():
    """Confronts Marjorie Sinclair, unraveling the final twist."""
    slow_print("\nScenario 6: Unraveling the Mystery")
    slow_print("Evelyn discovers that Marjorie Sinclair orchestrated the entire plot to gain control of the Sinclair fortune.")
    slow_print("Marjorie manipulated Arthur and staged his death to cover her tracks.")

    print("\nWhat do you do?")
    print("1. Accuse Marjorie outright.")
    print("2. Gather more evidence before confronting her.")

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                slow_print("Marjorie confesses under pressure, revealing that Elara is alive and hidden in a secluded cabin.")
                end_game()
                break
            elif choice == 2:
                slow_print("Evelyn finds more evidence linking Marjorie to the crime and forces her to confess.")
                end_game()
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def end_game():
    """Resolves the mystery and concludes the story."""
    slow_print("\nScenario 7: The Resolution")
    slow_print("Evelyn rescues Elara from the cabin and brings her back to Ravenswood.")
    slow_print("The revelation of Marjorie's betrayal shakes the Sinclair family, but justice is served.")
    slow_print("Elara vows to rebuild her family's legacy with integrity, and Evelyn is hailed as a hero.")
    slow_print("Congratulations, detective. You have solved The Enigmatic Case of the Vanishing Heiress!")

# Start the game
if __name__ == "__main__":
    main_menu()
