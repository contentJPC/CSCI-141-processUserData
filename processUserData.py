#Name : Joseph Cormier
#Class : CSCI 141
#Assignment : process student responses
#I hope to be retired in 10 years, I have high hopes for myself and the 3 other students who answered the same
#But we really just don't know how its gonna end up

#studentResponses2018s.txt

def main():
    fullList = [[], #months coding
                [], #knowledge of loops
                [], #hopes for job or career in 10 years
                []] #first gen college student?
    filename = input("File name to parse ")
    fileInput = open(filename, "r")
    
    for line in fileInput:
        answers = line.split("|")
        fullList[0].append(answers[0])
        fullList[1].append(answers[1])
        fullList[2].append(answers[2])
        fullList[3].append(answers[3].rstrip("\n"))
        
    print(fullList[0])
    print("")
    print(fullList[1])
    print("")
    print(fullList[2])
    print("")
    print(fullList[3])
    
    print(fullList[0][96])
    print("")
    print(fullList[1][96])
    print("")
    print(fullList[2][96])
    print("")
    print(fullList[3][96])
    
        
    
main()