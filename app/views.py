from django.shortcuts import render, redirect
from app.models import (
    GeneralInfo, 
    Service, 
    Testimonial,
    FrequentlyAskedQuestion,
)

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

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    faqs = FrequentlyAskedQuestion.objects.all()
    
    context = {
        "company_name": general_info.company_name,
        "location": general_info. location,
        "email": general_info.email,
        "phone": general_info.phone,
        "open_hours": general_info.open_hours,
        "video_url": general_info.video_url,
        "twitter_url": general_info.twitter_url,
        "facebook_url": general_info.facebook_url,
        "instagram_url": general_info.instagram_url,
        "linkedin_url": general_info.linkedin_url,

        "services" : services,
        "testimonials" : testimonials,

        "faqs": faqs,
    }

    return render(request, "index.html", context)

def contact_form(request):
    print("\nUser has submit a contact form\n")
    return redirect('home')

