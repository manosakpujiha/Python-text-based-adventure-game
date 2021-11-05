import time
import os
wallet=100
health=100
inventory = ["Shield"]

def dead():
    global health
    if health <=0:
      health = 0
    print(f"Health = {health}%")
    print("You are dead!\nGame Over!")
    print("                                         ")
    time.sleep(1)
    print("                                         ")
    time.sleep(1)
    print("Do you want to play again?")
    time.sleep(1)
    run()
  
def addToWallet(amount):
  global wallet
  wallet+=amount

def removeFromWallet(amount):
  global wallet
  wallet-=amount

def addToHealth(healthPoints):
  global health
  health+=healthPoints

def removeFromHealth(healthPoints):
  global health
  health-=healthPoints
  if health <= 0:
    dead()

def addToInventory(item):
  global inventory
  inventory.append(item)
  if 'Inventory is empty' in inventory:
    inventory.remove('Inventory is empty')

def removeFromInventory(item):
  global inventory
  inventory.remove(item)
  if inventory == []:
    inventory.append('Inventory is empty')

def room_7():
  print("                                         ")
  time.sleep(1)
  print(f"You are in Room 7!\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  time.sleep(1)
  print("The dragon takes the first attack and puffs out its fire\nYou loose a lot of your health\n ")
  time.sleep(1)
  removeFromHealth(80)
  if health <=0:
    return
  print(f"Health = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  response=input("The dragon breaths in again and gets ready to melt you with its fire, what do you do now?\nType '1' to attack the dragon with your sword, Type '2' to defend with your shield, Type '3' to run away or Type '4' to use magic potion ")
  if response == str(1):
    if "Sword" in inventory:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You jump into action and slice of its head, just before it breaths out its fire....")
      time.sleep(2)
      print("...the dragon falls down and dies in a shriek.\nCongratulations! you have saved the princess and are victorious!")
      time.sleep(2)
      print('The game has ended you are a champion!.\nDo you want to play again?')
      run()
    else:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("Oops!, You dont have a sword.")
      time.sleep(1)
      print("The dragon finishes you off like roast beef.")
      removeFromHealth(80)
      if health <= 0:
        return
    
  elif response == str(2):
    if "Shield" in inventory:
      print("                                         ")
      print("******************************************************************************************")
      print("The shield melts in your hands like a candle.")
      time.sleep(1)
      print(f"Health = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
      time.sleep(1)
      print("The dragon quickly finishes you off, before you can think again.")
      removeFromHealth(20)
      if health <=0:
        return
    else:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("Yikes!, you sold your shield remember.")
      time.sleep(1)
      print("Your hand is still in your bag, searching for the shield, when the dragon's fire fries and pops you like a popcorn in an oven.")
      removeFromHealth(80)
      if health <= 0:
        return

  elif response == str(4):
    if "Powerful Potion" in inventory:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You throw the potion at the dragon and it suddenly freezes and turns into a glass statue....")
      time.sleep(2)
      print("...the glass dragon statue cracks and shatters into a thousand pieces.\nCongratulations! you have saved the princess and are victorious!")
      time.sleep(2)
      print('The game has ended you are a champion!.\nDo you want to play again?')
      run()
    else:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("Oopsy!, You must have possessed such a potion in your dreams, beacuse it's not in you bag right now.")
      time.sleep(1)
      print("You are still searching through your bag for the potion, when the dragon finishes you off like a Hot Dog.")
      removeFromHealth(80)
      if health <= 0:
        return
  else:
    print("******************************************************************************************")
    print("                                         ")
    print("The dragon is too fast and too powerful compared to you, it finshes you of like roast beef.")
    removeFromHealth(80)
    if health <0:
      return

def room_6():
  print("                                         ")
  time.sleep(1)
  print(f"You are now in Room 6!\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  response=input("You come across another lonely adventurer like yourself, What do you do? \nType '1' to Rob him  or Type '2' to offer to sell your shield to him for $50 ")
  if response == str(1):
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("It was a though battle, you lost some health but, you were eventually successfull at robbing him.")
    print("You then go back to purchase the potion.")
    addToInventory('Stolen Sword')
    addToWallet(200)
    removeFromHealth(30)
    print(f"Health = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
    room_5()
  elif response == str(2):
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("He happily buys your shield from you, so you go back to the market to buy the potion.")
    addToWallet(50)
    removeFromInventory('Shield')
    print(f"Health = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
    room_5()

def room_5():
  print("                                         ")
  time.sleep(1)
  print(f"You are now in Room 5!\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  response=input("You come to a market and meet a merchant who offers to sell a potion that can kill dragons for $200, What do you do? \nType '1' to buy the potion, Type '2' rob him of the potion ")
  if response == str(1):
    if wallet >=200:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You buy the powerful potion and as an added bonus, the merchant shows you a shortcut to the dragon's room.")
      print("Your morale gets boosted by this assistance, hence you gain health of 10 points.")
      removeFromWallet(200)
      addToInventory('Powerful Potion')
      addToHealth(10)
      time.sleep(1)
      room_7()
    else:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You do not have enough money, the merchant chases you away, you continue your journey.")
      room_6()

  elif response == str(2):
    print("******************************************************************************************")
    print("                                         ")
    time.sleep(1)
    print("You rob him successfully but the market security catch up with you and you try to fight your way out but you are killed in the process.")
    removeFromHealth(100)

def room_4():
  print("                                         ")
  time.sleep(1)
  print(f"You are now in Room 4!\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  response=input("You see a key on a table and and a red door in front of you, what do you do? \nType '1' use the key to open the red door. ")
  if response == str(1):
    os.system('cls')
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("You open the door and come face to face with a fire breathing Dragon and Princess Evelyn trapped behind it")
    time.sleep(1)
    addToInventory('Key')
    room_7() 
  
def secretRoom_3():
  print("                                         ")
  time.sleep(1)
  print(f"You are in the Secret Room!\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  response=input("You see a merchant who offers to sell you a sword and you also see a door leading to a bright room, What do you do? \nType '1' to buy the sword or Type '2' to go to the bright room. ")
  if response == str(1):
    os.system('cls')
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("You buy the sword and the merchant directs you to the bright room.")
    removeFromWallet(100)
    addToInventory('Sword')
    time.sleep(1)
    room_4()
  elif response == str(2):
    os.system('cls')
    print("******************************************************************************************")
    print("                                         ")
    time.sleep(1)
    print("You walk into the bright room.")
    time.sleep(1)
    room_4()
  else:
    os.system('cls')
    print("******************************************************************************************")
    print("You can only select option '1' or '2'                                         ")
    time.sleep(1)
    secretRoom_3()

def choices():
  response=input("Type '1' to give him the ring, Type '2' to give him some money instead or Type '3' to eliminate the old man: ")
  if response == str(1):
    os.system('cls')
    if "Old Ring" in inventory:
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("The old man collects the ring, revives your health, and guides you to a secret ROOM...")
      addToHealth(20)
      removeFromInventory('Old Ring')
      time.sleep(1)
      secretRoom_3() 
    else: 
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You did not collect the old ring, you can only pick option '2' or '3' ")
      choices()
  elif response == str(2):
    os.system('cls')
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("Oops! he does not want your money, so he magically invokes some bats that immediately begin to attack you and drain some of your health, you then run into a bright room which scares them away before they finish you off. ")
    removeFromHealth(50)
    time.sleep(1)
    room_4()
  elif response == str(3):
    os.system('cls')
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("You rob the old man of $50, tie him up and continue your journey. ")
    addToWallet(50)
    time.sleep(1)
    room_5() 
  else: 
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print("Wrong input, you can only pick option '1', '2' or '3' ")
    choices()

def room_2():
  print("                                         ")
  time.sleep(1)
  print(f"You are now in ROOM 2\nHealth = {health}%, Money = ${wallet} & Your bag contains: {inventory} ")
  time.sleep(1)
  print("                                         ")
  print("You meet and old man who is requesting for the ring, What do you do?")
  time.sleep(1)
  choices()

def room_1():
  print(f"New Game started!")
  print("                                         ")
  print(f"You are now in ROOM 1 \nHealth = {health}%, Money = ${wallet} & Your bag contains {inventory} ")
  time.sleep(1)
  print("                                         ")
  start=input("You see a talking turtle which offers you an old ring, what do you do?\nType '1' to take the ring or Type '2' to leave the ring and proceed to room 2: ")
  if start == str(2):
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print(f"You walk past the turtle and refuse it's offer, then it licks you and drains some of your health")
    removeFromHealth(20)
    time.sleep(1)
    room_2()
  elif start == str(1):
    os.system('cls')
    addToInventory("Old Ring")
    removeFromHealth(20)
    print("                                         ")
    print("******************************************************************************************")
    time.sleep(1)
    print(f"You take the ring but the turtle licks you and drains some of your health, you make it to the next room though.")
    time.sleep(1)
    room_2()
  else:
    print("only 1 or 2 is allowed")
    time.sleep(1)
    room_1()

def startGame():
  print("                                         ")
  print("******************************************************************************************")
  time.sleep(1)
  room_1()

def run():
  time.sleep(1)
  message=input("Type '1' to Start the game or Type '2' to Exit the program: ") 
  while True:
    if message == str(1):
      global wallet, health, inventory
      wallet=100
      health=100
      inventory = ["Shield"]
      startGame()
      break
    elif message == str(2):
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print('Exiting the game...')
      time.sleep(1)
      print("                                         ")
      time.sleep(1)
      print("******************************************************************************************")
      time.sleep(1)
      break
    else:
      os.system('cls')
      print("                                         ")
      print("******************************************************************************************")
      time.sleep(1)
      print("You can only Type '1' or '2', Try again...")
      time.sleep(1)
      run()
      break

def welcomeMessage():
  print("                                         ")
  print("******************************************************************************************")
  time.sleep(1)
  print("Welcome to the Boring Space Dragon Adventure Game, if you snooze, you loose!") 
  run()

welcomeMessage()