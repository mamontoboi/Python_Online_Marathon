# Example:
# If John's scriptures are ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"],
# then filterBible(scripture, "01", "001") => ["01001001","01001002"]

def filterBible(scripture, book, chapter):
    lst1 = []
    lst2 = []
    for i in scripture:
        if i[0:2] == book:
            lst1.append(i)

    for j in lst1:
        if j[2:5] == chapter:
            lst2.append(j)

    return lst2


scriptures = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
print(filterBible(scriptures, "01", "001"))