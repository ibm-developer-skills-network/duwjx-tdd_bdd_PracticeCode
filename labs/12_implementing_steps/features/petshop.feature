Feature: Search for pets by category

As a pet shop customer
I need to be able to search for a pet by category
So that I only see the category of the pet I am interested in buying

Background:
    Given the following pets
        | name       | category | available | gender  | birthday   |
        | Fido       | dog      | True      | MALE    | 2019-11-18 |
        | Kitty      | cat      | True      | FEMALE  | 2020-08-13 |
        | Leo        | lion     | False     | MALE    | 2021-04-01 |

Scenario: Search for dogs
    Given I am on the "Home Page"
    When I set the "Category" to "dog"
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Fido" in the results
    But I should not see "Kitty" in the results
    And I should not see "Leo" in the results
