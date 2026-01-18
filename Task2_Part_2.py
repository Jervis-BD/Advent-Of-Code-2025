
## For Part 2 i need to check if each id is a repeated sequence of numbers of any length 
## ie 111 is invalid, so is 123123123 so is 11221122
## ill probbaly make a function which seaches across in increasing sizes for the pattern
## and run it through for each number ie x^2 loops + a linear search for pattern sizes up to half the number length

id_ranges = "1090286-1131879,3259566-3404881,138124-175118,266204727-266361099,16765-24272,7657360692-7657593676,88857504-88926597,6869078-6903096,48444999-48532270,61427792-61580535,71-103,8077-10421,1920-2560,2-17,951-1259,34-50,28994-36978,1309-1822,9393918461-9393960770,89479-120899,834641-988077,5389718924-5389797353,34010076-34214499,5063-7100,607034-753348,19098586-19261191,125085556-125188689,39839-51927,3246-5037,174-260,439715-473176,187287-262190,348-535,58956-78301,4388160-4505757,512092-584994,13388753-13534387".split(",")
dummy_id = 0

### This does not work right now i do not know why
### It picks up some but not all invalids and some not invalids
### might be a size issue as it picks up no small length invalids

def pattern(number):
    for i in range(1, (len(number) // 2) + 1):
        j = i
        k = 0
        while j < len(number) and number[k:j] == number[k + i:j + i]:
            k += i
            j += i
        if j == len(number) and number[k:j] == number[k - i:j - i]:
            return int(number)
    return 0

def range_pattern(start, end):
    subtot = 0
    for number in range(start, end + 1):
        number = str(number)
        subtot += pattern(number)
    return subtot
      
for ranges in id_ranges:
    start, end = int(ranges.split("-")[0]), int(ranges.split("-")[1])
    dummy_id += (range_pattern(start, end))

print(dummy_id)