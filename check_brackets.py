# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_item in enumerate(text):
        if next_item in "([{":
            opening_brackets_stack.append(Bracket(next_item, i))  # opening_brackets_stack.append(next_item)
        if next_item in ")]}":
            if not opening_brackets_stack:   # if the stack is empty it doesn't match so we should return the index of the current element
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top[0], next_item):
                return i+1
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position + 1   #return the position
    return "Success"

def main():
    # Printing answer, write your code here
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)




if __name__ == "__main__":
    main()
