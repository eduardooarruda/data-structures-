#pip install rich
#Google Colab: https://colab.research.google.com/drive/1EKMmjOOLzGeEs6V79b4PC8Dh4Y2dP7SB?usp=sharing

from rich import print
from rich.console import Console
from rich.progress import track
from rich.table import Table

console = Console()

class QuickFind:
    def __init__(self):
        self.listPeople = []

    def add(self, name):
        if name not in [names["name"] for names in self.listPeople]:
             self.listPeople.append({"name":name, "group":len(self.listPeople)})
        else:
          print("Name already registered")

    def printList(self):
        table = Table(title='\nPeople')
        table.add_column('Name', justify='left')
        table.add_column('Group', justify='left', style='green')
        for person in track(self.listPeople):
            table.add_row(f"{person['name']}", f"{person['group']}")
        console.print(table)

    def find(self, name1, name2):
        person1 = [people for people in self.listPeople if people["name"] == name1]
        person2 = [people for people in self.listPeople if people["name"] == name2]
        if person1 == [] or person2 == []:
            print("[yellow]non-existent user.[/]")
            return
        if person1[0]["group"] == person2[0]["group"]:
            print("\nThey belong to the same group :blush:")
        else:
            print("\nThey [on red][underline]DON'T[/][/] belong to the same group :pensive:")

    def union(self, name1, name2):
        person1 = [people for people in self.listPeople if people["name"] == name1]
        person2 = [people for people in self.listPeople if people["name"] == name2]

        if person1 == [] or person2 == []:
            print("[yellow]non-existent user.[/]")
            return

        id1 = person1[0]["group"]
        id2 = person2[0]["group"]

        for person in self.listPeople:
            if person["group"] == id1:
                person["group"] = id2
    
        

def menu():
    print("""[bold][yellow]MENU[/][/]
1: add a person to the group.
2: Check whether two people belong to the same group.
3: join groups.
4: show people list.
5: close.""")
    print()

group_people = QuickFind()
menu()

while True:
     
     option = input("\nChoose any option: ")

     if option == '1':
        name = input("Enter a name: ")
        group_people.add(name)
     elif option == '2':
         name1 = input("Enter the first person's name: ")
         name2 = input("Enter the second person's name: ")
         group_people.find(name1, name2)
     elif option == '3':
        name1 = input("Enter the first person's name: ")
        name2 = input("Enter the second person's name: ")
        group_people.union(name1, name2)        
     elif option == '4':
         group_people.printList()
     elif option == '5':
         print("Program closed")
         break
     else:
         console.print("Invalid option!", style="on red white")
         menu()  
         