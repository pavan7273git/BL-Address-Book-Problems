class Contact:
    def __init__(self,first_name,last_name,address,state,city,zip_code,phone_number,mail):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.state=state
        self.city=city
        self.zip_code=zip_code
        self.phone_number=phone_number
        self.mail=mail


    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone_number} | {self.address} | {self.mail} | {self.city} | {self.state} | {self.zip_code}"