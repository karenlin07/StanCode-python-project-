"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Compute hailstone sequence by any given positive numbers。
    """
    print("This program computes hailstone sequence。")
    data =int(input("Enter a positive number:"))
    step = 0
    while data != 1:
        if data % 2 == 1:   # data is odd
            data = (data * 3) + 1
            print((data-1)/3, " is odd, so I make 3n+1:",data)
        else:   # data is even
            data= data / 2
            print(data*2, "is even, so I take half:",data)
        step += 1 # count steps
    print("It took ",step," steps"+" to reach 1")



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
