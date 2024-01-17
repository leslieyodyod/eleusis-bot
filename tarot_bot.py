#import from another file
import meanings as m
#tarot bot 
import random 
#major arcana
major_arcana = [["the fool", 0], ["the magician, 1"], ["the high priestess", 2], ["the empress", 3], ["the emperor", 4], ["the hierophant", 5], ["the lovers", 6], ["the chariot", 7], ["strength", 8], ["the hermit", 9], ["wheel of fortune", 10], ["justice", 11], ["the hanged man", 12], ["death", 13], ["temperance", 14], ["the devil", 15], ["the tower", 16], ["the star", 17], ["the moon", 18], ["the sun", 19], ["judgement", 20], ["the world", 21]]

print("You've made it to Eleusis. I invite you to pick a card")
answer = input("Press any key to pull a card.\n")
  
#pulling card 
def pulling_card():
  random_number = random.randint(0,21)
  if random_number == 0:
    print("Your card is " + major_arcana[0][0])
    return m.the_fool
  elif random_number == 1:
    print("Your card is " + major_arcana[1][0])
    return m.the_magician
  elif random_number == 2:
    print("Your card is " + major_arcana[2][0])
    return m.the_high_priestess
  elif random_number == 3:
    print("Your card is " + major_arcana[3][0])
    return m.the_empress
  elif random_number == 4:
    print("Your card is " + major_arcana[4][0])
    return m.the_empreror
  elif random_number == 5:
    print("Your card is " + major_arcana[5][0])
    return m.the_hierophant
  elif random_number == 6:
    print("Your card is " + major_arcana[6][0])
    return m.the_lovers
  elif random_number == 7:
    print("Your card is " + major_arcana[7][0])
    return m.the_chariot
  elif random_number == 8:
    print("Your card is " + major_arcana[8][0])
    return m.strength
  elif random_number == 9:
    print("Your card is " + major_arcana[9][0])
    return m.the_hermit
  elif random_number == 10:
    print("Your card is " + major_arcana[10][0])
    return m.the_wheel_of_fortune
  elif random_number == 11:
    print("Your card is " + major_arcana[11][0])
    return m.justice
  elif random_number == 12:
    print("Your card is " + major_arcana[12][0])
    return m.the_hanged_man
  elif random_number == 13:
    print("Your card is " + major_arcana[13][0])
    return m.death
  elif random_number == 14:
    print("Your card is " + major_arcana[14][0])
    return m.temperance
  elif random_number == 15:
    print("Your card is " + major_arcana[15][0])
    return m.the_devil
  elif random_number == 16:
    print("Your card is " + major_arcana[16][0])
    return m.the_tower
  elif random_number == 17:
    print("Your card is " + major_arcana[17][0])
    return m.the_star
  elif random_number == 18:
    print("Your card is " + major_arcana[18][0])
    return m.the_moon
  elif random_number == 19:
    print("Your card is " + major_arcana[19][0])
    return m.the_sun
  elif random_number == 20:
    print("Your card is " + major_arcana[20][0])
    return m.judgment
  else:
    print("Your card is " + major_arcana[21][0])
    return m.the_world

if answer: 
    print(pulling_card())