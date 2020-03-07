# ___________________________________ #
# ~ ~ ~   IMPORT SOME MODULES   ~ ~ ~ #

# Import the os module so we can can create a path to the data file
import os

# Import the csv module so we can read the data file
import csv


# _____________________________________ #
# ~ ~ ~   CREATE SOME VARIABLES   ~ ~ ~ #

# Create and initialize the total number of months included in the dataset
total_months = 0

# Create and initialize the average of the changes in "Profit/Losses" over the entire period
average_change = 0.0

# Create and initialize the greatest monthly profits (date and amount) over the entire period
greatest_increase = 0

# Create and initialize the month of greatest profits (date and amount) over the entire period
greatest_increase_month = ""

# Create and initialize the greatest monthly losses (date) over the entire period
greatest_decrease = 0

# Create and initialize the month of greatest losses (date) over the entire period
greatest_increase_month = ""

# Create and initialize the row of the month of greatest loss
greatest_loss_row = 1

# Create a variable for printing the analysis
#analysis = ""

# ___________________________________________ #
# ~ ~ ~   CREATE SOME LOOPING VARIABLES ~ ~ ~ #

# Create and initialize the starting (e.g. previous monthly ending) net total "Profit/Losses"
starting_profit_loss = 0

# Create and initialize the net total (e.g. current monthly ending) net total "Profit/Losses" over the entire period
ending_profit_loss = 0

# Create and initialize the current monthly change in "Profit/Losse"
monthly_change = 0


# ________________________________________ #
# ~ ~ ~   GRAB AND ANALYZE OUR DATA  ~ ~ ~ #

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

# Split the data on commas
    budget_data = csv.reader(csvfile, delimiter=',')
    
   #  Skip the header
    next(budget_data)
    
    # Start the loop!
    for month in budget_data:
        
        # Add this row to the list of monthly data
        total_months += 1
        
        # Set this month's starting total "Profit/Losses"
        starting_profit_loss = ending_profit_loss
        
        # Add (or subtract) the current row's value for profit/loss to the variable tracking total amount of profit/loss
        ending_profit_loss = ending_profit_loss + int(month[1])
        
        # Calculate the monthly change
        monthly_change = ending_profit_loss - starting_profit_loss
        
        # Determine endpoints for the dataset (min and max monthly profit/loss changes)
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            greatest_increase_month = month[0]
        
        elif monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_month = month[0]
        

# _________________________________________ #
# ~ ~ ~   PERFORM ADDITIONAL ANALYSIS ~ ~ ~ #


# Calculate the average of the changes in "Profit/Losses" over the entire priod
average_change = ending_profit_loss / total_months

# Format the analysis
analysis =  "Total Months: " + str(total_months) + "\nTotal: $" + str(ending_profit_loss) + ("\nAverage Change: $%8.2f" % (average_change)) + "\nGreatest Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")\nGreatest Losses: " + str(greatest_decrease_month)+ " ($" + str(greatest_decrease) + ")"


# ____________________________________________ #
# ~ ~ ~   OUTPUT ANALYSIS TO THE TERMINAL ~ ~ ~ #

# Print the analysis to the terminal
print(analysis)

# ____________________________________________ #
# ~ ~ ~   OUTPUT ANALYSIS TO A NEW FILE ~ ~ ~ #

# Specify the file to write to
output_data = open("data.txt", "w+")

# Print the analysis to the file
output_data.write(analysis)

# Finish storing the file
output_data.close()
