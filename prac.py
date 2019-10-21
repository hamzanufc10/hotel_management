class Customer:
    price_dict = {'Acacia': 1000, 'Oak': 1500, 'Maple': 2000, 'Mahogany': 3000}
    room_count_dict = {'Acacia': 5, 'Oak': 5, 'Maple': 5, 'Mahogany': 5}


    def __init__(self,name,gender,age,roomtype):
        self.name=name
        self.gender=gender
        self.age=age
        self.roomtype=roomtype

#for booking of room


    def booking(self):
        a = self.price_dict
        c=self.room_count_dict
        if self.roomtype in a:
                ans = ('{0} {1} is avalible your room no is {2} '.format(self.name, self.roomtype,c[self.roomtype]))
                b = {self.name: self.roomtype}
                if self.roomtype in c.keys():
                    c[self.roomtype]=c[self.roomtype]-1


        return (ans)

#for getting room type by name

    def getname(self,roomtype):
        b = {roomtype: self.name}
        if roomtype in b:
            return ('{1} is occupied by {0}'.format(b[roomtype], roomtype))

# for getting name by roomtype

    def getroomno(self,name):
        b = {name: self.roomtype}
        if name in b:
            return ('{0} is in {1}'.format(name, b[name]))


#for checking avaiabilty

    def avilable(self,roomtype):
        c = self.room_count_dict


        if self.roomtype in c:
            if c[self.roomtype]==0:
                print('Sorry,Room not availble')
            else:
                print('Congo,Room are available')






obj = Customer('Hamza','male',3,'Oak')

print("Congo :",obj.booking())

print('search by name:',obj.getname('Oak'))

print("Search by room type :",obj.getroomno('Hamza'))

print(obj.avilable('Oak'))




