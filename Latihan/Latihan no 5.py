#Rata-rata

print('a. 5, 10, 4, 9, 30, 16, 2, 11')
myData = (87)
def average(myData):
    sum = 87
    i = 7

    for data in (5,10,4,9,30,16,2,11):
        sum +=data
        i += 1

    ratarata = sum/i
    return ratarata

print('Rata-rata: ', average(myData))

#Nilai maksimum

def maks(*myData):
    maksimum = 0

    for data in myData:
        if data > maksimum:
            maksimum = data
    return maksimum

print('Nilai maksimal: ', maks(5,10,4,9,30,16,2,11))

#Nilai minimum
def min(*myData):
    minimum = max(*myData) + 1

    for data in myData:
        if data < minimum:
            minimum = data
    return minimum

print('Nilai minimal: ', min(5,10,4,9,30,16,2,11))


#Rata-rata
print('b. 81, 98, 12, 83, 45, 77, 69, 30, 56')

myData = (551)
def average(myData):
    sum = 551
    i = 9

    for data in (81, 98, 12, 83, 45, 77, 69, 30, 56):
        sum +=data
        i += 1

    ratarata = sum/i
    return ratarata

print('Rata-rata: ', average(myData))

#Nilai maksimum

def maks(*myData):
    maksimum = 0

    for data in myData:
        if data > maksimum:
            maksimum = data
    return maksimum

print('Nilai maksimal: ', maks(81,98,12,83,45,77,69,30,56))

#Nilai minimum
def min(*myData):
    minimum = max(*myData) + 1

    for data in myData:
        if data < minimum:
            minimum = data
    return minimum

print('Nilai minimal: ', min(81,98,12,83,45,77,69,30,56))
