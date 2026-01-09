""" 
Create a dictionary named order with the following structure:
    order_id: String
    customer:
        name: String
        contact:
            phone: List of integers (phone numbers)
            email: String
    items: A list of dictionaries where each dictionary contains:
        item_name: String
        quantity: Integer
        price: Float
    total_amount: Float
    status: String (e.g., "Pending", "Shipped", "Delivered")
    
    
    
Functions to Perform Operations

Calculate Total Amount: Write a function calculate_total that takes the items list as input and calculates the total order amount based on the quantities and prices.
Add Item: Write a function add_item that takes the item name, quantity, and price as parameters. It should add this item to the items list and update the total amount accordingly.
Update Status: Write a function update_status that takes a new status as a parameter and updates the status of the order.
Display Order Details: Write a function display_order_details that prints out the order details, including customer info, items purchased, total amount, and order status.

"""

