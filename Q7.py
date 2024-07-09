def maxScore(cardPoints, k):
    n = len(cardPoints)

    window_sum = sum(cardPoints[:k])
    max_sum = window_sum
    
    try:
        
        for i in range(1, k + 1):
            window_sum += cardPoints[-i] - cardPoints[k - i]
            max_sum = max(max_sum, window_sum)
    except:
        print("INVALID INPUT !\nThe given value of k is greater than the number of card points given")
        max_sum="Not possible to find because of the invalid input"
    
    return max_sum
    
l1=list(map(int,input("Enter the card points seperated by space : ").split()))
k1=int(input("Enter the k value : "))

print(f"\nThe maximum card points possible are : {maxScore(l1,k1)}")
