# Script: week4part1.py
# Author: Owen Sheehan
# Description: week4part1




def main ():
    student = readFile()
    data = createList(student)
    getStudentAverage(data)

def readFile ():
    studentDetails = open('studentDetails.txt') #opens the studentDetails file

    return studentDetails

def createList(data):
    data = data
    listOfLists = [] # creates a list which will be populated by lists created from each line of the file
    for line in data.readlines():
        y = [] # creates a list from an individual line
        x = line.strip() # strips /n from the end of each line 
        y = x.split(" ") # splits the line where ever there is a space character and adds everything to the list
        listOfLists.append(y) # adds the y list to listOfLists
    return listOfLists

def getStudentAverage(data):

    a = 0
    for i in data:
        x = []
        x = data[a]
        name = x[0]
        sumForAverage = 0
        c = 0
        for b in x:
            if c > 0:
                sumForAverage = sumForAverage + int(x[c])

                c = c + 1
                
            else:
                c = c + 1
                continue
        average = sumForAverage/(len(x)-1)
        a = a + 1
        print(name,average)
    
    
    
main()