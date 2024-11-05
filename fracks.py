class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    #Calculating the value to weight ratio for each item and sorting this ratio in descending order
    items = sorted(items, key = lambda x: x.value/x.weight, reverse = True)

    total_value = 0 #Total value of items that can be carried
    for item in items:
        if capacity >= item.weight:
            #If the item can be picked completely
            capacity -= item.weight
            total_value += item.value
            print(f"Add entire item with value {item.value} and weight {item.weight}")
            print(f"Remaining capacity: {capacity}. Current total value: {total_value}")
        else:
            #If item cannot be picked completely, take fraction of it
            fraction = capacity/item.weight
            added_value = item.value * fraction
            total_value += item.value * fraction
            print(f"Added {fraction} fraction of item with item value {item.value} and weight {item.weight}")
            print(f"Added value: {added_value}. Remaining capacity : 0. Current total value: {total_value}")
            break #Knapsack is full
    
    return total_value

items = [Item(60,10), Item(100,20), Item(120,30)]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in knapsack = {max_value}")