from pet import Pet

def main():
    print("🐾 Welcome to Group 789's Digital Pet Simulator!")
    name = input("What would you like to name our pet? ")
    pet = Pet(name)

    print(f"\n🎉 Great! We have adopted {name}. Type 'help' for commands.\n")

    while True:
        command = input("Type a command (eat, play, sleep, train, status, tricks, help, quit): ").strip().lower()

        if command == "eat":
            pet.eat()
        elif command == "play":
            pet.play()
        elif command == "sleep":
            pet.sleep()
        elif command == "train":
            trick = input("What trick do you want to teach? ")
            pet.train(trick)
        elif command == "status":
            pet.get_status()
        elif command == "tricks":
            pet.show_tricks()
        elif command == "help":
            print("""
Available commands:
  eat     - Feed our pet
  play    - Play with our pet
  sleep   - Let our pet rest
  train   - Teach a new trick
  status  - Show our pet's current status
  tricks  - Show learned tricks
  help    - Show this help menu
  quit    - Exit the game
""")
        elif command == "quit":
            print(f"👋 Goodbye! {name} will miss you!")
            break
        else:
            print("❗ Unknown command. Type 'help' for a list of valid commands.")

if __name__ == "__main__":
    main()
