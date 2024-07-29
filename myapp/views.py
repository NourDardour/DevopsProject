from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Company, Review, Recruiter, RecruiterReview
from .forms import CompanyForm, ReviewForm, RecruiterForm, RecruiterReviewForm, ContactForm

def home(request):
    return render(request, 'home.html')

def company_list(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 10)  # Show 10 companies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'companies.html', {'page_obj': page_obj})

def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)
    reviews = Review.objects.filter(company=company)
    return render(request, 'company_detail.html', {'company': company, 'reviews': reviews})

@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})

@login_required
def add_review(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.company = company
            review.save()
            return redirect('company_detail', company_id=company.id)
    else:
        form = ReviewForm(initial={'company': company})
    return render(request, 'add_review.html', {'form': form, 'company': company})

def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    paginator = Paginator(recruiters, 10)  # Show 10 recruiters per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recruiters.html', {'page_obj': page_obj})

def recruiter_detail(request, recruiter_id):
    recruiter = Recruiter.objects.get(id=recruiter_id)
    reviews = RecruiterReview.objects.filter(recruiter=recruiter)
    return render(request, 'recruiter_detail.html', {'recruiter': recruiter, 'reviews': reviews})

@login_required
def add_recruiter(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recruiter_list')
    else:
        form = RecruiterForm()
    return render(request, 'add_recruiter.html', {'form': form})

@login_required
def add_recruiter_review(request, recruiter_id):
    recruiter = Recruiter.objects.get(id=recruiter_id)
    if request.method == 'POST':
        form = RecruiterReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.recruiter = recruiter
            review.save()
            return redirect('recruiter_detail', recruiter_id=recruiter.id)
    else:
        form = RecruiterReviewForm(initial={'recruiter': recruiter})
    return render(request, 'add_recruiter_review.html', {'form': form, 'recruiter': recruiter})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')
