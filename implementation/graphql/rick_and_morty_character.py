import requests


class RMCharactersGql:
    base_url = 'https://rickandmortyapi.com/graphql'

    def post_query(self, query):
        response = requests.post(self.base_url, json={'query': query})
        return response
