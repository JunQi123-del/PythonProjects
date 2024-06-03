FirstName = input("Please enter the first name: ")
SecondName = input("Please etner the second name: ")
sameLetter = {""}

def filteredName(firstName,secondName):
    for c in firstName:
         for h in secondName:
              if(c == h):
                   sameLetter.add(c)
    concatenatedName = firstName+secondName
    return[i for i in concatenatedName if i not in sameLetter]


uniqueLetter = filteredName(FirstName,SecondName)

print(uniqueLetter)

flames_list = ["F","L", "A", "M", "E", "S"]

while(len(flames_list)!=1):
      indexToRemove = len(uniqueLetter)-1%len(flames_list)-1
      del flames_list[indexToRemove]

if flames_list[0]=="F":
     print("You all are friends")
elif flames_list[0]=="L":
     print("You all are lovers")
elif flames_list[0]=="A":
     print("You all are Affectionate")
elif flames_list[0]=="M":
     print("You all are Marriage")    
elif flames_list[0]=="E":
     print("You all are Enemies")
elif flames_list[0]=="S":
     print("You all are Siblings")