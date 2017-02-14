# Log Parser for RTI Connext.
#
#   Copyright 2016 Real-Time Innovations, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""Create the dictionary for log functions for unmatched logs for debugging.

Functions:
  + get_regex_list: Get the regular expressions and function list.
"""
from __future__ import absolute_import
import logparser.logs.debug.debug as debug


def get_regex_list():
    """Return the regular expressions and functions list for this module."""
    regex = []

    # Blacklist - Messages that we want to ignore.
    regex.append([debug.on_ignored_message,
                  r"^\s*$"])
    regex.append([debug.on_ignored_message,
                  r"DDS_Registry_lock:Locking the storage service"])
    regex.append([debug.on_ignored_message,
                  r"DDS_Registry_unlock:Unlocking the storage service"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveDatabaseThread_loop:created \w+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:created \w+"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacadeReceiver_loop:created \w+"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacade_threadStarted:thread count ref " +
                  r"count \d+"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacade_addReceiverThread:thread count ref " +
                  r"count \d+"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacade_new:active object count ref " +
                  r"count \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_distributeTokens: \d+ agents " +
                  r"at priority [-\d]+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_updateAgentPriorities:agent:" +
                  r"0x\w+ priority set to [-\d]+"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_receive_rEA:\w+ woke up"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_scheduleJob:agent:\w+ job:\w+ " +
                  r"scheduled at priority \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapiThread_sleep: nanosleep\(\d+.\d+ s\)"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ gathering events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ firing events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ " +
                  r"rescheduling events"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveGeneratorThread_loop:\w+ sleeping " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveDatabaseThread_loop:\w+ collecting garbage"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventActiveDatabaseThread_loop:\w+ sleeping " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_updateAgentPriorities:agent:\w+ " +
                  r"priority set to \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIEventJobDispatcher_distributeTokens: \w+ agents at " +
                  r"priority \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapiThread_sleep: Sleep\(\d+ ms\)"])
    regex.append([debug.on_ignored_message,
                  r"RTISystemClock_init:epoch range \{\w+,\w+\}, " +
                  r"frequency \d+ Hz"])

    regex.append([debug.on_ignored_message,
                  r"DDS_StringSeq_ensure_length:memory allocation: " +
                  r"original \d+, new \d+"])
    regex.append([debug.on_ignored_message,
                  r"DDS_PropertySeq_ensure_length:memory allocation: " +
                  r"original \d+, new \d+"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_addEntryport:" +
                  r"NetioReceiver_Entryport reused"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioSender_addDestination:" +
                  r"NetioSender_Destination reused"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacadeReceiver_loop:\w+ disowning receive " +
                  r"resource"])
    regex.append([debug.on_ignored_message,
                  r"COMMENDActiveFacadeReceiver_loop:\w+ parsing message"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_receiveFast:\w+ received \d+ bytes"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_Shmem_receive_rEA:\w+ blocking on 0X\w+"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_Shmem_receive_rEA:\w+ woke up"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_receive_rEA:\w+ blocking on 0X\w+"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapi_getFirstValidInterface:found address for " +
                  r"interface .+ \(address family = \d+\)"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapi_getFirstValidInterface:skipped interface .+, " +
                  r"\(not valid address family \([\w/]+\)\)"])
    regex.append([debug.on_ignored_message,
                  r"RTIOsapi_getFirstValidInterface:skipped interface .+, " +
                  r"\(loopback interface\)"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_removeEntryport:NetioReceiver_" +
                  r"Entryport ref count \d+"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_SocketFactory_create_" +
                  r"receive_socket:invalid port (\d+)"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_create_recvresource_rrEA:" +
                  r"Created receive resource for port (\d+)"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_create_sendresource_srEA:Created " +
                  r"send resource for 0X\w+:\d+"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_query_interfaces:" +
                  r"skipped (\w+)"])
    regex.append([debug.on_ignored_message,
                  r"NDDS_Transport_UDPv4_create_recvresource_rrEA:" +
                  r"!create socket"])

    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipantFactory_create_participant_" +
                  r"disabledI:created participant: domain=\d+, index=-1"])
    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipantPresentation_reserve_participant_" +
                  r"index_entryports:Domain \d+:Trying to reserve " +
                  r"participant index=\d+..."])
    regex.append([debug.on_ignored_message,
                  r"DISCPluginManager_onAfterLocalEndpointEnabled:at " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleEndpointDiscoveryPluginPDFListener_" +
                  r"onAfterLocalWriterEnabled:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleEndpointDiscoveryPlugin_" +
                  r"subscriptionReaderListenerOnDataAvailable:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCPluginManager_onAfterLocalParticipantEnabled:at " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCEndpointDiscoveryPlugin_assertRemoteEndpoint:at " +
                  r"\{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCPluginManager_activateEdpListenersFor" +
                  r"RemoteParticipant:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCParticipantDiscoveryPlugin_assertRemoteParticipant:" +
                  r"at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleParticipantDiscoveryPluginReaderListener_" +
                  r"onDataAvailable:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleParticipantDiscoveryPlugin_" +
                  r"remoteParticipantDiscovered:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleEndpointDiscoveryPlugin_publicationReader" +
                  r"ListenerOnDataAvailable:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleEndpointDiscoveryPluginPDFListener_" +
                  r"onAfterLocalReaderEnabled:at \{\w+,\w+\}"])
    regex.append([debug.on_ignored_message,
                  r"DDS_Topic_createI:!create presentation topic"])
    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipant_create_topic_disabledI:" +
                  r"!create topic"])
    regex.append([debug.on_ignored_message,
                  r"DDSTopic_impl::createI:!create topic"])
    regex.append([debug.on_ignored_message,
                  r"PRESParticipant_destroyAllEntities:" +
                  r"!delete flow controller"])
    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipant_delete_contained_entities:" +
                  r"!delete contained entitie"])
    regex.append([debug.on_ignored_message,
                  r"DISCSimpleParticipantDiscoveryPluginReaderListener_" +
                  r"onDataAvailable:discovered modified participant: " +
                  r"host=0x\w+, app=0x\w+, instance=0x\w+"])

    regex.append([debug.on_ignored_message,
                  r"PRESPsService_onWriterResendEvent:writer resend event: " +
                  r"\(([\w,]+)\)"])
    regex.append([debug.on_ignored_message,
                  r"WriterHistoryMemoryPlugin_addEntryToSessions:" +
                  r"!initialize sample"])
    regex.append([debug.on_ignored_message,
                  r"WriterHistoryMemoryPlugin_getEntry:" +
                  r"!add virtual sample to sessions"])
    regex.append([debug.on_ignored_message,
                  r"WriterHistoryMemoryPlugin_addSample:!get entry"])
    regex.append([debug.on_ignored_message,
                  r"PRESWriterHistoryDriver_addWrite:!add_sample"])
    regex.append([debug.on_ignored_message,
                  r"PRESPsWriter_writeInternal:!collator addWrite"])
    regex.append([debug.on_ignored_message,
                  r"WriterHistoryMemoryPlugin_addSampleToWH:!add keyed entry"])
    regex.append([debug.on_ignored_message,
                  r"WriterHistoryMemoryPlugin_addSample:writer history full"])
    regex.append([debug.on_ignored_message,
                  r"PRESWriterHistoryDriver_addWrite:!instance history full"])
    regex.append([debug.on_ignored_message,
                  r"PRESWriterHistoryDriver_addWrite:!instance not found"])
    regex.append([debug.on_ignored_message,
                  r"PRESPsWriter_writeInternal:!collator write no instance"])
    regex.append([debug.on_ignored_message,
                  r"PRESCstReaderCollator_addCollatorEntryToPolled:" +
                  r"!add keyed entry"])
    regex.append([debug.on_ignored_message,
                  r"PRESCstReaderCollator_commitRemoteWriterQueue:" +
                  r"!add to polled"])
    regex.append([debug.on_ignored_message,
                  r"PRESCstReaderCollator_updateRemoteWriterQueue" +
                  r"FirstRelevant:"])
    regex.append([debug.on_ignored_message,
                  r"PRESPsService_readerSampleListenerOnNewData:" +
                  r"!goto WR pres psRemoteWriter"])
    regex.append([debug.on_ignored_message,
                  r"PRESPsReaderQueue_storeSampleToEntry:!store sample data"])
    regex.append([debug.on_ignored_message,
                  r"PRESPsReaderQueue_newData:!get entries"])
    regex.append([debug.on_ignored_message,
                  r"MIGGeneratorContext_addData:!space assert"])

    regex.append([debug.on_ignored_message,
                  r"This can occur if multicast is not enabled in the local " +
                  r"participant."])
    regex.append([debug.on_ignored_message,
                  r"See https://community.rti.com/kb/what-does-cant-reach-" +
                  r"locator-error-message-mean for additional info."])
    regex.append([debug.on_ignored_message,
                  r"can't reach:"])
    regex.append([debug.on_ignored_message,
                  r"transport: \d+ \([\w\d]+\)"])
    regex.append([debug.on_ignored_message,
                  r"address: [\d\.]+"])
    regex.append([debug.on_ignored_message,
                  r"Recv Resource:"])
    regex.append([debug.on_ignored_message,
                  r"Send Resource:"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioSender_addDestination:!create NetioSender_" +
                  r"SendResource"])
    regex.append([debug.on_ignored_message,
                  r"RTINetioReceiver_addEntryport:!create NetioReceiver_" +
                  r"ReceiveResource"])

    regex.append([debug.on_ignored_message, r"send failed:"])
    regex.append([debug.on_ignored_message, r"^\s*locator:\s*$"])
    regex.append([debug.on_ignored_message, r"^\s*transport: \d+$"])
    regex.append([debug.on_ignored_message, r"^\s*address: [\d:]+$"])
    regex.append([debug.on_ignored_message, r"^[\d:]+$"])
    regex.append([debug.on_ignored_message, r"^\s*port: \d+$"])
    regex.append([debug.on_ignored_message, r"^\s*encapsulation:$"])
    regex.append([debug.on_ignored_message, r"^\s{3}transport_priority: \d+$"])
    regex.append([debug.on_ignored_message, r'^\s{3}aliasList: ""$'])
    regex.append([debug.on_ignored_message,
                  r"DDS_DomainParticipantFactory_initializeI:Welcome to NDDS"])
    regex.append([debug.on_ignored_message,
                  r"DDS_DiscoveryQosPolicy_get_default:no environment " +
                  r"variable or file NDDS_DISCOVERY_PEERS"])
    regex.append([debug.on_ignored_message,
                  r"Creating domain participant..."])
    regex.append([debug.on_ignored_message,
                  r"loading QoS ..."])

    # The rest of unmatched message will be saved into a file to analyze them.
    regex.append([debug.on_unmatched_message, r"(.*)"])

    return regex
