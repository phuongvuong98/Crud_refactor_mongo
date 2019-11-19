Feature: Test all function of /city

  Scenario Outline: Open a table, then create city
    Given When get into "city" page with blank list and click the create button.
    When When redirected to create window, at "cityName" form, i type in <cityName> and click on button with css ".btn.btn-primary"
    Then When redirected back to list window, i should see <cityName>

    Examples:
      | cityName      |
      | Quy Nhon      |
      | Binh Dinh     |
      | Ho Chi Minh   |
      | Da Nang       |
      | Ha Noi        |
      | Hong Kong     |
      | BangKok       |
      | Singapore     |
      | Kualar Lumpur |
      | New York      |
      | California    |
      | Paris         |
      | Rome          |

  Scenario Outline: Given a table with datas, create duplicate data
    Given When get into "city" page with blank list and click the create button.
    When When redirected to create window, at "cityName" form, i type in <cityName> and click on button with css ".btn.btn-primary"
    Then We should not be able to create city.

    Examples:
      | cityName    |
      | Quy Nhon    |
      | Da Nang     |
      | Ho Chi Minh |
      | California  |
      | Rome        |

  Scenario: Open website and edit city
    Given I open city
    Then I click edit the first city
    Then I edit this city and submit form