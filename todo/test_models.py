from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestItemModel(TestCase):
    
    
    def test_done_defaults_to_false(self):
        item = Item(name="Create a test. ")
        item.save()
        self.assertEqual(item.name, "Create a test. ")
        self.assertEqual(item.done, False)
        
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create a test. ", done=True)
        item.save()
        self.assertEqual(item.name, "Create a test. ")
        self.assertTrue(item.done)
        
        
    def test_item_as_a_string(self):
        item = Item(name="Create a test. ")
        self.assertEqual(item.name, str(item))
        
        
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        
        
    def test_post_edit_an_item(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id
        
        response = self.client.post("/edit/{0}".format(id), {"name": "a different name"})
        item = get_object_or_404(Item, pk=1)
        
        self.assertEqual("a different name", item.name)
        
        
    def test_toggle_status(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id
        
        response = self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)