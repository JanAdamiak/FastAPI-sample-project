# class TestSalesWebhook:
#     def test_read_main(self, client):
#         response = client.post(
#             "/v1/sales-webhook",
#             json={"regional_office": 2, "external_order_number": "y3827vy5tn8724ytcn9842nyt98", "car_model": "Corolla", "brand": "Toyota"},
#         )

#         assert response.status_code == 200
#         assert response.json() == {"regional_office": 2, "external_order_number": "y3827vy5tn8724ytcn9842nyt98", "car_model": "Corolla", "brand": "Toyota"}


# class TestUpdateStateWebhook:
#     def test_getting_stuff(self, test_client):
#         print(test_client)
#         assert False
