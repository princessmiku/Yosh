from Libary import YoshData

Y = YoshData.file("test.yosh")
print(Y.data)
Y.add("Max", "gender", "male")
Y.add("Cookies", "taste", "yes")
print(Y.data)
Y.save()
