#!/usr/bin/python3
import requests
import csv

"""
Function to fetch and print the titles of posts
"""
def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

"""
Function to fetch and save posts to a CSV file
"""
def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        posts_data = []

        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts_data.append(post_dict)

        """
        Write the data to a CSV file
        """
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts_data:
                writer.writerow(post)
