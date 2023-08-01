class Bank(object):

    def __init__(self, sum, months, rate):
        self.sum = sum
        self.months = months
        self.rate = rate

    #дифференцированный платеж
    def diff_int(self):
        answer = []
        first = self.sum / self.months
        for i in range(1, self.months + 1):
            answer.append([i, round(self.sum - first * (i-1), 2), round(first, 2), round((self.sum - first * (i-1)) * self.rate / 1200, 2), round((first + (self.sum - first * (i-1)) * self.rate / 1200), 2)])
        return answer

    #аннуитетный платеж
    def ann_int(self):
        answer = []
        full = (self.sum * self.rate / 1200) / (1 - pow(1 + (self.rate / 1200), -self.months))
        arr = [self.sum, self.sum - full + (self.sum * self.rate / 1200)]
        for i in range(1, self.months + 1):
            arr.append(arr[-1] - full + (arr[-1] * self.rate / 1200))
        for i in range(1, self.months + 1):
            answer.append([i, round(arr[i-1], 2), round(full - arr[i-1] * self.rate / 1200, 2), round(arr[i-1] * self.rate / 1200, 2), round(full, 2)])
        return answer

    #депозитный калькулятор
    def deposit(self):
        answer = []
        for i in range(1, self.months + 1):
            answer.append([i, round((self.sum * pow((1 + ((self.rate / 100) / 12)), i)) * self.rate / 1200, 2), round((self.sum * pow((1 + ((self.rate / 100) / 12)), i)), 2)])
        return answer
