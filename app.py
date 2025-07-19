def getOneBits(n):
    # Write your code here
    binary = bin(n)[2:]
    bin_list = [int(digit) for digit in binary]
    counter = 0
    for index in range(len(bin_list)):
        value = bin_list[index]
        counter += 1
        if value == 1:
            mylist = list(index+1, counter)
            print(mylist)


            

if __name__ == "__main__":
    n = int(input())
    getOneBits(n)
    