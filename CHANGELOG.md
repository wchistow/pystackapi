# Changelog of the PyStackAPI library

## 0.3.0 (??.??.2024)

### Added:

 + class `pystackapi.Chat` - client for StackExchange Chat;

## 0.2.0 (06.12.2023)

### Added:

 + exception `AccessTokenOrAppKeyRequired` - raises, when method requires access token or app key, but it's not set.
 + method `add_answer` to class `Site`;
 + method `add_answers_suggested_edit` to class `Site`;
 + method `add_questions_suggested_edit` to class `Site`;
 + method `add_comment` to class `Site`;
 + method `add_question` to class `Site`;
 + method `delete_answer` to class `Site`;
 + method `delete_comment` to class `Site`;
 + method `delete_question` to class `Site`;
 + method `edit_answer` to class `Site`;
 + method `edit_comment` to class `Site`;
 + method `edit_question` to class `Site`;
 + method `get_me` to class `Site`;
 + method `get_my_inbox` to class `Site`; 
 + method `get_my_full_reputation_history` to class `Site`;
 + method `get_my_unread_inbox` to class `Site`;
 + method `get_unanswered_questions_on_my_tags` to class `Site`;
 + method `post` to class `Site`

### Changed:

 + error messages, it was: `"{message}" on URL {url} (status code {status_code})`, it became: `{message} (status code {status_code})`

## 0.1.1 (25.09.2023)

### Added:

 + method `__str__` to class `Item` for more pretty result printing.
