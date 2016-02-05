#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlobject
from sqlobject.sqlite import builder


# C:\Program Files (x86)\Thunder Network\Thunder\Profiles\TaskDb.dat
# TaskDb.dat 文件为迅雷任务存储文件
# 每个迅雷Profiles目录存都存在TaskDb.dat文件
# 迅雷自定义添加下载任务。运行前请关闭迅雷，并检查以上文件是否存在
class XLTaskDb:
    class P2spTask(sqlobject.SQLObject):
        # app_id = sqlobject.StringCol(length=14, unique=True)
        Id = sqlobject.BigIntCol(length=0, dbName='TaskId', alternateID=False)
        ResourceUsageStrategy = sqlobject.IntCol(length=0, dbName='ResourceUsageStrategy')
        ResourceReportStrategy = sqlobject.IntCol(length=0, dbName='ResourceReportStrategy')
        Cookie = sqlobject.StringCol(length=0)
        AccountNeeded = sqlobject.IntCol(length=0, dbName='AccountNeeded')
        UserName = sqlobject.StringCol(length=0, dbName='UserName')
        Password = sqlobject.StringCol(length=0)
        UseOriginResourceOnly = sqlobject.IntCol(length=0, dbName='UseOriginResourceOnly')
        OriginResourceSupportRange = sqlobject.IntCol(length=0, dbName='OriginResourceSupportRange')
        ReceiveOriginResourceSize = sqlobject.BigIntCol(length=0, dbName='ReceiveOriginResourceSize')
        OriginResourceRetryInterval = sqlobject.IntCol(length=0, dbName='OriginResourceRetryInterval')
        OriginResourceRetryTimes = sqlobject.IntCol(length=0, dbName='OriginResourceRetryTimes')
        OriginResourceThreadCount = sqlobject.IntCol(length=0, dbName='OriginResourceThreadCount')
        DownloadSpeedLimit = sqlobject.IntCol(length=0, dbName='DownloadSpeedLimit')
        FileNameFixed = sqlobject.IntCol(length=0, dbName='FileNameFixed')
        HttpRequestHeader = sqlobject.BLOBCol(length=0, dbName='HttpRequestHeader')
        VideoHeadFirstTime = sqlobject.IntCol(length=0, dbName='VideoHeadFirstTime')
        VideoHeadFirstStatus = sqlobject.IntCol(length=0, dbName='VideoHeadFirstStatus')
        ResourceQuerySize = sqlobject.BigIntCol(length=0, dbName='ResourceQuerySize')
        DisplayUrl = sqlobject.StringCol(length=0, dbName='DisplayUrl')
        UserAgent = sqlobject.StringCol(length=0, dbName='UserAgent')

        class sqlmeta:
            table = 'P2spTask'
            idName = 'TaskId'

    class TaskBase(sqlobject.SQLObject):
        # app_id = sqlobject.StringCol(length=14, unique=True)
        Id = sqlobject.BigIntCol(length=0, dbName='TaskId')
        Type = sqlobject.IntCol(length=0, dbName='Type')
        Status = sqlobject.IntCol(length=0, dbName='Status')
        StatusChangeTime = sqlobject.BigIntCol(length=0, dbName='StatusChangeTime')
        SavePath = sqlobject.StringCol(length=0, dbName='SavePath')
        TotalReceiveSize = sqlobject.BigIntCol(length=0, dbName='TotalReceiveSize')
        TotalSendSize = sqlobject.BigIntCol(length=0, dbName='TotalSendSize')
        TotalReceiveValidSize = sqlobject.BigIntCol(length=0, dbName='TotalReceiveValidSize')
        TotalUploadSize = sqlobject.BigIntCol(length=0, dbName='TotalUploadSize')
        CreationTime = sqlobject.BigIntCol(length=0, dbName='CreationTime')
        FileCreated = sqlobject.IntCol(length=0, dbName='FileCreated')
        CompletionTime = sqlobject.BigIntCol(length=0, dbName='CompletionTime')
        DownloadingPeriod = sqlobject.BigIntCol(length=0, dbName='DownloadingPeriod')
        RemovingToRecycleTime = sqlobject.BigIntCol(length=0, dbName='RemovingToRecycleTime')
        FailureErrorCode = sqlobject.IntCol(length=0, dbName='FailureErrorCode')
        Url = sqlobject.StringCol(length=0, dbName='Url')
        ReferenceUrl = sqlobject.StringCol(length=0, dbName='ReferenceUrl')
        ResourceSize = sqlobject.BigIntCol(length=0, dbName='ResourceSize')
        Name = sqlobject.StringCol(length=0, dbName='Name')
        Cid = sqlobject.BLOBCol(length=0, dbName='Cid')
        Gcid = sqlobject.BLOBCol(length=0, dbName='Gcid')
        Description = sqlobject.StringCol(length=0, dbName='Description')
        CategoryId = sqlobject.IntCol(length=0, dbName='CategoryId')
        ResourceQueryCid = sqlobject.BLOBCol(length=0, dbName='ResourceQueryCid')
        CreationRequestType = sqlobject.IntCol(length=0, dbName='CreationRequestType')
        StartMode = sqlobject.IntCol(length=0, dbName='StartMode')
        NamingType = sqlobject.IntCol(length=0, dbName='NamingType')
        StatisticsReferenceUrl = sqlobject.StringCol(length=0, dbName='StatisticsReferenceUrl')
        UserRead = sqlobject.IntCol(length=0, dbName='UserRead')
        FileSafetyFlag = sqlobject.IntCol(length=0, dbName='FileSafetyFlag')
        Playable = sqlobject.IntCol(length=0, dbName='Playable')
        BlockInfo = sqlobject.BLOBCol(length=0, dbName='BlockInfo')
        OpenOnComplete = sqlobject.IntCol(length=0, dbName='OpenOnComplete')
        SpecialType = sqlobject.IntCol(length=0, dbName='SpecialType')
        Proxy = sqlobject.BLOBCol(length=0, dbName='Proxy')
        OriginReceiveSize = sqlobject.BigIntCol(length=0, dbName='OriginReceiveSize')
        P2pReceiveSize = sqlobject.BigIntCol(length=0, dbName='P2pReceiveSize')
        P2sReceiveSize = sqlobject.BigIntCol(length=0, dbName='P2sReceiveSize')
        OfflineReceiveSize = sqlobject.BigIntCol(length=0, dbName='OfflineReceiveSize')
        VipReceiveSize = sqlobject.BigIntCol(length=0, dbName='VipReceiveSize')
        VipResourceEnableNecessary = sqlobject.IntCol(length=0, dbName='VipResourceEnableNecessary')
        ConsumedVipSize = sqlobject.BigIntCol(length=0, dbName='ConsumedVipSize')
        Forbidden = sqlobject.IntCol(length=0, dbName='Forbidden')
        OptionalChannelDataSize = sqlobject.BLOBCol(length=0, dbName='OptionalChannelDataSize')
        OwnerProductId = sqlobject.IntCol(length=0, dbName='OwnerProductId')
        UserData = sqlobject.BLOBCol(length=0, dbName='UserData')
        # UserData = sqlobject.StringCol(length=0, dbName='UserData')
        UrlCodePage = sqlobject.IntCol(length=0, dbName='UrlCodePage')
        ReferenceUrlCodePage = sqlobject.IntCol(length=0, dbName='ReferenceUrlCodePage')
        StatisticsReferenceUrlCodePage = sqlobject.IntCol(length=0, dbName='StatisticsReferenceUrlCodePage')
        GroupTaskId = sqlobject.BigIntCol(length=0, dbName='GroupTaskId')
        DownloadSubTask = sqlobject.IntCol(length=0, dbName='DownloadSubTask')
        TagValue = sqlobject.IntCol(length=0, dbName='TagValue')
        InnerNatReceiveSize = sqlobject.BigIntCol(length=0, dbName='InnerNatReceiveSize')
        AdditionFlag = sqlobject.IntCol(length=0, dbName='AdditionFlag')
        ProductInfo = sqlobject.StringCol(length=0, dbName='ProductInfo')

        class sqlmeta:
            table = 'TaskBase'
            idName = 'TaskId'

    def __init__(self, db_path='C:/Program Files (x86)/Thunder Network/Thunder/Profiles/TaskDb.dat'):
        self.conn = builder()(db_path)
        self.P2spTask._connection = self.conn
        self.TaskBase._connection = self.conn
        self.P2spTask.createTable(ifNotExists=True)
        self.TaskBase.createTable(ifNotExists=True)
        current_id = self.TaskBase.select().max('TaskId')
        self.task_id = current_id + 1 if current_id is not None else 1

    def task(self,
             SavePath,
             Url,
             # TaskBase
             Type=1,
             Status=5,  # 3 排队. 5 开始. 7暂停. 8完成
             StatusChangeTime=0,
             TotalReceiveSize=0,
             TotalSendSize=0,
             TotalReceiveValidSize=0,
             TotalUploadSize=0,
             CreationTime=0,
             FileCreated=0,
             CompletionTime=0,
             DownloadingPeriod=0,
             RemovingToRecycleTime=0,
             FailureErrorCode=0,
             ReferenceUrl='',
             ResourceSize=0,
             Name=None,
             Cid=None,
             Gcid=None,
             Description='',  # 备注名称
             CategoryId=-1,
             ResourceQueryCid=None,
             CreationRequestType=0,
             StartMode=0,
             NamingType=1,
             StatisticsReferenceUrl='',
             UserRead=0,
             FileSafetyFlag=0,
             Playable=0,
             BlockInfo=None,
             OpenOnComplete=0,
             SpecialType=-1,
             Proxy=None,
             OriginReceiveSize=0,
             P2pReceiveSize=0,
             P2sReceiveSize=0,
             OfflineReceiveSize=0,
             VipReceiveSize=0,
             VipResourceEnableNecessary=0,
             ConsumedVipSize=0,
             Forbidden=0,
             OptionalChannelDataSize=None,
             OwnerProductId=0,
             UserData=None,
             UrlCodePage=-1,
             ReferenceUrlCodePage=-1,
             StatisticsReferenceUrlCodePage=-1,
             GroupTaskId=-1,
             DownloadSubTask=0,
             TagValue=0,
             InnerNatReceiveSize=0,
             AdditionFlag=0,
             ProductInfo='',
             # P2spTask
             ResourceUsageStrategy=0,
             ResourceReportStrategy=0,
             Cookie='',
             AccountNeeded=0,
             UserName='',
             Password='',
             UseOriginResourceOnly=0,
             OriginResourceSupportRange=1,
             ReceiveOriginResourceSize=0,
             OriginResourceRetryInterval=-1,
             OriginResourceRetryTimes=-1,
             OriginResourceThreadCount=5,
             DownloadSpeedLimit=0,
             FileNameFixed=0,
             HttpRequestHeader=None,
             VideoHeadFirstTime=-1,
             VideoHeadFirstStatus=0,
             ResourceQuerySize=0,
             UserAgent=''):
        taskid = self.task_id
        if Name is None:
            Name = Url.split('/')[-1].split('#')[0].split('?')[0]
        tp = self.P2spTask(Id=taskid,
                           ResourceUsageStrategy=ResourceUsageStrategy, ResourceReportStrategy=ResourceReportStrategy,
                           Cookie=Cookie, AccountNeeded=AccountNeeded, UserName=UserName, Password=Password,
                           UseOriginResourceOnly=UseOriginResourceOnly,
                           OriginResourceSupportRange=OriginResourceSupportRange,
                           ReceiveOriginResourceSize=ReceiveOriginResourceSize,
                           OriginResourceRetryInterval=OriginResourceRetryInterval,
                           OriginResourceRetryTimes=OriginResourceRetryTimes,
                           OriginResourceThreadCount=OriginResourceThreadCount,
                           DownloadSpeedLimit=DownloadSpeedLimit, FileNameFixed=FileNameFixed,
                           HttpRequestHeader=HttpRequestHeader,
                           VideoHeadFirstTime=VideoHeadFirstTime, VideoHeadFirstStatus=VideoHeadFirstStatus,
                           ResourceQuerySize=ResourceQuerySize,
                           DisplayUrl=Url,
                           UserAgent=UserAgent)
        tb = self.TaskBase(Id=taskid, Type=Type, Status=Status, StatusChangeTime=StatusChangeTime,
                           SavePath=SavePath, TotalReceiveSize=TotalReceiveSize, TotalSendSize=TotalSendSize,
                           TotalReceiveValidSize=TotalReceiveValidSize, TotalUploadSize=TotalUploadSize,
                           CreationTime=CreationTime, FileCreated=FileCreated, CompletionTime=CompletionTime,
                           DownloadingPeriod=DownloadingPeriod, RemovingToRecycleTime=RemovingToRecycleTime,
                           FailureErrorCode=FailureErrorCode, Url=Url, ReferenceUrl=ReferenceUrl,
                           ResourceSize=ResourceSize, Name=Name, Cid=Cid, Gcid=Gcid, Description=Description,
                           CategoryId=CategoryId, ResourceQueryCid=ResourceQueryCid,
                           CreationRequestType=CreationRequestType, StartMode=StartMode, NamingType=NamingType,
                           StatisticsReferenceUrl=StatisticsReferenceUrl, UserRead=UserRead,
                           FileSafetyFlag=FileSafetyFlag, Playable=Playable, BlockInfo=BlockInfo,
                           OpenOnComplete=OpenOnComplete, SpecialType=SpecialType, Proxy=Proxy,
                           OriginReceiveSize=OriginReceiveSize, P2pReceiveSize=P2pReceiveSize,
                           P2sReceiveSize=P2sReceiveSize, OfflineReceiveSize=OfflineReceiveSize,
                           VipReceiveSize=VipReceiveSize, VipResourceEnableNecessary=VipResourceEnableNecessary,
                           ConsumedVipSize=ConsumedVipSize, Forbidden=Forbidden,
                           OptionalChannelDataSize=OptionalChannelDataSize, OwnerProductId=OwnerProductId,
                           UserData=UserData, UrlCodePage=UrlCodePage, ReferenceUrlCodePage=ReferenceUrlCodePage,
                           StatisticsReferenceUrlCodePage=StatisticsReferenceUrlCodePage, GroupTaskId=GroupTaskId,
                           DownloadSubTask=DownloadSubTask, TagValue=TagValue, InnerNatReceiveSize=InnerNatReceiveSize,
                           AdditionFlag=AdditionFlag, ProductInfo=ProductInfo)
        self.task_id += 1
