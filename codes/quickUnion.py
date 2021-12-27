#Reference: https://researchhubs.com/post/computing/algorithm-1/quick-union.html
#Google Colab: https://colab.research.google.com/drive/1uEtRcjFJD7Nmkh9cUIpN_H5cWzfMl4Nz?usp=sharing

class QuickUnion:
    def __init__(self, i = 0):
        self.id = list(range(i))

    def root(self, ind):
        while ind != self.id[ind]:
            ind = self.id[ind]
        return ind

    def connected(self, p, q):
        print("Are connected") if self.root(p) == self.root(q) else print("Are NOT connected")

    def connect_node(self, p, q):
        self.id[p] = q

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q) 
        self.id[i] = j
        print("DONE")

    def __str__(self):
        return str(self.id)
           

def menu():
    print("""
-----MENU-----
1: To connect.
2: connect node.
3: Join.
4: Show list.
5: Close.
    """)


number_of_indexes = int(input("Enter the number of indexes in the list: "))

list_numbers = QuickUnion(number_of_indexes)

menu()

while True:
    option = input("\nChoose any option: ")
    
    if option == '1':
        ind1 = int(input("index one: "))
        ind2 = int(input("index two: "))
        list_numbers.connected(ind1, ind2)

    elif option == '2':
        ind1 = int(input("index one: "))
        ind2 = int(input("index two: "))
        list_numbers.connect_node(ind1, ind2)
    
    elif option == '3':
        ind1 = int(input("index one: "))
        ind2 = int(input("index two: "))
        list_numbers.union(ind1, ind2)
    
    elif option == '4':
        print(list_numbers)
    
    elif option == '5':
        print("Program closed")
        break
    else:
        print("Invalid option!")
        menu()