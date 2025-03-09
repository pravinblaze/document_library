from app.models import Document

def test_document_creation():
    doc = Document(title="Test Doc", description="A test description", s3_key="test-key")
    assert doc.title == "Test Doc"
    assert doc.s3_key == "test-key"
