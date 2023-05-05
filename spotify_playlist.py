from utils import create_playlist


def main():
    # Display the main menu
    print("Select an option:")
    print("1. Create a playlist with your all-time top tracks")
    print("2. Create a playlist with your last 6 months top tracks")
    print("3. Create a playlist with your last month top tracks")
    print("4. Exit")

    # Get the user's choice from the main menu
    choice = int(input("Enter the option number: "))

    # Define the time ranges mapping
    time_ranges = {
        1: "long_term",
        2: "medium_term",
        3: "short_term"
    }

    # Check if the user chose a valid option
    if choice in time_ranges:
        # Get the size of the playlist from the user
        size = int(input("Enter the number of tracks to include in the playlist: "))

        # Create the playlist based on the chosen option and size
        create_playlist(time_ranges[choice], size)
    elif choice == 4:
        print("Exiting the application.")
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
