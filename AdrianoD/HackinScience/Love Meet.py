alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

def love_meet(bob, alice):
    meet = set(bob).intersection(alice)
    return meet

print(love_meet(bob, alice))


def affair_meet(bob, alice, silvester):
    affair = set(alice).difference(bob)
    meet = affair.intersection(silvester)
    return meet

#     ...
print(affair_meet(bob, alice, silvester))