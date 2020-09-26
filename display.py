import datetime         # this function display the name,books name and their quantity and price.
def display_information(list_2d):     
     print( "list of book available in library")
     print("\n")
     print ("S.no \t\t Name of book \t\t\t Name of author \t\t Total number of book \t\t Price per book ")
     for i in range (len(list_2d)):
          if i==2:
               print(i+1,"\t ",end=" ")
          else:
               print (i+1,"\t\t",end=" ")
          for j in range (len(list_2d[i])):
               if list_2d[0][2] or list_2d[1][2]:
                    print(list_2d[i][j],"\t\t\t",end=" ")
               else:
                    print(list_2d[i][j],end=" ")
          print("\n")
     print("Note: Student can take only 3 at a time and provided book is only for 10 days.")
     print("if it is returned late then you will be charged with 3$.")
# it is to display the individual user information.
def display_userinformation(user_list):
     roll_no=str(input("To view your information you must enter your roll no. ="))
     print("\n")
     print("Your information")
     print ("Name \t\t roll no. \t\t Name of books \t\t Total cost of book \t\t Date of book taken \t\t Date of summission")
     num=0
     for i in range (len(user_list)):
          for j in range (len(user_list[i])):
               if user_list[i][j]== roll_no:
                    num=i
     l2=[ ]
     for i in range (len(user_list)):
          for j in range (len(user_list[i])):
               if num==i:
                    l2.append(user_list[i][j])
                    print(user_list[i][j].replace("\n"," "),"\t",end=" ")
     print("\n")
     return l2


     
