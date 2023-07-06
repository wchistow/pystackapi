# ToDo

 + [X] fix type of `**kwargs` argument in method `Site.get`. Now it's `dict[str, Any]`, but have to be only `Any`;
 + [X] remove argument `api_key` of method `Site.__init__` and add `access_token` and `app_key` arguments to it. Also, add  usage of these arguments to method `Site.get`;
 + [X] sort constants in file `src/pystackapi/sites.py` by alphabet order;
 + [X] change type of return value in method `Site.get` and, also in `Site.get_*` from `dict` to subclass of `typing.TypedDict`;
 + [ ] add more examples to directory `examples/`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
