



class TestMobile:
    def test_bstack_android(self, browser):
        mobile_page.courier_login()
        mobile_page.scroll_to_faq()
        mobile_page.get_question(1)
        mobile_page.get_answers(1)
