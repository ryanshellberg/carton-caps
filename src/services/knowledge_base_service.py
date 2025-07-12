from typing import List
import pymupdf
from openai.types.embedding import Embedding


class KnowledgeBaseService:
    @staticmethod
    def get_matching_documents(search_embeddings: List[Embedding]) -> List[str]:
        faq_content = KnowledgeBaseService.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral FAQs.pdf"
        )
        referral_rules = KnowledgeBaseService.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral Program Rules.pdf"
        )

        return [faq_content, referral_rules]

    @staticmethod
    def get_text_from_pdf(filepath: str) -> str:
        pdf = pymupdf.open(filepath)
        page_contents = [page.get_text() for page in pdf]
        merged_text_content = "\n".join(page_contents)

        return merged_text_content
