Feature: Login and get data foody

  Scenario Outline: Open foody login and scraping data
#    Given Login by username and password.
#    When Search into Ho Chi Minh with <category_link>
#    When Handle each system store with <category_link>
    When Handle price each store with <category_link>
    When Open google maps
    When Save link with <category_link>
#    When Handle google api with <category>

    Examples:
      | category_link   |
#      | sang-trong |
#      | buffet     |
#      | nha-hang   |
#      | an-vat-via-he      |
#      | an-chay            |
#      | cafe               |
#      | quan-an            |
#      | quan-nhau          |
#      | beer-club          |
#      | tiem-banh          |
#      | tiec-tan-noi       |
#      | shop-online        |
#      | giao-com-van-phong |
      | foodcourt          |



#  1. Doi ten cate
#["Sang trọng", "Nhà hàng", "Beer club", "Buffet", "Tiệm bánh",
#    "Café/Dessert", "Ăn vặt/Vỉa hè", "Khu ẩm thực", "Shop Online", "Quán nhậu",
#    "Tiệc tận nơi", "Ăn chay", "Giao cơm văn phòng", "Quán ăn"];
#  2. Tach min price, max price
#    3. Doi dau , thanh .
#    4. price la kieu int