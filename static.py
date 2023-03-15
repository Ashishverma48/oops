class Atm:

    # Static/class

    __conter = 1

    def __init__(self):
        #  Instance variable

        self.pin = ""
        self.balance = 0

        self.s_no = Atm.__conter
        Atm.__conter+=1

        self.menu()

    #     use static method

    @staticmethod
    def get_counter():
        return Atm.__conter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__conter = new
        else:
            print("Not Allowed")


    def menu(self):
        user_input = input("""
        Hello, how would to create to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_bal()
        else:
            print("Wrong Number Entered")

    def create_pin(self):
        self.pin = input("Enter your pin :")
        print("Pin Create Succesfully")
        self.menu()

    def deposit(self):
        temp = input("Enter The Pin")
        if temp == self.pin:
            amount = int(input("Enter Deposit Amount : "))
            self.balance = self.balance + amount
            print("Deposit Successfully")
        else:
            print("Invalid Pin")
        self.menu()
    def withdraw(self):
        temp = input("Enter The Pin")
        if temp == self.pin:
            amount = int(input("Enter Amount : "))
            if amount < self.balance:

                self.balance = self.balance + amount
                print("Deposit Successfully")
            else:
                print("Balance Kam Hai Bhai")
        else:
            print("Invalid Pin")
        self.menu()

    def check_bal(self):
        temp = input("Enter Pin Code : ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
        self.menu()

bob = Atm()
sbi = Atm()
hdfc = Atm()

