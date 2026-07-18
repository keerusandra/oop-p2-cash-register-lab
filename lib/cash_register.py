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
        """Add an item to the register."""
        self.total += price * quantity

        # Add one entry per quantity
        self.items.extend([item] * quantity)

        # Save the transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount to the total."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        """Remove the last transaction."""
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # Remove the transaction amount
        self.total -= last["price"] * last["quantity"]

        # Remove the items from the items list
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])