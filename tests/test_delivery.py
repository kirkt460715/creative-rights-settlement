"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        products = read_table("composition.json")
        bills = read_table("bills.json")
        rights = read_table("licenses.json")
        self.assertTrue({r["parent"] for r in rights if r["parent"]} <= {r["license"] for r in rights})
        self.assertTrue({r["sku"] for r in bills} <= {r["sku"] for r in products})
        affected = {r["line"] for r in read_table("disputes.json")} & {r["original"] for r in read_table("refunds.json")}
        self.assertTrue(affected & {r["line"] for r in read_table("issued.json")})
