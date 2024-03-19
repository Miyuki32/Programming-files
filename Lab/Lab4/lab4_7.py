my_dictionary = {"student1":78, "student2":64, "student3":62, "student4":56, "student5":71}

total = sum(my_dictionary.values())
average = sum(my_dictionary.values())/float(len(my_dictionary))
minimum = min(my_dictionary.values())

maximum = max(my_dictionary.values())

print('Total marks (among 5 students): ',total)

print('Average marks (among 5 students): ',average)

print('Minimum marks (among 5 students): ',minimum)

print('Maximum marks (among 5 students): ',maximum)