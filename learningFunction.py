def countWordsFromFile():

    fileName=input("Enter the file name")
    file=open(fileName,"r") 
    numberofWords=0

    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)

    print("Number of words is",numberofWords)

countWordsFromFile()    