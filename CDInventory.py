#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (DTsakalos, 2021-Feb-14, Completing Assignment 05)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declare variables
strChoice = '' # User input
lstTbl = []  # list of dics to hold data
dicRow = {}  # dic of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory')
while True:

    # 1. Display menu allowing the user to choose:
    print('\n------------MENU------------')
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('\nl, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    # 2. Exit the program if the user chooses so
    if strChoice == 'x':
        print('\nThank you for choosing us!')
        break

    # 3. Load existing data
    # no elif necessary, as this code is only reached if strChoice is not 'exit'
    if strChoice == 'l':
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('=====|==============================|==============================|')
        print(' ID  |           CD Title           |          Artist Name         |')
        print('=====|==============================|==============================|')
        for row in lstTbl:
            print("{0:<5}|{1:^30}|{2:^30}|\n-----|------------------------------|------------------------------|".format(*row.values()))
        print()

    # 4. Add data to the table (2d-list) each time the user wants to add data
    elif strChoice == 'a':
        while True:
            try:
                intID = int(input('Enter an ID: '))
                break
            except ValueError:
                print('Invalid Input! Try again.')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)

    # 5. Display the current data to the user each time the user wants to display the data
    elif strChoice == 'i':
        print('=====|==============================|==============================|')
        print(' ID  |           CD Title           |          Artist Name         |')
        print('=====|==============================|==============================|')
        for row in lstTbl:
            print("{0:<5}|{1:^30}|{2:^30}|\n-----|------------------------------|------------------------------|".format(*row.values()))

    # 6. Delete an entry
    elif strChoice == 'd':
        # Display existing data
        print('=====|==============================|==============================|')
        print(' ID  |           CD Title           |          Artist Name         |')
        print('=====|==============================|==============================|')
        for row in lstTbl:
            print("{0:<5}|{1:^30}|{2:^30}|\n-----|------------------------------|------------------------------|".format(*row.values()))
        # Remove selected rows
        old = len(lstTbl) #count old entries
        while True:
            try:
                idRemove = int(input('\nPlease select the ID number of the row to be removed: ').strip())
                break
            except ValueError:
                print('Invalid Input! Try again.')
        lstTbl[:] = [i for i in lstTbl if i.get('id') != idRemove]
        new = len(lstTbl) # count new entries
        dif = old - new
        print('\nYou removed', dif, 'entries') # display entries removed
        # Display new data
        print('Current Inventory:')
        print('=====|==============================|==============================|')
        print(' ID  |           CD Title           |          Artist Name         |')
        print('=====|==============================|==============================|')
        for row in lstTbl:
            print("{0:<5}|{1:^30}|{2:^30}|\n-----|------------------------------|------------------------------|".format(*row.values()))

    # 7. Save the data to a text file CDInventory.txt if the user chooses so
    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Your Data has been saved!')

    else:
        print('Please choose either l, a, i, d, s or x!')















