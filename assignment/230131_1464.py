class PublicTransport:
    cnt = 0
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def get_in(self):
        PublicTransport.cnt += 1

    def get_out(self):
        PublicTransport.cnt -= 1

    def profit(self):
        return self.fare * PublicTransport.cnt

class Bus(PublicTransport):
    def __init__(self, name, fare, until):
        super().__init__(name, fare)
        self.until = until

    def get_in(self):
        Bus.cnt += 1
        if Bus.cnt > self.until:
            print('더이상 탑승할 수 없습니다')
    
p1 = Bus('1', 1, 4)
p1.get_in()    
p1.get_in()    
p1.get_in()    
p1.get_in()
p1.get_in()
p1.get_in()


