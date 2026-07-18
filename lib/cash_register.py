#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity

        # Add one item for each quantity
        self.items.extend([item] * quantity)

        # Save the transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply the discount
        self.total = self.total - (self.total * self.discount / 100)

        # Print the success message expected by the tests
        if self.total == int(self.total):
            amount = int(self.total)
        else:
            amount = self.total

        print(f"After the discount, the total comes to ${amount}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # Remove the value of the last transaction
        self.total -= last["price"] * last["quantity"]

        # Remove each occurrence of the item
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])