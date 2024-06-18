import requests


class RMCharacters:
    base_url = 'https://rickandmortyapi.com/api/character/'

    def _validate_params(*args, **kwargs):
        params = {}
        for k in kwargs:
            params[k] = kwargs.get(k)
        return params

    def get_all(self, page=None):
        params = self._validate_params(page=page)
        response = requests.get(self.base_url, params=params)
        return response

    def get_by_id(self, ids, page=None):
        if isinstance(ids, tuple):
            ids_url = ','.join(ids)
        else:
            ids_url = ids
        complete_url = f'{self.base_url}{ids_url}/'
        params = self._validate_params(page=page)
        response = requests.get(complete_url, params=params)
        return response

    def get_filtered(self, name=None, status=None, species=None, type=None, gender=None, page=None):
        params = self._validate_params(name=name, status=status, species=species, type=type, gender=gender, page=page)
        response = requests.get(self.base_url, params=params)
        return response
