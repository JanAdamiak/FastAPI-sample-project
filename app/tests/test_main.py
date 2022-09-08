class TestSalesWebhook:
    def test_read_main(self, client):
        response = client.post(
            "/v1/sales-webhook",
            headers={"X-Token": "coneofsilence"},
            json={"regional_office": 2, "external_order_number": "y3827vy5tn8724ytcn9842nyt98", "car_model": "Corolla", "brand": "Toyota"},
        )

        assert response.status_code == 200
        print('-------------------------')
        print('-------------------------')
        print(response.json())
        print('-------------------------')
        print('-------------------------')
        print('-------------------------')
        assert False


# class TestUpdateStateWebhook:
#     def test_getting_stuff(self, test_client):
#         print(test_client)
#         assert False
