from typing import Any


class Response:
    """
    Implements result of method `Client.call`.

    Usage:

    ```py
    cl = pystackapi.Client(pystackapi.sites.StackOverflow)
    res = cl.call('info/')
    print(res.total_questions)  # prints: `23730861`.
    ```

    Use getitem notation, if key isn't valid Python identifier:

    ```
    print(res['total_questions'])  # prints: `23730861`.
    ```
    """
    def __init__(self, data: dict) -> None:
        self.__data = data['items'][0]
        self.response_info = {k: v for k, v in data.items() if k != 'items'}

    def __iter__(self):
        return ((k, v) for k, v in self.__data.items())

    def __repr__(self) -> str:
        return f'<Response object with {len(self.__data.keys())} keys>'

    def __getattr__(self, name: Any) -> Any:
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return self.__data[name]

    def __getitem__(self, item: Any) -> Any:
        return self.__data[item]
