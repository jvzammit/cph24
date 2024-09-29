import pytest
from httpx import ASGITransport, AsyncClient

from backend.main import app


class override_dependency:
    """
    Override a dependency in a test. Deletes the override on exit.
    """

    def __init__(self, dependency, fake_dependency):
        self.dependency = dependency
        self.fake_dependency = fake_dependency

    def __enter__(self):
        app.dependency_overrides[self.dependency] = self.fake_dependency

    def __exit__(self, *args):
        del app.dependency_overrides[self.dependency]


transport = ASGITransport(app=app)


@pytest.fixture
async def client():
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
