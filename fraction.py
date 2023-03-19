import functools

@functools.total_ordering 
class Save:
    def __init__(self, numerator, denominator, approx, delta):
        self.numerator = numerator
        self.denominator = denominator
        self.approx = approx
        self.delta = delta

    def __lt__(self, other):
        return self.delta < other.delta


def main():
    target = float(input("Please input a decimal number to approximate:"))

    list = []

    numerator = 1
    denominator = 1
    approx = numerator / denominator

    while denominator <= 1000 and numerator <= 1000:
        approx = numerator / denominator
        if approx < target:
            numerator += 1
            list.append(Save(numerator, denominator, approx, abs(approx - target)))

        else:
            denominator += 1
            list.append(Save(numerator, denominator, approx, abs(approx - target)))

        
    list.sort()

    for i in range(0, 10):
        print("{:} / {:} = {:.5f} = ".format(list[i].numerator, list[i].denominator, list[i].approx))






if __name__ == "__main__":
    main()
