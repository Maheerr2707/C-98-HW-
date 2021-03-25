def swapfile():
    file1=input("Enter the name of the 1st file")
    file2=input("Enter the name of the 2nd file")
    A=open(file1,'r') 
    data_A= A.read()
    B=open(file2,'r')
    data_B=B.read()
    A=open(file1,'w') 
    A.write(data_B)
    B=open(file2,'w')
    B.write(data_A)

swapfile()