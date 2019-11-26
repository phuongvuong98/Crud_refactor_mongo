from flask_mongoengine import Pagination
from app.entity.mongo.product import Product as ProductEntity
from app.search import query_index
from constants import Pages, Errors


class ProductModel(ProductEntity):
    objects = ProductEntity.objects

    def query_all(self):
        return self.objects

    def query_paginate(self, page):
        products = Pagination(self.objects, int(page), int(Pages['NUMBER_PER_PAGE']))
        return products.items, products.pages, products.page

    def find(self, name):
        return self.objects(name__exact=name)

    def get_name_by_id(self, product_id):
        return self.objects.get(id=product_id).name

    def edit(self, _id, category_id, name):
        try:
            self.objects(id__exact=_id).update(set__name=name, set__category_id=category_id)
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def create(cls, category_id, name):
        try:
            if not category_id or not name:
                return False, Errors.ERROR_EXIST.value
            ProductEntity(name=name, category_id=category_id).save()
            ProductEntity.reindex()
            return True, None
        except Exception as e:
            return False, e.__str__()

    @classmethod
    def search(cls, expression, page, per_page):
        ids, obj = query_index(cls.__tablename__, expression, page, per_page)
        ids = [str(_id) for _id in ids]
        if len(obj) == 0:
            return cls.objects(id__exact=0), 0
        arr_model = []
        for _id in ids:
            try:
                arr_model.append(cls.objects.get(id=_id))
            except Exception as e:
                continue
        return arr_model, obj

    def get_value(self):
        return self.name
