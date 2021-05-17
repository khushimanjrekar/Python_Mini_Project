def play_again():
  print("\nDo you want to play again? (yes or no)")
  answer = input(":-").lower()

  if "yes" in answer:
    start()
  elif "no" in answer:
    exit()

def game_over(reason):
  print("\n" + reason)
  print("Game Over!")
  print("Precautions to be taken :-")
  print("Clean your hands often. Use soap and water, or an alcohol-based hand rub.\nMaintain a safe distance from anyone who is coughing or sneezing.")
  print("Wear a mask when physical distancing is not possible.\nDon’t touch your eyes, nose or mouth.")
  print("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\nStay home if you feel unwell.")
  print("If you have a fever, cough and difficulty breathing, seek medical attention.")
  play_again()

def test_room3():
  print("\nHere are three boxes, each box has some inscription on it.")
  print("To get a vaccine you have to select one correct box.")
  print("The box which you choose will be your's along with the vaccine.")
  print("Which box would you choose? (1, 2 or 3)")
  print("Choose wisely!!!")
  print("1). Who chooses me shall gain what many desire.(Golden box)")
  print("2). Whoever chooses me shall gain as much they deserve.(Silver box)")
  print("3). Whoever chooses me must give and risk all that they possess.(Lead box)")
  answer = input(":-")
  
  if answer == "1":
    game_over("All that gilters is not gold! \nProbably,your preference was towards the golden box and not the vaccine \nHence you have chosen the wrong box")
  elif answer == "2":
    game_over("\nYou should not be materialistic in your choice!\nProbably,your preference was towards the silver box and not the vaccine\nYou have chosen the wrong box")
  elif answer == "3":
    print("You're not a voracious person, may you always be fortunate and choose as truly as here!")
    print("You won the game and successfuly defeated COVID !!")
    play_again()  
  else :
    game_over("Go and learn how to type a number.")

def test_room2():
  print("\nYou're stuck in a city due to pandemic and \nyour family stays in another city.")
  print("Now its been a year what would you choose to do (1 or 2)")
  print("1). You getting vaccinated and then go to meet them with all precautions?")
  print("2). You still not wish to get vaccinated and reach there risking your family's safety.")
  answer = input(":-")

  if answer == "1":
    print("\nWe're happy that you got the importance of vaccination.")
    print("Now we hope that you would like to take a vaccine")
    print("Here is last level ")
    test_room3()
  elif answer == "2":
    game_over("\nYou're careless person,you must think of your personal saftey as well as saftey of your family and society")
  else:
    game_over("Go and learn how to type a number.")

def test_room1():
  print("\nToday it's your friends Birthday.")
  print("He's inviting you for a birthday Party.")
  print("But as we all know we're in a pandemic!")
  print("What would you do? (1 or 2)")
  print("1). Go to the party with all precautions.")
  print("2). Say no and make that friend aware of the situation``.")
  answer = input(":-")
  
  if answer == "1":
    game_over("You are careless person!You should be aware that social gathering is not allowed in this pandemic")
  elif answer == "2":
    print("\nYou're a good friend and a good citizen as you know the seriousness of pandemic ")
    print("Here is last level ")
    test_room3()
  else:
    game_over("Don't you know how to type a number?")

def start():
  name = input("Enter your name : ")

  print("Welcome to the New Normal!,", name)
  print("Beware this is a game, vaccination is guaranteed unlike reality!")
  print("Do you wish to take a vaccine? (yes or no)")
  answer = input(":-").lower()

  if "yes" in answer:
    print("Let us see if you're aware of the precautions that should be taken to prevent COVID")
    test_room1()
  elif "no" in answer:
    print("You're being an irresponsible citizen,you have been given an opportunity to get vaccinated and yet you're refusing!!!")
    print("Have a look at this situation.")
    test_room2()
  else:
    game_over("Don't you know how to type something properly?")

start()
