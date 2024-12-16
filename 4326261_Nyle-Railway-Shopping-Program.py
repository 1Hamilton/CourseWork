# Online Railway Ticketing System 

# Destination dictionary 
destinations = {
    1: ("London", 10.15),
    2: ("Manchester", 22.50),
    3: ("Birmingham", 21.40)
}

# Welcoming user and asking for their name
user_name = input("\nPlease enter your name: ")
print(f"\nWelcome to the National Railway {user_name}")

# Display destinations and prices
print("\nAvailable Destinations")
for num, (destination, price) in destinations.items():
    print(f"{num}. {destination} - £{price:.2f}")

# Destination seclection 
while True:
    destination_choice = int(input("\nPlease select a destinaton 1, 2 or 3: "))
    if destination_choice not in destinations:
        print("Invalid Choice")
        continue
    elif destination_choice == 1:
        print("\nYou have selected London")
        
        # Ticket amount
        quantity = int(input("\nHow many tickets would you like to purchase: "))
        if quantity < 1:
            print("You must select at least one ticket. Try again")
        else:
            total_price = quantity * 10.15

            # Display transactioin summary
            print("\n--Transaction Summary--\n")
            print("  Destinatioin: London")
            print(f"  Number of tickets: {quantity}")
            print(f"  Total price: £{total_price:.2f}")     

        # Generate Reciept 
        more = input("\nWould you like a reciept (yes/no)? ")
        name = user_name + ".txt"
        if more == "yes":
            invoice = open(name, "w")
            invoice.write(f"\n\n---- Transaction Receipt ----\n\n   Customer name: {user_name}\n   Destination: London\n   Number of tickets: {quantity}\n   Total price: £{total_price:.2f}\n\n----------------------------")
            invoice.close()
        else:
            print(f"\nThank you for shopping with National Railway {user_name}")    
        break 

    elif destination_choice == 2:
        print("\nYou have selected Manchester")
        
        # Ticket amount
        quantity = int(input("\nHow many tickets would you like to purchase: "))
        if quantity < 1:
            print("You must select at least one ticket. Try again")
        else:
            total_price = quantity * 22.50 
            
            # Display transactioin summary
            print("\n--Transaction Summary--\n")
            print(f"  Destinatioin: Manchester")
            print(f"  Number of tickets: {quantity}")
            print(f"  Total price: £{total_price:.2f}")

        # Generate Reciept 
        more = input("\nWould you like a reciept (yes/no)? ")
        name = user_name + ".txt"
        if more == "yes":
            invoice = open(name, "w")
            invoice.write(f"\n\n---- Transaction Receipt ----\n\n   Customer name: {user_name}\n   Destination: Manchester\n   Number of tickets: {quantity}\n   Total price: £{total_price:.2f}\n\n----------------------------")
            invoice.close()
        else:
            print(f"\nThank you for shopping with National Railway {user_name}")         
        break         
    
    elif destination_choice == 3:
        print("\nYou have selected Birmingham")
        
        # Ticket amount
        quantity = int(input("\nHow many tickets would you like to purchase: "))
        if quantity < 1:
            print("You must select at least one ticket. Try again")
        else:
            total_price = quantity * 21.40 
            
            # Display transactioin summary
            print("\n--Transaction Summary--\n")
            print(f"  Destinatioin:Birmingham")
            print(f"  Number of tickets: {quantity}")
            print(f"  Total price: £{total_price:.2f}")

        # Generate Reciept 
        more = input("\nWould you like a reciept (yes/no)? ")
        name = user_name + ".txt"
        if more == "yes":
            invoice = open(name, "w")
            invoice.write(f"\n\n---- Transaction Receipt ----\n\n   Customer name: {user_name}\n   Destination: Birmingham\n   Number of tickets: {quantity}\n   Total price: £{total_price:.2f}\n\n----------------------------")
            invoice.close()
        else:
            print(f"\nThank you for shopping with National Railway {user_name}")     
        break 
        




              