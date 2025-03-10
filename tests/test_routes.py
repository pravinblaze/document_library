def test_upload_document(client):
    jd = {"title": "Sample", "description": "Test file", "s3_key": "s3/test"}
    response = client.post(
        "/api/documents",
        json=jd,
    )
    assert response.status_code == 201


def test_list_documents(client):
    response = client.get("/api/documents")
    assert response.status_code == 200


def test_upload_document_missing_title(client):
    jd = {"description": "Test file without title", "s3_key": "s3/test2"}
    response = client.post(
        "/api/documents",
        json=jd,
    )
    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"] == "Title is required"

def test_get_document(client):
    # First create a document
    jd = {"title": "Get Doc Test", "description": "Test file for get", "s3_key": "s3/get-test"}
    create_response = client.post("/api/documents", json=jd)
    assert create_response.status_code == 201
    doc_id = create_response.json["id"]

    # Now try to get it
    get_response = client.get(f"/api/documents/{doc_id}")
    assert get_response.status_code == 200
    assert get_response.json["title"] == "Get Doc Test"

def test_get_nonexistent_document(client):
    response = client.get("/api/documents/9999")
    assert response.status_code == 404
    assert "error" in response.json

def test_delete_document(client):
    # First create a document
    jd = {"title": "Delete Test", "description": "Test file for deletion", "s3_key": "s3/delete-test"}
    create_response = client.post("/api/documents", json=jd)
    assert create_response.status_code == 201
    doc_id = create_response.json["id"]

    # Now delete it
    delete_response = client.delete(f"/api/documents/{doc_id}")
    assert delete_response.status_code == 200
    assert "message" in delete_response.json

    # Verify it's gone
    get_response = client.get(f"/api/documents/{doc_id}")
    assert get_response.status_code == 404

def test_delete_nonexistent_document(client):
    response = client.delete("/api/documents/9999")
    assert response.status_code == 404
    assert "error" in response.json
