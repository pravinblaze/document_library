
def test_upload_document(client):
    response = client.post("/api/documents", json={
        "title": "Sample",
        "description": "Test file",
        "s3_key": "s3/test"
    })
    assert response.status_code == 201

def test_list_documents(client):
    response = client.get("/api/documents")
    assert response.status_code == 200
