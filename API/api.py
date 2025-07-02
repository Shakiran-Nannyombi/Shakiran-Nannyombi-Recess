#Example of a Rest API enpoints: Get, Post, Put, Delete
# Get /api/users - Create a new user
# Post /api/users/{id} - Get user by ID
# Put /api/users/{id} - Update user by ID
# Delete /api/users/{id} - Delete user by ID

# Example of a Rest API client using requests library
# This code snippet demonstrates how to make a GET request to a REST API endpoint using the requests library in Python.
# It retrieves a resource and prints the status code and response body.

import requests

# Example of a GET request to a REST API endpoint
# In this example, we are making a GET request to the GitHub API to retrieve user information.
# The URL is the endpoint we are accessing, and we will pass query parameters to filter the results.
# The requests library will handle the HTTP request and response for us.
url = 'https://api.github.com/users/octocat'

# Example of a GET request with query parameters
# In this case, we are passing parameters to the API to filter the results.
# The parameters are passed as a dictionary to the 'params' argument of the requests.get()
# method. The requests library will automatically encode these parameters into the URL.
# The response will contain the user information for 'octocat'.
data = {
    'name': 'Octocat',
    'email': 'octocat@example.com'
}

# Making the GET request with parameters
# The requests.get() method sends a GET request to the specified URL with the provided parameters.
response = requests.get(url, params=data)

# Checking the response status code and printing the response body
# The response object contains the status code and the response body.
# We can access the status code using response.status_code and the response body using response.json().
# The status code indicates whether the request was successful (200 OK) or if there was an error (e.g., 404 Not Found).
# The response body is typically in JSON format, which we can parse using response.json().
# Printing the status code and response body
print("Status Code:", response.status_code)
print("Response Body:", response.json())

# Example of a POST request to create a new resource
# In this example, we are making a POST request to the GitHub API to create a new repository.
# The URL is the endpoint we are accessing, and we will pass the data for the new repository in the request body.
# The requests library will handle the HTTP request and response for us.
post_url = 'https://jsonplaceholder.typicode.com/posts'

# Example of a POST request with JSON data
# In this case, we are passing the data for the new repository as a JSON object in the request body.
# The requests library will automatically encode this data into JSON format.
post_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Making the POST request with JSON data
# The requests.post() method sends a POST request to the specified URL with the provided JSON data.
response = requests.post(post_url, json=post_data)

# Checking the response status code and printing the response body
# The response object contains the status code and the response body.
# We can access the status code using response.status_code and the response body using response.json().
# The status code indicates whether the request was successful (201 Created) or if there was an error (e.g., 404 Not Found).
# The response body is typically in JSON format, which we can parse using response.json().
# Printing the status code and response body
print("Status Code:", response.status_code)
print("Response Body:", response.json())