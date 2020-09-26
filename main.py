import read as R
import datetime
import display as D
import list2d as L
import write as W
import returnbook as RB
try:
      #  first it is read from the file.
     def initialtable():
          lists=[ ]
          lists_1= R.read_information(lists)
          list_2d=L.arrange(lists_1) # the read data which is in list is converted into 2d lists.
          D.display_information(list_2d) #  2d list is now displayed in the form of table.
          return  list_2d
     library_book=initialtable() # it has the library books in 2d list .
     # second it is to ask input to the user.
     def mainwork(answer):
          answer= str(input("Do you want a book(yes or no) :")).lower()
          return answer
     word=str()
     answer=mainwork(word)
     def process(answer):
          if answer== "yes":
                    W.user_information()  # it is to keep the total cost of the book along with information in 2d list and the display the information.
                    def information_of_user(lists):
                         received=R.read_information2(lists) # it has the infomation of the user in a list.
                         list_2d=L.arrange(received)# it is to keep information in a 2d list along with price.
                         user=D.display_userinformation(list_2d) # to display user inputed information along with price.
                         return user
                    list2=[ ]
                    new_2d= information_of_user(list2)
                    # it is to get the total number of books taken and update the initialtable.
                    def count(new_2d,library_book):
                         num1=0
                         num2=0
                         num3=0
                         for i in range (len(new_2d)):
                              if new_2d[i]=="harry potter":
                                   num1+=1
                              if new_2d[i]=="start with why":
                                   num2+=1
                              if new_2d[i]=="programming with python":
                                   num3+=1
                         new_book1=str((int(library_book[0][2])-num1))
                         new_book2=str((int(library_book[1][2])-num2))
                         new_book3=str((int(library_book[2][2])-num3))
                         if int(new_book1)  <= 0:
                              new_book1=0
                         if int(new_book2)  <= 0:
                              new_book2=0
                         if int(new_book3)  <= 0:
                              new_book3=0
                         for i in range (len(library_book)):
                              for j in range (len(library_book[i])):
                                   library_book[0][2]=new_book1
                                   library_book[1][2]=new_book2
                                   library_book[2][2]=new_book3
                         return(library_book)
                    quantity_changed=count(new_2d,library_book)

                    # it is to display the updated table and ask user if they want to take book or return to the library. 
                    def newtable(lists):
                         W.library_stock(lists)
                         question=str(input("Type 'yes' to view library books or Type 'return' to give back books =")).lower()
                         if question=="yes":
                              D.display_information(lists)
                              answer=mainwork(word)
                              process(answer)
                         
                         elif question=="return":
                              listss=[ ]
                              list1d=R.read_information2(listss)
                              list2d=L.arrange(list1d)
                              (user,returnbooks)=RB.bookreturncheck(list2d,lists)
                              W.library_stock(returnbooks)
                              W.user_stock(user)
                              D.display_information(returnbooks)
                              answer=mainwork(word)
                         else:
                              print("Thank you for visiting")
                              initialtable()
                              answer=mainwork(word)
                              process(answer)
                                                  
                    newtable(quantity_changed)
          elif answer=="no":
               answer=str(input("Type yes to return book :")).lower()
               if answer=="yes":
                    listss=[ ]
                    list1d=R.read_information2(listss)
                    list2d=L.arrange(list1d)
                    (user,returnbooks)=RB.bookreturncheck(list2d,library_book)
                    W.library_stock(returnbooks)
                    W.user_stock(user)
                    D.display_information(returnbooks)
                    answer=mainwork(word)
                    process(answer)
               else:
                    print("thankyou for the visit")
                    initialtable()
                    answer=mainwork(word)
                    process(answer)
          else:
               print("Invalid input please try again")
               initialtable()
               answer=mainwork(word)
               process(answer)
     process(answer)
except Exception :
     initialtable()
     answer=mainwork(word)
     process(answer)

     




     
