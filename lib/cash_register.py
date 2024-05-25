#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.quantity_items = {}
        self.previous_totals = [self.total]

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.previous_totals.append(self.total)
        if title not in self.quantity_items:
            self.quantity_items[title] = 0
        self.quantity_items[title] += quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            discounted_total = int(self.total * ((100 - self.discount) / 100))
            self.total = discounted_total
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
            self.total = self.previous_totals[-1]

    def void_last_transaction(self):
        if not self.previous_totals:
            return "There are no transactions to void."
        last_item_cost = sum([price * quantity for price, quantity in self.quantity_items.items()])
        self.total -= last_item_cost
        self.quantity_items.clear()
        self.items.clear()
        self.previous_totals.pop()
        if not self.items:
            self.total = 0.0
        print(f"The last transaction has been voided. Total now: ${self.total}")

    def get_all_items(self):
        return self.items

    def reset_total(self):
        self.total = 0.0
        self.items.clear()
        self.quantity_items.clear()
        self.previous_totals = [self.total]

# Example usage
if __name__ == "__main__":
    cash_register = CashRegister(discount=10)
    cash_register.add_item("Apple", 0.5, 5)
    cash_register.apply_discount()
    print(cash_register.get_all_items())
    print(cash_register.total)
    cash_register.void_last_transaction()
    print(cash_register.get_all_items())
    print(cash_register.total)
    cash_register.reset_total()
    print(cash_register.get_all_items())
    print(cash_register.total)
