import csv
import time
# Define the URL of the remote server
#url = 'http://remote.server.com/data/upload'

# Update 1.0:
# We want to read the KrakenSim starting with the last row. Then a counter should increment so it outputs each following row.

# Update 1.1: 
# The Parser is reading data from the KrakenOutputSim.csv, however the data is being updated 4 lines at a time. As a result, the Parser is 
# only outputting every 4 lines. 

# Update 1.2: A counter (nextRow) is added to replace the [-1] last line idea. The issue now is to fine a way to start the counter from the last line

# Update 1.3: Added another csv.reader to count the number of rows in the file. This needed for the file to start at the same line of the 
# KrakenSim.py output and to build off on it when counting future data. 

# Update 1.4: A sleep(1/2) is required before the start of the while loop to prevent the loop from starting before the next KrakenSim cycle.
# Update 1.5: In the practical sense of using the KrakenSDR GUI, you need to adjust the sleep value according to the latency shown on the menu.
confidence = -1
nextRow = 0
#print("longitude ", ' | ' , "  latitude  ", ' | ', "confidence")
with open('/home/krakenrf/krakensdr_doa/krakensdr_doa/poop.csv', 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Get the total number of rows in the file
    num_rows = len(list(csv_reader))
    
    # Reset the file pointer to the beginning of the file
    csvfile.seek(0)
    
    # Create a new CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Get the row number of the last row
    for row_num, row in enumerate(csv_reader):
        if row_num == num_rows - 1:
            nextRow = row_num
            print(nextRow)
            break

time.sleep(1/2) # See Update 1.4 
while confidence < 8.3: 
    # Open the CSV file
    with open('/home/krakenrf/krakensdr_doa/krakensdr_doa/poop.csv', 'r') as csvfile:
        time.sleep(1.6) # See Update 1.5 
        final_line = csvfile.readlines()[nextRow]    # Pulls data from the last line of the csv file (most updated)
        lastRow = final_line.split(',') # Converts string of data into elements in a list seperated by a ,
        longitude = lastRow[8]  # Longitude coordinates
        latitude = lastRow[9]   # Latitude coordinates
        confidence = float(lastRow[2])   # Confidence values
        print(longitude, ' | ' , latitude, ' | ', confidence)
        print(nextRow)
        nextRow = nextRow + 1
        
