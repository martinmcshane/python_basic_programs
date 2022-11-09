import csv

oldfile = open("/home/dell/Desktop/test_file_image_location.csv","r")
reader = csv.reader(oldfile)
rows = list(reader)
for i in rows:
    extractedAddress = i[0]
    newRecord = extractedAddress[extractedAddress.rfind("/")::] + "\n"
    print(newRecord)
    newFile = open("/home/dell/Desktop/newFile.csv","a")
    newFile.write(str(newRecord))
    newFile.close


    


