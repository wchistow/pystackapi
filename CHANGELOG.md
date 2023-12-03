# Changelog of the PyStackAPI library

## 0.2.0 (??.??.202?)

### Added:

 + method `add_answer` to class `Site`;
 + method `add_answers_suggested_edit` to class `Site`;
 + method `add_questions_suggested_edit` to class `Site`;
 + method `add_comment` to class `Site`;
 + method `add_question` to class `Site`;
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
