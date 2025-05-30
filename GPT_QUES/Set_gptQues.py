def get_friends(name):
    print(f"\nEnter friends of {name} (type 'done' to finish):")
    friends = set()
    while True:
        friend = input(f"Add a friend of {name}: ").strip()
        if friend.lower() == "done":
            break
        elif friend:
            friends.add(friend)
    return friends

def main():
    print("=== Mutual Friends Finder ===")
    
    person1 = input("Enter name of first person: ").strip()
    person2 = input("Enter name of second person: ").strip()
    
    friends1 = get_friends(person1)
    friends2 = get_friends(person2)

    mutual_friends = friends1 & friends2  # Intersection of sets

    print("\n--- Results ---")
    if mutual_friends:
        print(f"Mutual friends of {person1} and {person2}:")
        for friend in mutual_friends:
            print(f"- {friend}")
    else:
        print(f"{person1} and {person2} have no mutual friends.")

if __name__ == "__main__":
    main()
