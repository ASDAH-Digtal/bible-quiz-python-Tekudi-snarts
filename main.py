score = 0
 
print("___________________________________________________________")
print("Come forth females and temales to this bible quiz")
print("___________________________________________________________")
print("Ten questions, Ten points.")
print("___________________________________________________________")
print("What are you doing? if you even think of getting this score you need some jesus in your life")
print("___________________________________________________________")
print("Pretty mid score if you got 4 - 7.")
print("___________________________________________________________")
print("You're a nerd if you got 8 - 10 points")
print("___________________________________________________________")
 
while True:
 question_one = input(". Who was the first king of Israel? \n (a) Colossians\n (b) Hebrews\n (c) John\n (d) Revelation  \n>>")
  correct_q1 = ["D","d","(d)","Revelation", "revelation"]
 incorrect_q1 = ["A","a","(a)","Colossians","colossians","B","b","(b)","Hebrews","hebrews","C","c","(c)","John","john"]
 
 if question_one.lower() in correct_q1:
   print("===========================================================")
   print("Great Job, you got the answer right.")
   score += 1
   print("You now have: {} point".format(score))
   break
 elif question_one.lower() in incorrect_q1:
   print("Not the answer i'm looking for. Nice try.")
   score += 0
   print("You now have: {} point".format(score))
   break
 else:
   print("You did not choose one of the options")
print("===========================================================")
