"""
('avatar_url', 'https://avatars.githubusercontent.com/u/2363295?s=96&v=4')
('gravatar_id', '')
('url', 'https://api.github.com/users/wanghaisheng')
('html_url', 'https://github.com/wanghaisheng')
('followers_url', 'https://api.github.com/users/wanghaisheng/followers')
('following_url', 'https://api.github.com/users/wanghaisheng/following{/other_user}')
('gists_url', 'https://api.github.com/users/wanghaisheng/gists{/gist_id}')
('starred_url', 'https://api.github.com/users/wanghaisheng/starred{/owner}{/repo}')
('subscriptions_url', 'https://api.github.com/users/wanghaisheng/subscriptions')
('organizations_url', 'https://api.github.com/users/wanghaisheng/orgs')
('repos_url', 'https://api.github.com/users/wanghaisheng/repos')
('events_url', 'https://api.github.com/users/wanghaisheng/events{/privacy}')
('received_events_url', 'https://api.github.com/users/wanghaisheng/received_events')
('issues_url', 'https://api.github.com/search/issues?q=type:pr+is:merged+author:wanghaisheng&per_page=100')
"""
# -*- coding: utf-8 -*-
# Time       : 2022/5/11 18:48
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import os
from datetime import datetime
from typing import Union, Optional, List

import requests

GITHUB_ACTOR = os.getenv("GITHUB_ACTOR", "QIN2DIM")

PATH_SUMMARY_OUTPUT = "README.md"

API_ROOT = "https://api.github.com"
USER_ROOT = f"{API_ROOT}/users/{GITHUB_ACTOR}"
REPO_URLS = f"{USER_ROOT}/repos"
EVENT_URLS = f"{USER_ROOT}/events"
ISSUE_URLS = f"{API_ROOT}/search/issues"

PATH_SUMMARY_OUTPUT="content/changelog.md"
class GitUserStatus:
    def __init__(self):
        self.user_obj = {}
        self.repo_objs = {}
        self.forked_repo_objs = {}
        self.contributed_repo_objs = {}

        self.repo2hyperlink = {}

        # User basic
        self.avatar_url = "https://avatars.githubusercontent.com/u/000000?v=4"
        self.public_repos = 0

        # User statistics
        self.total_stars_earned = 0
        self.total_commits = 0
        self.total_prs = 0
        self.total_issues = 0
        self.contributed_to = 0

        # Enter api root
        self._init_user_info()

        # Split tasks according to the number of projects.
        # 30 <= per_page <= 100
        self.per_page = 100
        self.pages = (
            1 if self.public_repos <= self.per_page else int(self.public_repos / self.per_page) + 1
        )

    def _init_user_info(self):
        self.user_obj.update(requests.get(USER_ROOT).json())

        self.avatar_url = self.user_obj.get("avatar_url", self.avatar_url)
        self.public_repos = self.user_obj.get("public_repos", self.public_repos)

    def get_repos_info(self, patch_statistics: bool = True):
        """获取仓库 stars forks watches"""
        # 解析用户仓库对象
        for index, page in enumerate(range(1, self.pages + 1)):
            url = f"{REPO_URLS}?page={page}&&per_page={self.per_page}"
            repos = requests.get(url).json()
            for repo in repos:
                # 仅统计原创项目
                _docker = self.forked_repo_objs if repo["fork"] else self.repo_objs
                _docker[repo["full_name"]] = {
                    "stars": repo["stargazers_count"],
                    "forks": repo["forks_count"],
                    # "watches": repo["watchers_count"], # 失效
                    "pushed_at": repo["pushed_at"],
                }
                # 获取仓库超链接映射
                self.repo2hyperlink[repo["full_name"]] = repo["html_url"]
                # 補充用戶統計信息
                if patch_statistics and not repo["fork"]:
                    self.total_stars_earned += repo["stargazers_count"]

    def get_contributed_repos(self):
        skip_repo = []
        content = []
        repo2stars = {}

        for _, page in enumerate(range(1, 10)):
            url = f"{ISSUE_URLS}?q=type:pr+is:merged+author:{GITHUB_ACTOR}&page={page}&per_page=100"
            events = requests.get(url).json()

            # Ending Unexpected Retrieval Tasks.
            if not events.get("items"):
                break
            content.extend(events["items"])

        for event in reversed(content):
            repo_owner = event["repository_url"].split("/")[-2]
            repo_name = f'{repo_owner}/{event["repository_url"].split("/")[-1]}'
            repo_api = event["repository_url"]

            # Strategy: Skip task. Filtering your own project.
            if repo_owner.lower() == GITHUB_ACTOR.lower():
                continue
            # Strategy: Skip task. API response is outdated, skip task.
            if repo_name in skip_repo:
                continue
            # Strategy: Skip task. Filtering duplicate request tasks.
            if repo2stars.get(repo_name):
                continue

            data = requests.get(repo_api).json()
            message = data.get("message", "")

            # Strategy: Skip task. API response is outdated, skip task.
            if "Not Found" in message:
                skip_repo.append(repo_name)
                continue
            # Strategy: Mission compete. IP address has been flagged.
            elif "limited" in message:
                break

            # Get statistics on contributed repository objects.
            repo2stars[repo_name] = data["stargazers_count"]
            updated_at = event["updated_at"]
            stick_url = event["html_url"]
            stick_alias = f"pull/{event['number']}"
            self.contributed_repo_objs[repo_name] = {
                "stars": repo2stars[repo_name],
                "updated_at": updated_at,
                "stick": f"[{stick_alias}]({stick_url})",
            }
            self.repo2hyperlink[repo_name] = stick_url


class MarkdownTemplater:
    def __init__(self):
        self.summary_context = []

    def update_summary(self, context: Union[str, list]):
        if isinstance(context, str):
            context = [context]
        for ctx in context:
            self.summary_context.append(ctx)

    def get_summary(self) -> str:
        return "\n".join(self.summary_context)

    def to_table(self, title: list, sequence: list) -> Optional[list]:
        try:
            if not title or not sequence or len(title) != len(sequence[0]):
                return []
        except (IndexError, TypeError):
            return []

        context = [
            f"|{'|'.join([f' **{t}** ' for t in title])}|",  # table title
            f"|{'|'.join([' :---- ', ] * len(sequence[0]))}|",  # table divider
        ]
        for s in sequence:
            context.append(f"|{'|'.join([str(i) for i in s])}|")  # table content

        self.update_summary(context)

        return context

    def to_title(self, text: str, level: int = 2) -> str:
        ctx = f"{'#' * level} {text}\n"
        self.update_summary(ctx)
        return ctx

    def to_unordered_list(self, sequence: Union[str, dict, List[str]]) -> Optional[List[str]]:
        context = []
        if isinstance(sequence, str):
            context.append(f"- {sequence}")
        elif isinstance(sequence, list):
            context = [f"- {s}" for s in sequence]
        elif isinstance(sequence, dict):
            context = [f"- **{str(k)}**: {str(v)}\n" for k, v in sequence.items()]
        self.update_summary(context)
        return context

    def to_ordered_list(self, sequence: Union[str, List[str]]) -> Optional[List[str]]:
        if isinstance(sequence, str):
            sequence = [sequence]

        context = [f"{i + 1}. {s}" for i, s in enumerate(sequence)]
        self.update_summary(context)
        return context

    def to_html_img(self, alt, src) -> str:
        ctx = f'<img width="30%" src="{src}" alt="{alt}"/>\n'
        self.update_summary(ctx)
        return ctx

    def to_content(self, text: str) -> Optional[str]:
        self.update_summary(text)
        return text

    def sayhi(self) -> str:
        ctx = f"## Hi there :heart:, I'm {GITHUB_ACTOR}\n"
        self.update_summary(ctx)
        return ctx


def cache_summary(summary,PATH_SUMMARY_OUTPUT):
    with open(PATH_SUMMARY_OUTPUT, "w", encoding="utf8") as file:
        file.write(summary)


def register_user_data():
    """Get the corresponding user statistics."""
    gus = GitUserStatus()
    gus.get_repos_info()
    gus.get_contributed_repos()

    return gus


def arrange_summary():
    gus = register_user_data()
    mt = MarkdownTemplater()

    # SayHi
    mt.sayhi()
    mt.to_html_img(alt=GITHUB_ACTOR, src=gus.avatar_url)

    # == Statistics ==
    mt.to_title("Statistics", level=2)
    mt.to_content(f"> Automated deployment @ {str(datetime.now()).split('.')[0]} Asia/Shanghai")

    # === User Statistics ===
    mt.to_title("User", level=3)
    # -- Arrange content --
    _user_statistics = {"Total_stars_earned": gus.total_stars_earned, "Projects": gus.public_repos}
    # -- Write content --
    mt.to_unordered_list(_user_statistics)

    # === Repositories Statistics ===
    mt.to_title("Sources", level=3)
    # -- Arrange content --
    repo_obj = sorted(
        gus.repo_objs.items(), key=lambda kv: (kv[-1]["pushed_at"], kv[0]), reverse=True
    )
    title = ["name"] + list(repo_obj[0][-1].keys())
    sequence = [[f"[{k}]({gus.repo2hyperlink[k]})"] + list(v.values()) for k, v in repo_obj]
    # -- Write content --
    mt.to_unordered_list({"count": len(sequence)})
    mt.to_table(title=title, sequence=sequence)

    # === Forked ===
    mt.to_title("Forks", level=3)
    # -- Arrange content --
    repo_obj = sorted(
        gus.forked_repo_objs.items(), key=lambda kv: (kv[-1]["pushed_at"], kv[0]), reverse=True
    )
    title = ["name"] + list(repo_obj[0][-1].keys())
    sequence = [[f"[{k}]({gus.repo2hyperlink[k]})"] + list(v.values()) for k, v in repo_obj]
    # -- Write content --
    mt.to_unordered_list({"count": len(sequence)})
    mt.to_table(title=title, sequence=sequence)

    # === Contributed ===
    mt.to_title("Contributed", level=3)
    # -- Arrange content --
    repo_obj = sorted(
        gus.contributed_repo_objs.items(), key=lambda kv: (kv[-1]["stars"], kv[0]), reverse=True
    )
    title = ["name"] + list(repo_obj[0][-1].keys())
    sequence = [[f"[{k}]({gus.repo2hyperlink[k]})"] + list(v.values()) for k, v in repo_obj]
    # -- Write content --
    mt.to_unordered_list({"count": len(sequence)})
    mt.to_table(title=title, sequence=sequence)
    # return mt.get_summary()
    # Output
    cache_summary(mt.get_summary())


if __name__ == "__main__":
    arrange_summary()
