
imageURL = "sdfihieosjsisce/cehsuiscejijsoec/duhciu/3234.png"
reverseimageAddy = imageURL[::-1]
theSlash = "/"
theSlashPos = reverseimageAddy.find("/")
newString = (reverseimageAddy[0:theSlashPos+1])
print(newString[::-1])


word = 'dfsdfs/dfsdfsdf/sd/s/dfsdfsdfsdf/fdsdfsdf.png'
print(word[word.rfind("/")::])

cunt = (word.rfind("/"))
print(word[cunt:len(word)], "fuck")