# this function is used to store user input information in a informationfile.
import datetime
def user_information():
     file=open("informationfile.txt","a")
     try:
          num=int(input("How many book do you want ="))
          if num>0 and num<4:
               name=str(input("enter your name="))
               file.write(str(name))
               file.write(",")
               roll_no=str(input("enter your roll no. with an alphabet in the end="))
               file.write(str(roll_no))
               file.write(",")
          else:
               print("error in number")
               user_information()
          total_cost=0
          for i in range (num):
               book_taken=str(input("enter name of the book you want=")).lower()
               file.write(str(book_taken))
               file.write(str(","))
               if book_taken == "harry potter":
                    total_cost+=2
               if book_taken=="start with why":
                    total_cost+=1.5
               if book_taken=="programming with python":
                    total_cost+=1.5
          file.write(str(total_cost))
          file.write(str(","))
          file.write(str(datetime.date.today()))
          file.write(str(","))
          timetoday=datetime.date.today()
          tdelta=datetime.timedelta(days=10)
          finaltime=timetoday+tdelta
          file.write(str(finaltime))         
          file.write("\n")
     except Exception as e:
          print(e)
          user_information()
     file.close()
def library_stock(lists):
     file=open("text.txt","w")
     for i in range (len(lists)):
          for j in range (len(lists[i])):
               if j==3:
                    file.write(str(lists[i][j]))
               else:
                    file.write(str(lists[i][j]))
                    file.write(",")
          file.write("\n")
     file.close()  
def user_stock(lists):
     file=open("informationfile.txt","w")
     for i in range (len(lists)):
          for j in range (len(lists[i])):
               if i ==6:
                    file.write(str(lists[i][j]))
               elif i ==5:
                    file.write(str(lists[i][j]))
               else:
                    file.write(str(lists[i][j]))
                    file.write(",")
          file.write("\n")
     file.close()
     



               
