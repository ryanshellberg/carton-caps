from typing import List
import pymupdf
from openai.types.embedding import Embedding


class KnowledgeBaseService:
    @staticmethod
    def get_matching_documents(search_embeddings: List[Embedding]) -> List[str]:
        """Gets matching document contents based on search Embeddings.

        Args:
            search_embeddings: A list of embeddings to use for document matching. Currently unused in the prototype.

        Returns:
            A list of Strings containing the text contents of matching documents.
        """

        faq_content = KnowledgeBaseService.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral FAQs.pdf"
        )
        referral_rules = KnowledgeBaseService.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral Program Rules.pdf"
        )

        return [faq_content, referral_rules]

    @staticmethod
    def get_text_from_pdf(filepath: str) -> str:
        """Get's the text content of a PDF file.

        Args:
            filepath: The filepath of the PDF, relative to the root of the repository.

        Returns:
            The text content of the PDF.
        """
        pdf = pymupdf.open(filepath)
        page_contents = [page.get_text() for page in pdf]
        merged_text_content = "\n".join(page_contents)

        return merged_text_content
