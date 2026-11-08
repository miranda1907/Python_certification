def verify_card_number(card_number):

    card_number = card_number.replace(" ", "").replace("-", "")
    numbers = []
    print(card_number)


    for i in range(len(card_number)):
        char = card_number[i]
        print(card_number[i])

        if (len(card_number) - 1 - i) % 2 != 0:
            doubled = int(char) * 2
            print(doubled)
            if doubled > 9:
                doubled = doubled - 9
            
            print(doubled)    
            numbers.append(doubled)
        else: 
            numbers.append(int(char))    

    print(numbers)  

    print(sum(numbers))  

    if sum(numbers) % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"    


print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
