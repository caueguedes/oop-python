subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print(
    f"Sub: ${1} Tax: ${1} Total: ${total}".format(
        subtotal, tax, total=total
    )
)  # Sub: $12.32 Tax: $0.8624 Total: $13.182400000000001


print(
    "Sub: ${0:0.2f} Tax: ${1:0.2f} "
    "Total: ${total:0.2f}".format(subtotal, tax, total=total)
)


orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]

print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d}"  # 10s (10 strings) - ^9d ^align center 9 char integer
        f"${price: <8.2f}${subtotal: >7.2f}"  # <8.2f # align left 8 integer chars and 2 f float
    )

# PRODUCT     QUANTITY    PRICE   SUBTOTAL
# burger          5       $2.00   $  10.00
# fries           1       $3.50   $   3.50
# cola            3       $1.75   $   5.25


#  % - transform a value in percentage
#  X - Hexadecimal
#  o - octa





