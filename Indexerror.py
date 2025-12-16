#Handle Index Error
def index():
 try:
  list=[10,20,30]
  print(list[4])
 except IndexError:
  print("Wrong Indexing !")

index()
