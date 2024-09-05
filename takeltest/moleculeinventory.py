import ansible_runner


class MoleculeInventory(object):

    def __init__(
            self,
            inventory_file):

        out, err = ansible_runner.get_inventory(
            action='list',
            inventories=[str(inventory_file)],
            response_format='json'
        )
        try:
            self._hosts = out['private']['hosts']
        except (KeyError):
            self._hosts = ['localhost']


    def get(self):
        return self._inventory

    def hosts(self):
        return self._hosts
