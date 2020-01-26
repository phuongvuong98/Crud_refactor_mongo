from entity.category import Category


def cate_to_vi(category_link):
    return Category.objects(name_link__exact=category_link)[0].name_vi


def cate_to_link(category_vi):
    return Category.objects(name_vi__exact=category_vi)[0].name_link
