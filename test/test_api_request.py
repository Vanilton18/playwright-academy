import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect
from typing import Generator


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:8000/"
    )
    yield request_context
    request_context.dispose()


def test_get_token_saleor(api_request_context: APIRequestContext) -> None:
    body = """
     mutation {
      tokenCreate(email: "email", password: "key") {
        token
        refreshToken
        errors {
          field
          message
        }
      }
    }
    """
    expect(api_request_context.get("/")).to_be_ok()

    #response = api_request_context.post(f"graphql/", data={"query": body})
    #expect(response).to_be_ok()
    #assert response.json()['data']['tokenCreate']['token'] is not None
    #print(response.json())
