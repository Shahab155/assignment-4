# Problem Statement

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

# Solution: 1

def in_range(n,low,high):
    if n in range(low,high+1):
        return True
    else:
        return False
       

def main():
    print(in_range(3,1,14))   
    print(in_range(10,1,20))    
    print(in_range(4,2,8))    
    print(in_range(8,1,6))    
    print(in_range(12,1,32))    
    print(in_range(33,1,50))


if __name__ == "__main__":
    main()

