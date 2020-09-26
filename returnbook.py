# here list2d has the information from informationfile.txt while lists has the updated table elements. 
def bookreturncheck(list2d,lists):
     print("To return books you need to give your roll no.")
     roll_no=str(input("enter your roll no. ="))
     num=0
     value=roll_no
     for i in range (len(list2d)):
          for j in range (len(list2d[i])):
               if list2d[i][j]== roll_no:
                    num=i                    
     
     l1=[ ]
     for i in range (len(list2d)):
          for j in range (len(list2d[i])):
               if num==i:
                    l1.append(list2d[i][j])
          
     for i in range (len(list2d)):
          if num==i:
               del list2d[i]

     num1=0
     num2=0
     num3=0
     for i in range (len(l1)):
          if l1[i]=="harry potter":
               num1+=1
          if l1[i]=="start with why":
               num2+=1
          if l1[i]=="programming with python":
               num3+=1

     new_book1=str((int(lists[0][2])+num1))
     new_book2=str((int(lists[1][2])+num2))
     new_book3=str((int(lists[2][2])+num3))
     if int(new_book1)  > 30:
          new_book1=30
     if int(new_book2)  > 30:
          new_book2=0
     if int(new_book3)  > 30:
          new_book3=0
     
     for i in range (len(lists)):
          for j in range (len(lists[i])):
               lists[0][2]=new_book1
               lists[1][2]=new_book2
               lists[2][2]=new_book3

     print("the book is returned") 
     return(list2d,lists)

    
