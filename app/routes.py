from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Document

blueprint = Blueprint("documents", __name__)


@blueprint.route("/documents", methods=["POST"])
def upload_document():
    data = request.json
    title = data.get("title")
    description = data.get("description", "")
    s3_key = data.get("s3_key", None)

    if not title:
        return jsonify({"error": "Title is required"}), 400

    document = Document(title=title, description=description, s3_key=s3_key)
    db.session.add(document)
    db.session.commit()

    return jsonify(document.to_dict()), 201


@blueprint.route("/documents", methods=["GET"])
def list_documents():
    documents = Document.query.all()
    return jsonify([doc.to_dict() for doc in documents]), 200


@blueprint.route("/documents/<int:doc_id>", methods=["GET"])
def get_document(doc_id):
    document = Document.query.get(doc_id)
    if not document:
        return jsonify({"error": "Document not found"}), 404
    return jsonify(document.to_dict()), 200


@blueprint.route("/documents/<int:doc_id>", methods=["DELETE"])
def delete_document(doc_id):
    document = Document.query.get(doc_id)
    if not document:
        return jsonify({"error": "Document not found"}), 404

    db.session.delete(document)
    db.session.commit()

    return jsonify({"message": "Document deleted"}), 200
