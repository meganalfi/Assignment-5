#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dicTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # DONE - 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # DONE - Add the functionality of loading existing data
        pass
        objFile = open(strFileName,'r') # create .txt file
        for row in objFile:
            lstRow = row.strip().split(',')
            print (lstRow)
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. DONE - Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title':strTitle, 'Artist':strArtist}       
        dicTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. DONE - Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in dicTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # DONE - Add functionality of deleting an entry
        dicDelete = input('Enter ID you want to delete: ')
        dicDeleteInt = int(dicDelete)
        for row in dicTbl:
            if row['ID'] == dicDeleteInt:
                dicTbl.remove(row)
    elif strChoice == 's':
        # DONE - 4. Save the data to a text file CDInventory.txt if the user chooses so    
        objFile = open(strFileName, 'a')
        for row in dicTbl:
            strRow = str(row['ID'])+','+ row['Title']+','+ row['Artist']
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')
