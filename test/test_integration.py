from test import does_not_raise

import pytest

import mozilla_repo_urls


@pytest.mark.parametrize(
    "url_string, expectation, expected",
    (
        (
            "https://hg.mozilla.org/mozilla-central",
            does_not_raise(),
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central",
                "path_raw": "",
                "path": "",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/mozilla-central",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central",
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/releases/mozilla-beta",
            does_not_raise(),
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "releases/mozilla-beta",
                "normalized": "https://hg.mozilla.org/releases/mozilla-beta",
                "path_raw": "",
                "path": "",
                "pathname": "/releases/mozilla-beta",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "releases/mozilla-beta",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/releases/mozilla-beta",
                "urls": {
                    "https": "https://hg.mozilla.org/releases/mozilla-beta",
                    "ssh": "ssh://hg.mozilla.org/releases/mozilla-beta",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/releases/mozilla-release",
            does_not_raise(),
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "releases/mozilla-release",
                "normalized": "https://hg.mozilla.org/releases/mozilla-release",
                "path_raw": "",
                "path": "",
                "pathname": "/releases/mozilla-release",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "releases/mozilla-release",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/releases/mozilla-release",  # noqa: E501
                "urls": {
                    "https": "https://hg.mozilla.org/releases/mozilla-release",
                    "ssh": "ssh://hg.mozilla.org/releases/mozilla-release",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/try",
            does_not_raise(),
            {
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "try",
                "normalized": "https://hg.mozilla.org/try",
                "path_raw": "",
                "path": "",
                "pathname": "/try",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "try",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/try",
                "urls": {
                    "https": "https://hg.mozilla.org/try",
                    "ssh": "ssh://hg.mozilla.org/try",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
            does_not_raise(),
            {
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
                "path_raw": "/raw-file/tip/taskcluster/ci/config.yml",
                "path": "tip/taskcluster/ci/config.yml",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/mozilla-central",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
            does_not_raise(),
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
                "path_raw": "/file/tip/taskcluster/ci/config.yml",
                "path": "tip/taskcluster/ci/config.yml",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "taskcluster_role_prefix": "repo:hg.mozilla.org/mozilla-central",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://github.com/mozilla-mobile/fenix",
            does_not_raise(),
            {
                "github": True,
                "groups": [],
                "hgmo": False,
                "host": "github.com",
                "name": "fenix",
                "normalized": "https://github.com/mozilla-mobile/fenix.git",
                "owner": "mozilla-mobile",
                "path_raw": "",
                "path": "",
                "pathname": "/mozilla-mobile/fenix",
                "platform": "github",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "fenix",
                "repo_type": "git",
                "resource": "github.com",
                "taskcluster_role_prefix": "repo:github.com/mozilla-mobile/fenix",
                "urls": {
                    "git": "git://github.com/mozilla-mobile/fenix.git",
                    "https": "https://github.com/mozilla-mobile/fenix.git",
                    "ssh": "git@github.com:mozilla-mobile/fenix.git",
                },
                "user": "git",
                "valid": True,
            },
        ),
        (
            "git@github.com:mozilla-mobile/firefox-android.git",
            does_not_raise(),
            {
                "github": True,
                "groups": [],
                "hgmo": False,
                "host": "github.com",
                "name": "firefox-android",
                "normalized": "git@github.com:mozilla-mobile/firefox-android.git",
                "owner": "mozilla-mobile",
                "path_raw": "",
                "path": "",
                "pathname": "mozilla-mobile/firefox-android.git",
                "platform": "github",
                "port": "",
                "protocol": "ssh",
                "protocols": [],
                "repo": "firefox-android",
                "repo_type": "git",
                "resource": "github.com",
                "taskcluster_role_prefix": "repo:github.com/mozilla-mobile/firefox-android",  # noqa: E501
                "urls": {
                    "git": "git://github.com/mozilla-mobile/firefox-android.git",
                    "https": "https://github.com/mozilla-mobile/firefox-android.git",
                    "ssh": "git@github.com:mozilla-mobile/firefox-android.git",
                },
                "user": "git",
                "valid": True,
            },
        ),
        (
            "https://some.unknown/repo",
            pytest.raises(mozilla_repo_urls.InvalidRepoUrlError),
            None,
        ),
    ),
)
def test_parse(url_string, expectation, expected):
    with expectation:
        url_object = mozilla_repo_urls.parse(url_string)
        actual = {
            attribute_name: getattr(url_object, attribute_name)
            for attribute_name in expected.keys()
        }
        assert actual == expected
