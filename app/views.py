from django.http import HttpResponse
from django.db import connection


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from volunteers")
        rows = cursor.fetchall()
    return HttpResponse(rows)