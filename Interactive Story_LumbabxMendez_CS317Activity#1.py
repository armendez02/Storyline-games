print("You came home from school and entered the front door of the house, went inside and looked for your cat. You are standing at the front door, to your right is the kitchen, left is the living room, and in front of you is the stair to the bedroom."
)


def main_menu():
   while True:
      print("There are 3 places you can look for Victorina: (^◕.◕^)")
      print("1 - Kitchen\n2 - Living area\n3 - Bedroom")

      choice = input("Where do you want to go first? (1, 2, 3): ")
      if choice in ["1", "2", "3"]:
         sub_menu(choice)
      else:
         print("where is that place? :/ try again!")


def sub_menu(option):
   while True:
      if option == "1":
         print("\nAreas in the kitchen")
         print(
             "a - counter\nb - cupboard\nc - under the dining table\nd - go back"
         )
         action = input("choose an option (a, b, c, d):").strip().lower()
         if action == "a":
            print("aww she's not here :(")
         elif action == "b":
            print("oh not here, look for other places?")
         elif action == "c":
            print("oh she's not here, sorry!")
         elif action == "d":
            return
         else:
            print("go back?")

         input("\nPress enter to go back to the kitchen")

      elif option == "2":
         print("\nAreas in the living room:")
         print("a - sofa\nb - shoerack\nc - windows\nd - go back")
         action = input("choose an option (a, b, c, d):").strip().lower()
         if action == "a":
            print("only found a pair of socks, but no cat")
         elif action == "b":
            print(
                "you check the shoerack, but only found mismatched shoes but don't see victorina"
            )
         elif action == "c":
            print("you look out the window but don't see victorina")
         elif action == "d":
            return
         else:
            print("go back?")

         input("\nPress enter to go back to the living room")

      elif option == "3":
         print("\nAreas in the bedroom:")
         print(" a - Bathroom\n b - Cabinet\n c - Bed\n d - Go back")
         action = input("Choose an option(a, b, c, d):").strip().lower()
         if action == "a":
            print("Victorina's not here! :(")
         elif action == "b":
            print("She's not here, aaah: (")
         elif action == "c":
            print(
                "You check under the bed and see the sleeping victorina <3 :")
            return
         elif action == "d":
            return
         else:
            print("What's that?")

         input("\nPress enter to go back to the bedroom.")


if __name__ == "__main__":
   main_menu()
