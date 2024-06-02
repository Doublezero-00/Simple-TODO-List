todo_list = []
status = []

#Add items to the list
def add_items(todo_list): 
    item = input('Add item : ')
    todo_list.append(item)
    status.append("Not Completed")
    return todo_list, status

#Remove items from the list
def remove_items(todo_list):
    rm_item = int(input("What item do you want to delete : "))
    todo_list.pop(rm_item-1)
    status.pop(rm_item-1)
    return todo_list, status

#Update items in the list
def update_status(todo_list, status):
    user_finished = int(input("What item did you finish : "))
    status[user_finished-1] = "Completed"
    return status

#Display items from the list
def display_items(todo_list, status):
    count = 0
    for itm in todo_list:
        print(f'{count+1} : {itm}  |  Status : {status[count]}')
        count += 1

#Display main menu
def main():
    print("---Simple TODO List---")
    print("1) Add items to the list")
    print("2) Display items in the list")
    print("3) Remove items from the list")
    print("4) Update status in the list")
 
while True:
    main()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        todo_list, status = add_items(todo_list)
    elif choice == 2:
        display_items(todo_list, status)  
    elif choice == 3:
        todo_list, status = remove_items(todo_list)
    elif choice == 4: 
        status = update_status(todo_list, status)
