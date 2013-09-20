import test_aoslib

for func in dir(test_aoslib):
    if func.find('test_') == 0:
        exec 'test_aoslib.' + func + '()'
