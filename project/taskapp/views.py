from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
def calculator(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            operator = request.POST['operator']

            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
                result = num1 / num2

        except ValueError:
            result = "Invalid input"
    return render(request, 'calculator.html', {'result': result})

