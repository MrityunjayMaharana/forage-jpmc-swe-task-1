import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        # Add assertions to check if the getDataPoint function returns the correct values
        for quote in quotes:
            stock = quote['stock']
            top_bid_price = quote['top_bid']['price']
            top_ask_price = quote['top_ask']['price']
            avg_price = (top_bid_price + top_ask_price) / 2
            self.assertEqual(getDataPoint(quote), (stock, top_bid_price, top_ask_price, avg_price))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Add assertions to check if the getDataPoint function returns the correct values
        for quote in quotes:
            stock = quote['stock']
            top_bid_price = quote['top_bid']['price']
            top_ask_price = quote['top_ask']['price']
            avg_price = (top_bid_price + top_ask_price) / 2
            self.assertEqual(getDataPoint(quote), (stock, top_bid_price, top_ask_price, avg_price))

if __name__ == '__main__':
    unittest.main()

