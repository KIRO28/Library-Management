# it is arrange the list in to 2d list.
def arrange(lists_1):
     L_2=[ ]
     for i in (lists_1):
          L_2.append(i.replace("\n"," ").split(","))
     return L_2


