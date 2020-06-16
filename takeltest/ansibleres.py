from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader


class AnsibleInventory(object):

    def __init__(
            self,
            inventoryfile):
        self._inventory = InventoryManager(
            loader=DataLoader(),
            sources=str(inventoryfile))

    def get(self):
        return self._inventory
