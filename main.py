from user import User
from admin import Admin


def user_input(user):
    option = input("1. TransferMoney 2.DepositMoney 3.WithdrawMoney 4.ViewProfile")
    if option == '1':
        acc_no = input("Enter Account_No you want to transfer  ")
        if User.is_valid_acc(acc_no):
            amount = input("Enter Amount")
            if Admin.is_valid_transfer(user, int(amount)):
                user.transfer(acc_no, (int(amount)))
                print("successfully transferred")
            else:
                print("Not valid transaction")
        else:
            print(" Sorry!Not valid account_no")

    elif option == '2':
        amount = input("Enter Amount")
        user.deposit(int(amount))
        print("successfully deposit")
    elif option == '3':
        amount = input("Enter Amount")
        if Admin.is_valid_withdraw(user, int(amount)):
            user.withdraw(int(amount))
            print("successfully withdraw")
        else:
            print("Not valid transaction")
    elif option == '4':
        user.show_profile()

    else:
        print("invalid option selected")


def admin_input(admin):
    option = input("1. AddUser 2. DeleteUser 3.SearchUser 4.ViewUser 5. ViewAllUsers 6.AddAdmin"
                   " 7.DeleteAdmin 8.ChangePassword  9.ViewProfile  10.ViewTransaction")
    if option == '1':
        name = input("Enter name")
        acc_no = input("Enter account_no")
        if User.unique(acc_no):
            print("Please enter unique account_no")
        else:
            password = input("Enter password")
            user = User(name, acc_no, password)
            Admin.add_user(user)
    elif option == '2':
        acc_no = input("Enter account_no you want to remove ")
        if User.is_valid_acc(acc_no):
            Admin.del_user(acc_no)
        else:
            print("Sorry! wrong account no")
    elif option == '3':
        acc_no = input("Enter account_no you want to search")
        if Admin.search_user(acc_no):
            print('exist')
        else:
            print("Not exist")
    elif option == '5':
        Admin.show()
    elif option == '4':
        acc_no = input("Enter account_no you want to search")
        if User.is_valid_acc(acc_no):
            Admin.show_user_profile(acc_no)
        else:
            print("Sorry! wrong account no")
    elif option == '6':
        name = input("Enter name")
        id = input("Enter id")
        if Admin.unique(id):
            print("Please enter unique id")
        else:
            password = input("Enter password")
            admin = Admin(name, id, password)
            admin.add_admin()
    elif option == "7":
        acc_no = input("Enter id you want to remove")
        if Admin.is_valid_acc(acc_no):
            Admin.del_admin(acc_no)
        else:
            print("Sorry! wrong account no")
    elif option == '8':
        new_password = input("Enter new password")
        admin.change_password(new_password)
    elif option == '9':
        admin.show_profile()
    elif option == '10':
        acc_no = input("Enter the account no ")
        if User.is_valid_acc(acc_no):
            Admin.view_transaction(acc_no)
        else:
            print("Sorry! wrong account no")
    else:
        print("wrong input")


option = input("1. Admin  2.User  ")
if option == '1':
    print("Login")
    id = input("Enter id ")
    Pass = input("Enter Password ")
    admin = Admin.is_valid(id, Pass)
    if admin == None:
        print("wrong id and password")
    else:
        admin_input(admin)
elif option == '2':
    print("Login")
    Account_no = input("Enter Account_No ")
    Pass = input("Enter Password ")
    user = User.is_valid(Account_no, Pass)
    if user == None:
        print("wrong id and password")
    else:
        user_input(user)
else:
    print("invalid option selected")
