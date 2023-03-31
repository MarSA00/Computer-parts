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
        print ('adding {} to the list'.format(current_item))
