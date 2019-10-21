s = 'abc'#input() #'abacabadaba'
fs = 'd'#input() #'aba'

start = 0
found_index = 0
while found_index != -1:
    found_index = s.find(fs, start)
    if found_index >= 0 or start == 0:
        print (str(found_index) + " ", end = "")
    start = found_index + 1




