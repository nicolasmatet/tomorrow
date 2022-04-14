import importlib

from api.api_v1.dynamodb.boto_default import get_default_ressource


def execute_fixtures(db=None):
    fixture_module = importlib.import_module('fixtures')
    if db is None:
        db = get_default_ressource()
    for fixture_name in fixture_module.__all__:
        fixture = getattr(fixture_module, fixture_name)
        for pk, value in enumerate(fixture.values):
            fixture.model.write({"id": pk, "type": 1, **value}, db)
