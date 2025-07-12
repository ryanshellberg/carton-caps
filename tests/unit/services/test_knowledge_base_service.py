from openai.types.embedding import Embedding
from services.knowledge_base_service import KnowledgeBaseService


def test_get_matching_documents():
    embeddings = [Embedding(index=0, embedding=[0.5], object="embedding")]
    documents = KnowledgeBaseService.get_matching_documents(embeddings)

    assert len(documents) == 2
    assert "Carton Caps" in documents[0]
    assert "Carton Caps" in documents[1]
