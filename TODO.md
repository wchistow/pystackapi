# ToDo

 + [ ] add more examples to directory `examples/`;
 + [ ] add methods, that requires authentication (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [X] `get_me(self, **kwargs: Any) -> Item` - API method `me`;
   + [X] `get_my_full_reputation_history(self, **kwargs: Any) -> list[Item]` - API method `me/reputation-history/full`;
   + [ ] `get_my_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox`;
   + [X] `get_my_unread_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox/unread`;
 + [ ] add methods with POST-requests (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [ ] `edit_answer(self, a_id: int, body: str, **kwargs: Any) -> Item` - API method `answers/{id}/edit`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
