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

        self._hosts = []
        host_groups = []

        try:
            for host_group in out['all']['children']:
                host_groups.append(host_group)
        except (IndexError, KeyError):
            pass

        for host_group in host_groups:
            try:
                for host in out[host_group]['hosts']:
                    self._hosts.append(host)
            except (IndexError, KeyError):
                continue

        if not self._hosts:
            self._hosts = ['localhost']

    def get(self):
        return self._inventory

    def hosts(self):
        return self._hosts
