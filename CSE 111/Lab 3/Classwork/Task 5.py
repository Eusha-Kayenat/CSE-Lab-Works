class CellPackage:
    def __init__(self, price, data, talk_time, messages, cashback_percentage, validity):
        if 'GB' in data:
            data_in_mb = int(data.split()[0]) * 1024
        else:
            data_in_mb = 0
        cashback_value = (price * int(cashback_percentage.replace('%', ''))) / 100

        self.data = data_in_mb
        self.talk_time = talk_time
        self.messages = messages
        self.cashback = cashback_value
        self.validity = validity
        self.price = price
    
    def display_package_details(self):
        if self.data > 0:
            print(f"Data = {self.data} MB")
        if self.talk_time > 0:
            print(f"Talktime = {self.talk_time} Minutes")
        if self.messages > 0:
            print(f"SMS/MMS = {self.messages}")
        print(f"Validity = {self.validity} Days")
        print(f"--> Price = {self.price} tk")
        if self.cashback > 0:
            print(f"Buy now to get {int(self.cashback)} tk cashback.")
pkg1 = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('===========Package 1=============')
pkg1.display_package_details()

pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('===========Package 2=============')
pkg2.display_package_details()

pkg3 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('===========Package 3=============')
pkg3.display_package_details()
