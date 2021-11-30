score = 0
 
 #This is the start of the code and the first thing that will be displayed to the user.
print("___________________________________________________________")
print("Come forth females and temales to this bible quiz")
print("___________________________________________________________")
print("Ten questions, Ten points.")
print("___________________________________________________________")
print("0 - 3, What are you doing? if you even think of getting this score you need some jesus in your life")
print("___________________________________________________________")
print("Pretty mid score if you got 4 - 7.")
print("___________________________________________________________")
print("You're a nerd if you got 8 - 10 points")
print("___________________________________________________________")
print("When answering a question try to use one concise word or the letter infront of your answer. \n")
 
while True: #Question one

#This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_one = input(". Who was the first king of Israel? \n (a) Saul\n (b) God\n (c) Me\n (d) David  \n>>")
  correct_q1 = ["a","saul"]#This is the correct answer
  incorrect_q1 = ["b","god","me", "c", "d", "david"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_one.lower() in correct_q1:
    print("===========================================================")
    print("Correeeeeeecccccccccct.")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_one.lower() in incorrect_q1:
    print("lol noob. Try getting the next one correct")
    score += 0
    print("You now have: {} point".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")


while True:#Question two

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_two = input(". What was Elijah? \n (a) A Leader\n (b) A king\n (c) A prophet\n (d) Your dad  \n>>")
  correct_q2 = ["c","prophet", "a prophet"]#This is the correct answer
  incorrect_q2 = ["a","leader", "a leader" "king", "a king" "b", "d", "dad", "your dad"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_two.lower() in correct_q2:
    print("===========================================================")
    print("some people would have actually gotten that wrong.")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_two.lower() in incorrect_q2:
    print("Can't say I blame you but, I blame you")
    score += 0
    print("You now have: {} point".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question three

#This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_three = input(". How many people did Jesus feed in one go? \n (a) 21\n (b) 5,000\n (c) 420\n (d) 119  \n>>")
  correct_q3 = ["b","5000", "5,000"]#This is the correct answer
  incorrect_q3 = ["a","21","420", "c", "420", "d", "119"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_three.lower() in correct_q3:
    print("===========================================================")
    print("Good work.")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_three.lower() in incorrect_q3:
    print("If you said 21, then you have some of the worst faith I have seen, if you said 420 the answer was wrong but you will always be right to me")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question four

#This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_four = input(". In creation, what came first? Heaven or the animals? \n (a) Heaven\n (b) The animals\n (c) Queen Elizabeth II\n (d) deez.  \n>>")
  correct_q4 = ["a","heaven"]#This is the correct answer
  incorrect_q4 = ["b","the animals", "animals", "queen elizabeth", "queen", "elizabeth", "c", "d", "deez"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_four.lower() in correct_q4:
    print("===========================================================")
    print("If you got that wrong then we would have a problem. Good thing you didn't")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_four.lower() in incorrect_q4:
    print("Guys. Come on, this is probably the easiest question. HAVE YOU EVEN READ THE BIBLE.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question five

#This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_five = input(". Who was the cousin of Jesus? \n (a) The father\n (b) The son\n (c) The holy spirit\n (d) James.  \n>>")
  correct_q5 = ["d","james"]#This is the correct answer
  incorrect_q5 = ["a","the father", "father" "the son", "son", "the holy spirit", "spirit", "holy", "c", "b"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_five.lower() in correct_q5:
    print("===========================================================")
    print("Good work on avoiding the trick")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_five.lower() in incorrect_q5:
    print("LOL YOU FELL FOR THE TRICK.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question six

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_six = input(". Who or what did Moses lead? \n (a) pack of wolves\n (b) Israelites\n (c) clouds\n (d) Sheep.  \n>>")
  correct_q6 = ["Israelites","b"]#This is the correct answer
  incorrect_q6 = ["a","pack", "wolves", "pack of wolves", "clouds" "sheep", "c", "b"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_six.lower() in correct_q6:
    print("===========================================================")
    print("That is correct, nice")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_six.lower() in incorrect_q6:
    print("WOW, you know I can't tell if I'm shocketh or disappointed.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question seven

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_seven = input(". Was peter a tax collector? \n (a) yes\n (b) no\n (c) maybe\n (d) no clue.  \n>>")
  correct_q7 = ["yes","a", "true"]#This is the correct answer
  incorrect_q7 = ["c","maybe", "no clue", "b", "d", "no"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_seven.lower() in correct_q7:
    print("===========================================================")
    print("Very nice, round of applause for you, ok no more clapping, hurry up and move on to the next question")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_seven.lower() in incorrect_q7:
    print("He  is litterally the fisher of man, dude I tried to make these easy for you..")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question eight

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_eight = input(". Who was the waifu of Abraham/Abram? \n (a) Bathsheeba\n (b) Naomi\n (c) Sarah/Sarai\n (d) Nico Robin.  \n>>")
  correct_q8 = ["c","sarah", "sarai", "sarah/sarai"]#This is the correct answer
  incorrect_q8 = ["a","bathsheeba", "nico robin", "d", "b", "naomi"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_eight.lower() in correct_q8:
    print("===========================================================")
    print("Pretty easy question but a point is a point notheless.")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_eight.lower() in incorrect_q8:
    print("ok no. But if you picked 'Nico Robin', then I must say that you are a man of culture, although I cannot award you a point know that you will always have my respect.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question nine

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_nine = input(". Ok this one is very easy. Was David a shepherd or a king? \n (a) no\n (b) Shepherd\n (c) king\n (d) both.  \n>>")
  correct_q9 = ["d","both",]#This is the correct answer
  incorrect_q9 = ["a","no", "shepherd", "king", "b", "c "]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_nine.lower() in correct_q9:
    print("===========================================================")
    print("Phew I would have gone brain dead if you got that wrong, I mean you have to be pretty brain dead to get that wrong.")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_nine.lower() in incorrect_q9:
    print("no.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")

while True:#Question ten

  #This is where the user will be answered a question and where they will be putting an input, it will be stored in the variable 'question one'
  question_ten = input(". Alright, this is the final question. Who was the wisest man in the bible? \n (a) me\n (b) you\n (c) Solomon\n (d) Salmon.  \n>>")
  correct_q10 = ["Solomon","c",]#This is the correct answer
  incorrect_q10 = ["a","me", "you", "salmon", "b", "d"]#These are the incorrect answers

  #This is all the responses for the various answers
  if question_ten.lower() in correct_q10:
    print("===========================================================")
    print("Looks like you are not .")
    score += 1
    print("You now have: {} points".format(score))
    break
  elif question_ten.lower() in incorrect_q1:
    print("no.")
    score += 0
    print("You now have: {} points".format(score)) 
    break
  else:
    print("Please remember to use the letters or one word for your answer. (TLDR: you didn't give an eligble answer)")
  print("===========================================================")


#This is the final out-come, This is where the user will be shown their final score as well as some final text before they leave the quiz.

score += 0
print=("Your final score is: {} points, How many did you get? If you want to try again. Don't. That would be cheating.".format(score))
  