class Parent:
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    """Reusing the above method"""
    def show_info(self):
        print ("Last Name - "+self.last_name)
        print ("Eye Color - "+self.eye_color)
    
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child Constructor Called")

        """Inheriting the variables defined in the class parent"""
        Parent.__init__(self, last_name, eye_color)
        
        self.number_of_toys = number_of_toys

    """Since we are defining the show_info function again in the child class, this function """
    """this function will be called insteas of the one in the Parent class"""
    """This is called method overriding"""
    def show_info(self):
        print ("Last Name - "+self.last_name)
        print ("Eye Color - "+self.eye_color)
        print ("Number of Toys - "+str(self.number_of_toys))

billy_cyrus = Parent("cyrus","blue")
print (billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child("cyrus", "blue", 5)
print(miley_cyrus.last_name)
print (miley_cyrus.number_of_toys)

"Since the class inherits ftom class parent, the method show_info is avaialable for class child"
miley_cyrus.show_info()
