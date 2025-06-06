# Integrate the logic and orchestrate the process of loading the data,
# organizing seats, displaying results, and storing them back into Excel

# Import necessary modules
import sys  # To access command-line arguments
from src.utils import load_colleagues  # Function to load colleague data from a file
from src.openspace import OpenSpace   # Main class to manage seating arrangement in the open space


# Entry point of the program
if __name__ == "__main__":
    # Load the Excel file containing the list of colleagues
    filename = sys.argv[1]  # The filename should be passed as a command-line argument
    colleagues = utils.load_colleagues(filename)  # Load the colleague data into a list or similar structure

    # If the colleague list was successfully loaded
    if colleagues:
        # Create an OpenSpace object with a given layout:
        # 6 tables, each with 4 seats (can be adjusted as needed)
        open_space = openspace.OpenSpace(number_of_tables=6, seats_per_table=4)
        
        # Organize the seating: distribute colleagues across tables
        open_space.organize(colleagues)
        
        # Display the result to the console
        open_space.display()
        
        # Save the seating arrangement to an Excel file
        open_space.store('seating_arrangement.xlsx')
    else:
        # In case the colleague data was not loaded correctly (e.g. file not found or empty)
        print("No colleagues data found. Exiting...")
