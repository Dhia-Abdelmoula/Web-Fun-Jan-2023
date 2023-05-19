
class User:
    
    def init(self, fname, lname, email, age):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.age = age
        
        self.is_rewards_member = False
        self.gold_card_points = 0

     
    def display_info(self):
        print("First name: "+self.first_name)
        print("Last name: "+self.last_name)
        print("Email adress: "+self.email)
        print("Age: "+str(self.age))
        if self.is_rewards_member:
            print("He is good user and his total gold card points is", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("This member is already enrolled!!")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient balance!")
        else:
            self.gold_card_points -= amount


acc1 = User("John", "Doe", "JohnDoe@com", 25)

acc1.enroll()
acc1.spend_points(50)


acc2 = User("Jane", "Doe", "JaneDoe@com", 28)
acc2.enroll()
acc2.spend_points(80)

acc3 = User("Jamila", "Doe", "JamilaDoe@com", 30)

acc1.display_info()
acc2.display_info()
acc3.display_info()
acc1.enroll()
acc3.spend_points(40)