def Write(filename):
    try:
        with open(filename,'w') as f:
            f.write("Succesfully Write !")
    except Exception as e:
        print("Error :",e)

Write("Sample.txt")