'''
Write a class Train which has methods to book a ticket, 
get status(no of seats), 
and get fare information of trains running under Indian Railways.

[1,2,3,4,5]
'''

class Train:
    def __init__(self, tName, tNumber, tSeats, tFare):
        self.tName = tName
        self.tNumber = tNumber
        self.tSeats = tSeats
        self.tFare = tFare
        self.availableSeats = list(range(1, tSeats + 1))

    def getDetails(self):
        print(f"Name of train: {self.tName} and number: {self.tNumber}")
        print(f"Total seats available: {self.availableSeats}")
        print(f"Fare of each seat: {self.tFare}")
    
    def bookSeat(self, noOfSeats):
        if noOfSeats > len(self.availableSeats):
            print(f"Seats available: {len(self.availableSeats)}")
        else:
            temp = []
            for _ in range(noOfSeats):
                seatNo = self.availableSeats.pop()
                temp.append(seatNo)
            print(f"Seats booked: {temp}")
            print(f"Please pay: {noOfSeats * self.tFare}")


    def cancelSeat(self, seatNo):
        if seatNo in self.availableSeats or seatNo <=0 or seatNo > self.tSeats:
            print(f"Enter a valid seat number")
        else:
            self.availableSeats.append(seatNo)
                

t1 = Train("ABC", "AB123", 5, 50)
# t1.getDetails()
t1.bookSeat(3)
t1.cancelSeat(5)
t1.getDetails()