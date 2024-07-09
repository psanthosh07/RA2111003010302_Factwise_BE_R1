def count_letters(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
            "sixteen", "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    total_count = 0
    
    for i in range(1, n + 1):
        if i == 1000:
            total_count += len("onethousand")
        else:
            num_letters = 0
            hundreds = i // 100
            remainder = i % 100
            
            if hundreds > 0:
                num_letters += len(ones[hundreds]) + len("hundred")
                if remainder > 0:
                    num_letters += len("and")
            
            if remainder < 20:
                num_letters += len(ones[remainder])
            else:
                num_letters += len(tens[remainder // 10])
                num_letters += len(ones[remainder % 10])
            
            total_count += num_letters
    
    return total_count

total_count = count_letters(1000)
print("The Total Number of letters present from one to thousand are : ", total_count)
