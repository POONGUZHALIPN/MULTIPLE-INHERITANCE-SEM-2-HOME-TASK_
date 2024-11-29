class Library:
    def __init__(self,book_name,book_no):
        self.book_name=book_name
        self.book_no=book_no
    def showLibraryInfo(self):
        print(f"Name:{self.book_name}\nRoll_No:{self.book_no}")
class Member:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def showMemberInfo(self):
        print(f"Name:{self.name}\nRoll_No:{self.roll_no}")

class LibraryDetails(Library,Member):
    def __init__(self,book_name,book_no,name,roll_no):
        super().__init__(book_name,book_no)
        Member.__init__(self,name,roll_no)
    def displayDetails(self):
        self.showLibraryInfo()
        self.showMemberInfo()
x=LibraryDetails("Cindrella",5878,"Poongu",12)
x.displayDetails()


class Restaurant:
    def __init__(self,restaurant_name,dish_name,price):
        self.restaurant_name = restaurant_name
        self.dish_name = dish_name
        self.price = price 
    def displayRestaurantInfo(self):
        print(f"Restaurant Name:{self.restaurant_name}\nDishName:{self.dish_name}\nPrice:{self.price}") 
class Delivery:
    def __init__(self,rider_name,rider_contact):
        self.rider_name = rider_name
        self.rider_contact = rider_contact 
    def displayDeliveryInfo(self):
        print(f"Rider Name:{self.rider_name}\nRider Contact:{self.rider_contact}") 
class OrderInfo(Restaurant,Delivery):
    def __init__(self,restaurant_name,dish_name,price,rider_name,rider_contact):
        super().__init__(restaurant_name,dish_name,price)
        Delivery.__init__(self,rider_name,rider_contact)
    def displayOrderInfo(self):
        self.displayRestaurantInfo()
        self.displayDeliveryInfo() 
h = OrderInfo("Hungry Panda","Chicken Biriyani",200,"Adithya",8465149415) 
h.displayOrderInfo()
