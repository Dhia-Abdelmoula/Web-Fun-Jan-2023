class User :
    def __init__(self,fname,lname,mail,age):
        self.first_name=fname
        self.last_name=lname
        self.email=mail
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0
    def display_info(self) :
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Email Address : {self.email}")
        print(f"Age : {self.age} ")
        if self.is_rewards_member : 
            print("Rewards Member")
        else :
            print("Not a rewards Member")
        print(f"Gold card Points : {self.gold_card_points}")
        return self
    def enroll(self) :
        if self.is_rewards_member :
            print(f"{self.first_name} is already a member")
            
        else :
            self.is_rewards_member=True
            self.gold_card_points=200
        return self
        
    def spend_points(self, amount):
        if amount < self.gold_card_points :
            self.gold_card_points-=amount
        else :
            print("insufficient balance")
        return self
dhia=User("Dhia","Abdelmoula","dhia@com",25)
#tests
dhia.display_info().enroll().display_info().enroll().spend_points(300)

