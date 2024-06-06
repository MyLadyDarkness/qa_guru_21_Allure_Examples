import allure


@allure.id("32723")
@allure.title("Manual test case")
@allure.label("owner", "allure8")
def test_example_manual():
    with allure.step("Open issues page allure-framework/allure2"):
        pass
    with allure.step("Find any issue"):
        with allure.step("Issue about frontend"):
            pass
    with allure.step("Issue about api"):
        pass
    with allure.step("Edit record"):
        pass
    with allure.step("Save"):
        pass