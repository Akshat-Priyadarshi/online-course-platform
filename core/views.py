# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection
from django.db.models import Max
from .forms import AddContentForm
from .models import Course, OnlineContent, CourseContent
import datetime

@login_required
def dashboard_redirect(request):
    role = request.user.profile.role
    if role == 'Admin':
        return render(request, 'dashboards/admin.html')
    elif role == 'Instructor':
        return render(request, 'dashboards/instructor.html')
    elif role == 'Student':
        return render(request, 'dashboards/student.html')
    elif role == 'Analyst':
        return render(request, 'dashboards/analyst.html')
    return redirect('login')


@login_required
def course_list(request):
    # 1. Get the search query from the URL (e.g., ?q=Python)
    query = request.GET.get('q')
    
    if query:
        # Case-insensitive containment search
        courses = Course.objects.filter(course_name__icontains=query)
    else:
        # If no search, show all courses
        courses = Course.objects.all()
    
    return render(request, 'student/course_list.html', {'courses': courses})

@login_required
def register_course(request, course_id):
    if request.method == 'POST':
        # 1. Get the logged-in student's ID from the Profile we created in Phase 2
        try:
            student_id = request.user.profile.student_id
            if not student_id:
                messages.error(request, "Error: No Student ID linked to your account.")
                return redirect('course_list')
        except:
            messages.error(request, "Profile error. Please contact Admin.")
            return redirect('course_list')

        # 2. Use Raw SQL to check if already enrolled
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Enrollment WHERE student_id = %s AND course_id = %s",
                [student_id, course_id]
            )
            row = cursor.fetchone()

            if row:
                messages.warning(request, "You are already enrolled in this course!")
            else:
                # 3. Use Raw SQL to Insert (Avoids Django Composite Key issues)
                current_date = datetime.date.today()
                cursor.execute(
                    "INSERT INTO Enrollment (student_id, course_id, enrollment_date, status) VALUES (%s, %s, %s, %s)",
                    [student_id, course_id, current_date, 'Enrolled']
                )
                messages.success(request, f"Successfully registered for Course ID {course_id}!")

    return redirect('course_list')


@login_required
def add_content(request):
    # Security: Ensure only Instructors can access this feature [cite: 12, 17]
    if request.user.profile.role != 'Instructor':
        messages.error(request, "Access Denied: Instructor privileges required.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = AddContentForm(request.POST)
        if form.is_valid():
            try:
                # 1. Manually calculate the next content_id (Max ID + 1)
                max_id = OnlineContent.objects.aggregate(Max('content_id'))['content_id__max']
                new_id = 1 if max_id is None else max_id + 1
                
                # 2. Save the OnlineContent object
                content = form.save(commit=False)
                content.content_id = new_id
                content.save()
                
                # 3. Create the mapping in the Course_Content junction table
                selected_course = form.cleaned_data['course']
                # CourseContent.objects.create(
                #     course=selected_course, 
                #     content=content
                # )
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO Course_Content (course_id, content_id)
                        VALUES (%s, %s)
                        """,
                        [selected_course.course_id, content.content_id]
                    )
                
                messages.success(request, f"Successfully added '{content.title}' to {selected_course.course_name}!")
                return redirect('dashboard')
            except Exception as e:
                messages.error(request, f"Database Error: {str(e)}")

        else:
            messages.error(
                request,
                "Invalid form input. Please check all fields."
            )
    else:
        form = AddContentForm()

    return render(request, 'instructor/add_content.html', {'form': form})