# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # These link to your specific schema IDs
    student_id = models.IntegerField(null=True, blank=True)
    instructor_id = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'), 
        ('Instructor', 'Instructor'), 
        ('Student', 'Student'), 
        ('Analyst', 'Analyst')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.role}"



class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    # The FOreignKey needs to point to 'University' , make sure University model exists above this
    # university = models.ForeignKey('University', models.DO_NOTHING, db_column='university_id')
    course_name = models.CharField(max_length=100)
    duration_months = models.IntegerField(blank=True, null=True)
    program_type = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseContent(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    content = models.ForeignKey('OnlineContent', models.DO_NOTHING, db_column='content_id')

    class Meta:
        managed = False
        db_table = 'course_content'
        unique_together = (('course', 'content'),)



class CourseInstructor(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    instructor = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='instructor_id')

    class Meta:
        managed = False
        db_table = 'course_instructor'
        unique_together = (('course', 'instructor'),)



class CourseTextbook(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    isbn_number = models.ForeignKey('Textbook', models.DO_NOTHING, db_column='isbn_number')

    class Meta:
        managed = False
        db_table = 'course_textbook'
        unique_together = (('course', 'isbn_number'),)



class CourseTopic(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    topic = models.ForeignKey('Topic', models.DO_NOTHING, db_column='topic_id')

    class Meta:
        managed = False
        db_table = 'course_topic'
        unique_together = (('course', 'topic'),)


class CourseUniversity(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    university = models.ForeignKey('University', models.DO_NOTHING, db_column='university_id')

    class Meta:
        managed = False
        db_table = 'course_university'
        unique_together = (('course', 'university'),)
        

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_id')
    course = models.ForeignKey('Course', models.DO_NOTHING, db_column='course_id')
    enrollment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('student', 'course'),)


class Evaluation(models.Model):
    evaluation_id = models.IntegerField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey('Course', models.DO_NOTHING, blank=True, null=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation'


class Instructor(models.Model):
    instructor_id = models.IntegerField(primary_key=True)
    instructor_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    years_experience = models.IntegerField(blank=True, null=True)
    expertise = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'


class OnlineContent(models.Model):
    content_id = models.IntegerField(primary_key=True)
    content_type = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_content'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Textbook(models.Model):
    isbn_number = models.CharField(primary_key=True, max_length=20)
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'textbook'


class Topic(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    topic_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic'


class University(models.Model):
    university_id = models.IntegerField(primary_key=True)
    university_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university'
