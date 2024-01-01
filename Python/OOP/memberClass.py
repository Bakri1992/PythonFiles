class Member:
    users_number=0
    not_allowed_name=["Hell","Shit","Baloot"]
    def __init__(self,first_name,middle_name,last_name,gender="Male"):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.gender=gender
        Member.users_number +=1

    def full_name(self):
        if self.first_name in self.not_allowed_name:
            # To access class attribute => object.class_attribute.
            # To access class attribute => class_name.class_attribute.
            raise ValueError("Name is not allowed")
        else:
            return f"{self.first_name} {self.last_name}"
    def say_hello(self):
        if self.gender=="Male":
            return f"Hello Mr {self.first_name}"
        else:
            return f"Hello Miss {self.first_name}"
    def get_all_info(self):
        return f"{self.say_hello()} your full name is {self.full_name()}"
    
member_one=Member("Bakri","Abdulkader","Badet")
member_two=Member("Omar","Abdulkader","Badet")
member_three=Member("Manar","Omar","Sakalaik")
member_four=Member("Shit","Sami","Abdullah")
member_five=Member("Malek","Abdullah","Sakalaik")
print(member_one.full_name())
# print(member_one.get_all_info())
# print(member_one.say_hello())
# print(member_four.full_name()) # This will give error.
print(Member.users_number)# we can access the class attribute from 
#outside and inside the class attribute using Member.attribute_name
                                
print(member_one.users_number)
# We can access the class attribute with the instance from outside class 