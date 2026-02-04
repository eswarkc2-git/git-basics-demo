# Constants
CAPACITY = 350

# Variables to track status
total_tickets_sold = 0
total_bookings_count = 0
rejected_bookings_count = 0

while total_tickets_sold < CAPACITY:
    seats_left= CAPACITY- total_tickets_sold

    num_tickets = int(input("Enter number of tickets (1-15) or 0 to exit: "))
    if num_tickets <= 0:
        break
    if num_tickets > 15:
        print("Maximum allowed tickets 15 per booking!!")
        continue 
    all_ages_valid = True
    for i in range(num_tickets):
        age = int(input(f"  Age of person {i + 1}: "))
        if age < 12:
            all_ages_valid = False
            break
    
    if not all_ages_valid:
        print("BOOKING REJECTED - Age restriction")
        rejected_bookings_count +=1
    else:
        total_tickets_sold += num_tickets
        total_bookings_count += 1

print("FINAL BOOKING REPORT")
# print("="*30)
print(f"Total Bookings:    {total_bookings_count}")
print(f"Total Tickets Sold: {total_tickets_sold}")
print(f"Rejected Bookings:  {rejected_bookings_count}")
print(f"Remaining Seats:    {CAPACITY - total_tickets_sold}")
# print("="*30)