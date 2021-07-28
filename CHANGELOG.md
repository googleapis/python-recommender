# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-recommender/#history

### [2.3.2](https://www.github.com/googleapis/python-recommender/compare/v2.3.1...v2.3.2) (2021-07-28)


### Features

* add Samples section to CONTRIBUTING.rst ([#110](https://www.github.com/googleapis/python-recommender/issues/110)) ([23a901b](https://www.github.com/googleapis/python-recommender/commit/23a901b992697c0e4ccdfb42573bc34d7244c31e))


### Bug Fixes

* enable self signed jwt for grpc ([#114](https://www.github.com/googleapis/python-recommender/issues/114)) ([63d3fc9](https://www.github.com/googleapis/python-recommender/commit/63d3fc92cebeb8148b35cacaac4bfea096242f2f))


### Miscellaneous Chores

* release as 2.3.2 ([#115](https://www.github.com/googleapis/python-recommender/issues/115)) ([6e177d4](https://www.github.com/googleapis/python-recommender/commit/6e177d4790a2074d035516ada6b27c66315aa44c))

### [2.3.1](https://www.github.com/googleapis/python-recommender/compare/v2.3.0...v2.3.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#109](https://www.github.com/googleapis/python-recommender/issues/109)) ([c0979ca](https://www.github.com/googleapis/python-recommender/commit/c0979caf8d3d33ed1b914907b51c3647addea2da))

## [2.3.0](https://www.github.com/googleapis/python-recommender/compare/v2.2.0...v2.3.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#102](https://www.github.com/googleapis/python-recommender/issues/102)) ([facf208](https://www.github.com/googleapis/python-recommender/commit/facf208a7b698e8e5af113d4b151250d2ea84734))


### Bug Fixes

* disable always_use_jwt_access ([#106](https://www.github.com/googleapis/python-recommender/issues/106)) ([b823493](https://www.github.com/googleapis/python-recommender/commit/b82349335502dbd9ec15646b036af4e59d41014e))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-recommender/issues/1127)) ([#97](https://www.github.com/googleapis/python-recommender/issues/97)) ([f00fab2](https://www.github.com/googleapis/python-recommender/commit/f00fab2d3064c3a87823b444f556cce6cdccfab6)), closes [#1126](https://www.github.com/googleapis/python-recommender/issues/1126)

## [2.2.0](https://www.github.com/googleapis/python-recommender/compare/v2.1.0...v2.2.0) (2021-05-28)


### Features

* add `from_service_account_info` ([94a006e](https://www.github.com/googleapis/python-recommender/commit/94a006ea95f692e431cda4cea9e5042f494c0704))


### Bug Fixes

* **deps:** add packaging requirement ([#91](https://www.github.com/googleapis/python-recommender/issues/91)) ([bf202ab](https://www.github.com/googleapis/python-recommender/commit/bf202ab5656cbd7dfdff6847310d4321c48735d4))
* fix retry deadlines ([#74](https://www.github.com/googleapis/python-recommender/issues/74)) ([94a006e](https://www.github.com/googleapis/python-recommender/commit/94a006ea95f692e431cda4cea9e5042f494c0704))

## [2.1.0](https://www.github.com/googleapis/python-recommender/compare/v2.0.0...v2.1.0) (2021-01-29)


### Features

* add support for billingAccounts as another parent resource ([#59](https://www.github.com/googleapis/python-recommender/issues/59)) ([61d2c7b](https://www.github.com/googleapis/python-recommender/commit/61d2c7b0440c79a938cecd5a75822055934d8915))


### Bug Fixes

* remove client side gRPC receive limit ([#56](https://www.github.com/googleapis/python-recommender/issues/56)) ([10043cc](https://www.github.com/googleapis/python-recommender/commit/10043cc32d9c13ab92da62e214a972918336e88d))


### Documentation

* **python:** document adding Python 3.9 support, dropping 3.5 support ([#63](https://www.github.com/googleapis/python-recommender/issues/63)) ([5bb9b2c](https://www.github.com/googleapis/python-recommender/commit/5bb9b2c6b627e58a831be24d038f7b3f6bf55e3b)), closes [#787](https://www.github.com/googleapis/python-recommender/issues/787)

## [2.0.0](https://www.github.com/googleapis/python-recommender/compare/v1.1.1...v2.0.0) (2020-11-19)


### ⚠ BREAKING CHANGES

* use microgenerator (#54)

### Features

* use microgenerator ([#54](https://www.github.com/googleapis/python-recommender/issues/54)) ([63b8a43](https://www.github.com/googleapis/python-recommender/commit/63b8a43ce25a5305664424fa247ad82595c4342f)). See [Migration Guide](https://github.com/googleapis/python-recommender/blob/master/UPGRADING.md).

### [1.1.1](https://www.github.com/googleapis/python-recommender/compare/v1.1.0...v1.1.1) (2020-10-29)


### Bug Fixes

* tweak retry params for 'ListInsights'/'GetInsight'/'MarkInsightAccepted' API calls (via synth) ([#49](https://www.github.com/googleapis/python-recommender/issues/49)) ([0d2baaf](https://www.github.com/googleapis/python-recommender/commit/0d2baaf9e0d05897b4ea380510d3d899638cb45d))

## [1.1.0](https://www.github.com/googleapis/python-recommender/compare/v1.0.0...v1.1.0) (2020-07-13)


### Features

* add methods for interacting with insights ([#35](https://www.github.com/googleapis/python-recommender/issues/35)) ([940a3fb](https://www.github.com/googleapis/python-recommender/commit/940a3fb01013865c836bfb55397c25284004a7ad))


### Bug Fixes

* update retry config ([#31](https://www.github.com/googleapis/python-recommender/issues/31)) ([5c497e2](https://www.github.com/googleapis/python-recommender/commit/5c497e29d65d288a4b8b24a7b5aa487a5804e880))

## [1.0.0](https://www.github.com/googleapis/python-recommender/compare/v0.3.0...v1.0.0) (2020-05-21)


### Features

* release as production/stable ([#17](https://www.github.com/googleapis/python-recommender/issues/17)) ([b6f0a19](https://www.github.com/googleapis/python-recommender/commit/b6f0a1972df2d0eb49580e152f47b2d13ea1c53c))

## [0.3.0](https://www.github.com/googleapis/python-recommender/compare/v0.2.0...v0.3.0) (2020-03-14)


### Features

* add insight support; undeprecate resource name helper methods (via synth) ([#7](https://www.github.com/googleapis/python-recommender/issues/7)) ([876c383](https://www.github.com/googleapis/python-recommender/commit/876c383afed9a2384d9ef361b4054c381ab9a23b))

## 0.2.0

01-24-2020 14:03 PST

### Implementation Changes
- Deprecate resource name helper methods (via synth).  ([#9863](https://github.com/googleapis/google-cloud-python/pull/9863))

### New Features
- Add v1, set release level to beta. ([#10170](https://github.com/googleapis/google-cloud-python/pull/10170))

### Documentation
- Add Python 2 sunset banner to documentation. ([#9036](https://github.com/googleapis/google-cloud-python/pull/9036))
- Change requests intersphinx url (via synth). ([#9408](https://github.com/googleapis/google-cloud-python/pull/9408))
- Fix library reference doc link. ([#9338](https://github.com/googleapis/google-cloud-python/pull/9338))

### Internal / Testing Changes
- Correct config path in synth file for recommender. ([#10076](https://github.com/googleapis/google-cloud-python/pull/10076))

## 0.1.0

09-27-2019 12:20 PDT

### New Features
- initial release of v1beta1 ([#9257](https://github.com/googleapis/google-cloud-python/pull/9257))
