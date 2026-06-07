bookeds_slots=list(map(str,input("enter the booked slots: ").split()))
req_slot=str(input())
print("slot available" if req_slot not in bookeds_slots else print("slot already booked"))