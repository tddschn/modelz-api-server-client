from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_api_types_spend_limit import (
    GithubComTensorchordModelzApiserverApiTypesSpendLimit,
)
from ...types import Response


def _get_kwargs(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: GithubComTensorchordModelzApiserverApiTypesSpendLimit,
) -> Dict[str, Any]:
    url = "{}/users/{login_name}/settings/billing/spend_limit".format(client.base_url, login_name=login_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = GithubComTensorchordModelzApiserverApiTypesSpendLimit.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: GithubComTensorchordModelzApiserverApiTypesSpendLimit,
) -> Response[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (GithubComTensorchordModelzApiserverApiTypesSpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesSpendLimit]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: GithubComTensorchordModelzApiserverApiTypesSpendLimit,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (GithubComTensorchordModelzApiserverApiTypesSpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesSpendLimit
    """

    return sync_detailed(
        login_name=login_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: GithubComTensorchordModelzApiserverApiTypesSpendLimit,
) -> Response[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (GithubComTensorchordModelzApiserverApiTypesSpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesSpendLimit]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: GithubComTensorchordModelzApiserverApiTypesSpendLimit,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesSpendLimit]:
    """Create spend limit

     Create spend limit

    Args:
        login_name (str):
        json_body (GithubComTensorchordModelzApiserverApiTypesSpendLimit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesSpendLimit
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
