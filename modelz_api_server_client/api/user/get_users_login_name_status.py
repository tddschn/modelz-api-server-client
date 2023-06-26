from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_api_types_user_status import (
    GithubComTensorchordModelzApiserverApiTypesUserStatus,
)
from ...types import Response


def _get_kwargs(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/users/{login_name}/status".format(client.base_url, login_name=login_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GithubComTensorchordModelzApiserverApiTypesUserStatus.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
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
) -> Response[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
    """Get the user status.

     Get the user status.

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesUserStatus]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        client=client,
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
) -> Optional[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
    """Get the user status.

     Get the user status.

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesUserStatus
    """

    return sync_detailed(
        login_name=login_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
    """Get the user status.

     Get the user status.

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesUserStatus]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesUserStatus]:
    """Get the user status.

     Get the user status.

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesUserStatus
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            client=client,
        )
    ).parsed
