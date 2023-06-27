from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_pkg_query_template import (
    GithubComTensorchordModelzApiserverPkgQueryTemplate,
)
from ...types import Response


def _get_kwargs(
    login_name: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/users/{login_name}/templates/{id}".format(client.base_url, login_name=login_name, id=id)

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
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GithubComTensorchordModelzApiserverPkgQueryTemplate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Get the template.

     Get the template.

    Args:
        login_name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Get the template.

     Get the template.

    Args:
        login_name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverPkgQueryTemplate
    """

    return sync_detailed(
        login_name=login_name,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Get the template.

     Get the template.

    Args:
        login_name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Get the template.

     Get the template.

    Args:
        login_name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverPkgQueryTemplate
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            id=id,
            client=client,
        )
    ).parsed
