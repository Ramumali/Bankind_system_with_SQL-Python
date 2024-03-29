import mysql.connector
from datetime import date
#--------------------------------------------------------------------------------
def clear():
    for _ in range(65):
        print()
#--------------------------------------------------------------------------------
def account_status(acno):
    connection = mysql.connector.connect(host='localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    sql = "select status, balance from customer where acno = '" + acno + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    connection.close()
    return result
#--------------------------------------------------------------------------------
def deposit():
    connection = mysql.connector.connect(host='localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    clear()
    acno = input('Enter account No : ')
    amount = input('Enter amount: ')
    today = date.today()
    result = account_status(acno)
    if result[0] == 'active':
        sql1 = "update customer set balance = balance + " + amount + " where acno = " + acno + " and status = 'active';"
        sql2 = "insert into transaction (amount, type, acno, dot) values (" + amount + ", 'deposit', " + acno + ", '" + str(today) + "');"
        cursor.execute(sql1)
        cursor.execute(sql2)
        print("The amount deposited successfully")
    else:
        print("Suspend account")
    wait = input("Enter any key to press for continue")
    connection.close()
#--------------------------------------------------------------------------------
def withdraw():
    connection = mysql.connector.connect(host='localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    clear()
    acno = input('Enter account No : ')
    amount = input('Enter amount: ')
    today = date.today()
    result = account_status(acno)
    if result[0] == 'active' and int(result[1]) >= int(amount):
        sql1 = "update customer set balance = balance - " + amount + " where acno = " + acno + " and status = 'active';"
        sql2 = "insert into transaction (amount, type, acno, dot) values (" + amount + ", 'withdraw', " + acno + ", '" + str(today) + "');"
        cursor.execute(sql1)
        cursor.execute(sql2)
        print("The amount withdrawn successfully")
    else:
        print("Suspend account")
    wait = input("Enter any key to press for continue")
    connection.close()
#--------------------------------------------------------------------------------    
def transaction_menu():
    while True:
        clear()
        print('Trasaction menu')
        print("1.Deposit Amount")
        print('2.withoraw amount')
        print('3.Back to Main penu')
        print("\n\n\n")
        choice = int(input('Enter your choice:'))
        if choice == 1:
            deposit()
        if choice == 2:
            withdraw()
        if choice == 3:
            main_menu()
#--------------------------------------------------------------------------------
def search_menu():
    connection = mysql.connector.connect(host='localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    while True:
        clear()
        print("Search menu")
        print('1. Account number')
        print("2. Aadhar card")
        print('3. Phone number')
        print("4. Email")
        print('5. Name')
        print("6. Back to main menu")
        print("\n\n\n")
        choice = int(input('Enter your choice: '))
        field_name = ''
        if choice == 1:
            field_name = 'acno'
        if choice == 2:
            field_name = 'aadhar_no'  # Corrected variable name
        if choice == 3:
            field_name = 'phone'
        if choice == 4:
            field_name = 'email'
        if choice == 5:
            field_name = 'name'
        if choice == 6:
            main_menu()
        msg = 'Enter ' + field_name + ': '
        value = input(msg)
        if field_name == 'acno':
            sql = 'select * from customer where ' + field_name + ' = ' + value + ';'
        else:
            sql = 'select * from customer where ' + field_name + ' like "%' + value + '%";'  # Corrected SQL query
        cursor.execute(sql)
        records = cursor.fetchall()
        n = len(records)
        clear()
        print('Search Result for', field_name, ' ', value)
        print('-' * 80)
        for record in records:
            print(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8])
        if n <= 0:
            print(field_name, ' ', value, ' does not exist')  # Corrected message
        wait = input('\n\n\n Press any key to continue. ')

#--------------------------------------------------------------------------------
def account_details():
    clear()
    acno = input("Enter the account Number: ")
    connection = mysql.connector.connect(host = ' localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    sql1 = 'select * from customer where acno= '+acno+';'
    sql2 = 'select tid,dot,amount,type from transaction t where t.acno='+acno+';'
    cursor.execute(sql1)
    result = cursor.fetchone()
    clear()
    print("Account Details are given by:")
    print('-'*120)
    print("Account No:",result[0])
    print("Customer Name:",result[1])
    print("Address:",result[2])
    print("phone No:",result[3])
    print("Email:",result[4])
    print("Aadhar No:",result[5])
    print("Account Type",result[6])
    print("Account Status:",result[7])
    print("Account Balance:",result[8])
    print('-'*120)
    cursor.execute(sql2)
    results = cursor.fetchall()
    for result in results:
        print(result[0],result[1],result[2],result[3])
    connection.close()
    wait = input('\n\n\n Press any key to continue. ')
#--------------------------------------------------------------------------------
def add_account():
    connection = mysql.connector.connect(host = ' localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    today = date.today()
    name = input('Enter Name: ')
    addr = input('Enter address:')
    phone = input('Enter Phone no :')
    email = input('Enter Email :')
    aadhar = input('Enter AAdhar no :')
    actype = input('Account Type (saving/current): ')
    balance = input('Enter opening balance: ')
    sql = 'insert into customer(name,address,phone,email,aadhar_no,acc_type,balance,status) values ("' +name+'","'+addr+ '","'+phone+ '","'+email+ '","'+aadhar+ '","'+actype+ '","'+balance+ '","'+str(today)+' ");'
    cursor.execute(sql)
    print("New Custmer Account Created Succesfully")
    wait = input('\n\n\n Press any key to continue. ')
#--------------------------------------------------------------------------------
def modify_account():
    connection = mysql.connector.connect(host = 'localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    clear()
    acno = input("Enter the account Number:")
    print("Modification Screen")
    print("1.Customer Name")
    print("2.Customer Address")
    print("3.Customer Phone_no")
    print("4.Customer Email_id")
    choice = int(input("What do you want to Change in your Account? "))
    new_data = input("Enter a value: ")
    field_name = ''
    if choice == 1:
        field_name = 'name'
    if choice == 2:
        field_name = 'address'
    if choice == 3:
        field_name = 'phone'
    if choice == 4:
        field_name = 'email'
    sql = 'update customer set '+field_name+'="'+new_data+'"where acno='+ acno+';'
    print(sql)
    cursor.execute(sql)
    print("Customer Info modified Succesfully")
    wait = input('\n\n\n Press any key to continue. ')
#--------------------------------------------------------------------------------
def close_account():
    connection = mysql.connector.connect(host = 'localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    clear()
    acno = input("Enter the account Number:")
    sql = 'update customer set status = "close" where acno ='+acno+';'
    cursor.execute(sql)
    print("Account Closed Succesfully")
    wait = input('\n\n\n Press any key to continue. ')
#--------------------------------------------------------------------------------
def activate_account():
    connection = mysql.connector.connect(host = 'localhost', database='bank_project', user='root', password='ramu1234')
    cursor = connection.cursor()
    clear()
    acno = input("Enter the account Number:")
    sql = 'update customer set status = "active" where acno ='+acno+';'
    cursor.execute(sql)
    print("Account Activated Succesfully")
    wait = input('\n\n\n Press any key to continue. ')
#--------------------------------------------------------------------------------
def main_menu():
    clear()
    print("Main Menu")
    print("1.Add Account")
    print("2.Modify account")
    print("3.Close Account")
    print("4.Activate Account")
    print("5.Transaction Menu")
    print("6.Search Menu")
    print("7.Close the App")
    print("\n\n")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        add_account()
    if choice == 2:
        modify_account()
    if choice == 3:
        close_account()
    if choice == 4:
        activate_account()
    if choice == 5:
        transaction_menu()
    if choice == 6:
        search_menu()
    if choice == 7:
        return
#--------------------------------------------------------------------------------
if __name__ == '__main__':
    main_menu()
