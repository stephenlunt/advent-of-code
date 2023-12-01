"""
https://adventofcode.com/2022/day/1
"""

def main():
    totals = [ sum(int(i) for i in t.split("\n")) for t in open("./day-01/input.txt").read().split("\n\n") ]
    
    print(f"Problem 1: { max(totals) }")
    print(f"Problem 2: { sum(sorted(totals, reverse=True)[0:3]) }")

if __name__ == "__main__":
    main()
