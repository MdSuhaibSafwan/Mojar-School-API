# Generated by Django 4.2.4 on 2023-09-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MojarSchoolMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('is_guest', models.BooleanField(default=True)),
                ('subscription', models.CharField(choices=[['MO', 'MONTHLY'], ['QU', 'QUARTERLY'], ['WE', 'WEEKLY'], ['YE', 'YEARLY'], ['DA', 'DAILY']], max_length=2, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('street_address', models.TextField(null=True)),
                ('town', models.CharField(max_length=50, null=True)),
                ('post_code', models.CharField(max_length=4, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
