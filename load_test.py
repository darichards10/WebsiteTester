from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def task_0(self):
        self.client.get('https://apple.com/sitemap/')

    @task
    def task_1(self):
        self.client.get('https://apple.com/us/shop/back-to-school/terms-conditions')

    @task
    def task_2(self):
        self.client.get('https://apple.com/ipad-pro/')

    @task
    def task_3(self):
        self.client.get('https://apple.com/education/')

    @task
    def task_4(self):
        self.client.get('https://apple.com/tv-home/')

    @task
    def task_5(self):
        self.client.get('https://apple.com/iphone-14-pro/')

    @task
    def task_6(self):
        self.client.get('https://apple.com/compliance/')

    @task
    def task_7(self):
        self.client.get('https://apple.com/accessibility/')

    @task
    def task_8(self):
        self.client.get('https://apple.com/apple-fitness-plus/')

    @task
    def task_9(self):
        self.client.get('https://apple.com/apple-pay/')

    @task
    def task_10(self):
        self.client.get('https://apple.com/r/store/government/')

    @task
    def task_11(self):
        self.client.get('https://apple.com/legal/privacy/')

    @task
    def task_12(self):
        self.client.get('https://apple.com/us/shop/goto/trade_in')

    @task
    def task_13(self):
        self.client.get('https://apple.com/contact/')

    @task
    def task_14(self):
        self.client.get('https://apple.com#footnote-1')

    @task
    def task_15(self):
        self.client.get('https://apple.com/apple-arcade/')

    @task
    def task_16(self):
        self.client.get('https://apple.com/us/shop/goto/order/list')

    @task
    def task_17(self):
        self.client.get('https://apple.com/us/shop/goto/product/MQD83')

    @task
    def task_18(self):
        self.client.get('https://apple.com/wallet/')

    @task
    def task_19(self):
        self.client.get('https://apple.com/legal/')

    @task
    def task_20(self):
        self.client.get('https://apple.com/supplier-responsibility/')

    @task
    def task_21(self):
        self.client.get('https://apple.com/us/shop/goto/special_deals')

    @task
    def task_22(self):
        self.client.get('https://apple.com/apple-news/')

    @task
    def task_23(self):
        self.client.get('https://apple.com/us/shop/goto/account')

    @task
    def task_24(self):
        self.client.get('https://apple.com/us/search')

    @task
    def task_25(self):
        self.client.get('https://apple.com/racial-equity-justice-initiative/')

    @task
    def task_26(self):
        self.client.get('https://apple.com/mac/')

    @task
    def task_27(self):
        self.client.get('https://apple.com/apple-one/')

    @task
    def task_28(self):
        self.client.get('https://apple.com/apple-events/')

    @task
    def task_29(self):
        self.client.get('https://apple.com/apple-watch-series-8/')

    @task
    def task_30(self):
        self.client.get('https://apple.com/healthcare/')

    @task
    def task_31(self):
        self.client.get('https://apple.com/us/shop/goto/bag')

    @task
    def task_32(self):
        self.client.get('https://apple.com/privacy/')

    @task
    def task_33(self):
        self.client.get('https://apple.com/airpods/')

    @task
    def task_34(self):
        self.client.get('https://apple.com/legal/internet-services/terms/site.html')

    @task
    def task_35(self):
        self.client.get('https://apple.com/watch/')

    @task
    def task_36(self):
        self.client.get('https://apple.com/education/k12/how-to-buy/')

    @task
    def task_37(self):
        self.client.get('https://apple.com/apple-podcasts/')

    @task
    def task_38(self):
        self.client.get('https://apple.com/iphone/')

    @task
    def task_39(self):
        self.client.get('https://apple.com/us/shop/goto/buy_iphone/carrier_offers')

    @task
    def task_40(self):
        self.client.get('https://apple.com/airpods-pro/')

    @task
    def task_41(self):
        self.client.get('https://apple.com/us/shop/goto/buy_mac/macbook_air/15_inch_m2')

    @task
    def task_42(self):
        self.client.get('https://apple.com/apple-card/')

    @task
    def task_43(self):
        self.client.get('https://apple.com/us/shop/goto/buy_iphone/iphone_14')

    @task
    def task_44(self):
        self.client.get('https://apple.com/app-store/')

    @task
    def task_45(self):
        self.client.get('https://apple.com/retail/geniusbar/')

    @task
    def task_46(self):
        self.client.get('https://apple.com/careers/us/')

    @task
    def task_47(self):
        self.client.get('https://apple.com/us/shop/goto/ipad_pro/select')

    @task
    def task_48(self):
        self.client.get('https://apple.com/healthcare/health-records/')

    @task
    def task_49(self):
        self.client.get('https://apple.com/entertainment/')

    @task
    def task_50(self):
        self.client.get('https://apple.com/healthcare/apple-watch/')

    @task
    def task_51(self):
        self.client.get('https://apple.com/macbook-air-13-and-15-m2/')

    @task
    def task_52(self):
        self.client.get('https://apple.com/us/shop/goto/campaigns/tax_holiday')

    @task
    def task_53(self):
        self.client.get('https://apple.com/apple-tv-plus/')

    @task
    def task_54(self):
        self.client.get('https://apple.com/apple-books/')

    @task
    def task_55(self):
        self.client.get('https://apple.com/us/shop/goto/buy_watch/apple_watch_series_8')

    @task
    def task_56(self):
        self.client.get('https://apple.com/us/shop/goto/buy_accessories')

    @task
    def task_57(self):
        self.client.get('https://apple.com/choose-country-region/')

    @task
    def task_58(self):
        self.client.get('https://apple.com/airtag/')

    @task
    def task_59(self):
        self.client.get('https://apple.com/today/camp/')

    @task
    def task_60(self):
        self.client.get('https://apple.com/retail/business/')

    @task
    def task_61(self):
        self.client.get('https://apple.com/')

    @task
    def task_62(self):
        self.client.get('https://apple.com/apple-vision-pro/')

    @task
    def task_63(self):
        self.client.get('https://apple.com/us-hed/shop/back-to-school')

    @task
    def task_64(self):
        self.client.get('https://apple.com/apple-music/')

    @task
    def task_65(self):
        self.client.get('https://apple.com/us/shop/goto/help')

    @task
    def task_66(self):
        self.client.get('https://apple.com/ipad/')

    @task
    def task_67(self):
        self.client.get('https://apple.com/newsroom/')

    @task
    def task_68(self):
        self.client.get('https://apple.com')

    @task
    def task_69(self):
        self.client.get('https://apple.com/diversity/')

    @task
    def task_70(self):
        self.client.get('https://apple.com/education-initiative/')

    @task
    def task_71(self):
        self.client.get('https://apple.com/us/shop/goto/store')

    @task
    def task_72(self):
        self.client.get('https://apple.com/iphone-14/')

    @task
    def task_73(self):
        self.client.get('https://apple.com/us/shop/goto/educationrouting')

    @task
    def task_74(self):
        self.client.get('https://apple.com/retail/')

    @task
    def task_75(self):
        self.client.get('https://apple.com/business/')

    @task
    def task_76(self):
        self.client.get('https://apple.com/apple-cash/')

    @task
    def task_77(self):
        self.client.get('https://apple.com/us/shop/goto/payment_plan')

    @task
    def task_78(self):
        self.client.get('https://apple.com/us/shop/goto/help/sales_refunds')

    @task
    def task_79(self):
        self.client.get('https://apple.com/leadership/')

    @task
    def task_80(self):
        self.client.get('https://apple.com/today/')

    @task
    def task_81(self):
        self.client.get('https://apple.com/us/shop/goto/giftcards')

    @task
    def task_82(self):
        self.client.get('https://apple.com/environment/')

    @task
    def task_83(self):
        self.client.get('https://apple.com/us/shop/goto/buy_iphone/iphone_14_pro')

