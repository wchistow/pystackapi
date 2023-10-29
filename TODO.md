# ToDo

 + [ ] add more examples to directory `examples/`;
 + [ ] add methods, that requires authentication (of course, each of these methods needs tests) (they also need checks, that `self.access_token` and `self.app_key` are set):
   + [ ] `get_me(self) -> Item` - API method `me`;
   + [ ] `get_my_full_reputation_history(self) -> list[Item]` - API method `me/reputation-history/full`;
   + [ ] `get_my_inbox(self) -> list[Item]` - API method `me/inbox`;
   + [ ] `get_my_unread_inbox(self) -> list[Item]` - API method `me/inbox/unread`;

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
