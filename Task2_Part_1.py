
## This Task works as prescribed in the advent of code
## Couldve read the input as a file or as stdin but didnt feel it was needed since it need only run once
## Part 1s design will have to be basically fully changed for part 2
## Added a check to the function to skip a range where the entire range is not possibly invalid (odd number lengths)

id_ranges = "1090286-1131879,3259566-3404881,138124-175118,266204727-266361099,16765-24272,7657360692-7657593676,88857504-88926597,6869078-6903096,48444999-48532270,61427792-61580535,71-103,8077-10421,1920-2560,2-17,951-1259,34-50,28994-36978,1309-1822,9393918461-9393960770,89479-120899,834641-988077,5389718924-5389797353,34010076-34214499,5063-7100,607034-753348,19098586-19261191,125085556-125188689,39839-51927,3246-5037,174-260,439715-473176,187287-262190,348-535,58956-78301,4388160-4505757,512092-584994,13388753-13534387".split(",")
dummy_id = 0

def repeated(start, end):
    l_start, l_end = len(str(start)), len(str(end))
    live_count = 0
    if l_start == l_end and l_end % 2 == 1:
        return 0
    for i in range(start, end + 1):
        li = str(i)
        mid = len(li) // 2
        if li[:mid] == li[mid:]:
            live_count += i
    return live_count

for ranges in id_ranges:
    start, end = int(ranges.split("-")[0]), int(ranges.split("-")[1])
    dummy_id += repeated(start, end)

print(dummy_id)