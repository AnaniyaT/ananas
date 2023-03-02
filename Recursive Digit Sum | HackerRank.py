def superDigit(n, k):
    if len(n)* k == 1:
        return int(n)
    
    super_digit = 0
    
    for char in n:
        super_digit += int(char)
        
    super_digit *= k
    
    return superDigit(str(super_digit), 1)
