guest_1 = [1, 2, 3]
guest_2 = guest_1
guest_3 = [1, 2, 3]

print(guest_1 is guest_2)
print(guest_1 is guest_3)

party_crasher = [4, 5, 6]
guest_4= [4, 5, 6]

print(party_crasher is not guest_4)