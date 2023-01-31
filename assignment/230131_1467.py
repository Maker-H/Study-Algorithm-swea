class Stack:
    def __init__(self):
        self.s = []
    
    def empty(self):
        if len(self.s) == 0:
            return True
        return False
    
    def top(self):
        if self.empty():
            return None
        else:
            return self.s[-1]
    
    def pop(self):
        if self.empty():
            return None
        else:
            tmp = self.s.pop(-1)
            return tmp
    
    def push(self, val):
        self.s.append(val)

    def __str__(self):
        result = ''
        for one in self.s:
            result += str(one) + ' '
        return result

S = Stack()
print(S.empty())
S.push(1)
S.push(1)
S.push(1)
S.push(1)
S.push(4)
S.push(5)
S.push(6)
S.push(7)
print(S.top())
print(S.empty())
print(S)
print('pop', S.pop())
print('pop', S.pop())
print('pop', S.pop())
print(S)

