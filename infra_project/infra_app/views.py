from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! '
                        '(С одиннадцатой попытки, '
                        'но получилось!'
                        )


def second_page(request):
    return HttpResponse('А это вторая страница!')
