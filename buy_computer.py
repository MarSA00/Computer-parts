available_parts = [("computer", 20),
                   ('monitor', 40),
                   ('mouse', 60),
                   ('keyboard', 80),
                   ('speakers', 100),
                   ('hdmi cable', 120)
                   ]
valid_choices = [str(i) for i in range(1, len(available_parts) +  1)]
current_item = "-"
computer_parts = []
total_price = 0

while current_item != "0":
    if current_item in valid_choices:
        print('adding {} to the list'.format(current_item))
        index = int(current_item) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
        price = chosen_part[1]
        total_price += price
        print('price of current item is {}'.format(price))
    else:
        print("Please choose one of the following parts:")
        for number,  part in enumerate(available_parts):
            print('{0}: {1}'.format(number + 1, part))
    current_item = input()

print(computer_parts)
print('Your total is {}'.format(total_price))
