from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AccountTests(APITestCase):
    
    def setUp(self):
        self.email = 'test@gmail.com'
        self.username = 'jpueblo'
        self.password = 'password'
        self.user = User.objects.create_user(email=self.email, 
                                             password=self.password,
                                             username=self.username)
        p1 = Post(text='Some text', user=self.user)
        p1.save()
 
    def test_create_account(self):
        user = User.objects.filter(email='test@gmail.com').first()
        user.is_active = True
        user.admin = True
        user.save()
        url = reverse('token_obtain_pair')
        # with 'password': user.password - doesn't work!
        response = self.client.post(url, data={"username": user.username,  
                                               "password": 'password'}, 
                                    format='json')
        access = response.data['access']
        url = reverse('users_list')
        response = self.client.get(url, {}, 
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(access))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"email": "sdr@1aaa.au", "username": "somebody", 
                "password": "some_password"}
        response = self.client.post(url, data, 
                                    HTTP_AUTHORIZATION='Bearer {0}'.format(access))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_posts_create(self):
        user = User.objects.filter(email='test@gmail.com').first()
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data={"username": user.username,  
                                               "password": 'password'}, 
                                    format='json')
        access = response.data['access']
        url = reverse('posts_list')
        data = {"text": "1aaa.au", "user": user.id}
        response = self.client.post(url, data, 
                                    HTTP_AUTHORIZATION='Bearer {0}'.format(access))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_posts(self):
        user = User.objects.filter(email='test@gmail.com').first()
        url = reverse('token_obtain_pair')
        # Get posts
        response = self.client.post(url, data={"username": user.username,  
                                               "password": 'password'}, 
                                    format='json')
        access = response.data['access']
        url = reverse('posts_list')
        response = self.client.get(url, {}, 
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(access))
                                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Like post
        url = reverse('like_api', kwargs={'pk': 1})
        response = self.client.get(url, {}, 
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(access))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Unlike post
        url = reverse('unlike_api', kwargs={'pk': 1})
        response = self.client.get(url, {}, 
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(access))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
