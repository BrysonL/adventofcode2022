class Monkey():
    def __init__(self, id):
        self.id = id
        self.items = None
        self.operation = None
        self.test = None
        self.true_monkey = None
        self.false_monkey = None
        self.inspections = 0

    def set_params(self, items, operation, test, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def process_items(self, worry_divisor):
        for item in self.items:  # update the worry after each inspection
            if self.operation[0] == 'm':
                item *= self.operation[1]
            elif self.operation[0] == 'a':
                item += self.operation[1]
            elif self.operation[0] == 's':
                item *= item

            item //= worry_divisor  # divide worry by specified divisor (3 in pt1, 1 in pt2)

            # there's something special about primes that makes this work, but idk what...
            # I remembered something about this from theory of comp class but don't know how it preserves the results of
            # the operands (esp. the square).
            item %= 2*3*5*7*9*11*13*17*19

            if item % self.test == 0:  # check remainder
                self.true_monkey.add_item(item)
            else:
                self.false_monkey.add_item(item)

            self.inspections += 1

        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __lt__(self, obj):
        return self.inspections < obj.inspections

    def __eq__(self, obj):
        return self.inspections == obj.inspections


def ingest_data_pt1():
    # init all the monkeys so we can set the right true and false monkeys
    monkeys = [Monkey(i) for i in range(8)]

    monkeys[0].set_params(items=[83, 62, 93],
                          operation=['m', 17],
                          test=2,
                          true_monkey=monkeys[1],
                          false_monkey=monkeys[6])

    monkeys[1].set_params(items=[90, 55],
                          operation=['a', 1],
                          test=17,
                          true_monkey=monkeys[6],
                          false_monkey=monkeys[3])

    monkeys[2].set_params(items=[91, 78, 80, 97, 79, 88],
                          operation=['a', 3],
                          test=19,
                          true_monkey=monkeys[7],
                          false_monkey=monkeys[5])

    monkeys[3].set_params(items=[64, 80, 83, 89, 59],
                          operation=['a', 5],
                          test=3,
                          true_monkey=monkeys[7],
                          false_monkey=monkeys[2])

    monkeys[4].set_params(items=[98, 92, 99, 51],
                          operation=['s', 0],
                          test=5,
                          true_monkey=monkeys[0],
                          false_monkey=monkeys[1])

    monkeys[5].set_params(items=[68, 57, 95, 85, 98, 75, 98, 75],
                          operation=['a', 2],
                          test=13,
                          true_monkey=monkeys[4],
                          false_monkey=monkeys[0])

    monkeys[6].set_params(items=[74],
                          operation=['a', 4],
                          test=7,
                          true_monkey=monkeys[3],
                          false_monkey=monkeys[2])

    monkeys[7].set_params(items=[68, 64, 60, 68, 87, 80, 82],
                          operation=['m', 19],
                          test=11,
                          true_monkey=monkeys[4],
                          false_monkey=monkeys[5])

    return monkeys



def process_throws(monkeys, rounds, worry_divisor):
    for i in range(rounds):
        print('Round: ',i)
        for monkey in monkeys:
            print(len(monkey.items))
            monkey.process_items(worry_divisor)

    for monkey in monkeys:
        print(monkey.id, monkey.inspections)

    results = sorted(monkeys)
    print(results[6].inspections * results[7].inspections)


if __name__ == '__main__':
    monkeys = ingest_data_pt1()
    # process_throws(monkeys, 20, 3)  # only ever run one of these at a time, never both
    process_throws(monkeys, 10000, 1)