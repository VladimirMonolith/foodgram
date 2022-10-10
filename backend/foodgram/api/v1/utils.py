import io

from django.http import FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def create_shopping_list(ingredients_cart):
    """Функция для формирования списка покупок."""
    font = 'TNR'
    pdfmetrics.registerFont(TTFont('TNR', 'times.ttf', 'UTF-8'))
    buffer = io.BytesIO()
    pdf_file = canvas.Canvas(buffer)
    pdf_file.setFont(font, 24)
    pdf_file.drawString(200, 800, 'Список покупок.')
    pdf_file.setFont(font, 14)
    from_bottom = 750
    for number, ingredient in enumerate(ingredients_cart, start=1):
        pdf_file.drawString(
            50,
            from_bottom,
            f"{number}. {ingredient['ingredient__name']}: "
            f"{ingredient['ingredient_value']} "
            f"{ingredient['ingredient__measurement_unit']}.",
        )
        from_bottom -= 20
        if from_bottom <= 50:
            from_bottom = 800
            pdf_file.showPage()
            pdf_file.setFont(font, 14)
    pdf_file.showPage()
    pdf_file.save()
    buffer.seek(0)
    return FileResponse(
        buffer, as_attachment=True, filename='shopping_list.pdf'
    )
