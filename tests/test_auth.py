

def test_register_user(client):
    
    r= client.post("/auth/register", json= {"username": "loginuser1", "password": "secret123"})

    assert r.status_code == 200, r.text

    data= r.json()

    assert data["username"] == "loginuser1"

    assert "id" in data


def test_register_duplicate_username(client):

    r1 = client.post(
        "/auth/register",
        json={"username": "duplicateuser1234", "password": "secret123"}
    )
    assert r1.status_code == 200, r1.text

    r2 = client.post(
        "/auth/register",
        json={"username": "duplicateuser1234", "password": "secret123"}
    )

    assert r2.status_code == 409, r2.text

def test_login_success(client):

    r = client.post("/auth/register", json={"username": "loginuser12", "password": "secret123"})
    assert r.status_code == 200, r.text

    r = client.post(
        "/auth/login",
        data={"username": "loginuser12", "password": "secret123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert r.status_code == 200, r.text
    data = r.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong(client):

    r = client.post("/auth/register", json={"username": "loginuser2", "password": "secret123"})
    assert r.status_code == 200, r.text

    r = client.post(
        "/auth/login",
        data={"username": "loginuser2", "password": "wrongpass"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert r.status_code == 401, r.text