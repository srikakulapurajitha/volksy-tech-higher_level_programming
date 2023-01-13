The ``1-my_list`` module
========================

Using ``1-my_list``
-------------------

Import function:
	>>> MyList = _import_('1-my_list').MyList

Test for subclass:
	>>> issubclass(MyList, list)
	True

Test for isinstance:
	>>> my_list = MyList()
	>>> isinstance(my_list, list)
	True

Test empty list:
	>>> my_list = MyList()
	>>> my_list
	[]
	>>> print(my_list)
	[]
	>>> my_list.print_sorted()
	[]

Test print_sorted with one argument:
	>>> my_list.print_sorted([3])
	Traceback (most recent call last):
	TypeError: print_sorted() takes 1 positional argument but 2 were given

Append normal integers to list:
	>>> my_list.append(1)
	>>> my_list.append(4)
	>>> my_list.append(2)
	>>> my_list.append(3)
	>>> print(my_list)
	[1, 4, 2, 3]
	>>> my_list.print_sorted()
	[1, 2, 3, 4]
	>>> print(my_list)
	[1, 4, 2, 3]

Test with negative integers:
	>>> negative = MyList()
	>>> negative.append(-1)
	>>> negative.append(-4)
	>>> negative.append(-2)
	>>> negative.append(-3)
	>>> print(negative)
	[-1, -4, -2, -3]
	>>> negative.print_sorted()
	[-4, -3, -2, -1]

Test with negative and positive ints:
	>>> both = MyList()
	>>> both.append(-1)
	>>> both.append(2)
	>>> both.append(-3)
	>>> both.append(4)
	>>> print(both)
	[-1, 2, -3, 4]
	>>> both.print_sorted()
	[-3, -1, 2, 4]

Test with string:
	>>> string = MyList()
	>>> string.append('Hello')
	>>> string.append('World')
	>>> string.append(2)
	>>> string.append(3)
	>>> print(string)
	['Hello', 'World', 2, 3]
	>>> string.print_sorted()
	Traceback (most recent call last):
	TypeError: unorderable types: int() < str()
