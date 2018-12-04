#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : process student responses
#I hope to be retired in 10 years, I have high hopes for myself and the 3 other students who answered the same
#But we really just don't know how its gonna end up
#      studentResponses2018s.txt

def keywordCount(fullList):
    keyword = input("What keyword would you like to check? ")
    x = fullList.split()
    print(fullList.count(keyword))
    print(fullList)
    
    
def averageMonths():
    print("weeeeeeee")
    
def averageMonthsWithKeyword():
    print("hiiiiiiiii")
    
def percentLoop():
    print("teeeeaaaaaa")
    
def firstGen():
    print("chiiiiiiiii")
    

def main(): #hey, its only like 26 lines of code, don't get mad at me for following the rules \n\n\n\n\n\n :^)
    fullList = [[],[],[],[]]
    fileInput = open(input("What is the name of the data file "), "r")
    #now that we have our file read we can put it all into a 2d list, based on the separator |
    for line in fileInput:
        answers = line.split("|")
        fullList[0].append(answers[0])
        fullList[1].append(answers[1])
        fullList[2].append(answers[2])
        fullList[3].append(answers[3].rstrip("\n")) #removing the \n at the end of each line
        
    #loop data parsing until the user is finished, letting them parse in multiple ways    
    while True:
        #tell user how they can parse the data
        print("===========================\nSelect an analysis option\n\n'1' - Perform a keyword count from the answers to question 3\n'2' - Calculate the average months of coding experience\n'3' - Calculate average months of coding experience among all students who have a specific keyword in their answer to question 3 of the survey\n'4' - Calculate the percent of students familiar with for loops\n'5' - Calculate the percent of students who are first generation college students\n'6' - Quit")
        #get input
        choice = input("\nWhat analysis do you want to perform? ")
        #apply logic, nice
        if choice=="1":
            keywordCount(fullList[2])
        elif choice=="2":
            averageMonths()
        elif choice=="3":
            averageMonthsWithKeyword()
        elif choice=="4":
            percentLoop()
        elif choice=="5":
            firstGen()
        elif choice=="6":
            break
        else:
            print("Please enter a single digit, 1 through 6")
    
main() #run this bad boy