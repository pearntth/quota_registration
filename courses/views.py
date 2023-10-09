from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Course, QuotaRequest
# Create your views here.

def register(request):
    search_query = request.GET.get('search', '')

    courses = Course.objects.filter(name__icontains=search_query) | Course.objects.filter(code__icontains=search_query)

    context = { 'courses': courses }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'courses/course_list.html', context)
    

def request_quota(request, course_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please Login')
            return redirect('login') 

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            messages.error(request, 'ไม่พบรายวิชาที่ต้องการขอโควต้า')
            return redirect('course_list') 

        if course.seats_available <= 0:
            messages.error(request, 'โควต้าในรายวิชานี้เต็มแล้ว')
            return redirect('course_list')  

        existing_request = QuotaRequest.objects.filter(student=request.user, course=course).exists()
        if existing_request:
            messages.error(request, 'คุณเคยขอโควต้ารายวิชานี้ไปแล้ว')
            return redirect('course_list') 

        quota_request = QuotaRequest(student=request.user, course=course, is_approved=False)
        quota_request.save()

        course.seats_available -= 1
        course.save()

        messages.success(request, 'ขอโควต้าสำเร็จ')
        return redirect('course_list')  

    return redirect('course_list')


def cancel_request(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    course = Course.objects.get(id=course_id)

    quota_request = QuotaRequest.objects.filter(student=request.user, course=course).first()
    quota_request.delete()

    course.seats_available += 1
    course.save()

    return redirect('home')