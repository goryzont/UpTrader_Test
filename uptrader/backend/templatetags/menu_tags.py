from django import template
from backend.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    # Кастомный тег для отрисовки меню.

    menu = MenuItem.objects.get(name=menu_name)

    def render_menu(menu_item):
        # Рекурсивная функция для отрисовки меню.

        # html = f'''<ul><li><a href="{ menu_item.url}">{menu_item.name}</a>'''
        html = '''<ul><li><a href="''' + '''{% url 'menu' %}" ''' + f'''>{menu_item.name}</a>'''
        if menu_item.children.all():
            html += '<ul>'
            for child in menu_item.children.all():
                html += render_menu(child)
            html += '</ul>'
        html += '</li></ul>'
        return html

    return render_menu(menu)


@register.simple_tag
def test_menu():
    html = '''<ul>Меню
            <li>блюдо1</li>
            <li>блюдо2</li>
            <li>блюдо3</li>
            </ul>'''
    return html
