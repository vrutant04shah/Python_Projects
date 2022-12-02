print("FRIENDS - QUIZ")
print("Let's find out which character you are.")

print("\nQuestion 1 : How would your friends describe you? "
      "\nOption1 : Sarcastic"  # Chandler
      "\nOption2 : Nerdy"  # Ross
      "\nOption3 : Foodie"  # Joey
      "\nOption4 : Weird"  # Phoebe
      "\nOption5 : Control freak"  # Monica
      "\nOption6 : Cutie")  # Rachel

Answer1 = input("Enter your option : ")

print("\nQuestion 2 : How close are you with your parents?"
      "\nOption1 : I never knew them"  # Phoebe
      "\nOption2 : Embarrassed by them"  # Chandler
      "\nOption3 : Pretty close"  # Ross
      "\nOption4 : Preferred your sibling"  # Monica
      "\nOption5 : Only meet on holidays"  # Joey
      "\nOption6 : Scared by them")  # Rachel

Answer2 = input("Enter your option : ")

print("\nQuestion 3 : How do you feel about animals?"
      "\nOption1 : Monkeys are cool"  # Ross
      "\nOption2 : Scared of cute dogs"  # Chandler
      "\nOption3 : Not a food item"  # Phoebe
      "\nOption4 : Cat with no hair are purrfect"  # Rachel
      "\nOption5 : They taste amazing!"  # Joey
      "\nOption6 : They are fine")  # Monica

Answer3 = input("Enter your option : ")

print("\nQuestion 4 : What is the first thing that you do after coming to home?"
      "\nOption1 : Munch on snacks"  # Joey
      "\nOption2 : Clean my room"  # Monica
      "\nOption3 : Go for shopping"  # Rachel
      "\nOption4 : Hang with my friends"  # Phoebe
      "\nOption5 : Watch television"  # Chandler
      "\nOption6 : Apply hair gel")  # Ross

Answer4 = input("Enter your option : ")

print("\nQuestion 5 : What thing about people annoys you?"
      "\nOption1 : People eating animals"  # Phoebe
      "\nOption2 : Eating food from my plate"  # Joey
      "\nOption3 : My sibling's success"  # Rachel
      "\nOption4 : Messy people"  # Monica
      "\nOption5 : An annoying laugh"  # Chandler
      "\nOption6 : None believer of science")  # Ross

Answer5 = input("Enter your option : ")

print("\nQuestion 6 : What job would you love the most?"
      "\nOption1 : Singer"  # Phoebe
      "\nOption2 : Cooking for people"  # Monica
      "\nOption3 : Famous star"  # Joey
      "\nOption4 : Cool Scientist"  # Ross
      "\nOption5 : Fashion"  # Rachel
      "\nOption6 : I don't know - STOP asking me")  # Chandler

Answer6 = input("Enter your option : ")

print("\nQuestion 7 : Favourite thing to do on holidays."
      "\nOption1 : I hate them!"  # Chandler
      "\nOption2 : Being host"  # Monica
      "\nOption3 : Eating food"  # Joey
      "\nOption4 : Playing for geller cup"  # Ross
      "\nOption5 : Working for charity"  # Phoebe
      "\nOption6 : Meeting cute people")  # Rachel

Answer7 = input("Enter your option : ")

print("\nQuestion 8 : What would your favourite thing to do on the roof?"
      "\nOption1 : Stargazing"  # Ross
      "\nOption2 : Having a party"  # Monica
      "\nOption3 : Coming straight down"  # Phoebe
      "\nOption4 : Look at other people"  # Joey
      "\nOption5 : Kiss someone"  # Rachel
      "\nOption6 : Standing alone")  # Chandler

Answer8 = input("Enter your option : ")

print("\nQuestion 9 : What would you order in a cafe?"
      "\nOption1 : Hot tea"  # Phoebe
      "\nOption2 : Iced caramel macchiato"  # Ross
      "\nOption3 : An Americano"  # Rachel
      "\nOption4 : Coffee with extra cream and sugar"  # Chandler
      "\nOption5 : The house blend"  # Monica
      "\nOption6 : Cow's fat")  # Joey

Answer9 = input("Enter your option : ")

print("\nQuestion 10 : What clothes do you prefer?"
      "\nOption1 : Coat and suits"  # Ross
      "\nOption2 : Expandable pants"  # Joey
      "\nOption3 : Cute dresses"  # Monica
      "\nOption4 : Latest fashion only"  # Rachel
      "\nOption5 : Comfortable and long skirts"  # Phoebe
      "\nOption6 : Teenage boys clothes")  # Chandler

Answer10 = input("Enter your option : ")

chandler_points = 0
joey_points = 0
ross_points = 0
rachel_points = 0
monica_points = 0
phoebe_points = 0

if Answer1 == '1':
    chandler_points += 1
elif Answer1 == '2':
    ross_points += 1
elif Answer1 == '3':
    joey_points += 1
elif Answer1 == '4':
    phoebe_points += 1
elif Answer1 == '5':
    monica_points += 1
elif Answer1 == '6':
    rachel_points += 1

if Answer2 == '1':
    phoebe_points += 1
elif Answer2 == '2':
    chandler_points += 1
elif Answer2 == '3':
    ross_points += 1
elif Answer2 == '4':
    monica_points += 1
elif Answer2 == '5':
    joey_points += 1
elif Answer2 == '6':
    rachel_points += 1

if Answer3 == '1':
    ross_points += 1
elif Answer3 == '2':
    chandler_points += 1
elif Answer3 == '3':
    phoebe_points += 1
elif Answer3 == '4':
    rachel_points += 1
elif Answer3 == '5':
    joey_points += 1
elif Answer3 == '6':
    monica_points += 1

if Answer4 == '1':
    joey_points += 1
elif Answer4 == '2':
    monica_points += 1
elif Answer4 == '3':
    rachel_points += 1
elif Answer4 == '4':
    ross_points += 1
elif Answer4 == '5':
    phoebe_points += 1
elif Answer4 == '6':
    chandler_points += 1

if Answer5 == '1':
    phoebe_points += 1
elif Answer5 == '2':
    joey_points += 1
elif Answer5 == '3':
    rachel_points += 1
elif Answer5 == '4':
    monica_points += 1
elif Answer5 == '5':
    chandler_points += 1
elif Answer5 == '6':
    ross_points += 1

if Answer6 == '1':
    phoebe_points += 1
elif Answer6 == '2':
    monica_points += 1
elif Answer6 == '3':
    joey_points += 1
elif Answer6 == '4':
    ross_points += 1
elif Answer6 == '5':
    rachel_points += 1
elif Answer6 == '6':
    chandler_points += 1

if Answer7 == '1':
    chandler_points += 1
elif Answer7 == '2':
    monica_points += 1
elif Answer7 == '3':
    joey_points += 1
elif Answer7 == '4':
    ross_points += 1
elif Answer7 == '5':
    phoebe_points += 1
elif Answer7 == '6':
    rachel_points += 1

if Answer8 == '1':
    ross_points += 1
elif Answer8 == '2':
    monica_points += 1
elif Answer8 == '3':
    phoebe_points += 1
elif Answer8 == '4':
    joey_points += 1
elif Answer8 == '5':
    rachel_points += 1
elif Answer8 == '6':
    chandler_points += 1

if Answer9 == '1':
    phoebe_points += 1
elif Answer9 == '2':
    ross_points += 1
elif Answer9 == '3':
    rachel_points += 1
elif Answer9 == '4':
    chandler_points += 1
elif Answer9 == '5':
    monica_points += 1
elif Answer9 == '6':
    joey_points += 1

if Answer10 == '1':
    ross_points += 1
elif Answer10 == '2':
    joey_points += 1
elif Answer10 == '3':
    monica_points += 1
elif Answer10 == '4':
    rachel_points += 1
elif Answer10 == '5':
    phoebe_points += 1
elif Answer10 == '6':
    chandler_points += 1

points = {'Chandler': chandler_points, 'Ross': ross_points, 'Rachel': rachel_points, 'Monica': monica_points, 'Joey': joey_points, 'Phoebe': phoebe_points}
character = max(zip(points.values(), points.keys()))[1]
print(f"You are {character} of the F.R.I.E.N.D.S.")
