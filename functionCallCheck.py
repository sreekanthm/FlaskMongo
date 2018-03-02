def func1():

	dict1 = {
     
     "sreekanth" : "sreekanth123",
     "vivek" : "vivek123"

	}

	return dict1


def func2():
	dict2 = {}
	func1()
	dict2 = dict1
    
	return dict2

print dict2

