# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.ccc.v20200210 import models


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.tencentcloudapi.com'
    _service = 'ccc'


    def AbortPredictiveDialingCampaign(self, request):
        """This API is used to pause the predictive outbound call task.

        :param request: Request instance for AbortPredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.AbortPredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AbortPredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AbortPredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.AbortPredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindNumberCallOutSkillGroup(self, request):
        """This API is used to bind outbound skill group of number.

        :param request: Request instance for BindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindStaffSkillGroupList(self, request):
        """This API is used to bind the agent's skill group.

        :param request: Request instance for BindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.BindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAdminURL(self, request):
        """This API is used to create a management access link.

        :param request: Request instance for CreateAdminURL.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAdminURL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAdminURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoCalloutTask(self, request):
        """This API is used to create the automatic outbound call task.

        :param request: Request instance for CreateAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCCCSkillGroup(self, request):
        """This API is used to create a new skill group.

        :param request: Request instance for CreateCCCSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCCSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCCCSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCallOutSession(self, request):
        """This API is used to create outbound sessions. Currently, only dual call is supported. That is, firstly, please use the platform number to call the agent's cell phone. After the agent answers, then please make outbound calls to the user. Due to ISP frequency restrictions, the agent's phone number must first be added to the allowlist to avoid frequency control which may lead to the failure of the outbound call.

        :param request: Request instance for CreateCallOutSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCallOutSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCallOutSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExtension(self, request):
        """This API is used to create the telephone account.

        :param request: Request instance for CreateExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExtension", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePredictiveDialingCampaign(self, request):
        """This API is used to create the predictive outbound call task.

        :param request: Request instance for CreatePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreatePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreatePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSDKLoginToken(self, request):
        """This API is used to create the SDK log-in token.

        :param request: Request instance for CreateSDKLoginToken.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSDKLoginToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSDKLoginTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStaff(self, request):
        """This API is used to create the customer service account.

        :param request: Request instance for CreateStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStaff", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExtension(self, request):
        """This API is used to delete telephone accounts.

        :param request: Request instance for DeleteExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePredictiveDialingCampaign(self, request):
        """This API is used to delete the predictive outbound call task.

        :param request: Request instance for DeletePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeletePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeletePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStaff(self, request):
        """This API is used to delete the agent information.

        :param request: Request instance for DeleteStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStaff", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTask(self, request):
        """This API is used to query automatic outbound call task details.

        :param request: Request instance for DescribeAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTasks(self, request):
        """This API is used to query auto-task outbound calls in batch.

        :param request: Request instance for DescribeAutoCalloutTasks.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCCBuyInfoList(self, request):
        """This API is used to access the user purchasing information list.

        :param request: Request instance for DescribeCCCBuyInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCCBuyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCCBuyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallInMetrics(self, request):
        """This API is used to access the inbound real-time data statistical metrics.

        :param request: Request instance for DescribeCallInMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallInMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallInMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtension(self, request):
        """This API is used to access the telephone information.

        :param request: Request instance for DescribeExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtensions(self, request):
        """This API is used to query the telephone list information.

        :param request: Request instance for DescribeExtensions.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNumbers(self, request):
        """This API is used to query the number list.

        :param request: Request instance for DescribeNumbers.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNumbers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNumbersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePSTNActiveSessionList(self, request):
        """This API is used to access the current calling session list.

        :param request: Request instance for DescribePSTNActiveSessionList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePSTNActiveSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePSTNActiveSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingCampaign(self, request):
        """This API is used to query the predictive outbound call task.

        :param request: Request instance for DescribePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingCampaigns(self, request):
        """This API is used to query the predictive outbound call task list.

        :param request: Request instance for DescribePredictiveDialingCampaigns.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingCampaigns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingCampaignsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingSessions(self, request):
        """This API is used to query the predictive outbound call list.

        :param request: Request instance for DescribePredictiveDialingSessions.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingSessionsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectedTelCdr(self, request):
        """This API is used to access protected phone service records and recordings for both inbound and outbound calls.

        :param request: Request instance for DescribeProtectedTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectedTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectedTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillGroupInfoList(self, request):
        """This API is used to access the skill group information list.

        :param request: Request instance for DescribeSkillGroupInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillGroupInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillGroupInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffInfoList(self, request):
        """This API is used to access the agent information list.

        :param request: Request instance for DescribeStaffInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffStatusMetrics(self, request):
        """This API is used to access the real-time status statistics metrics of the agent.

        :param request: Request instance for DescribeStaffStatusMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffStatusMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffStatusMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCallInfo(self, request):
        """This API is used to access telephone consumption statistics by instance.

        :param request: Request instance for DescribeTelCallInfo.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCallInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCallInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCdr(self, request):
        """This API is used to access phone service records and recordings.

        :param request: Request instance for DescribeTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelSession(self, request):
        """This API is used to access the PSTN session information.

        :param request: Request instance for DescribeTelSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCCCPhoneNumber(self, request):
        """This API is used to disable numbers.

        :param request: Request instance for DisableCCCPhoneNumber.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCCCPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCCCPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HangUpCall(self, request):
        """This API is used to hang up the phone.

        :param request: Request instance for HangUpCall.
        :type request: :class:`tencentcloud.ccc.v20200210.models.HangUpCallRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.HangUpCallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HangUpCall", params, headers=headers)
            response = json.loads(body)
            model = models.HangUpCallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExtension(self, request):
        """This API is used to modify telephone accounts (binding skill group, binding agent account).

        :param request: Request instance for ModifyExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExtension", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStaff(self, request):
        """This API is used to modify the customer service account.

        :param request: Request instance for ModifyStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStaff", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PausePredictiveDialingCampaign(self, request):
        """This API is used to pause the predictive outbound call task.

        :param request: Request instance for PausePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.PausePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.PausePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PausePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.PausePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetExtensionPassword(self, request):
        """This API is used to reset the telephone register password.

        :param request: Request instance for ResetExtensionPassword.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetExtensionPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetExtensionPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumePredictiveDialingCampaign(self, request):
        """This API is used to resume the predictive outbound call task.

        :param request: Request instance for ResumePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ResumePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ResumePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.ResumePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAutoCalloutTask(self, request):
        """This API is used to stop the automatic outbound call task.

        :param request: Request instance for StopAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindNumberCallOutSkillGroup(self, request):
        """This API is used to unbind the number from the outbound call skill group.

        :param request: Request instance for UnbindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindStaffSkillGroupList(self, request):
        """This API is used to unbind the agent's skill group.

        :param request: Request instance for UnbindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCCCSkillGroup(self, request):
        """This API is used to update the skill group.

        :param request: Request instance for UpdateCCCSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UpdateCCCSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UpdateCCCSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCCCSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCCCSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePredictiveDialingCampaign(self, request):
        """This API is used to update the predictive outbound call task before it starts.

        :param request: Request instance for UpdatePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UpdatePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UpdatePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))