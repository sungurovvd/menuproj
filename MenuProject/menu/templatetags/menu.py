from django import template
from ..models import Item
from django.urls import resolve, reverse


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    cur_url= context['request'].path

    try:
        named_url = resolve(cur_url)
        name = named_url.url_name
    except:
        name = ''

    data = Item.objects.filter(menu_name=menu_name).values('id', 'text', 'url', 'parent')
    keys = ('id', 'text', 'url', 'parent')
    values = data.values_list(*keys)
    results = [dict(zip(keys, row)) for row in values]

    cur_item = {}
    for dictionary in results:
        if dictionary['url'] == cur_url or dictionary['url'] == name:
            if dictionary['url'][0] != '/':
                dictionary['url'] = reverse(dictionary['url'])
            cur_item = dictionary
    same_level = []

    for dictionary in results:
        if dictionary['parent'] == cur_item['parent'] and dictionary['id'] != cur_item['id']:
            if dictionary['url'][0] != '/':
                dictionary['url'] = reverse(dictionary['url'])
            same_level.append(dictionary)



    children = []
    for dictionary in results:
        if dictionary['parent'] == cur_item['id']:
            if dictionary['url'][0] != '/':
                dictionary['url'] = reverse(dictionary['url'])
            children.append(dictionary)

    parents = []
    find = cur_item['parent']

    while find is not None:
        for dictionary in results:
            if dictionary['id'] == find:
                if dictionary['url'][0] != '/':
                    dictionary['url'] = reverse(dictionary['url'])
                parents.insert(0, dictionary)
                find = dictionary['parent']
                break

    return {'parents': parents, 'current': cur_item, 'children': children, 'same': same_level}
