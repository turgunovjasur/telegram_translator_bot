"""
Tarjima xizmati - Gemini API bilan ishlash
"""
import google.generativeai as genai
from config import settings


class TranslatorService:
    """Gemini API orqali tarjima qilish xizmati"""
    
    def __init__(self):
        """Gemini'ni sozlash"""
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
    
    def _create_prompt(self, text: str, direction: str) -> str:
        """Tarjima uchun prompt yaratish"""
        if direction == 'uz_to_eng':
            return f"""Sen professional tarjimon botsan. 
Quyidagi o'zbek tilidagi matnni FAQAT ingliz tiliga tarjima qil.
Hech qanday qo'shimcha tushuntirish, izoh yoki savol berma.
FAQAT tarjimani yoz, boshqa hech narsa yozma!

O'zbek matni: {text}

Inglizcha tarjima:"""
        
        else:  # eng_to_uz
            return f"""Sen professional tarjimon botsan. 
Quyidagi ingliz tilidagi matnni FAQAT o'zbek tiliga tarjima qil.
Hech qanday qo'shimcha tushuntirish, izoh yoki savol berma.
FAQAT tarjimani yoz, boshqa hech narsa yozma!

Ingliz matni: {text}

O'zbekcha tarjima:"""
    
    async def translate(self, text: str, direction: str) -> str:
        """
        Matnni tarjima qilish
        
        Args:
            text: Tarjima qilinadigan matn
            direction: 'uz_to_eng' yoki 'eng_to_uz'
            
        Returns:
            Tarjima qilingan matn
            
        Raises:
            Exception: Gemini API xatoliklari
        """
        prompt = self._create_prompt(text, direction)
        response = self.model.generate_content(prompt)
        return response.text.strip()


# Translator service instansiyasi
translator_service = TranslatorService()
