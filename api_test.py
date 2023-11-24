import requests

def test_api():

    print("Running tests...")
    url = 'https://http.dog/418.jpg'
    response = requests.get(url)

    # Check if the response status code is 200
    if response.status_code == 200:
        print("API call successful")
    else:
        print(f"API call failed with status: {response.status_code}")

    # Check if the response contains data
    assert response.content, "Empty response content"

    # Check if the response has the expected content type
    expected_content_type = 'image/jpeg'
    assert response.headers['Content-Type'] == expected_content_type, f"Unexpected content type: {response.headers['Content-Type']}"

    import requests

def test_api():
    url = 'https://http.dog/418.jpg'
    response = requests.get(url)

    # Check the response status code is 200
    if response.status_code == 200:
        print("API call successful")
    else:
        print(f"API call failed with status: {response.status_code}")

    # Check the response contains data
    if response.content:
        print("Response contains data")
    else:
        print("Empty response content")

    # Check the response has the expected content type
    expected_content_type = 'image/jpeg'
    if response.headers['Content-Type'] == expected_content_type:
        print("Content type is as expected")
    else:
        print(f"Unexpected content type: {response.headers['Content-Type']}")

if __name__ == "__main__":
    test_api()
