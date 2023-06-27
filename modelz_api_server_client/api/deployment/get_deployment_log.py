from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_api_types_deployment_log_response import (
    GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{login_name}/deployments/{name}/logs".format(client.base_url, login_name=login_name, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["since"] = since

    params["end"] = end

    params["tail"] = tail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        name (str):
        since (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
        client=client,
        since=since,
        end=end,
        tail=tail,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        name (str):
        since (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse
    """

    return sync_detailed(
        login_name=login_name,
        name=name,
        client=client,
        since=since,
        end=end,
        tail=tail,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        name (str):
        since (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
        client=client,
        since=since,
        end=end,
        tail=tail,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        name (str):
        since (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesDeploymentLogResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            name=name,
            client=client,
            since=since,
            end=end,
            tail=tail,
        )
    ).parsed
