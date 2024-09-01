import ansible_runner
import json

class MoleculeInventory(object):

    def __init__(
            self,
            inventory_file):

        out, err = ansible_runner.get_inventory(
            action='list',
            inventories=[str(inventory_file)],
            response_format='json'
        )
        self._hosts = out['ungrouped']['hosts']

    def get(self):
        return self._inventory

    def hosts(self):
        return self._hosts
