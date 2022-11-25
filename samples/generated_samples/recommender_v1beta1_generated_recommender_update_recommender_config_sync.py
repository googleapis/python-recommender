# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Snippet for UpdateRecommenderConfig
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-recommender


# [START recommender_v1beta1_generated_Recommender_UpdateRecommenderConfig_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import recommender_v1beta1


def sample_update_recommender_config():
    # Create a client
    client = recommender_v1beta1.RecommenderClient()

    # Initialize request argument(s)
    request = recommender_v1beta1.UpdateRecommenderConfigRequest(
    )

    # Make the request
    response = client.update_recommender_config(request=request)

    # Handle the response
    print(response)

def sample_update_recommender_config_decrement_idle_vm_obs_period(project_id):

    # Create a client
    client = recommender_v1beta1.RecommenderClient()    

     # Initialize request argument(s)
    name="projects/{0}/locations/us-west1-b/recommenders/google.compute.instance.IdleResourceRecommender/config".format(project_id)    

    # Create the get request from the name
    get_request = recommender_v1beta1.GetRecommenderConfigRequest(name=name)    

    # Make the get request, assign results to config object
    recommender_config = client.get_recommender_config(request=get_request)

    # Get the current value for the target config key
    observation_period = recommender_config.recommender_generation_config.params["observation_period"][0:-1]
    print("Observation period prior to update:" + observation_period)    

    # Create the new value for the target config key
    observation_period = int(observation_period) - 1
    observation_period = str(observation_period) + "s"

    # Update the config object with the new value
    recommender_config.recommender_generation_config.params["observation_period"]=observation_period

    # Create the update request object from the updated config
    update_request = recommender_v1beta1.UpdateRecommenderConfigRequest(
        recommender_config=recommender_config,
    )

    # Make the update request
    update_response = client.update_recommender_config(request=update_request)

    # Remake the get request, assign results to config object
    recommender_config = client.get_recommender_config(request=get_request)

    # Get and print the current value
    observation_period = recommender_config.recommender_generation_config.params["observation_period"][0:-1]
    print("Observation period after update:" + observation_period)

# [END recommender_v1beta1_generated_Recommender_UpdateRecommenderConfig_sync]
