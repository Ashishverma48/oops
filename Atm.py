class Atm:
    def __init__(self):

        self.pin = ""
        self.balance = 0
        self.main()

    def main(self):
        user_input = input("""
        WHAT ABOUT TO PROCEED
        1. CREATE ATM PIN
        2. CHANGE PIN
        3. DEPOSIT AMOUNT
        4. WITHDRAW AMOUNT
        5. CHECK BALANCE 
        6. EXIT
        
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.deposit()
        elif user_input == '4':
            self.withdraw()
        elif user_input == '5':
            self.check_bal()
        else:
            print("SAHI NUNBER DAL ...")

    def create_pin(self):
        self.pin = input("CREATE PIN   ")
        print("PIN CREATE SUCCESSFULLY ")
        self.main()

    def change_pin(self):
        enter_pin = input("ENTER ATM PIN")

        if enter_pin == self.pin:

            change_pin = input("YOU WANT CHANGE YOUR PIN - Y/N  ").upper()
            if change_pin == "Y":

                self.pin = input("ENTER NEW PIN  ")
                print("PIN CHANGE SUCCESSFULLY ")
            else:
                print("MAT KAR MUJHE KYA")
        else:
            print("INVALID PIN DALTA HAI .....")
        self.main()

    def deposit(self):
        enter_pin = input("ENTER ATM PIN  ")

        if enter_pin == self.pin:
            amount = int(input("ENTER DEPOSIT AMOUNT   "))
            self.balance = self.balance + amount
            print("DEPOSIT SUCCESSFYLLY")
            
        else:
            print("INVALID PIN ")

        self.main()

    def withdraw(self):
        enter_pin = input("ENTER ATM PIN   ")
        if enter_pin == self.pin:
            withdraw = int(input("ENTER WITHDRAWAL AMOUNT   "))
            if withdraw < self.balance:
                self.balance = self.balance - withdraw

            else:
                print('PAHLE ACCOUNT ME PAISE TO DAL .....')
        else:
            print("INVALID PIN DALTA HAI ******* ")

        self.main()

    def check_bal(self):
        enter_pin = input('ENTER ATM PIN   ')
        if enter_pin == self.pin:
            print(self.balance)
        else:
            print("INVALID PIN DALTA HAI ******* ")

        self.main()


sbi = Atm()

sbi.pin