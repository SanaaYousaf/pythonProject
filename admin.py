import csv

from user import User
import json


class Admin:
    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    @staticmethod
    def is_valid_acc(id):
        jsonfile = open("admin.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        for key in mydata:
            if key["id"] == id:
                return True
        else:
            return False

    @staticmethod
    def add_user(self):
        jsonfile = open("user.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            temp = {}
            User.my_update(key, temp)
            new_data.append(temp)
        new_temp = {}
        new_temp['name'] = self.name
        new_temp['account_no'] = self.account_no
        new_temp['password'] = self.password
        new_temp['balance'] = self.balance
        new_data.append(new_temp)
        with open("user.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    @staticmethod
    def del_user(account_no):
        jsonfile = open("user.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key["account_no"] == account_no:
                continue
            else:
                temp = {}
                User.my_update(key, temp)
                new_data.append(temp)

        with open("user.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    @staticmethod
    def show():
        with open("user.json", 'r+') as j:
            mydata = json.load(j)
            print(mydata)

    @staticmethod
    def show_user_profile(acc_no):
        with open("user.json", 'r+') as j:
            mydata = json.load(j)
        for key in mydata:
            if key["account_no"] == acc_no:
                print(key)

    @staticmethod
    def search_user(acc_no):
        jsonfile = open("user.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        for key in mydata:
            if key["account_no"] == acc_no:
                return True
        return False

    @staticmethod
    def my_update(key, temp):
        temp['name'] = key['name']
        temp['id'] = key['id']
        temp['password'] = key['password']

    def add_admin(self):
        jsonfile = open("admin.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            temp = {}
            Admin.my_update(key, temp)
            new_data.append(temp)
        new_temp = {}
        new_temp['name'] = self.name
        new_temp['id'] = self.id
        new_temp['password'] = self.password
        new_data.append(new_temp)
        with open("admin.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    @staticmethod
    def del_admin(id):
        jsonfile = open("admin.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key["id"] == id:
                continue
            else:
                temp = {}
                Admin.my_update(key, temp)
                new_data.append(temp)

        with open("admin.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    def change_password(self, password):
        jsonfile = open("admin.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        new_data = []
        for key in mydata:
            if key["id"] == self.id:
                temp = {}
                key['password'] = password
                Admin.my_update(key, temp)
                new_data.append(temp)
            else:
                temp = {}
                Admin.my_update(key, temp)
                new_data.append(temp)
        with open("admin.json", "w") as f:
            f.write(json.dumps(new_data, indent=4))

    @staticmethod
    def is_valid_withdraw(user, amount):
        if amount < user.get_balance():
            return True
        else:
            return False

    @staticmethod
    def is_valid_transfer(user, amount):
        if user.get_balance() >= 40000 and amount < user.get_balance():
            return True
        else:
            return False

    @staticmethod
    def is_valid(id, password):
        jsonfile = open("admin.json", "r+")
        mydata = json.load(jsonfile)
        jsonfile.close()
        for key in mydata:
            if key["id"] == id and key['password'] == password:
                admin = Admin(key['name'], key['id'], key['password'])
                return admin

    @staticmethod
    def unique(id):
        with open("admin.json", 'r+') as j:
            mydata = json.load(j)
        for key in mydata:
            if key["id"] == id:
                return True
        return False

    @staticmethod
    def view_transaction(account_no):
        with open("transaction.csv", 'r+') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == account_no:
                    print(row[1])
        file.close()

    def show_profile(self):
        with open("admin.json", 'r+') as j:
            mydata = json.load(j)
        for key in mydata:
            if key["id"] == self.id:
                print(key)


