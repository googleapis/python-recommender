# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for MarkRecommendationSucceeded
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-recommender


# [START recommender_generated_recommender_v1_Recommender_MarkRecommendationSucceeded_async]
from google.cloud import recommender_v1


async def sample_mark_recommendation_succeeded():
    # Create a client
    client = recommender_v1.RecommenderAsyncClient()

    # Initialize request argument(s)
    request = recommender_v1.MarkRecommendationSucceededRequest(
        name="name_value",
        etag="etag_value",
    )

    # Make the request
    response = await client.mark_recommendation_succeeded(request=request)

    # Handle the response
    print(response)

# [END recommender_generated_recommender_v1_Recommender_MarkRecommendationSucceeded_async]