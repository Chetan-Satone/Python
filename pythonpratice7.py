"""Write a Python program that calculates the discounted price of a product based on its original price and a given discount percentage.
 The program should:

    Ask the user to input the original price of the product.
    Ask the user to input the discount percentage.
    Calculate the discounted price using the formula:
    Discounted Price=Original Price−(Original Price×Discount Percentage100)
    Discounted Price=Original Price−(Original Price×100Discount Percentage​)

    Ensure that the discount percentage is between 0 and 100. If the discount percentage is invalid (outside this range),
      prompt the user to enter a valid discount percentage.

    Display the final discounted price.
"""


original_price= float(input("Enter the original price : "))

if(original_price < 0):
    print("Invalid input")
else:
    discount_percentage= float(input("enter the discount(0-100): "))

    if(0 <= discount_percentage <=100):
        
        discount_percentage= original_price-(original_price*discount_percentage/100)
        print(f"The discount price of the product is: ${discount_percentage}")

    else:
        print("Invalid discount percentage")



