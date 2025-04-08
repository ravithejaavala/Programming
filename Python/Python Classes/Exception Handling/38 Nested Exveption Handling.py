'''

try:
    try:

    except:

except:

else:

finally:


'''


# nested exception handling

try:
    print('--main try block---')
    try:
        print('--nested try block----')
        a = 10
        b = 3
        print(a+b)
    except Exception as er:
        print(er)
    else:
        print('--nested else block---')
    finally:
        print('closing the nested block')
except Exception as e:
    print(e)


# example - 2


try: # main try block
    print('---sarath----')
    try:# nested try block
        a = 12
        b = 0
        print(a/b)
    except ZeroDivisionError as er: # nested except block
        print(er)
except Exception as e:
    print(e)

'''
try:
    try:
        try:
        
        except:
    except:
except:

        

'''

# example - 3


try:
    print('---main try block---')
    try:
        print('-nested try block-')
        try:
            print('--inner most try block-')
            a = 9
            b = 'hyma'
            print(a+b)
        except TypeError as e:
            print('--innner most except block::')
            print(e)
        except ValueError as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)


'''

nested exception handling in the except block:


try:

except:
    try:
    
    except:
    
    else:
    
    finally

'''

# example - 3

try:
    print(1/0)
except:
    try:
        print('nested try block under the main except block')
        try:
            print('--inner most----')
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
finally:
    print('closing')


'''
try:

except:

else:
    try:
    
    except:
    
    else:
    
    finally:


'''

# example - 4


try:
    print('try')
except Exception as e:
    print(e)
else:
    print('--Main else block--')
    try:
        print('nested try block under the main else block')
        a = 'sarath'
        b = ' k'
        print(b+a)
    except Exception as e:
        print(e)


'''

try:

except:

else:

finally:

    try:
    
    except:
    
    else:
    
    finally:

'''

# example - 5

try:
    print(1+1)
except Exception as e:
    print(e)
else:
    print('else  block')
finally:
    print('--main finally block---')
    try:
        a = 9
        b = 0
        print(a/b)
    except ZeroDivisionError as z:
        print(z)
    finally:
        print('nested finally block')


'''
Iterator
generator
decorator
file handling
regular expression
time and date modules
database connectivity
multi threading


Django
AWS Lambda
'''