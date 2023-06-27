from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_api_types_metric_response import (
    GithubComTensorchordModelzApiserverApiTypesMetricResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
    step: str,
) -> Dict[str, Any]:
    url = "{}/users/{login_name}/deployments/{name}/metrics/total_requests".format(
        client.base_url, login_name=login_name, name=name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

    params["step"] = step

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
) -> Optional[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GithubComTensorchordModelzApiserverApiTypesMetricResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
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
    start: str,
    end: str,
    step: str,
) -> Response[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
    """Get the deployment total requests metrics.

     Get the deployment total requests metrics with the given deployment name.

    Args:
        login_name (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesMetricResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
        client=client,
        start=start,
        end=end,
        step=step,
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
    start: str,
    end: str,
    step: str,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
    """Get the deployment total requests metrics.

     Get the deployment total requests metrics with the given deployment name.

    Args:
        login_name (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesMetricResponse
    """

    return sync_detailed(
        login_name=login_name,
        name=name,
        client=client,
        start=start,
        end=end,
        step=step,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
    step: str,
) -> Response[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
    """Get the deployment total requests metrics.

     Get the deployment total requests metrics with the given deployment name.

    Args:
        login_name (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverApiTypesMetricResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
        client=client,
        start=start,
        end=end,
        step=step,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
    step: str,
) -> Optional[GithubComTensorchordModelzApiserverApiTypesMetricResponse]:
    """Get the deployment total requests metrics.

     Get the deployment total requests metrics with the given deployment name.

    Args:
        login_name (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverApiTypesMetricResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            name=name,
            client=client,
            start=start,
            end=end,
            step=step,
        )
    ).parsed
