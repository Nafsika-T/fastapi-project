
def test_todos_requires_auth(client):
    r= client.get("/todos")
    assert r.status_code == 401, r.text

def get_token(client, username: str, password: str):
    r= client.post("/auth/register", json= {"username": username, "password": password})
    assert r.status_code == 200, r.text

    r= client.post("/auth/login", data= {"username": username, "password": password}, headers= {"Content-Type": "application/x-www-form-urlencoded"})
    assert r.status_code == 200, r.text

    return r.json()["access_token"]


def test_get_todos_with_token(client):
    token= get_token(client, "todo_user1", "secret123")

    r= client.get("/todos", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200, r.text
    assert r.json() == []

def test_todo_ownership_scoping(client):

    token_a= get_token(client, "alice", "secret123")
    token_b= get_token(client, "bob", "secret123")

    r= client.post("/todos", json= {"title": "A1", "description": "Alice todo", "completed": False}, headers={"Authorization":f"Bearer {token_a}"})

    assert r.status_code == 201, r.text
    todo_id= r.json()["id"]

    r= client.get("/todos", headers= {"Authorization": f"Bearer {token_b}"})

    assert r.json() == []

    r= client.get(f"/todos/{todo_id}", headers= {"Authorization": f"Bearer {token_b}"})

    assert r.status_code ==404, r.text

    
def test_delete_other_users_todo_returns_404(client):
    token_a = get_token(client, "alice_del", "secret123")
    token_b = get_token(client, "bob_del", "secret123")

    r = client.post(
        "/todos",
        json={"title": "A1", "description": "alice todo", "completed": False},
        headers={"Authorization": f"Bearer {token_a}"},
    )
    assert r.status_code == 201, r.text
    todo_id = r.json()["id"]

    r = client.delete(
        f"/todos/{todo_id}",
        headers={"Authorization": f"Bearer {token_b}"},
    )
    assert r.status_code == 404, r.text


def test_patch_todo_partial_update(client):

    token= get_token(client, "patch_user", "secret123")

    r= client.post("/todos", json= {"title": "T1", "description": "initial description", "completed": False}, headers= {"Authorization": f"Bearer {token}"})

    assert r.status_code == 201, r.text

    todo= r.json()

    todo_id= todo["id"]

    r= client.patch(f"/todos/{todo_id}", json= {"completed": True}, headers= {"Authorization": f"Bearer {token}"})

    updated= r.json()

    assert updated["title"] == "T1"
    assert updated["description"] == "initial description"
    assert updated["completed"] is True


def test_put_todo_full_update(client):
    token = get_token(client, "put_user", "secret123")

    r = client.post(
        "/todos",
        json={
            "title": "Old title",
            "description": "Old description",
            "completed": False,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert r.status_code == 201, r.text
    todo_id = r.json()["id"]

    r = client.put(
        f"/todos/{todo_id}",
        json={
            "title": "New title",
            "description": "New description",
            "completed": True,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert r.status_code == 200, r.text
    updated = r.json()

    assert updated["id"] == todo_id
    assert updated["title"] == "New title"
    assert updated["description"] == "New description"
    assert updated["completed"] is True