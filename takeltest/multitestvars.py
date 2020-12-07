import json


class MultiTestVars(object):
    '''Expose ansible variabless of a molecule scenario.

    Include ansible facts form molecule host.
    Include roles from ansible project directory.
    Resolve jinja2 template variables.
    '''

    def __init__(
            self,
            ansibleinventory,
            moleculelog,
            debug_jsonvars,
            moleculebook,
            jsonvars,
            gather_facts,
            extra_vars):

        # this variable will be returned by the multitestvars fixture
        self._multitestvars = dict()

        for ansiblehost in ansibleinventory.hosts:
            host = str(ansiblehost)

            # get ansible variables
            testvars_unresolved = moleculebook.get_vars(
                gather_facts,
                extra_vars,
                host)

            # convert python variables to json
            testvars_unresolved_json = json.dumps(testvars_unresolved)

            # set jsonvars to unresolved testvars
            jsonvars.set(testvars_unresolved_json)

            # resolve unresolved json testvars
            jsonvars.resolve()

            # print jsonvars debug info if command line flag is specified
            if debug_jsonvars:
                moleculelog.debug(jsonvars.get_debug())

            # get resolved testvars from jsonvars
            testvars_resolved_json = jsonvars.get()

            # convert json vars to python
            testvars = json.loads(testvars_resolved_json)

            # save testvars
            self._multitestvars[host] = testvars

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
