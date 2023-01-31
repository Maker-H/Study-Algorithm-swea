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

p1 = PublicTransport('n', 10)
p2 = PublicTransport('n', 10)
p3 = PublicTransport('n', 10)
p4 = PublicTransport('n', 10)

print(p4.profit())