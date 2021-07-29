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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param SecurityGroupId: ID of the security group to be associated in the format of sg-efil73jd.
        :type SecurityGroupId: str
        :param InstanceIds: ID(s) of the instance(s) to be associated in the format of tdsqlshard-lesecurk. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BriefNodeInfo(AbstractModel):
    """Node information of a sharded database

    """

    def __init__(self):
        """
        :param NodeId: Node ID
        :type NodeId: str
        :param Role: Node role. Valid values: `master`, `slave`
        :type Role: str
        :param ShardId: The ID of the shard where the node resides
        :type ShardId: str
        """
        self.NodeId = None
        self.Role = None
        self.ShardId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Role = params.get("Role")
        self.ShardId = params.get("ShardId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountRequest(AbstractModel):
    """CloneAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SrcUser: Source user account name
        :type SrcUser: str
        :param SrcHost: Source user host
        :type SrcHost: str
        :param DstUser: Target user account name
        :type DstUser: str
        :param DstHost: Target user host
        :type DstHost: str
        :param DstDesc: Description of a target account
        :type DstDesc: str
        """
        self.InstanceId = None
        self.SrcUser = None
        self.SrcHost = None
        self.DstUser = None
        self.DstHost = None
        self.DstDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUser = params.get("SrcUser")
        self.SrcHost = params.get("SrcHost")
        self.DstUser = params.get("DstUser")
        self.DstHost = params.get("DstHost")
        self.DstDesc = params.get("DstDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneAccountResponse(AbstractModel):
    """CloneAccount response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task flow ID
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of an instance for which to disable public network access. The ID is in the format of dcdbt-ow728lmc and can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ConstraintRange(AbstractModel):
    """Range of constraint type values

    """

    def __init__(self):
        """
        :param Min: Minimum value when constraint type is `section`
        :type Min: str
        :param Max: Maximum value when constraint type is `section`
        :type Max: str
        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param SrcUserName: Source username
        :type SrcUserName: str
        :param SrcHost: Access host allowed for a source user
        :type SrcHost: str
        :param DstUserName: Target username
        :type DstUserName: str
        :param DstHost: Access host allowed for a target user
        :type DstHost: str
        :param SrcReadOnly: `ReadOnly` attribute of a source account
        :type SrcReadOnly: str
        :param DstReadOnly: `ReadOnly` attribute of a target account
        :type DstReadOnly: str
        """
        self.InstanceId = None
        self.SrcUserName = None
        self.SrcHost = None
        self.DstUserName = None
        self.DstHost = None
        self.SrcReadOnly = None
        self.DstReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUserName = params.get("SrcUserName")
        self.SrcHost = params.get("SrcHost")
        self.DstUserName = params.get("DstUserName")
        self.DstHost = params.get("DstHost")
        self.SrcReadOnly = params.get("SrcReadOnly")
        self.DstReadOnly = params.get("DstReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param UserName: AccountName
        :type UserName: str
        :param Host: Host that can be logged in to, which is in the same format as the host of the MySQL account and supports wildcards, such as %, 10.%, and 10.20.%.
        :type Host: str
        :param Password: Account password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        :param ReadOnly: Whether to create a read-only account. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail; 3: only the secondary will be read from.
        :type ReadOnly: int
        :param Description: Account remarks, which can contain 0-256 letters, digits, and common symbols.
        :type Description: str
        :param DelayThresh: If the secondary delay exceeds the set value of this parameter, the secondary will be deemed to have failed.
It is recommended that this parameter be set to a value greater than 10. This parameter takes effect when `ReadOnly` is 1 or 2.
        :type DelayThresh: int
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")
        self.DelayThresh = params.get("DelayThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param UserName: Username, which is passed through from the input parameters.
        :type UserName: str
        :param Host: Host allowed for access, which is passed through from the input parameters.
        :type Host: str
        :param ReadOnly: Passed through from the input parameters.
        :type ReadOnly: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.ReadOnly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.ReadOnly = params.get("ReadOnly")
        self.RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """TencentDB account information

    """

    def __init__(self):
        """
        :param UserName: Username
        :type UserName: str
        :param Host: Host from which a user can log in (corresponding to the `host` field for a MySQL user; a user is uniquely identified by username and host; this parameter is in IP format and ends with % for IP range; % can be entered; if this parameter is left empty, % will be used by default)
        :type Host: str
        :param Description: User remarks
        :type Description: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Last updated time
        :type UpdateTime: str
        :param ReadOnly: Read-only flag. 0: no; 1: for the account's SQL requests, the secondary will be used first, and if it is unavailable, the primary will be used; 2: the secondary will be used first, and if it is unavailable, the operation will fail.
        :type ReadOnly: int
        :param DelayThresh: If the secondary delay exceeds the set value of this parameter, the secondary will be deemed to have failed.
It is recommended that this parameter be set to a value greater than 10. This parameter takes effect when `ReadOnly` is 1 or 2.
        :type DelayThresh: int
        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")
        self.DelayThresh = params.get("DelayThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DBParamValue(AbstractModel):
    """TencentDB parameter information.

    """

    def __init__(self):
        """
        :param Param: Parameter name
        :type Param: str
        :param Value: Parameter value
        :type Value: str
        """
        self.Param = None
        self.Value = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBInstanceInfo(AbstractModel):
    """TDSQL instance information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param AppId: Application ID
        :type AppId: int
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Region: Region
        :type Region: str
        :param Zone: AZ
        :type Zone: str
        :param VpcId: Numeric ID of a VPC
        :type VpcId: int
        :param SubnetId: Subnet Digital ID
        :type SubnetId: int
        :param StatusDesc: Status description
        :type StatusDesc: str
        :param Status: Instance status. Valid values: `0` (creating), `1` (running task), `2` (running), `3` (uninitialized), `-1` (isolated), `4` (initializing), `5` (eliminating), `6` (restarting), `7` (migrating data)
        :type Status: int
        :param Vip: Private IP
        :type Vip: str
        :param Vport: Private network port
        :type Vport: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param AutoRenewFlag: Auto-renewal flag
        :type AutoRenewFlag: int
        :param Memory: Memory size in GB
        :type Memory: int
        :param Storage: Storage capacity in GB
        :type Storage: int
        :param ShardCount: Number of shards
        :type ShardCount: int
        :param PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param IsolatedTimestamp: Isolation time
        :type IsolatedTimestamp: str
        :param Uin: Account ID
        :type Uin: str
        :param ShardDetail: Shard details
        :type ShardDetail: list of ShardInfo
        :param NodeCount: Number of nodes. 2: one master and one slave; 3: one master and two slaves
        :type NodeCount: int
        :param IsTmp: Temporary instance flag. 0: non-temporary instance
        :type IsTmp: int
        :param ExclusterId: Dedicated cluster ID. If this parameter is empty, the instance is a non-dedicated cluster instance
        :type ExclusterId: str
        :param UniqueVpcId: VPC ID in string type
        :type UniqueVpcId: str
        :param UniqueSubnetId: VPC subnet ID in string type
        :type UniqueSubnetId: str
        :param Id: Numeric ID of instance (this field is obsolete and should not be depended on)
        :type Id: int
        :param WanDomain: Domain name for public network access, which can be resolved by the public network
        :type WanDomain: str
        :param WanVip: Public IP address, which can be accessed over the public network
        :type WanVip: str
        :param WanPort: Public network port
        :type WanPort: int
        :param Pid: Product type ID (this field is obsolete and should not be depended on)
        :type Pid: int
        :param UpdateTime: Last updated time of an instance in the format of 2006-01-02 15:04:05
        :type UpdateTime: str
        :param DbEngine: Database engine
        :type DbEngine: str
        :param DbVersion: Database engine version
        :type DbVersion: str
        :param Paymode: Billing mode
        :type Paymode: str
        :param Locker: Async task flow ID when an async task is in progress on an instance
Note: this field may return null, indicating that no valid values can be obtained.
        :type Locker: int
        :param WanStatus: Public network access status. 0: not enabled; 1: enabled; 2: disabled; 3: enabling
        :type WanStatus: int
        :param IsAuditSupported: Whether the instance supports audit. 1: yes; 0: no
        :type IsAuditSupported: int
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Ipv6Flag: Indicates whether the instance uses IPv6
Note: this field may return null, indicating that no valid values can be obtained.
        :type Ipv6Flag: int
        :param Vipv6: Private network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vipv6: str
        :param WanVipv6: Public network IPv6 address
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanVipv6: str
        :param WanPortIpv6: Public network IPv6 port
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanPortIpv6: int
        :param WanStatusIpv6: Public network IPv6 status
Note: this field may return null, indicating that no valid values can be obtained.
        :type WanStatusIpv6: int
        :param DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param DcnStatus: DCN status. Valid values: 0 (null), 1 (creating), 2 (syncing), 3 (disconnected)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnStatus: int
        :param DcnDstNum: The number of DCN disaster recovery instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnDstNum: int
        :param InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (standard primary instance), `3` (standard disaster recovery instance), `4` (dedicated disaster recovery instance)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.StatusDesc = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.AutoRenewFlag = None
        self.Memory = None
        self.Storage = None
        self.ShardCount = None
        self.PeriodEndTime = None
        self.IsolatedTimestamp = None
        self.Uin = None
        self.ShardDetail = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.Id = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.Pid = None
        self.UpdateTime = None
        self.DbEngine = None
        self.DbVersion = None
        self.Paymode = None
        self.Locker = None
        self.WanStatus = None
        self.IsAuditSupported = None
        self.Cpu = None
        self.Ipv6Flag = None
        self.Vipv6 = None
        self.WanVipv6 = None
        self.WanPortIpv6 = None
        self.WanStatusIpv6 = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.DcnDstNum = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StatusDesc = params.get("StatusDesc")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardCount = params.get("ShardCount")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self.ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ShardDetail.append(obj)
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.Id = params.get("Id")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.Pid = params.get("Pid")
        self.UpdateTime = params.get("UpdateTime")
        self.DbEngine = params.get("DbEngine")
        self.DbVersion = params.get("DbVersion")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.Cpu = params.get("Cpu")
        self.Ipv6Flag = params.get("Ipv6Flag")
        self.Vipv6 = params.get("Vipv6")
        self.WanVipv6 = params.get("WanVipv6")
        self.WanPortIpv6 = params.get("WanPortIpv6")
        self.WanStatusIpv6 = params.get("WanStatusIpv6")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.DcnDstNum = params.get("DcnDstNum")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DCDBShardInfo(AbstractModel):
    """Information of a TDSQL shard.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ShardSerialId: Shard SQL passthrough ID, which is used to pass through SQL statements to the specified shard for execution
        :type ShardSerialId: str
        :param ShardInstanceId: Globally unique shard ID
        :type ShardInstanceId: str
        :param Status: Status. 0: creating; 1: processing; 2: running; 3: shard not initialized
        :type Status: int
        :param StatusDesc: Status description
        :type StatusDesc: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param VpcId: VPC ID in string format
        :type VpcId: str
        :param SubnetId: VPC subnet ID in string format
        :type SubnetId: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Region: Region
        :type Region: str
        :param Zone: AZ
        :type Zone: str
        :param Memory: Memory size in GB
        :type Memory: int
        :param Storage: Storage capacity in GB
        :type Storage: int
        :param PeriodEndTime: Expiration time
        :type PeriodEndTime: str
        :param NodeCount: Number of nodes. 2: one primary and one secondary; 3: one primary and two secondaries
        :type NodeCount: int
        :param StorageUsage: Storage utilization in %
        :type StorageUsage: float
        :param MemoryUsage: Memory utilization in %
        :type MemoryUsage: float
        :param ShardId: Numeric ID of a shard (this field is obsolete and should not be depended on)
        :type ShardId: int
        :param Pid: ProductID
        :type Pid: int
        :param ProxyVersion: Proxy version
        :type ProxyVersion: str
        :param Paymode: Billing mode
Note: this field may return null, indicating that no valid values can be obtained.
        :type Paymode: str
        :param ShardMasterZone: Master AZ of a shard
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardMasterZone: str
        :param ShardSlaveZones: List of secondary AZs of a shard
Note: this field may return null, indicating that no valid values can be obtained.
        :type ShardSlaveZones: list of str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Range: The value range of shardkey, which includes 64 hash values, such as 0-31, 32-63.
        :type Range: str
        """
        self.InstanceId = None
        self.ShardSerialId = None
        self.ShardInstanceId = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.PeriodEndTime = None
        self.NodeCount = None
        self.StorageUsage = None
        self.MemoryUsage = None
        self.ShardId = None
        self.Pid = None
        self.ProxyVersion = None
        self.Paymode = None
        self.ShardMasterZone = None
        self.ShardSlaveZones = None
        self.Cpu = None
        self.Range = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NodeCount = params.get("NodeCount")
        self.StorageUsage = params.get("StorageUsage")
        self.MemoryUsage = params.get("MemoryUsage")
        self.ShardId = params.get("ShardId")
        self.Pid = params.get("Pid")
        self.ProxyVersion = params.get("ProxyVersion")
        self.Paymode = params.get("Paymode")
        self.ShardMasterZone = params.get("ShardMasterZone")
        self.ShardSlaveZones = params.get("ShardSlaveZones")
        self.Cpu = params.get("Cpu")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """Database information

    """

    def __init__(self):
        """
        :param DbName: Database name
        :type DbName: str
        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseFunction(AbstractModel):
    """Database function information

    """

    def __init__(self):
        """
        :param Func: Function name
        :type Func: str
        """
        self.Func = None


    def _deserialize(self, params):
        self.Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseProcedure(AbstractModel):
    """Database stored procedure information

    """

    def __init__(self):
        """
        :param Proc: Stored procedure name
        :type Proc: str
        """
        self.Proc = None


    def _deserialize(self, params):
        self.Proc = params.get("Proc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTable(AbstractModel):
    """Database table information

    """

    def __init__(self):
        """
        :param Table: Table name
        :type Table: str
        """
        self.Table = None


    def _deserialize(self, params):
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseView(AbstractModel):
    """Database view information

    """

    def __init__(self):
        """
        :param View: View name
        :type View: str
        """
        self.View = None


    def _deserialize(self, params):
        self.View = params.get("View")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DcnDetailItem(AbstractModel):
    """DCN details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Region: Region where the instance resides
        :type Region: str
        :param Zone: Availability zone where the instance resides
        :type Zone: str
        :param Vip: Instance IP address
        :type Vip: str
        :param Vipv6: Instance IPv6 address
        :type Vipv6: str
        :param Vport: Instance port
        :type Vport: int
        :param Status: Instance status
        :type Status: int
        :param StatusDesc: Instance status description
        :type StatusDesc: str
        :param DcnFlag: DCN flag. Valid values: `1` (primary), `2` (disaster recovery)
        :type DcnFlag: int
        :param DcnStatus: DCN status. Valid values: `0` (none), `1` (creating), `2` (syncing), `3` (disconnected)
        :type DcnStatus: int
        :param Cpu: Number of CPU cores of the instance
        :type Cpu: int
        :param Memory: Instance memory capacity in GB
        :type Memory: int
        :param Storage: Instance storage capacity in GB
        :type Storage: int
        :param PayMode: Billing mode
        :type PayMode: int
        :param CreateTime: Creation time of the instance in the format of 2006-01-02 15:04:05
        :type CreateTime: str
        :param PeriodEndTime: Expiration time of the instance in the format of 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param InstanceType: Instance type. Valid values: `1` (dedicated primary instance), `2` (non-dedicated primary instance), `3` (non-dedicated disaster recovery instance), and `4` (dedicated disaster recovery instance).
        :type InstanceType: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.Vip = None
        self.Vipv6 = None
        self.Vport = None
        self.Status = None
        self.StatusDesc = None
        self.DcnFlag = None
        self.DcnStatus = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.PayMode = None
        self.CreateTime = None
        self.PeriodEndTime = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vipv6 = params.get("Vipv6")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DcnFlag = params.get("DcnFlag")
        self.DcnStatus = params.get("DcnStatus")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PayMode = params.get("PayMode")
        self.CreateTime = params.get("CreateTime")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc, which can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceId: str
        :param UserName: Username
        :type UserName: str
        :param Host: Access host allowed for a user
        :type Host: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored
        :type DbName: str
        :param Type: Type. Valid values: table; view; proc; func; \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be queried (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param Object: Type name. For example, if `Type` is table, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param ColName: If `Type` = table and `ColName` is `\*`, the permissions of the table will be queried; if `ColName` is a specific field name, the permissions of the corresponding field will be queried
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Privileges: List of permissions.
        :type Privileges: list of str
        :param UserName: Database account username
        :type UserName: str
        :param Host: Database account host
        :type Host: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Privileges = None
        self.UserName = None
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Privileges = params.get("Privileges")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is passed through from the input parameters.
        :type InstanceId: str
        :param Users: List of instance users.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Users: list of DBAccount
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param ShardId: Shard ID in the format of shard-7noic7tv
        :type ShardId: str
        :param Type: Requested log type. Valid values: 1 (binlog); 2 (cold backup); 3 (errlog); 4 (slowlog).
        :type Type: int
        """
        self.InstanceId = None
        self.ShardId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param Type: Requested log type. Valid values: 1 (binlog); 2 (cold backup); 3 (errlog); 4 (slowlog).
        :type Type: int
        :param Total: Total number of requested logs
        :type Total: int
        :param Files: List of log files
        :type Files: list of LogFileInfo
        :param VpcPrefix: For an instance in a VPC, this prefix plus URI can be used as the download address
        :type VpcPrefix: str
        :param NormalPrefix: For an instance in a common network, this prefix plus URI can be used as the download address
        :type NormalPrefix: str
        :param ShardId: Shard ID in the format of shard-7noic7tv
        :type ShardId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
        self.ShardId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Total = params.get("Total")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self.Files.append(obj)
        self.VpcPrefix = params.get("VpcPrefix")
        self.NormalPrefix = params.get("NormalPrefix")
        self.ShardId = params.get("ShardId")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param Params: Requests the current parameter values of a DB
        :type Params: list of ParamDesc
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Params = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self.Params.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.Product = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details
        :type Groups: list of SecurityGroup
        :param VIP: Instance VIP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VIP: str
        :param VPort: Instance port
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VPort: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Groups = None
        self.VIP = None
        self.VPort = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.VIP = params.get("VIP")
        self.VPort = params.get("VPort")
        self.RequestId = params.get("RequestId")


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of an instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode response structure.

    """

    def __init__(self):
        """
        :param SyncMode: Sync mode. 0: async; 1: strong sync; 2: downgradable strong sync
        :type SyncMode: int
        :param IsModifying: Whether a modification is in progress. 1: yes; 0: no.
        :type IsModifying: int
        :param CurrentSyncMode: Current sync mode. Valid values: `0` (async), `1` (sync).
        :type CurrentSyncMode: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SyncMode = None
        self.IsModifying = None
        self.CurrentSyncMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SyncMode = params.get("SyncMode")
        self.IsModifying = params.get("IsModifying")
        self.CurrentSyncMode = params.get("CurrentSyncMode")
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstanceNodeInfoRequest(AbstractModel):
    """DescribeDCDBInstanceNodeInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Limit: The maximum number of results returned at a time. Value range: (0-100]. Default value: `100`.
        :type Limit: int
        :param Offset: Offset of the returned results. Default value: `0`.
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstanceNodeInfoResponse(AbstractModel):
    """DescribeDCDBInstanceNodeInfo response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of nodes
        :type TotalCount: int
        :param NodesInfo: Node information
        :type NodesInfo: list of BriefNodeInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.NodesInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodesInfo") is not None:
            self.NodesInfo = []
            for item in params.get("NodesInfo"):
                obj = BriefNodeInfo()
                obj._deserialize(item)
                self.NodesInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Query by instance ID or IDs. Instance ID is in the format of dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param SearchName: Search field name. Valid values: instancename (search by instance name); vip (search by private IP); all (search by instance ID, instance name, and private IP).
        :type SearchName: str
        :param SearchKey: Search keyword. Fuzzy search is supported. Multiple keywords should be separated by line breaks (`\n`).
        :type SearchKey: str
        :param ProjectIds: Query by project ID
        :type ProjectIds: list of int
        :param IsFilterVpc: Whether to search by VPC
        :type IsFilterVpc: bool
        :param VpcId: VPC ID, which is valid when `IsFilterVpc` is 1
        :type VpcId: str
        :param SubnetId: VPC subnet ID, which is valid when `IsFilterVpc` is 1
        :type SubnetId: str
        :param OrderBy: Sort by field. Valid values: projectId; createtime; instancename
        :type OrderBy: str
        :param OrderByType: Sort by type. Valid values: desc; asc
        :type OrderByType: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Number of returned results. Default value: 10. Maximum value: 100.
        :type Limit: int
        :param ExclusterType: 1: non-dedicated cluster; 2: dedicated cluster; 0: all
        :type ExclusterType: int
        :param IsFilterExcluster: Identifies whether to use the `ExclusterType` field. false: no; true: yes
        :type IsFilterExcluster: bool
        :param ExclusterIds: Dedicated cluster ID
        :type ExclusterIds: list of str
        :param TagKeys: Tag key used in queries
        :type TagKeys: list of str
        :param FilterInstanceType: Instance types used in filtering. Valid values: 1 (dedicated instance), 2 (primary instance), 3 (disaster recovery instance). Multiple values should be separated by commas.
        :type FilterInstanceType: str
        :param Status: Use this filter to include instances in specific statuses
        :type Status: list of int
        :param ExcludeStatus: Use this filter to exclude instances in specific statuses
        :type ExcludeStatus: list of int
        """
        self.InstanceIds = None
        self.SearchName = None
        self.SearchKey = None
        self.ProjectIds = None
        self.IsFilterVpc = None
        self.VpcId = None
        self.SubnetId = None
        self.OrderBy = None
        self.OrderByType = None
        self.Offset = None
        self.Limit = None
        self.ExclusterType = None
        self.IsFilterExcluster = None
        self.ExclusterIds = None
        self.TagKeys = None
        self.FilterInstanceType = None
        self.Status = None
        self.ExcludeStatus = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SearchName = params.get("SearchName")
        self.SearchKey = params.get("SearchKey")
        self.ProjectIds = params.get("ProjectIds")
        self.IsFilterVpc = params.get("IsFilterVpc")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ExclusterType = params.get("ExclusterType")
        self.IsFilterExcluster = params.get("IsFilterExcluster")
        self.ExclusterIds = params.get("ExclusterIds")
        self.TagKeys = params.get("TagKeys")
        self.FilterInstanceType = params.get("FilterInstanceType")
        self.Status = params.get("Status")
        self.ExcludeStatus = params.get("ExcludeStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param Instances: List of instance details
        :type Instances: list of DCDBInstanceInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param ShardInstanceIds: Shard ID list.
        :type ShardInstanceIds: list of str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param OrderBy: Sort by field. Only `createtime` is supported currently
        :type OrderBy: str
        :param OrderByType: Sort by type. Valid values: desc; asc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.ShardInstanceIds = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible shards
        :type TotalCount: int
        :param Shards: Shard information list
        :type Shards: list of DCDBShardInfo
        :param DcnFlag: DCN type. Valid values: 0 (null), 1 (primary instance), 2 (disaster recovery instance)
Note: this field may return null, indicating that no valid values can be obtained.
        :type DcnFlag: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Shards = None
        self.DcnFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Shards") is not None:
            self.Shards = []
            for item in params.get("Shards"):
                obj = DCDBShardInfo()
                obj._deserialize(item)
                self.Shards.append(obj)
        self.DcnFlag = params.get("DcnFlag")
        self.RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        """
        self.InstanceId = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Passed through from the input parameters.
        :type InstanceId: str
        :param DbName: Database name.
        :type DbName: str
        :param Tables: List of tables.
        :type Tables: list of DatabaseTable
        :param Views: List of views.
        :type Views: list of DatabaseView
        :param Procs: List of stored procedures.
        :type Procs: list of DatabaseProcedure
        :param Funcs: List of functions.
        :type Funcs: list of DatabaseFunction
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Tables = None
        self.Views = None
        self.Procs = None
        self.Funcs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self.Tables.append(obj)
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self.Views.append(obj)
        if params.get("Procs") is not None:
            self.Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self.Procs.append(obj)
        if params.get("Funcs") is not None:
            self.Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self.Funcs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        :param DbName: Database name, which can be obtained through the `DescribeDatabases` API.
        :type DbName: str
        :param Table: Table name, which can be obtained through the `DescribeDatabaseObjects` API.
        :type Table: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance name.
        :type InstanceId: str
        :param DbName: Database name.
        :type DbName: str
        :param Table: Table name.
        :type Table: str
        :param Cols: Column information.
        :type Cols: list of TableColumn
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None
        self.Cols = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")
        if params.get("Cols") is not None:
            self.Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self.Cols.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow7t8lmc.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        """
        :param Databases: List of databases on an instance.
        :type Databases: list of Database
        :param InstanceId: Passed through from the input parameters.
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Databases = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeDcnDetailRequest(AbstractModel):
    """DescribeDcnDetail request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDcnDetailResponse(AbstractModel):
    """DescribeDcnDetail response structure.

    """

    def __init__(self):
        """
        :param DcnDetails: DCN synchronization details
        :type DcnDetails: list of DcnDetailItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DcnDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DcnDetails") is not None:
            self.DcnDetails = []
            for item in params.get("DcnDetails"):
                obj = DcnDetailItem()
                obj._deserialize(item)
                self.DcnDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Task ID returned by an async request API.
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow response structure.

    """

    def __init__(self):
        """
        :param Status: Task status. Valid values: `0` (succeeded), `1` (failed), `2` (running)
        :type Status: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param ProjectId: Project ID
        :type ProjectId: int
        """
        self.Product = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Groups: Security group details
        :type Groups: list of SecurityGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects request structure.

    """


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects response structure.

    """

    def __init__(self):
        """
        :param Projects: Project list
        :type Projects: list of Project
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Projects = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyDCDBInstanceRequest(AbstractModel):
    """DestroyDCDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of tdsqlshard-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyDCDBInstanceResponse(AbstractModel):
    """DestroyDCDBInstance response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DestroyHourDCDBInstanceRequest(AbstractModel):
    """DestroyHourDCDBInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of tdsqlshard-c1nl9rpv. It is the same as the instance ID displayed in the TencentDB console.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyHourDCDBInstanceResponse(AbstractModel):
    """DestroyHourDCDBInstance response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID, which can be used in the [DescribeFlow](https://intl.cloud.tencent.com/document/product/557/56485?from_cn_redirect=1) API to query the async task result.
        :type FlowId: int
        :param InstanceId: Instance ID, which is the same as the request parameter `InstanceId`.
        :type InstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param InstanceIds: Instance ID list, which is an array of one or more instance IDs.
        :type InstanceIds: list of str
        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param DbName: Database name. `\*` indicates that global permissions will be queried (i.e., `\*.\*`), in which case the `Type` and `Object ` parameters will be ignored
        :type DbName: str
        :param Privileges: Global permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE TEMPORARY TABLES; LOCK TABLES; EXECUTE; CREATE VIEW; SHOW VIEW; CREATE ROUTINE; ALTER ROUTINE; EVENT; TRIGGER; SHOW DATABASES 
Database permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE TEMPORARY TABLES; LOCK TABLES; EXECUTE; CREATE VIEW; SHOW VIEW; CREATE ROUTINE; ALTER ROUTINE; EVENT; TRIGGER 
Table/view permission. Valid values: SELECT; INSERT; UPDATE; DELETE; CREATE; DROP; REFERENCES; INDEX; ALTER; CREATE VIEW; SHOW VIEW; TRIGGER 
Stored procedure/function permission. Valid values: ALTER ROUTINE; EXECUTE 
Field permission. Valid values: INSERT; REFERENCES; SELECT; UPDATE
        :type Privileges: list of str
        :param Type: Type. Valid values: table; view; proc; func; \*. If `DbName` is a specific database name and `Type` is `\*`, the permissions of the database will be set (i.e., `db.\*`), in which case the `Object` parameter will be ignored
        :type Type: str
        :param Object: Type name. For example, if `Type` is table, `Object` indicates a specific table name; if both `DbName` and `Type` are specific names, it indicates a specific object name and cannot be `\*` or empty
        :type Object: str
        :param ColName: If `Type` = table and `ColName` is `\*`, the permissions will be granted to the table; if `ColName` is a specific field name, the permissions will be granted to the field
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Privileges = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Privileges = params.get("Privileges")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be initialized. The ID is in the format of `dcdbt-ow728lmc` and can be obtained through the `DescribeDCDBInstances` API.
        :type InstanceIds: list of str
        :param Params: List of parameters. Valid values: character_set_server (character set; required); lower_case_table_names (table name case sensitivity; required; 0: case-sensitive; 1: case-insensitive); innodb_page_size (InnoDB data page; default size: 16 KB); sync_mode (sync mode; 0: async; 1: strong sync; 2: downgradable strong sync; default value: strong sync).
        :type Params: list of DBParamValue
        """
        self.InstanceIds = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances response structure.

    """

    def __init__(self):
        """
        :param FlowIds: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowIds: list of int non-negative
        :param InstanceIds: Passed through from the input parameters.
        :type InstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """Information of a pulled log

    """

    def __init__(self):
        """
        :param Mtime: Last modified time of a log
        :type Mtime: int
        :param Length: File length
        :type Length: int
        :param Uri: Uniform resource identifier (URI) used during log download
        :type Uri: str
        :param FileName: Filename
        :type FileName: str
        """
        self.Mtime = None
        self.Length = None
        self.Uri = None
        self.FileName = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param Description: New account remarks, which can contain 0-256 characters.
        :type Description: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups request structure.

    """

    def __init__(self):
        """
        :param Product: Database engine name. Valid value: `dcdb`.
        :type Product: str
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SecurityGroupIds: List of IDs of security groups to be modified, which is an array of one or more security group IDs.
        :type SecurityGroupIds: list of str
        """
        self.Product = None
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: List of IDs of instances to be modified. Instance ID is in the format of dcdbt-ow728lmc.
        :type InstanceIds: list of str
        :param ProjectId: ID of the project to be assigned, which can be obtained through the `DescribeProjects` API.
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param Params: List of parameters. Every element is a combination of `Param` and `Value`.
        :type Params: list of DBParamValue
        """
        self.InstanceId = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters response structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param Result: Parameter modification results
        :type Result: list of ParamModifyResult
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of an instance for which to modify the sync mode. The ID is in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param SyncMode: Sync mode. 0: async; 1: strong sync; 2: downgradable strong sync
        :type SyncMode: int
        """
        self.InstanceId = None
        self.SyncMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess request structure.

    """

    def __init__(self):
        """
        :param InstanceId: ID of an instance for which to enable public network access. The ID is in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param Ipv6Flag: Whether IPv6 is used. Default value: 0
        :type Ipv6Flag: int
        """
        self.InstanceId = None
        self.Ipv6Flag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ipv6Flag = params.get("Ipv6Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess response structure.

    """

    def __init__(self):
        """
        :param FlowId: Async task ID. The task status can be queried through the `DescribeFlow` API.
        :type FlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """Parameter constraint

    """

    def __init__(self):
        """
        :param Type: Constraint type, such as enum and section
        :type Type: str
        :param Enum: List of valid values when constraint type is `enum`
        :type Enum: str
        :param Range: Range when constraint type is `section`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Range: :class:`tencentcloud.dcdb.v20180411.models.ConstraintRange`
        :param String: List of valid values when constraint type is `string`
        :type String: str
        """
        self.Type = None
        self.Enum = None
        self.Range = None
        self.String = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Enum = params.get("Enum")
        if params.get("Range") is not None:
            self.Range = ConstraintRange()
            self.Range._deserialize(params.get("Range"))
        self.String = params.get("String")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamDesc(AbstractModel):
    """DB parameter description

    """

    def __init__(self):
        """
        :param Param: Parameter name
        :type Param: str
        :param Value: Current parameter value
        :type Value: str
        :param SetValue: Previously set value, which is the same as `value` after the parameter takes effect. If no value has been set, this field will not be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SetValue: str
        :param Default: Default value
        :type Default: str
        :param Constraint: Parameter constraint
        :type Constraint: :class:`tencentcloud.dcdb.v20180411.models.ParamConstraint`
        :param HaveSetValue: Whether a value has been set. false: no, true: yes
        :type HaveSetValue: bool
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None
        self.HaveSetValue = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))
        self.HaveSetValue = params.get("HaveSetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamModifyResult(AbstractModel):
    """Parameter modification result

    """

    def __init__(self):
        """
        :param Param: Renames a parameter
        :type Param: str
        :param Code: Result of parameter modification. 0: success; -1: failure; -2: invalid parameter value
        :type Code: int
        """
        self.Param = None
        self.Code = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    """Project description

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param OwnerUin: The UIN of the resource owner (root account)
        :type OwnerUin: int
        :param AppId: Application ID
        :type AppId: int
        :param Name: Project name
        :type Name: str
        :param CreatorUin: Creator UIN
        :type CreatorUin: int
        :param SrcPlat: Source platform
        :type SrcPlat: str
        :param SrcAppId: Source APPID
        :type SrcAppId: int
        :param Status: Project status. Valid values: `0` (normal), `-1` (disabled), `3` (default project).
        :type Status: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param IsDefault: Whether it is the default project. Valid values: `1` (yes), `0` (no).
        :type IsDefault: int
        :param Info: Description
        :type Info: str
        """
        self.ProjectId = None
        self.OwnerUin = None
        self.AppId = None
        self.Name = None
        self.CreatorUin = None
        self.SrcPlat = None
        self.SrcAppId = None
        self.Status = None
        self.CreateTime = None
        self.IsDefault = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.CreatorUin = params.get("CreatorUin")
        self.SrcPlat = params.get("SrcPlat")
        self.SrcAppId = params.get("SrcAppId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.IsDefault = params.get("IsDefault")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID in the format of dcdbt-ow728lmc.
        :type InstanceId: str
        :param UserName: Login username.
        :type UserName: str
        :param Host: Access host allowed for a user. An account is uniquely identified by username and host.
        :type Host: str
        :param Password: New password, which can contain 6-32 letters, digits, and common symbols but not semicolons, single quotation marks, and double quotation marks.
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """Security group details

    """

    def __init__(self):
        """
        :param ProjectId: Project ID
        :type ProjectId: int
        :param CreateTime: Creation time in the format of yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        :param SecurityGroupName: Security group name
        :type SecurityGroupName: str
        :param SecurityGroupRemark: Security group remarks
        :type SecurityGroupRemark: str
        :param Inbound: Inbound rule
        :type Inbound: list of SecurityGroupBound
        :param Outbound: Outbound rule
        :type Outbound: list of SecurityGroupBound
        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.Inbound = None
        self.Outbound = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = SecurityGroupBound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBound(AbstractModel):
    """Security group inbound/outbound rule

    """

    def __init__(self):
        """
        :param Action: Policy, which can be `ACCEPT` or `DROP`
        :type Action: str
        :param CidrIp: Source IP or source IP range, such as 192.168.0.0/16
        :type CidrIp: str
        :param PortRange: Port
        :type PortRange: str
        :param IpProtocol: Network protocol. UDP and TCP are supported.
        :type IpProtocol: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShardInfo(AbstractModel):
    """Shard information

    """

    def __init__(self):
        """
        :param ShardInstanceId: Shard ID
        :type ShardInstanceId: str
        :param ShardSerialId: Shard set ID
        :type ShardSerialId: str
        :param Status: Status. 0: creating; 1: processing; 2: running; 3: shard not initialized; -2: shard deleted
        :type Status: int
        :param Createtime: Creation time
        :type Createtime: str
        :param Memory: Memory size in GB
        :type Memory: int
        :param Storage: Storage capacity in GB
        :type Storage: int
        :param ShardId: Numeric ID of a shard
        :type ShardId: int
        :param NodeCount: Number of nodes. 2: one primary and one secondary; 3: one primary and two secondaries
        :type NodeCount: int
        :param Pid: Product type ID (this field is obsolete and should not be depended on)
        :type Pid: int
        :param Cpu: Number of CPU cores
        :type Cpu: int
        """
        self.ShardInstanceId = None
        self.ShardSerialId = None
        self.Status = None
        self.Createtime = None
        self.Memory = None
        self.Storage = None
        self.ShardId = None
        self.NodeCount = None
        self.Pid = None
        self.Cpu = None


    def _deserialize(self, params):
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.Status = params.get("Status")
        self.Createtime = params.get("Createtime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardId = params.get("ShardId")
        self.NodeCount = params.get("NodeCount")
        self.Pid = params.get("Pid")
        self.Cpu = params.get("Cpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """Database column information

    """

    def __init__(self):
        """
        :param Col: Column name
        :type Col: str
        :param Type: Column type
        :type Type: str
        """
        self.Col = None
        self.Type = None


    def _deserialize(self, params):
        self.Col = params.get("Col")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        