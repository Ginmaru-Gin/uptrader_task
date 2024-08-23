from dataclasses import dataclass
from django import template

from ..models import MenuItem

register = template.Library()


@dataclass
class TreeItem:
    item: MenuItem
    children: list[MenuItem]

    def __str__(self):
        print(f"{self.item=}, {self.item.is_active=}")


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, title):

    request = context.get("request")
    items = MenuItem.objects.filter(menu__title=title).select_related("parent")

    menu_tree = {item.id: TreeItem(item, []) for item in items}
    menu_tree[0] = TreeItem(None, [])
    for item in items:
        parent_id = 0 if item.parent is None else item.parent.id
        menu_tree[parent_id].children.append(item.id)

    active_item_id = next((i.id for i in items if i.path == request.path), 0)
    while active_item_id != 0:
        menu_tree[active_item_id].item.is_active = True
        parent = menu_tree[active_item_id].item.parent
        if parent is None:
            break
        active_item_id = menu_tree[active_item_id].item.parent.id

    return {"title": title, "menu_tree": menu_tree}
