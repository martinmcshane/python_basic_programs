
imageURL = "sdfihieosjsisce/cehsuiscejijsoec/duhciu/3234.png"
reverseimageAddy = imageURL[::-1]
theSlash = "/"
theSlashPos = reverseimageAddy.find("/")
newString = (reverseimageAddy[0:theSlashPos+1])
print(newString[::-1])


word = 'dfsdfs/dfsdfsdf/sd/s/dfsdfsdfsdf/fdsdfsdf.png'
print(word[word.rfind("/")::])

wordywordy = (word.rfind("/"))
print(word[wordywordy:len(word)], "sausage")
