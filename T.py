#region Function
def F(n): #name of the function
    if n < 1: return 0 #if section
    elif n == 1: return 0
    else: return F(n-1)
#endregion

#region Print
print(F(21))
#endregion