def loop_func():
    number = int(raw_input("> "))
    numbers = []
    i = 0
    while i < number:
        numbers.append(i)
        i += 1
    print numbers
	

loop_func()