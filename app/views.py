from django.shortcuts import render
from app.models import GeneralInfo

# from django.db import connection
# def write_sql_queries_to_file(file_path):
#     with open(file_path, 'w') as file:
#         queries = connection.queries
#         for query in queries:
#             sql = query['sql']
#             file.write(f"{sql}\n")


# # Create your views here.
def index(request):

#     # ORM  - Object-Relational Mapping

#     # ORM is a programming technique that allows developers to interact
#     # with database using Python objects instead of raw SQL queries

#     # READ
#     all_records = GeneralInfo.objects.all()
#     print(all_records)
#     # DELETE
#     # UPDATE
#     # CREATE

#     file_path = 'sql_queries.txt'
#     write_sql_queries_to_file(file_path)

    general_info = GeneralInfo.objects.first()
    print(f"general_info:  {general_info.location}")

    context = {}
    return render(request, "index.html", context)
