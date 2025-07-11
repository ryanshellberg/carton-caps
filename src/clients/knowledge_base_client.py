import pymupdf


class KnowledgeBaseClient:
    @staticmethod
    def get_matching_documents(search_embedding: float, max_documents: int = 5):
        faq_content = KnowledgeBaseClient.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral FAQs.pdf"
        )
        referral_rules = KnowledgeBaseClient.get_text_from_pdf(
            "knowledge_base/Carton Caps Referral Program Rules.pdf"
        )

        return [faq_content, referral_rules]

    @staticmethod
    def get_text_from_pdf(filepath: str):
        pdf = pymupdf.open(filepath)
        page_contents = [page.get_text() for page in pdf]
        merged_text_content = "\n".join(page_contents)

        return merged_text_content
