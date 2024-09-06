class MultiTestVars(object):
    '''Expose ansible variabless of a molecule scenario.

    Include ansible facts form molecule host.
    Include roles from ansible project directory.
    Resolve jinja2 template variables.
    '''

    def __init__(
            self,
            moleculeinventory,
            moleculebook):

        # this variable will be returned by the multitestvars fixture
        self._multitestvars = dict()

        for ansiblehost in moleculeinventory.hosts():
            host = str(ansiblehost)
            vars = moleculebook.get_vars(host)
            self._multitestvars[host] = vars

    def get_multitestvars(self):
        return self._multitestvars

    def get_cache(request, cache_key):
        try:
            # read testvars from cache
            # you can enable cache support in molecule.yml:
            # molecule -> verifier -> options
            # option "p: cacheprovider"
            multitestvars = request.config.cache.get(cache_key, None)
        except AttributeError:
            multitestvars = None
        return multitestvars

    def set_cache(self, request, cache_key):
        try:
            request.config.cache.set(cache_key, self._testvars)
        except AttributeError:
            pass
