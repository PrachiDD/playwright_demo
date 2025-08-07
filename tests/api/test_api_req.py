def test_api_request(playwright):
    requests= playwright.request.new_context()
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    json_data= response.json()
    assert json_data["id"] == 2
    assert "sunt aut facere" in json_data["title"]
    requests.dispose()
    
