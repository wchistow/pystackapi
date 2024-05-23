# ToDo

 + [X] add class `pystackapi.chat.Chat` (wrapper for `chatexchange.Client`);
 + [ ] add the following methods to class `pystackapi.chat.Chat`:
   + [ ] `get_me(self) -> Item` - wrapper for `chatexchange.Client.get_me` (auth required);
   + [ ] `get_message(self, message_id: int, **kwargs: Any) -> Item` - wrapper for `chatexchange.Client.get_message`;
   + [ ] `cancel_message_stars(self, message_id: int) -> None` - wrapper for `chatexchange.messages.Message.cancel_stars`;
   + [ ] `delete_message(self, message_id: int) -> None` - wrapper for `chatexchange.messages.Message.delete`;
   + [ ] `edit_message(self, message_id: int, text: str) -> None` - wrapper for `chatexchange.messages.Message.edit`;
   + [ ] `reply_to_message(self, message_id: int, text: str) -> None` - wrapper for `chatexchange.messages.Message.reply`;
   + [ ] `star_message(self, message_id: int) -> None` - wrapper for `chatexchange.messages.Message.star`;
   + [ ] `get_room(self, room_id: int, **kwargs: Any) -> Item` - wrapper for `chatexchange.Client.get_room`;
   + [ ] `get_user(self, user_id: int, **kwargs: Any) -> Item` - wrapper for `chatexchange.Client.get_user`;
 + [ ] add more examples to directory `examples/`.

*when you're done any of these tasks, replace `[ ]` in start of line with this task to `[X]`.*
