import pytest
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer


@pytest.mark.django_db
def test_user_create():
    Group.objects.create(name='customer')
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_customer_create():
    Customer.objects.create(
        name='john', 
        email='lennon@thebeatles.com',
        )
    assert Customer.objects.count() == 1
