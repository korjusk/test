#!/usr/bin/python

def display(a):
    result_string = ''
    for i in range(100):
        result_string += '<p style="color:rgb({}, {}, {});font-size:{}px;">I love you {}!</p>'.format(
            32,
            62,
            12,
            52,
            a)
    return result_string

if __name__ == '__main__':
    print display('Laura')
