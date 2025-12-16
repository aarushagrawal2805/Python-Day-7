def Copy_file(Main_file,Copyfile):
    try:
        with open(Main_file,'r') as f:
            content=f.read()
        with open(Copyfile,'w') as f:
            f.write(content)
    except Exception as e:
        print("Error :",e)

Main=Copy_file("Sample.txt","Copy.txt")
