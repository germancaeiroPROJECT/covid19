class Statistics:
    def __init__(self, x, y):
        self.x = x if type(x) ==list else []
        self.y = y if type(y) == list else []
    
    @property
    def n(self):
        return len(self.x)

    @property
    def x_mean(self):
        return sum(self.x)/self.n
    
    @property
    def y_mean(self):
        return sum(self.y)/self.n
    
    @property
    def x_var(self):
        count = sum([(num - self.x_mean)**2 for num in self.x])
        return count/self.n
    
    @property
    def y_var(self):
        count = sum([(num - self.y_mean)**2 for num in self.x])
        return count/self.n

    @property
    def XY(self):
        XY = sum([tupla[0] * tupla[1] for tupla in zip(self.x, self.y)])
        return XY
    
    @property
    def cov(self):
        return (self.XY / self.n) - (self.x_mean * self.y_mean)
    
    @property
    def rxy(self):
        return self.cov / ((self.x_var ** 0.5) * (self.y_var ** 0.5))

    @property
    def B(self):
        return self.rxy / ((self.y_var ** 0.5) / (self.x_var ** 0.5))

    @property
    def B0(self):
        return self.y_mean - (self.B * self.x_mean)

    def prediction(self, value):
        return (self.B * value) + self.B0

test = Statistics([1,2,3], [4,5,6])

print(test.XY)
print(test.cov)
print(test.rxy)
print(test.B)
print(test.B0)
print(test.prediction(5))

