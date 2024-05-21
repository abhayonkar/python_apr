from bank import Bank

class Account(Bank):
    def __init__(self, name , email, addr):
        self.acc_name = name
        self.acc_email = email
        self.acc_addr = addr

# we can execute accout class without overinding cal_bal method

    def cal_bal(self):
        return 0
    
    def set_mobile(self, mobile):
        self.acc_mobile = mobile