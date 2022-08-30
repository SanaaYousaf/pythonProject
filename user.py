import json
from csv import writer


class User:

    def __init__(self, name, acc_no, password, balance=0):
        self.name = name
        self.account_no = acc_no
        self.password = password
        self.balance = balance

    def get_name(self):
        return self.name

    def get_account_no(self):
        return self.account_no

    def get_balance(self):
        return self.balance

    @staticmethod
    def my_update(key, temp):
        temp['name'] = key['name']
        temp['account_no'] = key['account_no']
        temp['password'] = key['password']
        temp['balance'] = key['balance']

    def is_valid(acc_no, password):
        jsonfile = open("user.json", "r")
        mydata = json.load(jsonfile)
        jsonfile.close()
        for key in mydata:
            if key["account_no"] == acc_no and key['password'] == password:
                user = User(key['name'], key['account_no'], key['password'], key['balance'])
                return user

    def is_valid_acc(acc_no):
        jsonfile = open("user.json", "r")
        mydata = json.load(jsonfile)
        jsonfile.close()
        for key in mydata:
            if key["account_no"] == acc_no :
                return True
        else:
            return False

    def deposit(self, amount):
        jsonfile = open("user.json", "r")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key['account_no'] == self.account_no:
                temp = {}
                key['balance'] += amount
                User.my_update(key, temp)
                new_data.append(temp)
                with open('transaction.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow({self.account_no, "You deposit "+str(amount)})
                    f_object.close()
            else:
                temp = {}
                User.my_update(key, temp)
                new_data.append(temp)
        with open("user.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    def withdraw(self, amount):
        jsonfile = open("user.json", "r")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key['account_no'] == self.account_no:
                temp = {}
                key['balance'] -= amount
                User.my_update(key, temp)
                new_data.append(temp)
                with open('transaction.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow({self.account_no, "You withdraw "+str(amount)})
                    f_object.close()
            else:
                temp = {}
                User.my_update(key, temp)
                new_data.append(temp)
        with open("user.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    def transfer(self, to_acc_no, amount):
        jsonfile = open("user.json", "r")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key['account_no'] == self.account_no:
                temp = {}
                key['balance'] -= amount
                User.my_update(key, temp)
                new_data.append(temp)
            elif key['account_no'] == to_acc_no:
                temp = {}
                key['balance'] += amount
                User.my_update(key, temp)
                new_data.append(temp)
                with open('transaction.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow({self.account_no, "You transfer " + str(amount) + " to " + to_acc_no})
                    f_object.close()
            else:
                temp = {}
                User.my_update(key, temp)
                new_data.append(temp)

            with open("user.json", "w") as f:
                f.write(json.dumps(new_data, indent=4))

    @staticmethod
    def unique(acc_no):
        with open("user.json", 'r') as j:
            mydata = json.load(j)
        for key in mydata:
            if key["account_no"] == acc_no:
                return True
        return False

    def show_profile(self):
        with open("user.json", 'r') as j:
            mydata = json.load(j)
        for key in mydata:
            if key["account_no"] == self.account_no:
                print(key)

    def update_user(self, user):
        user.add_user()
        self.del_user()