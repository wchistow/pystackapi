# ToDo

 + [X] fix type of `**kwargs` argument in method `Site.get`. Now it's `dict[str, Any]`, but have to be only `Any`;
 + [X] remove argument `api_key` of method `Site.__init__` and add `access_token` and `app_key` arguments to it. Also, add  usage of these arguments to method `Site.get`;
 + [X] sort constants in file `src/pystackapi/sites.py` by alphabet order;
 + [X] change type of return value in method `Site.get` and, also in `Site.get_*` from `dict` to subclass of `typing.TypedDict`;
 + [ ] add more examples to directory `examples/`;
 + [ ] add more site-level methods with following signatures (of course, each of these methods needs tests):
   + [X] `get_answers(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]` - API method `answers/` and `answers/{ids}`;
   + [X] `get_articles(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]` - API method `articles/` and `answers/{ids}`;
   + [X] `get_collectives(self, slugs: Iterable[str] | None = None, **kwargs: Any) -> list[Item]` - API method `collectives/` and `collectives/{slugs}`;
   + [X] `get_collective(self, slug: str, **kwargs: Any) -> Item`;
   + [X] `get_comments(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]` - API method `comments/` and `answers/{ids}`;
   + [X] `get_comment(self, c_id: int, **kwargs: Any) -> Item | None`;
   + [X] `get_privileges(self, **kwargs: Any) -> list[Item]` - API method `privileges/`;
   + [X] `get_tags(self, **kwargs: Any) -> list[Item]` - API method `tags/`;
   + [X] `get_badges(self, **kwargs: Any) -> list[Item]` - API method `badges/`;
   + [X] `get_revisions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `revisions/`;
   + [X] `get_posts(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]` - API method `posts/` and `posts/{ids}`;
   + [X] `get_post(self, c_id: int, **kwargs: Any) -> Item | None`;
   + [X] `get_suggested_edits(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]` - API method `suggested-edits/` and `suggested-edits/{ids}`;
   + [X] `get_comments_on_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `answers/{ids}/comments`;
   + [X] `get_comments_on_articles(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `articles/{ids}/comments`;
   + [X] `get_comments_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `posts/{ids}/comments`;
   + [X] `get_comments_on_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `questions/{ids}/comments`;
   + [X] `get_non_tag_based_badges(self, **kwargs: Any) -> list[Item]` - API method `badges/name`;
   + [X] `get_questions_on_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `answers/{ids}/questions`;
   + [X] `get_linked_in_articles(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `articles/{ids}/linked`;
   + [X] `get_questions_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]` - API method `collectives/{slugs}/questions`;
   + [X] `get_answers_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]` - API method `collectives/{slugs}/answers`;
   + [X] `get_tags_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]` - API method `collectives/{slugs}/tags`;
   + [ ] `get_users_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]` - API method `collectives/{slugs}/users`;
   + [ ] `get_revisions_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]` - API method `posts/{ids}/revisions`;
   + [ ] `get_suggested_edits_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[item]` - API method `posts/{ids}/suggested-edits`;
 + [X] `IndexError` raises in methods `Site.get_<singular>`, when there is no items in response;
 + [X] add constant `API_VERSION` to file `tests/test_client/__init__.py` and usage of it to tests.

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
