# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         SAM KINNARD
# Section:      565
# Assignment:   Lab 11.11
# Date:         10/11/2022

# getting the file name in input
file_name = input('Enter the name of the file: ')

# opening and then reading the file
openfile = open(file_name, 'r')

readingfile = openfile.read()

# splitting the barcode file by newline
barcode_list = readingfile.split('\n')

validcodes = []

count = 0

# for loop that does the necessary math on each barcode
for barcode in barcode_list:
    group1 = [int(barcode[b]) for b in range(0, 12, 2)]
    sum1 = sum(group1)
    group2 = [int(barcode[b]) for b in range(1, 12, 2)]
    sum2 = sum(group2)
    if ((sum2 * 3) + sum1) % 10 == 10 - int(barcode[-1]):
        validcodes.append(barcode)
        count += 1
        
# joining all of the valid codes into a string
validcodes = '\n'.join(validcodes)

# printing the number of valid codes
print(f'There are {count} valid barcodes')

# closing the original file
openfile.close()

# opening the new valid barcode file
newfile = open("valid_barcodes.txt", "w")

# writing the valid code string into the new file
newfile.write(validcodes)

# closing the new file
newfile.close


