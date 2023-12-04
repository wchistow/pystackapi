# ToDo

 + [ ] add more examples to directory `examples/`;
 + [ ] add methods, that requires authentication (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [X] `get_me(self, **kwargs: Any) -> Item` - API method `me`;
   + [X] `get_my_full_reputation_history(self, **kwargs: Any) -> list[Item]` - API method `me/reputation-history/full`;
   + [X] `get_my_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox`;
   + [X] `get_my_unread_inbox(self, **kwargs: Any) -> list[Item]` - API method `me/inbox/unread`;
   + [X] `get_unanswered_questions_on_my_tags(self, **kwargs: Any) -> list[Item]` - API method `questions/unanswered/my-tags`;
 + [ ] add methods with POST-requests (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [X] `add_answer(self, q_id: int, body: str, **kwargs: Any) -> Item` - API method `questions/{id}/answers/add`;
   + [X] `add_answers_suggested_edit(self, a_id: int, body: str, comment: str, **kwargs: Any) -> Item` - API method `answers/{id}/suggested-edit/add`;
   + [X] `add_comment(self, post_id: int, body: str, **kwargs: Any) -> Item` - API method `posts/{id}/comments/add`;
   + [X] `add_question(self, title: str, body: str, tags: list[str], **kwargs: Any) -> Item` - API method `questions/add`;
   + [X] `add_questions_suggested_edit(self, q_id: int, title: str, body: str, tags: list[str], comment: str, **kwargs: Any) -> Item` - API method `questions/{id}/suggested-edit/add`;
   + [X] `edit_answer(self, a_id: int, body: str, **kwargs: Any) -> Item` - API method `answers/{id}/edit`;
   + [ ] `edit_comment(self, c_id: int, body: str, **kwargs: Any) -> Item` - API method `comments/{id}/edit`;
   + [X] `edit_question(self, q_id: int, title: str, body: str, tags: list[str], **kwargs: Any) -> Item` - API method `questions/{id}/edit`;
   + [ ] `delete_answer(self, a_id: int, **kwargs: Any) -> None` - API method `answers/{id}/delete`;
   + [ ] `delete_comment(self, c_id: int, **kwargs: Any) -> None` - API method `comments/{id}/delete`;
   + [ ] `delete_question(self, q_id: int, **kwargs: Any) -> None` - API method `questions/{id}/delete`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
