# HOTEL MANAGEMENT SYSTEM- BOOKING, MENU, RENT AND BILLING#
# BY SANJAY PUGAL-CLASS 12B#
# RUSHIL KAUL- CLASS 12B#
# DASARI VAMSHI KRISHNA- CLASS 12B#

import time

import mysql.connector
from tabulate import tabulate

global mydb
global mycursor
global ID

# ENTERING PASSWORD
while True:
    try:
        Pass = input('Enter Password: ')
        mydb = mysql.connector.connect(host='localhost', user='root', passwd=Pass)
        break
    except mysql.connector.errors.DatabaseError as e:
        print(e)

# CREATING AND ACCESSING DATABASE
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
mycursor.execute('USE HOTEL')
mydb.autocommit = True


# Display menu
def Menu():
    print('Welcome to VRSG Inc!')
    time.sleep(2)
    print('Quality at its finest!')
    time.sleep(2)
    while True:
        print('--------------------------------')
        print('*         VRSG Main Menu       *')
        print('--------------------------------')
        print('*       1. Bookings Manager    *')
        print('*       2. Rent Facility       *')
        print('*       3. Restaurant Menu     *')
        print('*       4. Bill Manager        *')
        print('*           5. Quit            *')
        print('--------------------------------')
        while True:
            try:
                n = int(input('Enter Number from 1 to 5[Press 5 to quit]: '))
                if n not in [1, 2, 3, 4, 5]:
                    print("Invalid entry, try again")
                    print()
                    continue
                break
            except ValueError:
                print("Invalid entry, try again")
                print()
        print('Loading....')
        time.sleep(2)
        if n == 1:
            while True:
                print('--------------------')
                print('*   Bookings Menu  *')
                print('--------------------')
                print('*      1.Book      *')
                print('* 2.Cancel Booking *')
                print('*   3.View Table   *')
                print('*      4.Quit      *')
                print('--------------------')
                while True:
                    try:
                        n2 = int(input('Enter Number From 1 to 4: '))
                        if n not in [1, 2, 3, 4]:
                            print("Invalid entry, try again")
                            print()
                            continue
                        break
                    except ValueError:
                        print("Invalid entry, try again")
                        print()
                if n2 == 1:
                    print('Create Booking Menu')
                    print('Loading....')
                    time.sleep(2)
                    Book()
                elif n2 == 2:
                    cancel()
                elif n2 == 3:
                    print("Loading...")
                    time.sleep(1)
                    SelectTable()
                    time.sleep(2)
                elif n2 == 4:
                    print("Exiting...")
                    time.sleep(1)
                    break

        elif n == 2:
            roomRent()
        elif n == 3:
            while True:
                print('--------------------')
                print('*    Menu Manager  *')
                print('--------------------')
                print('*  1. View Table   *')
                print('*  2.Enter Items   *')
                print('*  3.Update Table  *')
                print('*     4. Quit      *')
                print('--------------------')
                while True:
                    try:
                        A = int(input('Enter Number from 1 - 4: '))
                        break
                    except ValueError:
                        print("Enter valid input")
                        time.sleep(1)
                if A == 1:
                    ViewMenu()
                elif A == 2:
                    MenuValues()
                elif A == 3:
                    Update()
                else:
                    print('Quitting')
                    time.sleep(2)
                    break
        elif n == 4:
            time.sleep(1)
            print('-----------------------')
            print('*     Bill Manager    *')
            print('-----------------------')
            print('*      1. Add Bill    *')
            print('*    2. Display Bill  *')
            print('-----------------------')
            global G
            while True:
                try:
                    G = int(input('Enter Number from 1 to 2: '))
                except ValueError as v:
                    print(v)
                if G == 1:
                    Bill()
                    break
                elif G == 2:
                    RetrieveBill()
                    break
                else:
                    print('Invalid Input')
                    continue

        elif n == 5:
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print('Invalid')
            continue


# Booking
def Book():
    while True:
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS BOOKINGS(FNAME VARCHAR(20), LNAME VARCHAR(20), ID int(5) PRIMARY KEY, ROOM INT(3), NIGHTS INT(5))")
        while True:
            fname = input('Enter First Name: ')
            if fname.isalpha() is False:  # Only alphabetical names
                print("Enter first name (alphabets a-z, A-Z only): ")
                time.sleep(1)
                continue
            else:
                break
        while True:
            lname = input('Enter Last Name: ')  # Only alphabetical names
            if lname.isalpha() is False:
                print("Enter last name (alphabets a-z, A-Z only): ")
                time.sleep(1)
                continue
            else:
                break
        while True:
            try:
                room = int(input("Enter room number: "))  # Room number entry
                break
            except ValueError:
                print("Enter room number correctly (digits 0-9 allowed only)")
        while True:
            try:
                bkid = int(input('Enter booking ID: '))  # Booking ID of customer entry
                break
            except ValueError:
                print("Enter booking ID correctly (digits 0-9 only)")
                print()
        while True:
            try:
                nights = int(input("Enter number of nights: "))  # No of nights entry
                break
            except ValueError:
                print("Enter number of nights correctly (digits 0-9 only)")
                print()
        try:
            com = """Insert into bookings values(%s,%s,%s,%s,%s)"""  # Insertion into table
            mycursor.execute(com, (fname, lname, room, bkid, nights))
        except mysql.connector.errors.IntegrityError as e:
            print(e)
            continue
        print('Data Entered Successfully')
        print()
        time.sleep(1)
        while True:
            q = input('Close Menu?: ').lower()  # If yes, closes menu, if no, returns to while loop
            if q in ['yes', 'y']:
                print('Closing Menu...')
                time.sleep(2)
                break
            elif q in ['no', "n"]:
                print()
                Book()
            else:
                print("Invalid input, enter again")
                print()
                continue
            break
        break


# Cancelling/removing bookings
def cancel():
    global ID
    while True:
        LName = input("Last Name registered for booking: ")
        if LName.isalpha():  # Last Name should only be alphabet
            try:
                ID = int(input("Booking ID: "))
            except ValueError:
                print("Booking ID should only contain digits 0-9")
                print()
                continue
            CMD = "Select * from bookings where LNAME=%s and ID=%s"
            mycursor.execute(CMD, (LName, ID))
            Data = mycursor.fetchall()
            if Data:
                break  # if Data has something it will exit
            else:
                print("The booking ID or last name entered are incorrect, please try again.")
                continue
        else:
            print("Invalid Name, please try again")
            continue  # prompts again
    print("Are you sure you wish to cancel this booking for booking with last name", LName, "with booking ID",
          ID, "?")
    print("Yes (Cancels booking)")
    print("No (Return to main menu)")
    while True:
        N = input('Please Enter Yes or No: ')
        if N == "Yes":
            print("Loading...")
            time.sleep(1)
            print("Cancelling booking...")
            time.sleep(2)
            Command = "Delete from bookings where LName=%s and ID=%s"
            mycursor.execute(Command, (LName, ID))
            break
        elif N == "No":
            print("Returning to menu...")
            time.sleep(1)
            Menu()
        else:
            print("Invalid, Please enter Yes or No")
            time.sleep(1)
            continue
    print("Booking has been cancelled successfully")
    time.sleep(1)


# Viewing bookings table
def SelectTable():
    mycursor.execute("Select * from bookings")
    DATA1 = mycursor.fetchall()
    Headers = ["FNAME", "LNAME", "ID", "ROOM", "NIGHTS"]
    print(tabulate(DATA1, Headers, tablefmt='fancy_grid'))


# TO SHOW RENT FOR A CUSTOMER
def roomRent():
    print('Entering Rent Facility')
    time.sleep(2)
    createTable = "CREATE TABLE IF NOT EXISTS ROOM_RENT(ID VARCHAR(20) PRIMARY KEY, ROOM_NO INT, ROOM_CHOICE INT, NO_OF_NIGHTS INT, ROOM_RENT INT)"
    mycursor.execute(createTable)
    print("  The following rooms are available: ")
    print(" 1. Suite ----> ₹ 9000")
    print(" 2. King ----> ₹ 7500")
    print(" 3. Double ----> ₹ 5000")
    print(" 4. Single ----> ₹ 3000")
    while True:
        try:
            roomtype = int(input("Enter choice: "))
            break
        except ValueError:
            print("Invalid room type (digits 1-4 allowed only)")
            print()
    while True:
        try:
            roomno = int(input("Enter customer room no : "))
            break
        except ValueError:
            print("Invalid room number (digits 0-9 allowed only)")
            print()
    while True:
        try:
            nights = int(input("Enter number of nights : "))
            break
        except ValueError:
            print("Invalid number of nights (enter digits 0-9 only)")
            print()
    while True:
        global BID
        try:
            BID = int(input("Enter Booking ID: "))
        except ValueError:
            print("Invalid Booking ID (enter digits 0-9 only)")
            print()
        if roomtype == 1:
            roomrent = nights * 9000
            print("Suite room rent : ", roomrent)
        elif roomtype == 2:
            roomrent = nights * 7500
            print("King room rent : ", roomrent)
        elif roomtype == 3:
            roomrent = nights * 5000
            print("Double room rent : ", roomrent)
        elif roomtype == 4:
            roomrent = nights * 3000
            print("Single room rent : ", roomrent)
        else:
            print("Incorrect input, try again")
            return
        try:
            sql = """INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"""  # Insert room rents of customers into table
            values = (BID, roomno, roomtype, nights, roomrent)
            mycursor.execute(sql, values)
            break
        except mysql.connector.errors.IntegrityError:  # Prevent duplicate error from arising
            print("Duplicate entry, enter again")
            print()
    print("Details stored in table")
    time.sleep(1)


# Viewing created menu

def ViewMenu():
    print('Restaurant Menu Manager')
    time.sleep(1)
    print('Access is prohibited for personnel with clearance level 3 or below')
    time.sleep(1)
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS RESTAURANT(FID INT, ITEM VARCHAR(30), PRICE INT)')
    print('Displaying Menu')
    mycursor.execute("Select * from restaurant")  # Accessing whole restaurant menu
    time.sleep(2)
    try:
        VM = mycursor.fetchall()
        headers = ["FID", "ITEM", "PRICE"]
        print(tabulate(VM, headers, tablefmt='fancy_grid'))
    except mysql.connector.errors.ProgrammingError as k:
        print(k)
    except mysql.connector.errors.DatabaseError as f:
        print(f)
    except mysql.connector.errors.PoolError as g:
        print(g)
    except mysql.connector.errors.InterfaceError:
        print('No Data to display')


# Entering items into menu
def MenuValues():
    print('Enter Restaurant Menu')
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS RESTAURANT(FID INT PRIMARY KEY, ITEM VARCHAR(30), BILL INT)')
    while True:
        while True:
            try:
                FID = int(input('Enter food reference ID: '))
                print()
                time.sleep(1)
                break
            except ValueError:
                print("Enter valid food ID (digits 0-9)")
                print()
                time.sleep(1)
                continue
        Cuisine = input('Enter food item name: ')
        while True:
            try:
                bill = int(input('Enter price of item: '))
                print()
                time.sleep(1)
                break
            except ValueError:
                print("Enter valid price (digits 0-9)")
                print()
                continue
        com = 'INSERT INTO RESTAURANT VALUES(%s,%s,%s)'
        mycursor.execute(com, (FID, Cuisine, bill,))
        print("Successful entry")
        print()
        T = input('Quit? Yes/No: ')
        if T in ['Y', 'y', 'YES', 'Yes']:
            break


# Update menu
def Update():
    mycursor.execute('CREATE TABLE IF NOT EXISTS RESTAURANT(FID INT, ITEM VARCHAR(30), PRICE INT)')
    while True:
        try:
            nme = int(input("Enter ID of food to Update/Delete: "))
            break
        except ValueError:
            print("Reenter ID, only digits 0-9 allowed")
            print()
            continue
    while True:
        choice = input('Update/Delete: ')
        if choice == 'Delete':  # Deletion of item from menu
            com = 'DELETE FROM RESTAURANT WHERE FID = %s'
            mycursor.execute(com, (nme,))
            print("Successful delete")
            print()
            break
        elif choice == "Update":  # Changing price of item in menu
            while True:
                try:
                    b = int(input('Enter new price: '))
                    break
                except ValueError:
                    print("Enter an integer value as price")
                    print()
                    continue
            com = 'UPDATE RESTAURANT SET BILL = %s WHERE FID = %s'  # Setting new price
            mycursor.execute(com, (b, nme))
            print("Successful update")
            print()
            break
        else:
            print("Enter Update/Delete ONLY")
            continue


# Bill for customer
def Bill():
    while True:
        while True:
            try:
                Item = int(input("Enter food item code to be added to bill: "))
                break
            except ValueError:
                print("Enter code again, must contain digits 0-9 only")
                print()
                continue
        while True:
            try:
                ID = int(input("Enter customer ID: "))
                break
            except ValueError:
                print("Please enter valid ID")
                print()
                continue
        while True:
            try:
                Qty = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Please enter valid quantity")
                print()
                continue
        CMD = "Select * from bookings, restaurant where bookings.id=%s and restaurant.fid=%s"
        mycursor.execute(CMD, (ID, Item))
        Data = mycursor.fetchall()
        if Data:
            break
        else:
            print("The item or ID entered are incorrect, please try again.")
            continue
    mycursor.execute(
        'CREATE TABLE IF NOT EXISTS BILL(Customer_ID INT, LNAME VARCHAR (20), ITEM VARCHAR(30), QUANTITY INT, BILL INT)')
    billdata = "select bill from restaurant where FID=%s"  # Retrieve bill from other table
    mycursor.execute(billdata, (Item,))
    BILLDATA = mycursor.fetchone()
    BILLDATA1 = sum(BILLDATA) * Qty
    name = "select LName from bookings where ID=%s"  # Retrieve name from other table
    mycursor.execute(name, (ID,))
    NAME = mycursor.fetchone()
    NAME1 = ""
    for i in NAME:
        NAME1 += i
    COMMAND = "Insert into bill values(%s,%s,%s,%s,%s)"  # Inserting details of order
    Values = (ID, NAME1, Item, Qty, BILLDATA1)
    mycursor.execute(COMMAND, Values)
    print("Successful input")
    print()
    time.sleep(1)


def RetrieveBill():
    while True:
        while True:
            try:
                BookingID = int(input("Enter booking ID for bill: "))
                print()
                break
            except ValueError:
                print("Please enter only digits")
                print()
                continue
        CMD = "select * from bookings where ID=%s"
        mycursor.execute(CMD, (BookingID,))
        Data = mycursor.fetchall()
        if Data:
            break
        else:
            print("ID incorrect, try again")
            print()
            continue
    BILLCOMMAND = "select * from bill where bill.Customer_ID=%s"
    mycursor.execute(BILLCOMMAND, (BookingID,))
    try:
        RETRIEVE1 = mycursor.fetchall()
        headers1 = ["Customer ID", "LName", "Item", "Quantity", "Bill"]
        print(tabulate(RETRIEVE1, headers1, tablefmt='fancy_grid'))
    except mysql.connector.errors.ProgrammingError as k:
        print(k)
    except mysql.connector.errors.DatabaseError as f:
        print(f)
    except mysql.connector.errors.PoolError as g:
        print(g)
    except mysql.connector.errors.InterfaceError:
        print('No Data to display')
    BILLSUM = "select sum(bill) from bill where Bill.Customer_ID=%s"  # Displaying bill for particular customers
    mycursor.execute(BILLSUM, (BookingID,))
    try:
        RETRIEVE = mycursor.fetchall()
        headers = ["Total_Bill"]
        print(tabulate(RETRIEVE, headers, tablefmt='fancy_grid'))
    except mysql.connector.errors.ProgrammingError as k:
        print(k)
    except mysql.connector.errors.DatabaseError as f:
        print(f)
    except mysql.connector.errors.PoolError as g:
        print(g)
    except mysql.connector.errors.InterfaceError:
        print('No data to display')


Menu()