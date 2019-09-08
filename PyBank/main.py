import os
import csv

csv_filename = 'python Homework PayBank.csv'

with open(csv_filename,newline='') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
    print("csv_header",csv_header)
    print()

    first_month_data = next(csv_reader)
    first_month = first_month_data[0]
    first_month_profit_loss = float(first_month_data[1])

    list_of_months = []
    monthly_changes = []
    nbr_of_list_of_months = 1
    net_profit_loss = first_month_profit_loss

    best_monthly_change = 0
    worst_monthly_change = 0
    month_of_best_monthly_change = ""
    month_of_worst_monthly_change = ""
    prev_month_profit_loss = first_month_profit_loss

    # Read second month onwards
    for each_data in csv_reader:

        nbr_of_list_of_months = nbr_of_list_of_months + 1
        print("each_data", each_data)

        current_month = each_data [0]
        list_of_months.append( current_month )

        current_month_profit_loss = float(each_data [1] )
        net_profit_loss = net_profit_loss + current_month_profit_loss

        change_current_month = current_month_profit_loss - prev_month_profit_loss
        print("change in month: ", current_month, " was: ", change_current_month)
        monthly_changes.append( change_current_month )

        if change_current_month > best_monthly_change:  # Change this month is more than best so far

            best_monthly_change = change_current_month
            month_of_best_monthly_change = current_month
            print('month_of_best_monthly_change: ', month_of_best_monthly_change)

        elif change_current_month < worst_monthly_change: # Change this month is worse than the worst change so far

            worst_monthly_change = change_current_month
            month_of_worst_monthly_change = current_month
            print('month_of_worst_monthly_change: ', month_of_worst_monthly_change )
        
        # For next time around the loop
        prev_month_profit_loss = current_month_profit_loss

        # For loop finished

    # CSV Reader also is at the bottom of CSV file
    print()
    print("Total_numbers_of_list_of_months:", nbr_of_list_of_months)
    print("Net_profit_loss:", round(net_profit_loss, 2))
    ave_change = sum (monthly_changes) / len (monthly_changes)
    print("Ave_change:", round(ave_change, 2))
    print("greatest increase in profits:", round(best_monthly_change,2) , " in month ", month_of_best_monthly_change)
    print("greatest decrease in losses:", round(worst_monthly_change, 2) , "in month", month_of_worst_monthly_change)

with open("results.txt","w") as file:

    
    file.write("Total_numbers_of_list_of_months:" + str(nbr_of_list_of_months) + "\n")
    file.write("Net_profit_loss:" + str(round(net_profit_loss, 2)) + "\n") 
    file.write("Ave_change:" + str(round(ave_change, 2)) + "\n") 
    file.write("greatest increase in profits:" + str(round(best_monthly_change,2)) + " in month " + str(month_of_best_monthly_change) + "\n")
    file.write("greatest decrease in losses:" + str(round(worst_monthly_change, 2)) + "in month" + str(month_of_worst_monthly_change) + "\n")

