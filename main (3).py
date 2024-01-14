print("Hello welcome to my first ever mini game. I hope you enjoy!")
name = input("What is your name? ")
age = int(input("What is your age? "))

hp = 10

if age >= 18:
  print("You are old enough to play!")


  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("you are starting with", hp, "health")
    print("Ok have fun playing!")

    left_or_right = input("First Decision... Left or Right (left/right)?")
    if left_or_right == "right":
      ans = input("You come to a lake do you swim across or go around (across/around) ")

      if ans == "around":
          print("you went around and reached the other side of the lake")
      elif ans == "across":
          print("You managed to get across,but were bit by a fish and lost 5 health")
          hp -= 5

      ans = input ("You notice a house and a river.Which do you go to (river/house)?")
      if ans == "house":
          print("The owner of the house hits you and you lose 5 health")
          hp -= 5

          if hp <= 0:
            print("You now have 0 health and you lost the game...")
          else:
            print("You have survived... You win!")       
      else:
        print("you fell in the river and died")
        
        
        
  else:
    print("ok goodbye")
    
else:
  print("You are not old enough to play!")

