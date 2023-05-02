import os
import csv
# budget_data csv file open as read only
with open("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) ## to skip header from total count
    print("Financial Analaysis")
    print("-------------------------------")
    total_num = []
    total_proloss = [] 
    for row in csv_reader:
        # list total_num append to row[0]
        total_num.append(row[0])
        # list totalproloss append to row[1]
        total_proloss.append(float(row[1]))    
    #print total months
    print("Total_month:", len(total_num))
    # sum of total profit/losses
    print("Total:", "$", int(sum(total_proloss)))
    # To find Total chnage of Profit/losses
    # Creat new list called total_chnage
    total_change = []
        # range given from loop
    for i in range(0,len(total_proloss)-1):
        # second valu-first value.....so on
        change = (total_proloss [i+1] - total_proloss [i])
        # chnage added to list total_change
        total_change.append(int(change))
        i=i+1
    # to find average cahnge        
    print("Average Change:","%.2f" % round(sum(total_change)/len(total_change),2))
    # Greatest Increased in profit
    max_val=max(total_change)
    # Greatest Decreased in profit
    min_val=min(total_change)
    # print both values with months
    print("Greatest Increase in Profits:", total_num[total_change.index(max_val)+1],"($"+str(int(max_val))+")")
    print("Greatest Decrease in Profits:", total_num[total_change.index(min_val)+1], "($"+str(int(min_val))+")")
# creat text file call anaylsis and print result in it
f= open ("analysis.txt", "w")
f.write("Financial Analaysis")
f.write("\n-------------------------------")
f= open ("analysis.txt", "a")
print("\nTotal_month:", len(total_num),file=f)
print("Total:", "$", int(sum(total_proloss)),file=f)
print("Average Change:","%.2f" % round(sum(total_change)/len(total_change),2),file=f)            
print("Greatest Increase in Profits:", total_num[total_change.index(max_val)+1],"($"+str(int(max_val))+")",file=f)
print("Greatest Decrease in Profits:", total_num[total_change.index(min_val)+1], "($"+str(int(min_val))+")",file=f)
f.close()


        

