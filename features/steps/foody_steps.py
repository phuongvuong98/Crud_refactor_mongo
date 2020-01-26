from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from entity.foody import Foody
from entity.category import Category
import time

from features.utils.util import cate_to_vi


@given('Login by username and password.')
def login_foody(context):
    context.browser.close()

    context.browser = webdriver.Firefox()

    context.browser.get("https://id.foody.vn/account/login")

    context.browser.find_element_by_id("Email").send_keys("phuongvuong98@gmail.com")
    context.browser.find_element_by_id("Password").send_keys("Vuong0935986100")

    context.browser.find_element_by_id("bt_submit").click()


@when(u'Search into Ho Chi Minh with {category_link}')
def search_ho_chi_minh(context, category_link):

    context.browser.get("https://www.foody.vn/ho-chi-minh/food/" + category_link)
    time.sleep(3)

    context.browser.find_element_by_class_name("fd-btn-login-new").click()
    time.sleep(2)

    store_lst = []
    queue_check_heigh = []

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = context.browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = context.browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        # remove banner agency
        # element = context.browser.find_element_by_id("catfish-banner")
        # context.browser.execute_script("arguments[0].setAttribute('style','display:none;')", element)

        context.browser.find_element_by_class_name("fa-times").click()

    except:
        pass

    while True:
        print("Prepare click")

        try:
            context.browser.find_element_by_partial_link_text('Xem tiếp').click()
        except:
            pass
        while True:
            # Scroll down to bottom
            context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = context.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        height = context.browser.execute_script("return document.documentElement.scrollHeight")
        queue_check_heigh.append(height)
        print('Height:', height)

        if queue_check_heigh.count(height) == 3:
            break

        try:
            check = context.browser.find_element_by_partial_link_text('Xem tiếp')
        except NoSuchElementException:
            print("End game")
            break

        context.browser.execute_script("window.scrollTo(0, " + str(height - 1500) + ");")


        if int(int(height) / 50000) % 2 == 0:
            items = context.browser.find_elements_by_class_name('filter-result-item')
            for i in range(0, len(items) - 6):
                try:
                    if items[i].find_element_by_tag_name('h2'):
                        name = items[i].find_element_by_tag_name('h2').text
                        link = items[i].find_element_by_tag_name('a').get_attribute('href')
                        address = items[i].find_element_by_class_name('address').text
                        address = address[:-1] if address[len(address) - 1] == ',' else address
                        system = "0"
                        # if store is system -> save system = 1
                        if address.find("chi nhánh") != -1:
                            system = "1"
                        str_store = name + '|' + link + '|' + address + '|' + system
                        store_lst.append(str_store)
                except:
                    continue

            obj_store = set(store_lst)

            print(obj_store)
            print(len(obj_store))

            for item in obj_store:
                name = item.split("|")[0]
                link_foody = item.split("|")[1]
                address = item.split("|")[2]
                system = item.split("|")[3]

                if len(Foody.objects(name__exact=name)) == 0:
                    store = Foody(name=name, link_foody=link_foody, address=address, system=system)
                    cate = Category.objects(name_link__exact=category_link)[0]
                    store.categories = [cate.name_vi]
                    store.save()
                else:
                    stores = Foody.objects(name__exact=name)
                    cate = Category.objects(name_link__exact=category_link)[0]
                    category_vi = cate.name_vi
                    for store in stores:
                        if category_vi not in store.categories:
                            category_lst = store.categories
                            category_lst.append(category_vi)
                            store.categories = category_lst
                            store.save()

    items = context.browser.find_elements_by_class_name('filter-result-item')
    for i in range(0, len(items) - 6):
        try:
            if items[i].find_element_by_tag_name('h2'):
                name = items[i].find_element_by_tag_name('h2').text
                link = items[i].find_element_by_tag_name('a').get_attribute('href')
                address = items[i].find_element_by_class_name('address').text
                address = address[:-1] if address[len(address) - 1] == ',' else address
                system = "0"
                # if store is system -> save system = 1
                if address.find("chi nhánh") != -1:
                    system = "1"
                str_store = name + '|' + link + '|' + address + '|' + system
                store_lst.append(str_store)
        except:
            continue

    time.sleep(7)

    obj_store = set(store_lst)

    print(obj_store)
    print(len(obj_store))

    for item in obj_store:
        name = item.split("|")[0]
        link_foody = item.split("|")[1]
        address = item.split("|")[2]
        system = item.split("|")[3]

        if len(Foody.objects(name__exact=name)) == 0:
            store = Foody(name=name, link_foody=link_foody, address=address, system=system)
            cate = Category.objects(name_link__exact=category_link)[0]
            store.categories = [cate.name_vi]
            store.save()
        else:
            stores = Foody.objects(name__exact=name)
            cate = Category.objects(name_link__exact=category_link)[0]
            category_vi = cate.name_vi
            for store in stores:
                if category_vi not in store.categories:
                    category_lst = store.categories
                    category_lst.append(category_vi)

                    store.categories = category_lst
                    store.save()


@when(u'Handle each system store with {category_link}')
def handle_system_store(context, category_link):
    store_list = []
    category_vi = cate_to_vi(category_link)
    for item in Foody.objects:
        if item.system == "1" and category_vi in item.categories:
            print(item.name)
            context.browser.get(item.link_foody)
            items = context.browser.find_elements_by_class_name('ldc-item')

            for i in range(0, len(items)):
                try:
                    if items[i].find_element_by_tag_name('h2'):
                        print(items[i].find_element_by_tag_name('h2').text)

                        name = items[i].find_element_by_tag_name('h2').text
                        link = items[i].find_element_by_tag_name('a').get_attribute('href')
                        address = items[i].find_element_by_class_name('ldc-item-h-address').text
                        address = address[:-1] if address[len(address) - 1] == ',' else address
                        system = "0"
                        str_store = name + '|' + link + '|' + address + '|' + system
                        store_list.append(str_store)
                except:
                    continue

            obj_store = set(store_list)
            print(len(obj_store))

            for y in obj_store:
                print(y)
                name = y.split("|")[0]
                link_foody = y.split("|")[1]
                address = y.split("|")[2]
                system = y.split("|")[3]

                if len(Foody.objects(name__exact=name)) == 0:
                    print(name)
                    store = Foody(name=name, link_foody=link_foody, address=address, system=system)
                    cate = Category.objects(name_link__exact=category_link)[0]
                    store.categories = [cate.name_vi]
                    store.save()

            Foody.objects(name=item.name).delete()


@when(u'Handle price each store with {category_link}')
def handle_price(context, category_link):
    category_vi = cate_to_vi(category_link)
    for item in Foody.objects:
        if item.system == "0" and category_vi in item.categories:
            if not item.min_price:
                print(item.name)
                context.browser.get(item.link_foody)
                time.sleep(0.5)
                price = context.browser.find_element_by_class_name('res-common-minmaxprice').text
                if "Đang cập nhật" in price:
                    Foody.objects(name=item.name).delete()
                    continue

                str_price = price.replace("đ", "").replace(" ", "").replace(".", "")
                min_price = str_price.split("-")[0]
                max_price = str_price.split("-")[1]
                Foody.objects(id__exact=item.id).update(set__min_price=min_price)
                Foody.objects(id__exact=item.id).update(set__max_price=max_price)


@when(u'Open google maps')
def open_gg(context):
    context.browser.get("https://www.google.com/maps")


@when(u'Save link with {category_link}')
def save_link_gg(context, category_link):
    test_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
    test_input.send_keys(Foody.objects[0].name)
    test_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
    test_btn.click()
    time.sleep(3)

    for item in Foody.objects:
        category_vi = cate_to_vi(category_link)
        if not item.link_gg and category_vi in item.categories:

            # search by name + address
            print(item.name.split("-")[0])

            search_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
            search_input.clear()
            search_input.send_keys(item.name.split("-")[0] + " " + category_vi + " " + item.address)

            search_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
            search_btn.click()

            time.sleep(3)

            print(context.browser.current_url)
            link_gg = "no_n_a" if context.browser.current_url.find("/maps/place/") == -1 else context.browser.current_url

            print(Foody.objects(link_gg__exact=link_gg))

            # search by name
            if link_gg == "no_n_a":
                search_input = context.browser.find_element_by_class_name("tactile-searchbox-input")
                search_input.clear()
                search_input.send_keys(category_vi + " " + item.name.split("-")[0] + " TP Hồ Chí Minh")

                search_btn = context.browser.find_element_by_class_name("searchbox-searchbutton")
                search_btn.click()

                time.sleep(3)

            print(context.browser.current_url)
            link_gg = "no_n" if context.browser.current_url.find(
                "/maps/place/") == -1 else context.browser.current_url

            if Foody.objects(link_gg__exact=link_gg):
                link_gg = "dup"

            location = {"lat": 0, "long": 0}
            # handle link_gg into lat and long
            if link_gg.find("https://www.google.com/maps/place/") != -1:
                print("Link_gg:", link_gg)
                idx_1 = link_gg.find("/@")
                idx_2 = link_gg.find("z/data=")

                sub_link = link_gg[idx_1:idx_2]
                print("Sub:", sub_link)
                lat = sub_link.split(",")[0][2:]
                long = sub_link.split(",")[1]
                location = {"lat": lat, "long": long}

            Foody.objects(id__exact=item.id).update(set__link_gg=link_gg, set__location=location)


# @when(u'Handle google api with {category}')
# def handle_google_api(context, category):
#     for item in Foody.objects:
#         crawl_by_name(item.name, category, item.price, item.address)
