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

# Create and initialize the net total amount of profit/losses
total_profit_loss = 0

total_relative_change = 0

# Create and initialize the average of the changes in "Profit/Losses" over the entire period
average_change = 0.0

# Create and initialize the greatest monthly relative increase in profit growth
greatest_increase = 0

# Create and initialize the month of greatest relative increase in profit growth
greatest_increase_month = ""

# Create and initialize the greatest monthly relative decrease in profit growth
greatest_decrease = 0

# Create and initialize the month of greatest relative decrease in profit growth
greatest_decrease_month = ""


# Create a variable for printing the analysis
analysis = ""

# ___________________________________________ #
# ~ ~ ~   CREATE SOME LOOPING VARIABLES ~ ~ ~ #

# Create and initialize the previous month's "Profit/Losses"
previous_profit_loss = 0

# Create and initialize the current month's "Profit/Losses"
current_profit_loss = 0

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
        
        # Store this month's change in profit/loss
        current_profit_loss = int(month[1]) - previous_profit_loss
        
        # Store last month's change in profit/loss
        previous_profit_loss = int(month[1])
        
        # Add this month's profit/loss to the running count of profit/loss
        total_profit_loss = total_profit_loss + previous_profit_loss
        
        # Add this month's change in profit/loss to the total change
        total_relative_change = total_relative_change + current_profit_loss
        
        # Determine endpoints for the dataset (min and max monthly profit/loss changes)
        if current_profit_loss > greatest_increase:
            greatest_increase = current_profit_loss
            greatest_increase_month = month[0]
        
        elif current_profit_loss < greatest_decrease:
            greatest_decrease = current_profit_loss
            greatest_decrease_month = month[0]
        
        # Capture first month's profit/loss
        if total_months == 1:
            first_month = int(month[1])

# _________________________________________ #
# ~ ~ ~   PERFORM ADDITIONAL ANALYSIS ~ ~ ~ #


# Calculate the average of the changes in "Profit/Losses" over the entire priod
average_change = (total_relative_change - first_month) / (total_months - 1)

# Format the analysis
analysis =  "Total Months: " + str(total_months) + "\nTotal: $" + str(total_profit_loss) + ("\nAverage Change: $%8.2f" % (average_change)) + "\nGreatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")\nGreatest Decrease in Profits: " + str(greatest_decrease_month)+ " ($" + str(greatest_decrease) + ")"


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
