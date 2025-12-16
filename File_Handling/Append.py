def Append(filename):
    try:
        with open(filename,'a') as f:
            f.write("Succesfully Executed !")
    except Exception as e:
        print("Error :",e)

Append("Sample.txt")