from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'course_title': 'Django Course',
        'current_date': '2024-12-12',
        'user': {
            'name': 'John Doe',
            'email': 'john@example.com',
        },
        'product_price': 199.99999,
        'random_text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    }
    return render(request, "index.html", context)
