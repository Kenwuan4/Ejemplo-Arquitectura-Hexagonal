from adapters.RickMortyAPI_Adapter import Rick_Adapter


rick_adapter = Rick_Adapter("Rick")


def get_caracter(page):
    return rick_adapter.get_characters_info(page=page)
