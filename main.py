#2243392-Pınar Dilbaz

import matplotlib.pyplot as plt
import sys

def read_file(data):
    #this is the first line of datafile.txt and we should skip this line
    skip = ["PageName", "ElementName", "UserID", "UserGender", "UserGroup", "TimeViewed", "Fixations", "Revisits"]
    #we take the file name from the command-line argument 
    if (len(sys.argv))!=2:
        #if the command-line argument is invalid, the program will display the error message and exit
        print("Invalid parameter!")
        exit()
    try:
        #try to read the file
        file = open(sys.argv[1],"r")
    except:
        #if the file could not open, the program will display the error message and exit
        print("File could not opened!")
        exit()
    else:
        with open(sys.argv[1]) as file:
            for line in file:
                if not any(x in line for x in skip):
                    #split the line with ';'
                    paramSet = [param.strip() for param in line.split(';')]
                    pageName = paramSet[0]
                    elementName = paramSet[1]
                    userID = paramSet[2]
                    userGender = paramSet[3]
                    userGroup = paramSet[4]
                    timeViewed: str = paramSet[5]
                    fixations = paramSet[6]
                    revisits = paramSet[7]
                    #create the dictionary for required data
                    #if there is no pageName in dictionary then we it to dictionary as key
                    if pageName in data.keys():
                        elements = data[pageName]
                    #if there is pageName in dictionary then we it to dictionary as value 
                    else:
                        data[pageName] = dict()
                        elements = data[pageName]

                    if elementName in elements.keys():
                        groups = elements[elementName]
                    else:
                        elements[elementName] = dict()
                        groups = elements[elementName]

                    if userGroup in groups.keys():
                        users = groups[userGroup]
                    else:
                        groups[userGroup] = [0,0,0]
                        users = groups[userGroup]
                    #the sum of timeViewed, fixations and revisits
                    users[0]+=float(timeViewed)
                    users[1]+=int(fixations)
                    users[2]+=int(revisits)


def run():
    #create a dictionary
    data = dict()
    read_file(data)
    print(data)
    # display the menu
    print(
        "1. Compare the total time viewed, the total number of fixations or the total number of revisits for people with and without autism for a particular element on a specific web page")
    print(
        "2. Compare the total time viewed, the total number of fixations or the total number of revisits for people with and without autism on a specific web page")
    print("3. Exit")
    #take the selection from the user
    selection = int(input("Please enter your selection: "))
    metricName = ""
    metricName2 = ""
    #if the user does not want to exit, program will keep asking the selection again
    while (selection != 3):
        #if the selection 1 is chose
        if (selection == 1):
            print("Please enter the required details for first choice!")
            #displaying the required data
            print("1. The total time viewed")
            print("2. The total number of fixations")
            print("3. The total number of revisits)")
            #and user select the required data
            metric = int(input("Choose one of the metric above: "))
            if (metric == 1):
                metricName = "The total time viewed"
            elif (metric == 2):
                metricName = "The total number of fixations"
            elif (metric == 3):
                metricName = "The total number of revisits"

            element = input("Please enter the element: ")

            page = input("Please enter the page: ")

            # ploting the first choice
            groups = ["People with Autism", "People Without Autism"]
            valNorm = data[page][element]['CONTROL'][metric-1]
            valAuth = data[page][element]['ASD'][metric-1]
            
            values = [valAuth,valNorm]
            plt.bar(groups, values)
            plt.xlabel('Groups')
            plt.ylabel(metricName)
            plt.title('Comparison Between People With & Without Autism\nfor Element %s on Page %s' % (element, page))
            plt.show()

        #if the selection 2 is chose
        elif (selection == 2):
            print("2")
            print("Please enter the required details for second choice!")

            print("1. The total time viewed")
            print("2. The total number of fixations")
            print("3. The total number of revisits)")

            metric2 = int(input("Choose one of the metric above: "))
            if (metric2 == 1):
                metricName2 = "The total time viewed"
            elif (metric2 == 2):
                metricName2 = "The total number of fixations"
            elif (metric2 == 3):
                metricName2 = "The total number of revisits"

            page2 = input("Please enter the page: ")

            # ploting the seconf choice
            groups = ["People with Autism", "People Without Autism"]
            valNorm = 0
            valAuth = 0
            for i in data[page2]:
                valNorm += data[page2][i]['CONTROL'][metric2 - 1]
                valAuth += data[page2][i]['ASD'][metric2 - 1]

            values = [valAuth, valNorm]
            plt.bar(groups, values)
            plt.xlabel('Groups')
            plt.ylabel(metricName2)
            plt.title('Comparison Between People With & Without Autism\n on Page %s' % (page2,))
            plt.show()


        else:
            print("Invalid input! Please try again")

        selection = int(input("Please enter your selection: "))

    if (selection == 3):
        print("Good Bye!!")


if __name__ == '__main__':
    run()
