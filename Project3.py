# File: Project3.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 11/24/2021
# Date Last Modified: 12/1/2021
# Description of Program: The following program builds a Query Processing Utility and carries out a series of commands inputted by an user.
    
def dictionaryandcountynames():
    populationdata = open("populationdata.csv", "r")
    census2010total = 0
    estimated2020total = 0
    countynames = [] #create list of county names
    dictionary = {} #create empty dictionary

    line = populationdata.readline()

    while line: #as this is a while loop, it will be repeated for all lines in the file
       #ignore lines that begin with #
       if "#" in line:
            line = populationdata.readline()
            continue
       else:
            countyNamed, census, estimated = line.split(",") #split the line into the county name, the population of the county as of the 2010 census, and the estimate of the county population as of January 1, 2020 on the basis of commas
            countyName = countyNamed.lower() #lowercase county names
            estimated20200 = estimated.strip("\n") #strip newline from estimate
            estimated2020 = int(estimated20200)
            census2010 = int(census)
            census2010total += census2010 #keep a running total of census2010
            estimated2020total += estimated2020  #maintain a running total of estimated2020
            countynames.append(countyName) #add each county name to the list of county names
            dictionary[countyName] = (census2010, estimated2020) #create an entry in the dictionary with the county name as the key and census2010 and estimated2020 as the values
            line = populationdata.readline()

    dictionary["texas"] = (census2010total, estimated2020total) #create one more entry in the dictionary with "texas" as the key and census2010total and estimated2020total as the values

    return (dictionary, countynames)

def main():
    import os.path
    if not os.path.isfile("populationdata.csv"): #Check if file truly exists, and if not, print the corresponding error message and return
        print("File does not exist")
        return
    dictionary, countynames = dictionaryandcountynames()
    #Print the welcome message displayed to the user
    print()
    print("Welcome to the Texas Population Dashboard.\nThis provides census data from the 2010 census and\nestimated population data in Texas as of 1/1/2020.")
    print()
    print("Creating dictionary from file: populationdata.csv")
    print()
    print("Enter any of the following commands:")
    print("Help - list available commands;\nQuit - exit this dashboard;\nCounties - list all Texas counties;\nCensus <countyName>/Texas - population in 2010 census by specified county or statewide;\nEstimated <countyName>/Texas - estimated population in 2020 by specified county or statewide.\nGrowth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
    print()
    while(True):
        commandInput = input("Please enter a command: ")
        # Parse the command into a list of words, assuming there's no punctuation.
        commWords = commandInput.split()
        # Extract the first word in the command.  It will be the instruction to perform.
        comm = commWords[0].strip()
        # Extract the rest of the words and re-assemble them into a single string,
        # separated by spaces.  These are the instuction's argument, if any.
        args = commWords[1:]
        arg = " ".join(args).strip()
        commmodified = comm.lower() #lowercase the argument, as commands are not case-sensitive
        if (commmodified == "help"): #if "help" is entered, print the list of commands
            print()
            print("Help - list available commands;\nQuit - exit this dashboard;\nCounties - list all Texas counties;\nCensus <countyName>/Texas - population in 2010 census by specified county or statewide;\nEstimated <countyName>/Texas - estimated population in 2020 by specified county or statewide.\nGrowth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
            print()
        elif (commmodified == "quit"): #display goodbye message if "quit" is entered
            print("Thank you for using the Texas Population Database Dashboard.  Goodbye!")
            return
        elif (commmodified == "counties"): #print the list of counties with 10 per line if "counties" is inputted
            linecount = 0 #this is used to keep track of how many counties have been printed on each line
            for element in range(len(countynames)): #this for loop will be executed for each element in the list of county names
                newelement = countynames[element].title() #capitalize first letter of each county name
                print(newelement, ", ", sep="", end="")
                linecount += 1 #every time a county name is printed, increase counter by 1
                if (linecount == 10): #if 10 county names have already been printed on the line, move to the next line
                    print()
                    linecount = 0 #reset counter to 0
            print()
            print()
        elif (commmodified == "census"): #if "census" is entered, retrieve and display the census2010 information from the dictionary
            argumodified = arg.lower() #lowercase the following input
            if (argumodified == "texas"): #if input is "texas", retrieve and display the census2010total information
                print("Texas total population in the 2010 Census:", dictionary["texas"][0])
                print()
            else:
                if (argumodified in dictionary): #if input is a county, retrieve and display the corresponding population in the census of 2010
                    print(argumodified.title(), "county had", dictionary[argumodified][0], "citizens in the 2010 Census.")
                    print()
                else: #if input is not "texas" or a county name, print the error message
                    print("County", argumodified.title(), "is not recognized.")
                    print()
        elif (commmodified == "estimated"): #if "estimated" is entered, retrieve and display the estimated2020 information from the dictionary
            argumodified = arg.lower()
            if (argumodified == "texas"): #if input is "texas", retrieve and display the estimated2020total information
                print("Texas estimated population (January, 2020):", dictionary["texas"][1])
                print()
            else:
                if (argumodified in dictionary): #if input is a county, retrieve and display the corresponding estimated population in 2020
                    print(argumodified.title(), "county had estimated population (January, 2020):", dictionary[argumodified][1])
                    print()
                else: #if input is not "texas" or a county name, print the following error message
                    print("County", argumodified.title(), "is not recognized.")
                    print()
        elif (commmodified == "growth"): #if "growth" is entered, calculate and display the percentage difference between the 2010 census data and the corresponding 2020 estimated population data
            argumodified = arg.lower() 
            if (argumodified == "texas"): #if "texas" is inputted, compute and print the relevant population change
                print("Texas had percent population change (2010 to 2020): ", format(((dictionary[argumodified][1] - dictionary[argumodified][0])/dictionary[argumodified][0]) * 100.0, ".2f"), "%", sep="")
                print()
            else:
                if (argumodified in dictionary):#if a county is inputted, compute and print the relevant population change
                    print(argumodified.title(), " county had percent population change (2010 to 2020): ", format(((dictionary[argumodified][1] - dictionary[argumodified][0])/dictionary[argumodified][0]) * 100.0, ".2f"), "%", sep="")
                    print()
                else: #if any other name is entered, print an error message suggesting that the name is not recognized as a county
                    print("County", argumodified.title(), "is not recognized.")
                    print()
        else: #if any other command is entered, print the following error message and allow the user to try again
            print("Command is not recognized.  Try again!")
            print()

main()
