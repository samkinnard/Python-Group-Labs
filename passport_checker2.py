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


def byr(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "byr" in element:
            year = element[4:]
            if not 1920 <= int(year) <= 2005:
                passport_list.remove(passport)
                return -1


def iyr(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "iyr" in element:
            year = element[4:]
            if not 2012 <= int(year) <= 2022:
                passport_list.remove(passport)
                return -1


def eyr(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "eyr" in element:
            year = element[4:]
            if not 2022 <= int(year) <= 2032:
                passport_list.remove(passport)
                return -1


def hgt(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "hgt" in element:
            number = element[4:]
            number = number[:-2]

            if "in" not in element and "cm" not in element:
                passport_list.remove(passport)
                return -1
            if "in" in element:
                if not 59 <= int(number) <= 76:
                    passport_list.remove(passport)
                    return -1
            elif "cm" in element:
                if not 150 <= int(number) <= 193:
                    passport_list.remove(passport)
                    return -1


def ecl(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "ecl" in element:
            if (
                "amb" in element
                or "blu" in element
                or "brn" in element
                or "gry" in element
                or "grn" in element
                or "hzl" in element
                or "oth" in element
            ):
                return
            else:
                passport_list.remove(passport)
                return -1


def pid(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        if "pid" in element:
            number = element[4:]
            if len(element) != 13:
                passport_list.remove(passport)
                return -1
            else:
                try:
                    int(number)
                    return
                except:
                    passport_list.remove(passport)
                    return -1


def cid(passport):
    passport_split = passport.replace("\n", " ")
    passport_split = passport_split.split(" ")
    for element in passport_split:
        number = element[4:]
        if "cid" in element:
            try:
                int(number)
            except:
                passport_list.remove(passport)
                return -1

            if len(str(int(number))) != 3:
                passport_list.remove(passport)
                return -1


def valid_passport(passport):
    global pos
    if byr(passport) == -1:
        pos -= 1
        return
    if iyr(passport) == -1:
        pos -= 1
        return
    if eyr(passport) == -1:
        pos -= 1
        return
    if hgt(passport) == -1:
        pos -= 1
        return
    if ecl(passport) == -1:
        pos -= 1
        return
    if pid(passport) == -1:
        pos -= 1
        return
    if cid(passport) == -1:
        pos -= 1
        return


# input passports file
filename = input("Enter the name of the file: ")
passports = open(filename, "r")
pos = 0

# read passports file
x = passports.read()
passport_list = x.split("\n\n")
passport = 0
length = len(passport_list)
while passport < len(passport_list):
    if passport_list[passport].count(":") < 7:
        passport_list.pop(passport)
        passport = 0
        continue
    elif passport_list[passport].count(":") == 7 and "hcl" in passport_list[passport]:
        passport_list.pop(passport)
        passport = 0
        continue
    passport += 1


while pos < len(passport_list):
    valid_passport(passport_list[pos])
    pos += 1

# print valid passports
print(f"There are {len(passport_list)} valid passports")


passports.close()

good_passports = open("valid_passports2.txt", "w")

for each in passport_list:
    good_passports.write(each)
    good_passports.write("\n\n")

good_passports.close()
