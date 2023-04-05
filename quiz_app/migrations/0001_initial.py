# Generated by Django 4.1.7 on 2023-02-19 05:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExaminationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=200)),
                ('per_ques_marks', models.IntegerField()),
                ('total_time', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('created', 'created')], default='pending', max_length=10)),
                ('published', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='মডেল টেস্ট', max_length=250)),
                ('top_header', models.CharField(max_length=200, null=True)),
                ('homepage_message', ckeditor.fields.RichTextField(null=True)),
                ('activation_message', ckeditor.fields.RichTextField(null=True)),
                ('after_payment_message', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_num', models.IntegerField()),
                ('phone_number', models.IntegerField(null=True)),
                ('is_student', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuizInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_answered_quiz_pk', models.IntegerField(default=0)),
                ('num_of_correct_ans', models.IntegerField(default=0)),
                ('exam_done', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('time_delta', models.DurationField(blank=True, null=True)),
                ('examination_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exami_info', to='quiz_app.examinationinfo')),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stud_info', to='quiz_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(null=True)),
                ('is_teacher', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=True)),
                ('user_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz_app.teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='user_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('hints', models.CharField(blank=True, max_length=3000, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('exam_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam_data', to='quiz_app.examinationinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(null=True)),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stu_pay_info', to='quiz_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('is_correct', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='quiz_app.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='examinationinfo',
            name='subject_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic', to='quiz_app.subject'),
        ),
        migrations.AddField(
            model_name='examinationinfo',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_info', to='quiz_app.teacher'),
        ),
    ]