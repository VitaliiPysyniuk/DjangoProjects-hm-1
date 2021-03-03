from django.shortcuts import render

from calc.models import Operation


def do_calculation(request, **kwargs):
    if kwargs['x'].isalpha() or kwargs['y'].isalpha():
        return render(request, 'calc/calculate.html')
    kwargs['x'] = int(kwargs['x'])
    kwargs['y'] = int(kwargs['y'])
    if kwargs['action'] == '+':
        result = kwargs['x'] + kwargs['y']
    elif kwargs['action'] == '-':
        result = kwargs['x'] - kwargs['y']
    elif kwargs['action'] == '*':
        result = kwargs['x'] * kwargs['y']
    elif kwargs['action'] == 'div':
        result = kwargs['x'] / kwargs['y']
    else:
        result = 'Error'
    operation = Operation(result=result, **kwargs)
    return render(request, 'calc/calculate.html', {'operation': operation})
