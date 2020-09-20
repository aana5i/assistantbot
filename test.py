# -*- coding: utf-8 -*-
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator("rama.ahn@gmail.com", "a$tAte11")
discovery = DiscoveryV1(version='2018-08-01', authenticator=authenticator)
discovery.set_service_url('<url_as_per_region>')


"ja-JP_EmiV3Voice"
"こんばんは"
