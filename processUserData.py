#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : process student responses
#I hope to be retired in 10 years, I have high hopes for myself and the 3 other students who answered the same, but we really just don't know how its gonna end up
#It took me a solid week to actually get this done, I've probably had this file open in thonny for like an elapsed 15 hours and for just about all of that I haven't touched it
#I hope that doesn't foreshadow how long it will take me to retire...

#users enter a keyword and the program outputs the number of its instances
def keywordCount(fullList):
    fullString = " ".join(fullList)
    keyword = input("What keyword would you like to check? (case sensitive) ")
    print(fullString.count(keyword))
#outputs the average months students have been programming
def averageMonths(fullList):
    monthCount = 0
    totalCount = 0
    for x in range(0,len(fullList)):
        totalCount = totalCount + 1
        #make the current answer a string for testing
        oneString = "".join(fullList[x])
        #if the string converts to an int its a good answer and is added to the total
        try:
            num = int(oneString)
        #if the user answer isn't good it defaults to 0
        except:
            num = 0
        monthCount = monthCount+num
    print("{:.2f}".format(monthCount/totalCount))
#outputs average months of programming for students with a user chosen keyword in their response
def averageMonthsWithKeyword(fullList):
    monthCount = 0
    totalCount = 0
    keyword = input("What keyword would you like to check user month average? (case sensitive) ")
    for x in range(0,len(fullList[0])):
        #turn current 3rd answer into string, test for keyword
        oneString = "".join(fullList[2][x])
        #if keyword is there convert the corresponding 1st answer to an int, if it isn't good it defaults to 0
        if keyword in oneString:
            totalCount = totalCount +1
            oneNumString = "".join(fullList[0][x])
            try:
                num = int(oneNumString)
            except:
                num = 0
            monthCount = monthCount+num
    print("{:.1f}".format(monthCount/totalCount))
#prints out the percent of students who know about for loops
def percentLoop(fullList):
    totalCount = 0
    totalYes = 0
    for x in range(0,len(fullList)):
        totalCount = totalCount + 1
        #convert current answer to string, test for yes
        oneString = "".join(fullList[x])
        if "yes" in oneString.lower():
            totalYes = totalYes + 1
    print("{:.2f}".format(totalYes/totalCount))
#prints percent of students who are first gen college students
def firstGen(fullList):
    totalCount = 0
    totalYes = 0
    for x in range(0,len(fullList)):
        totalCount = totalCount + 1
        #convert current answer to string, test for yes
        oneString = "".join(fullList[x])
        if "yes" in oneString.lower():
            totalYes = totalYes + 1
    print("{0:.2%}".format(totalYes/totalCount)) #yeah, one more decimal then in the example, im tired and I can probably eat a -1 on this assignment :^)
#hey, its only like 26 lines of code, don't get mad at me for following the rules \n\n\n\n\n\n :^)
def main():
    #prepare list and get file
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
        #apply logic based on choice, nice
        if choice=="1":
            #we only need the 3rd answer from each student, so we pull that specific list
            keywordCount(fullList[2])
        elif choice=="2":
            #only want the 1st answers
            averageMonths(fullList[0])
        elif choice=="3":
            #only need the 1st and 3rd answers, lazy method, could be optimized instead of grabbing the entire list
            averageMonthsWithKeyword(fullList)
        elif choice=="4":
            #only want 2nd answers
            percentLoop(fullList[1])
        elif choice=="5":
            #only want 4th answers
            firstGen(fullList[3])
        elif choice=="6":
            break
        else:
            #they entered something wrong
            print("Please enter a single digit, 1 through 6")
main() #run this bad boy