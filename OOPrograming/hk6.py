class MathDojo(object):

    def __init__(self, total_sum=0):
        self.total_sum = total_sum

    def add(self, *args):
        for i in args:
            if type(i) == int:
                self.total_sum += i
            elif type(i) == list or tuple:
                for j in i:
                    self.total_sum += j
            else:
                pass
        return self

    def subtract(self, *args):
        for i in args:
            if type(i) == int:
                self.total_sum -= i
            elif type(i) == list or tuple:
                for j in i:
                    self.total_sum -= j
            else:
                pass
        return self

    def result(self):
        print self.total_sum
        return self

md = MathDojo()

md.add(2).add(2,5).subtract(3,2).result()
md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result()
