# Problem Statement

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Here's a sample run of the program:

# 10 9 8 7 6 5 4 3 2 1 Liftoff!

# Solution:1

# def main():
#     for i in range(10,-1,-1):
#         if i > 0:
#             print(i,end=" ")
#         else:
#             print("LiftOff!")    

# if __name__ == "__main__":
#     main()


# solution:2 
count = 10
def main():
    global count
    while count >= 0:
      if count > 0:
        print(count, end=" ")
      else:
        print("LiftOff!")
      count -= 1  


if __name__ == "__main__":
    main()
          