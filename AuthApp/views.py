# AuthApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
import requests
from .models import CustomUser
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

def login(request):
    client_id = settings.TWITCH_CLIENT_ID
    redirect_uri = "http://localhost:8000/auth/callback/"
    response_type = "code"
    scope = "user:read:email"

    auth_url = f"https://id.twitch.tv/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&scope={scope}"
    return redirect(auth_url)

def callback(request):
    code = request.GET.get('code')
    redirect_uri = "http://localhost:8000/auth/callback/"

    token_url = "https://id.twitch.tv/oauth2/token"
    token_data = {
        'client_id': settings.TWITCH_CLIENT_ID,
        'client_secret': settings.TWITCH_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
    }
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    token_json = token_response.json()
    access_token = token_json.get('access_token')
    refresh_token = token_json.get('refresh_token')
    expires_in = token_json.get('expires_in')
    token_expires = timezone.now() + timedelta(seconds=expires_in)

    user_info_url = "https://api.twitch.tv/helix/users"
    user_info_headers = {
        'Authorization': f'Bearer {access_token}',
        'Client-Id': settings.TWITCH_CLIENT_ID,
    }
    user_info_response = requests.get(user_info_url, headers=user_info_headers)
    user_info_json = user_info_response.json()
    user_data = user_info_json['data'][0]

    user, created = CustomUser.objects.update_or_create(
        twitch_id=user_data['id'],
        defaults={
            'username': user_data['login'],
            'profile_image_url': user_data['profile_image_url'],
            'email': user_data['email'],
            'description': user_data['description'],
            'view_count': user_data['view_count'],
            'created_at': user_data['created_at'],
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_expires': token_expires,
        }
    )

    auth_login(request, user)

    return redirect('authapp:login-success')

def login_success(request):
    return render(request, 'login_success.html')
