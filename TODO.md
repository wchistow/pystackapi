# ToDo

 + [ ] add more examples to directory `examples/`;
 + [ ] add methods, that requires authentication (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [X] `get_me(self, **kwargs: Any) -> Item` - API method `me`;
   + [X] `get_my_full_reputation_history(self, **kwargs: Any) -> list[Item]` - API method `me/reputation-history/full`;
   + [X] `get_my_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox`;
   + [X] `get_my_unread_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox/unread`;
   + [ ] `get_unanswered_questions_on_my_tags(self, **kwargs: Any) -> list[Item]` - API method `questions/unanswered/my-tags`;
 + [ ] add methods with POST-requests (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [ ] `add_answer(self, q_id: int, body: str, **kwargs: Any) -> Item` - API method `answers/add`;
   + [ ] `add_comment(self, post_id: int, body: str, **kwargs: Any) -> Item` - API method `posts/{id}/comments/add`;
   + [ ] `add_question(self, title: str, body: str, tags: list[str], **kwargs: Any) -> Item` - API method `questions/add`;
   + [ ] `edit_answer(self, a_id: int, body: str, **kwargs: Any) -> Item` - API method `answers/{id}/edit`;
   + [ ] `edit_question(self, q_id: int, title: str, body: str, tags: list[str], **kwargs: Any) -> Item` - API method `questions/{id}/edit`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
