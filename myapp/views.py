from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Company, Recruiter, Review
from .forms import ReviewForm
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def company_list(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 10)  # Show 10 companies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'company_list.html', {'page_obj': page_obj})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})

def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    paginator = Paginator(recruiters, 10)  # Show 10 recruiters per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recruiter_list.html', {'page_obj': page_obj})

def recruiter_detail(request, pk):
    recruiter = get_object_or_404(Recruiter, pk=pk)
    return render(request, 'recruiter_detail.html', {'recruiter': recruiter})

def add_review(request, review_type, pk):
    if review_type == 'company':
        reviewed_instance = get_object_or_404(Company, pk=pk)
    else:
        reviewed_instance = get_object_or_404(Recruiter, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewed_instance = reviewed_instance
            review.save()
            return redirect(reverse(f'{review_type}_detail', args=[pk]))
    else:
        form = ReviewForm()
    
    return render(request, 'review_form.html', {'form': form})

def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('home')
    return render(request, 'review_confirm_delete.html', {'review': review})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email or save contact message to database
            send_mail(
                subject=f"Contact Form: {form.cleaned_data['subject']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your_email@example.com'],
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def help(request):
    return render(request, 'help.html')
    

def search(request):
    query = request.GET.get('q')
    if query:
        companies = Company.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        recruiters = Recruiter.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        companies = Company.objects.all()
        recruiters = Recruiter.objects.all()
    
    return render(request, 'search_results.html', {'companies': companies, 'recruiters': recruiters, 'query': query})




