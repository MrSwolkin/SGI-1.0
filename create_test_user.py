#!/usr/bin/env python3
"""Create a test user for manual testing"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import CustomUser

# Create test user
email = "test@sgi.com"
password = "ComplexPassword123!@#"

# Delete if exists
CustomUser.objects.filter(email=email).delete()

# Create new
user = CustomUser.objects.create_user(
    email=email,
    password=password,
    first_name="Test",
    last_name="User"
)

print(f"Test user created:")
print(f"  Email: {email}")
print(f"  Password: {password}")
print(f"  ID: {user.id}")
