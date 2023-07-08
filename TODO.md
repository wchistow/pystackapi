# ToDo

 + [X] fix type of `**kwargs` argument in method `Site.get`. Now it's `dict[str, Any]`, but have to be only `Any`;
 + [X] remove argument `api_key` of method `Site.__init__` and add `access_token` and `app_key` arguments to it. Also, add  usage of these arguments to method `Site.get`;
 + [X] sort constants in file `src/pystackapi/sites.py` by alphabet order;
 + [X] change type of return value in method `Site.get` and, also in `Site.get_*` from `dict` to subclass of `typing.TypedDict`;
 + [ ] add more examples to directory `examples/`;
 + [ ] add more site-level methods with following signatures (of course, each of these methods needs tests):
   + [X] `get_answers(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict` - API method `answers/` and `answers/{ids}`;
   + [ ] `get_articles(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict` - API method `articles/` and `answers/{ids}`;
   + [ ] `get_collectives(self, slugs: list[str] | None = None, **kwargs: Any) -> ResponseDict` - API method `collectives/` and `collectives/{slugs}`;
   + [ ] `get_comments(self, ids: list[int] | None = None, **kwargs: Any) -> ResponseDict` - API method `comments/` and `answers/{ids}`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
