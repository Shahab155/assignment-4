# licing the List:

# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.

# --------------------------------------------------------------------------------------------------
# --------------------------- Solution -----------------------------
# --------------------------------------------------------------------------------------------------

def slicing_lst(lst,start_index,end_index):
    if start_index >= -len(lst) and start_index <= len(lst):
        if end_index >= -len(lst) and end_index <= len(lst):
            result = lst[start_index:end_index]
            print(f"\nThe result after slicing is: {result}\n")
        else:
            print(f"\nStarting Index is out of range!\n")
    else:
        print(f"\nEnding Index is out of range!\n")

start_index = int(input("\nEnter starting index: "))
end_index = int(input("\nEnter end index: "))
lst = [1,2,3,4,5,6]
slicing_lst(lst,start_index,end_index)