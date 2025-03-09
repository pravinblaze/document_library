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
