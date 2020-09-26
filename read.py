# it is to read data contained in the library from text file.
def read_information(lists):
     file= open( "text.txt" , "r")
     data= file.readlines()# readlines keeps all the data into a list.
     file.close()
     return data
     
# it is used to read the information of the user from informationfile text.
def read_information2(lists):
     file=open("informationfile.txt","r")
     information=file.readlines()
     file.close()
     return information
     
