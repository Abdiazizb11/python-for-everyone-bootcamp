# my name is Abdihamidhussein >Shiine
# A simple study log that takes a notes from user saves and displays All notes
# load
notes=[]
def read_old_note() :
  try:
   with open('notes.txt','r',encoding='utf8') as  file:
     for line in file:
       notes.append(line.strip())
  except:
    pass
def save_note():
  with open('notes.txt','w',encoding='utf8') as  file:
    for items in notes:
      file.write(items+'\n')
def add_note():
  try:
    user_input=input("write a note:")
    notes.append(user_input)
  except ValueError:
   print("number not allowed here")
def show_note():
  
  if len(notes)==0:
    print("not a note yet to show")
  else:
    
    for  note in notes :
      
      print(note)
while True:
  print('\n welcome note program')
  print("1.Add note")
  print("2.show a note")
  print("3.quit")
  
  select=input("choose:")
  if select=="":
    print("please enter a note")
  if select=="1":
      add_note()
      save_note()
      print("note created successfuly")
  elif select=="2":
      show_note()
      read_old_note()
  elif select=="3":
   
    break

   
  
   
    


    
  
  

