import sys


def print_menu():
    print("1. See schedule")
    print("2. Add event")
    print("3. Delete event")
    print("4. Quit")


def see_events():
    for i in event_array:
        print(i)


def add_event():
    event_name = input("What event should we add?")
    event_array.append(event_name)


if __name__ == '__main__':
    event_array = ['hello', 'goodbye']

    print_menu()
    # while answer < 1 or answer > 4:
    answer = input("Please select an option:")
    ans = int(answer)

    if answer == 1:
        see_events()
    if answer == 2:
        add_event()
    if answer == 3:
        print("delete")
    if answer == 4:
        sys.exit(0)
        