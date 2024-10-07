# create the class ItemToPurchase
class ItemToPurchase:
    def __init__(self, item_name='none',item_price=0.0,item_quantity=0):

        # Initialize the attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Create the function print_item_cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

def main():
    
    # Create list to store ItemToPurchase objects and a variable for the number of items to ask the user for
    items = []
    num_items = 2

    # Loop through the number of items
    for i in range(1, num_items + 1):
        print(f'Item {i}')
        item_name = input('Enter the item name: ')
        item_price = float(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))

        # Create the ItemToPurchase object and append it
        item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)
        print()
    
    # Print the total cost for each item
    print('TOTAL COST')
    total_cost = 0
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    # Print the total cost for everything together
    print(f'\nTotal: ${total_cost:.2f}')

main()