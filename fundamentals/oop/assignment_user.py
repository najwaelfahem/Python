class User:
    #constractor
    def __init__(self, first_name, last_name, email, age)
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.age= age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def print_info(self):
        print(f"User fullname is {self.first_name} {self.last_name} email is {self.email} and he is {self.age} old !")
        return self

    user1= User("najwa", "elfahem", "najwa@gmail.com", 30)    