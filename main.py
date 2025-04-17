from pet import Pet

def main():
    print("🐾 Welcome to My Digital Pet Simulator!")
    name = input("My Pet Name is? ")
    pet = Pet(name)

    print(f"\n🎉 Great! I Have adopted {name}. Type 'help' for commands.\n")

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
  eat     - Feed your pet
  play    - Play with your pet
  sleep   - Let your pet rest
  train   - Teach a new trick
  status  - Show your pet's current status
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

