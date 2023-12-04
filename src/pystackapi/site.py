from typing import Any, NoReturn
from collections.abc import Iterable

from ._base_client import BaseClient
from ._raw_response_dict import RawResponseDict
from ._utils import (_join_with_semicolon, _check_iterable_is_not_empty,
                     _check_iterable_arg, _check_period_value,
                     _check_access_token_and_app_key_are_passed)
from .errors import BadArgumentsError
from .item import Item


class Site(BaseClient):
    """Implements the StackExchange APIs client for a specific site."""
    version = '2.3'
    base_url = f'https://api.stackexchange.com/{version}/'

    def __init__(self, name: str, access_token: str | None = None,
                 app_key: str | None = None) -> None:
        self.name = name
        self.access_token = access_token
        self.app_key = app_key

    def get(self, query: str, **kwargs: Any) -> RawResponseDict:
        """Returns raw result of calling `query` to API."""
        params = {'site': self.name}
        if self.access_token is not None:
            params['access_token'] = self.access_token
        if self.app_key is not None:
            params['key'] = self.app_key

        params.update(kwargs)

        return self._get(f'{self.base_url}{query}', params)

    def post(self, query: str, **kwargs: Any) -> RawResponseDict:
        """Returns raw result of POST-calling `query` to API."""
        _check_access_token_and_app_key_are_passed(self)

        data = {'site': self.name, 'access_token': self.access_token, 'key': self.app_key, **kwargs}

        return self._post(f'{self.base_url}{query}', data)

    # CONTRIBUTORS: Please, sort methods by alphabet.

    def add_answer(self, q_id: int, body: str, **kwargs: Any) -> Item:
        """Create a new answer on the given question."""
        return Item(self.post(f'questions/{q_id}/answers/add', body=body, **kwargs)['items'][0])

    def add_answers_suggested_edit(self, a_id: int, body: str, comment: str, **kwargs: Any) -> Item:
        """Create a suggested edit on an existing answer."""
        return Item(self.post(f'answers/{a_id}/suggested-edit/add', body=body, comment=comment,
                              **kwargs)['items'][0])

    def add_comment(self, post_id: int, body: str, **kwargs: Any) -> Item:
        """Create a new comment."""
        return Item(self.post(f'posts/{post_id}/comments/add', body=body, **kwargs)['items'][0])

    def add_question(self, title: str, body: str, tags: list[str], **kwargs: Any) -> Item:
        """Create a new question."""
        return Item(self.post('questions/add', title=title, body=body,
                              tags=';'.join(tags), **kwargs)['items'][0]
                    )

    def add_questions_suggested_edit(self, q_id: int, title: str, body: str, tags: list[str],
                                     comment: str, **kwargs: Any) -> Item:
        """Create a suggested edit on an existing question."""
        return Item(self.post(f'questions/{q_id}/suggested-edit/add', title=title, body=body,
                              tags=';'.join(tags), comment=comment, **kwargs)['items'][0])

    def edit_answer(self, a_id: int, body: str, **kwargs: Any) -> Item:
        """Edit an existing answer."""
        return Item(self.post(f'answers/{a_id}/edit', body=body, **kwargs)['items'][0])

    def edit_comment(self, c_id: int, body: str, **kwargs: Any) -> Item:
        """Edit an existing comment."""
        return Item(self.post(f'comments/{c_id}/edit', body=body, **kwargs)['items'][0])

    def edit_question(self, q_id: int, title: str, body: str, tags: list[str],
                      **kwargs: Any) -> Item:
        """Edit an existing question."""
        return Item(self.post(f'questions/{q_id}/edit', title=title, body=body,
                              tags=';'.join(tags), **kwargs)['items'][0])

    def get_answers(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all the undeleted answers in the system,
        else the set of answers identified by `ids`.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'answers/{addition}', **kwargs)['items']]

    def get_answer(self, a_id: int, **kwargs: Any) -> Item | None:
        """
        Returns answer identified by `a_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_answers([a_id], **kwargs)[0]
        except IndexError:
            return None

    def get_answers_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns answers belonging to collectives in `slugs` found on the site."""
        _check_iterable_is_not_empty(slugs, arg_name='slugs')
        return [Item(data) for data in
                self.get(f'collectives/{_join_with_semicolon(slugs)}/answers', **kwargs)['items']]

    def get_answers_on_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the answers to a set of questions identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'questions/{_join_with_semicolon(ids)}/answers', **kwargs)['items']]

    def get_articles(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all articles on the site,
        else the articles identified by `ids`.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'articles/{addition}', **kwargs)['items']]

    def get_article(self, a_id: int, **kwargs: Any) -> Item | None:
        """
        Returns article identified by `a_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_articles([a_id], **kwargs)[0]
        except IndexError:
            return None

    def get_badges(self, **kwargs: Any) -> list[Item]:
        """Returns all badges in the system."""
        return [Item(data) for data in self.get('badges', **kwargs)['items']]

    def get_badges_recipients(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, recently awarded badges in the system,
        constrained to a certain set of badges, else recently awarded badges in the system.
        """
        if ids is not None:
            url = 'badges/' + _join_with_semicolon(_check_iterable_arg(ids)) + '/recipients'
        else:
            url = 'badges/recipients'
        return [Item(data) for data in self.get(url, **kwargs)['items']]

    def get_tag_based_badges(self, **kwargs: Any) -> list[Item]:
        """Returns the badges that are awarded for participation in specific tags."""
        return [Item(data) for data in self.get('badges/tags', **kwargs)['items']]

    def get_non_tag_based_badges(self, **kwargs: Any) -> list[Item]:
        """Returns all non-tagged-based badges in alphabetical order."""
        return [Item(data) for data in self.get('badges/name', **kwargs)['items']]

    def get_collectives(self, slugs: Iterable[str] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `slugs` is set, collectives in `slugs` found on the site,
        else, all collectives in the system.
        """
        addition = _join_with_semicolon(_check_iterable_arg(slugs, arg_name='slugs'))
        return [Item(data) for data in self.get(f'collectives/{addition}', **kwargs)['items']]

    def get_collective(self, slug: str, **kwargs: Any) -> Item | None:
        """
        Returns collective with specific `slug`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_collectives([slug], **kwargs)[0]
        except IndexError:
            return None

    def get_comments(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the comments identified by `ids`,
        else, all comments on the site.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'comments/{addition}', **kwargs)['items']]

    def get_comment(self, c_id: int, **kwargs: Any) -> Item | None:
        """
        Returns the comment identified in `c_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_comments([c_id], **kwargs)[0]
        except IndexError:
            return None

    def get_comments_on_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the comments on a set of answers."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'answers/{_join_with_semicolon(ids)}/comments', **kwargs)['items']]

    def get_comments_on_articles(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the comments on a set of articles."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'articles/{_join_with_semicolon(ids)}/comments', **kwargs)['items']]

    def get_comments_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the comments on a set of posts."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'posts/{_join_with_semicolon(ids)}/comments', **kwargs)['items']]

    def get_comments_on_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the comments on a set of questions."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'questions/{_join_with_semicolon(ids)}/comments', **kwargs)['items']]

    def get_info(self) -> Item:
        """Returns a collection of statistics about the site."""
        return Item(self.get('info')['items'][0])  # here can't be `IndexError`

    def get_linked_in_articles(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions that are linked to the articles identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'articles/{_join_with_semicolon(ids)}/linked', **kwargs)['items']]

    def get_linked_in_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns questions which link to those questions identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'questions/{_join_with_semicolon(ids)}/linked', **kwargs)['items']]

    def get_posts(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the posts identified by `ids`,
        else, all posts on the site.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in
                self.get(f'posts{"/" if addition else ""}{addition}', **kwargs)['items']]

    def get_post(self, p_id: int, **kwargs: Any) -> Item | None:
        """
        Returns the post identified in `p_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_posts([p_id], **kwargs)[0]
        except IndexError:
            return None

    def get_privileges(self, **kwargs: Any) -> list[Item]:
        """Returns the earnable privileges on a site."""
        return [Item(data) for data in self.get('privileges', **kwargs)['items']]

    def get_questions(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, all the undeleted questions in the system,
        else the set of questions identified by `ids`.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'questions/{addition}', **kwargs)['items']]

    def get_question(self, q_id: int, **kwargs: Any) -> Item | None:
        """
        Returns the question identified in `q_id`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_questions([q_id], **kwargs)[0]
        except IndexError:
            return None

    def get_questions_on_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions on a set of answers."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'answers/{_join_with_semicolon(ids)}/questions', **kwargs)['items']]

    def get_bountied_questions(self, **kwargs: Any) -> list[Item]:
        """Returns all the questions with active bounties in the system."""
        return [Item(data) for data in self.get('questions/featured', **kwargs)['items']]

    def get_questions_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns the questions on a set of collectives."""
        _check_iterable_is_not_empty(slugs, arg_name='slugs')
        return [Item(data) for data in
                self.get(f'collectives/{_join_with_semicolon(slugs)}/questions', **kwargs)['items']]

    def get_questions_with_no_answers(self, **kwargs: Any) -> list[Item]:
        """Returns questions which have received no answers."""
        return [Item(data) for data in self.get('questions/no-answers', **kwargs)['items']]

    def get_related_to_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns questions that the site considers related to those identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'questions/{_join_with_semicolon(ids)}/related', **kwargs)['items']]

    def get_unanswered_questions(self, **kwargs: Any) -> list[Item]:
        """Returns questions the site considers to be unanswered."""
        return [Item(data) for data in self.get('questions/unanswered', **kwargs)['items']]

    def get_unanswered_questions_on_my_tags(self, **kwargs: Any) -> list[Item]:
        """
        Returns questions the site considers to be unanswered,
        which are within a user's favorite tags.
        If a user has no favorites, their frequented tags are used instead.
        """
        _check_access_token_and_app_key_are_passed(self)
        return [Item(data) for data in self.get('questions/unanswered/my-tags', **kwargs)['items']]

    def get_revisions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns edit revisions identified by `ids`."""
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'revisions/{addition}', **kwargs)['items']]

    def get_revisions_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns revisions on the set of posts, identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data)
                for data in self.get(f'posts/{_join_with_semicolon(ids)}/revisions',
                                     **kwargs)['items']
                ]

    def search(self, **kwargs: Any) -> list[Item]:
        """
        Searches a site for any questions which fit the given criteria.
        **Warning:** one of `tagged` or `intitle` keyword arguments must be set.
        """
        if 'tagged' not in kwargs and 'intitle' not in kwargs:
            raise BadArgumentsError('one of `tagged` or `intitle` keyword arguments must be set.')

        return [Item(data) for data in self.get('search', **kwargs)['items']]

    def advanced_search(self, **kwargs: Any) -> list[Item]:
        """Searches a site for any questions which fit the given criteria."""
        return [Item(data) for data in self.get('search/advanced', **kwargs)['items']]

    def get_similar(self, title: str, **kwargs: Any) -> list[Item]:
        """
        Returns questions which are similar to a hypothetical one based
        on a title and tag combination.
        """
        return [Item(data) for data in self.get('similar', title=title, **kwargs)['items']]

    def get_suggested_edits(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the suggested edits identified by `ids`,
        else all suggested edits on the site.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'suggested-edits/{addition}', **kwargs)['items']]

    def get_suggested_edits_on_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns suggested edits on the set of posts, identified by `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data)
                for data in self.get(f'posts/{_join_with_semicolon(ids)}/suggested-edits',
                                     **kwargs)['items']
                ]

    def get_tags(self, **kwargs: Any) -> list[Item]:
        """Returns all tags in the system."""
        return [Item(data) for data in self.get('tags', **kwargs)['items']]

    def get_top_answerers_on_tag(self, tag: str, period: str, **kwargs: Any)\
            -> list[Item] | NoReturn:
        """
        Returns the top 20 answerers active in a given `tag`,
        of either all-time or the last 30 days.
        """
        _check_period_value(period)
        return [Item(data) for data in
                self.get(f'tags/{tag}/top-answerers/{period}', **kwargs)['items']]

    def get_top_askers_on_tag(self, tag: str, period: str, **kwargs: Any)\
            -> list[Item] | NoReturn:
        """
        Returns the top 20 askers active in a given `tag`, of either all-time or the last 30 days.
        """
        _check_period_value(period)
        return [Item(data) for data in
                self.get(f'tags/{tag}/top-askers/{period}', **kwargs)['items']]

    def get_tags_wikis(self, tags: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns the wikis that go with the given set of tags in `tags`."""
        _check_iterable_is_not_empty(tags, arg_name='tags')
        return [Item(data) for data in
                self.get(f'tags/{_join_with_semicolon(tags)}/wikis', **kwargs)['items']]

    def get_tags_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns tags belonging to collectives in `slugs` found on the site."""
        _check_iterable_is_not_empty(slugs, arg_name='slugs')
        return [Item(data) for data in
                self.get(f'collectives/{_join_with_semicolon(slugs)}/tags', **kwargs)['items']]

    def get_tags_info(self, tags: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns tags' info from the `tags` found on the site."""
        _check_iterable_is_not_empty(tags, arg_name='tags')
        return [Item(data) for data in
                self.get(f'tags/{_join_with_semicolon(tags)}/info', **kwargs)['items']]

    def get_tags_faq(self, tags: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns the frequently asked questions for the given set of tags in `tags`."""
        _check_iterable_is_not_empty(tags, arg_name='tags')
        return [Item(data) for data in
                self.get(f'tags/{_join_with_semicolon(tags)}/faq', **kwargs)['items']]

    def get_me(self, **kwargs: Any) -> Item:
        """Returns the user associated with the passed `access_token`."""
        _check_access_token_and_app_key_are_passed(self)
        return Item(self.get('me', **kwargs)['items'][0])

    def get_moderator_only_tags(self, **kwargs: Any) -> list[Item]:
        """Returns the tags found on a site that only moderators can use."""
        return [Item(data) for data in self.get('tags/moderator-only', **kwargs)['items']]

    def get_my_full_reputation_history(self, **kwargs: Any) -> list[Item]:
        """Returns user's full reputation history, including private events."""
        _check_access_token_and_app_key_are_passed(self)
        return [Item(data) for data in self.get('me/reputation-history/full', **kwargs)['items']]

    def get_my_inbox(self, **kwargs: Any) -> list[Item]:
        """Returns the user identified by access_token's inbox."""
        _check_access_token_and_app_key_are_passed(self)
        return [Item(data) for data in self.get('me/inbox', **kwargs)['items']]

    def get_my_unread_inbox(self, **kwargs: Any) -> list[Item]:
        """Returns the unread items in the user identified by `access_token`'s inbox."""
        _check_access_token_and_app_key_are_passed(self)
        return [Item(data) for data in self.get('me/inbox/unread', **kwargs)['items']]

    def get_related_tags(self, tags: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns the tags that are most related to those in `tags`."""
        _check_iterable_is_not_empty(tags, arg_name='tags')
        return [Item(data) for data in
                self.get(f'tags/{_join_with_semicolon(tags)}/related', **kwargs)['items']]

    def get_required_tags(self, **kwargs: Any) -> list[Item]:
        """Returns the tags found on a site that fulfill required tag constraints on questions."""
        return [Item(data) for data in self.get('tags/required', **kwargs)['items']]

    def get_tags_synonyms(self, tags: Iterable[str] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `tags` is set, all the synonyms that point to the tags identified in `tags`,
        else all tag synonyms found on the site.
        """
        if tags is not None:
            url = (f'tags/{_join_with_semicolon(_check_iterable_arg(tags, arg_name="tags"))}'
                   '/synonyms')
        else:
            url = 'tags/synonyms'
        return [Item(data) for data in self.get(url, **kwargs)['items']]

    def get_questions_timeline(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """
        Returns a subset of the events that have happened to the questions identified by `ids`.
        """
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'questions/{_join_with_semicolon(ids)}/timeline', **kwargs)['items']]

    def get_users(self, ids: Iterable[int] | None = None, **kwargs: Any) -> list[Item]:
        """
        Returns, if `ids` is set, the users identified by `ids`,
        else all users on a site.
        """
        addition = _join_with_semicolon(_check_iterable_arg(ids))
        return [Item(data) for data in self.get(f'users/{addition}', **kwargs)['items']]

    def get_user(self, uid: int, **kwargs: Any) -> Item | None:
        """
        Returns the user identified in `uid`.
        Returns `None` if requested object don't found.
        """
        try:
            return self.get_users([uid], **kwargs)[0]
        except IndexError:
            return None

    def get_users_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the answers the users in `ids` have posted."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/answers', **kwargs)['items']]

    def get_users_badges(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the badges the users in `ids` have earned."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/badges', **kwargs)['items']]

    def get_users_on_collectives(self, slugs: Iterable[str], **kwargs: Any) -> list[Item]:
        """Returns users belonging to collectives in `slugs` found on the site."""
        _check_iterable_is_not_empty(slugs, arg_name='slugs')
        return [Item(data) for data in
                self.get(f'collectives/{_join_with_semicolon(slugs)}/users', **kwargs)['items']]

    def get_users_comments(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the comments posted by users in `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/comments', **kwargs)['items']]

    def get_users_comments_to(self, ids: Iterable[int], toid: int, **kwargs: Any) -> list[Item]:
        """
        Returns the comments that the users in `ids` have posted in reply
        to the single user identified in `toid`.
        """
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/comments/{toid}',
                         **kwargs)['items']
                ]

    def get_users_favorites(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions that users in `ids` have bookmarked."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/favorites', **kwargs)['items']]

    def get_users_mentions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns all the comments that the users in `ids` were mentioned in."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/mentioned', **kwargs)['items']]

    def get_users_posts(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the posts the users in `ids` have posted."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/posts', **kwargs)['items']]

    def get_user_privileges(self, uid: int, **kwargs: Any) -> list[Item]:
        """Returns the privileges a user with ID `uid` has."""
        return [Item(data) for data in
                self.get(f'users/{uid}/privileges', **kwargs)['items']]

    def get_users_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions asked by the users in `ids`."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/questions', **kwargs)['items']]

    def get_users_unaccepted_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """
        Returns the questions asked by the users in `ids` which have at least one answer,
        but no accepted answer.
        """
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/questions/unaccepted',
                         **kwargs)['items']
                ]

    def get_users_unanswered_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """
        Returns the questions asked by the users in `ids` which the site considers unanswered,
        while still having at least one answer posted.
        """
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/questions/unanswered',
                         **kwargs)['items']
                ]

    def get_users_bountied_questions(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions on which the users in {ids} have active bounties."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/questions/featured', **kwargs)['items']
                ]

    def get_users_questions_with_no_answers(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the questions asked by the users in `ids` which have no answers."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/questions/no-answers',
                         **kwargs)['items']
                ]

    def get_users_reputation(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns a subset of the reputation changes for users in {ids}."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/reputation', **kwargs)['items']]

    def get_users_reputation_history(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns users' public reputation history."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/reputation-history', **kwargs)['items']
                ]

    def get_users_suggested_edits(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the suggested edits that the users in `ids` have submitted."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/suggested-edits', **kwargs)['items']]

    def get_users_tags(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns the tags the users identified in `ids` have been active in."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/tags', **kwargs)['items']]

    def get_user_top_answers_on_tags(self, uid: int, tags: Iterable[str], **kwargs: Any)\
            -> list[Item]:
        """
        Returns the top 30 answers a user has posted in response to questions with the given tags.
        """
        return [Item(data) for data in
                self.get(f'users/{uid}/tags/{_join_with_semicolon(tags)}/top-answers',
                         **kwargs)['items']
                ]

    def get_user_top_questions_on_tags(self, uid: int, tags: Iterable[str], **kwargs: Any)\
            -> list[Item]:
        """Returns the top 30 questions a user has asked with the given tags."""
        return [Item(data) for data in
                self.get(f'users/{uid}/tags/{_join_with_semicolon(tags)}/top-questions',
                         **kwargs)['items']
                ]

    def get_users_timeline(self, ids: Iterable[int], **kwargs: Any) -> list[Item]:
        """Returns a subset of the actions the users in `ids` have taken on the site."""
        _check_iterable_is_not_empty(ids)
        return [Item(data) for data in
                self.get(f'users/{_join_with_semicolon(ids)}/timeline', **kwargs)['items']]

    def get_user_top_answers_tags(self, uid: int, ** kwargs: Any) -> list[Item]:
        """Returns a single user's top tags by answer score."""
        return [Item(data) for data in self.get(f'users/{uid}/top-answer-tags', **kwargs)['items']]

    def get_user_top_questions_tags(self, uid: int, ** kwargs: Any) -> list[Item]:
        """Returns a single user's top tags by question score."""
        return [Item(data) for data in
                self.get(f'users/{uid}/top-question-tags', **kwargs)['items']]

    def get_user_top_tags(self, uid: int, ** kwargs: Any) -> list[Item]:
        """Returns a single user's top tags by combined question and answer score."""
        return [Item(data) for data in self.get(f'users/{uid}/top-tags', **kwargs)['items']]

    def get_moderators(self, **kwargs: Any) -> list[Item]:
        """Returns those users on a site who can exercise moderation powers."""
        return [Item(data) for data in self.get('users/moderators', **kwargs)['items']]

    def get_elected_moderators(self, **kwargs: Any) -> list[Item]:
        """
        Returns those users on a site who both have moderator powers, and were actually elected.
        """
        return [Item(data) for data in self.get('users/moderators/elected', **kwargs)['items']]
