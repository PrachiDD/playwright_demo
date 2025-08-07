def test_api_hearders(playwright):
    requests=playwright.request.new_context(
        extra_http_headers= {
            "Accept": "application/json",
            "Authorization": "Bearer Your Token Here",
            "x-api-key": "reqres-free-v1"
        }
    )
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status == 200
    json_data = response.json()
    print (json_data)
    assert json_data["data"]["id"] == 2
    assert "Janet" in json_data["data"]["first_name"]
    requests.dispose()