# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: 11.9 LAB: Passport
# Date: 11/8/22

#input passports file
filename = input("Enter the name of the file: ")
passports = open(filename, "r")
x = passports.read()

#read passports file and split file
passport_list = x.split("\n\n")
passport = 0
length = len(passport_list)
while (passport < len(passport_list)):
    if passport_list[passport].count(':') < 7:
        passport_list.pop(passport)
        passport = 0
        continue
    elif passport_list[passport].count(':') == 7 and 'hcl' in passport_list[passport]:
        passport_list.pop(passport)
        passport = 0
        continue
    passport += 1

#print valid passports
print(f'There are {len(passport_list)} valid passports')

passports.close()

good_passports=open("valid_passports.txt",'w')
for passport in passport_list:
  good_passports.write(passport)
  good_passports.write('\n\n')

good_passports.close()

