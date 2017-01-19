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
"""Log parsing functions for logs related to DDS events.

Functions:
  + on_query_udpv4_interfaces: it happens when it queries the interfaces.
  + on_find_valid_interface: it happens when a valid interface is found.
  + on_get_valid_interface: it happens when a valid interface is queried.
  + on_skipped_interface: it happens when an interface is skipped.
  + on_create_participant: it happens for new participants.
  + on_delete_participant: it happens for deleted participants.
  + on_create_topic: it happens for new topics.
  + on_create_cft: it happens for new CFT.
  + on_delete_topic: it happens for deleted topics.
  + on_create_writer: it happens for new DataWriters.
  + on_create_reader: it happens for new DataReader.
  + on_delete_writer: it happens for deleted DataWriters.
  + on_delete_reader: it happens for deleted DataReaders.
  + on_duplicate_topic_name_error: it happens for topics with same name.
  + on_delete_topic_before_cft: it happens when deleting a topic before a CFT.
  + on_fail_delete_flowcontrollers: it happens when delete FC fails.
  + on_inconsistent_transport_discovery_configuration: it happens for discovery
  + on_discover_participant: it happens for discovered participants.
  + on_update_remote_participant: it happens when updating remote participant.
  + on_announce_local_participant: it happens when announcing participant.
  + on_discover_publication: it happens for discovered writers.
  + on_update_endpoint: it happens when updating an endpoint.
  + on_announce_local_publication: it happens when announcing a writer.
  + on_announce_local_subscription: it happens when announcing a reader.
  + on_participant_ignore_itself: it happens when ignoring itself.
  + on_lose_discovery_samples: it happens when losing discovery samples.
  + on_match_entity: it happens when an entity is matched.
  + on_different_type_names: it happens when TypeNames are different.
  + on_typeobject_received: it happens when comparing TypeObjects.
  + on_register_unkeyed_instance: it happens on registering unkeyed instances.
  + on_get_unkeyed_key: it happens when getting key from unkeyed sample.
  + on_unregister_unkeyed_instance: it happens when unregistering unkeyed.
  + on_library_version: it happens for the library version.
  + on_participant_initial_peers: it happens for the initial peers.
  + on_envvar_file_not_found: it happens when it can't find an env var or file.
  + on_envvar_file_found: it happens when it finds an env var or file.
"""
from __future__ import absolute_import
from logparser.utils import (get_locator, get_oid, get_participant,
                             get_topic_name, get_type_name, hex2ip,
                             is_builtin_entity, parse_guid, set_local_address)


# --------------------------------------------------------------------------- #
# -- Network Interfaces                                                    -- #
# --------------------------------------------------------------------------- #
def on_query_udpv4_interfaces(match, state, logger):
    """It happens when it queries the interfaces."""
    flags = {
        0x01: "UP", 0x02: "BROADCAST", 0x04: "LOOPBACK", 0x08: "POINTOPOINT",
        0x10: "MULTICAST", 0x20: "RUNNING"}

    addr = get_participant(hex2ip(match[0], True), state)
    flag = int(match[1], 16)
    flag_name = ""
    for bit in flags:
        if flag & bit != 0:
            flag_name += flags[bit] + "|"
    logger.event("Interface: %s is %s" % (addr, flag_name[:-1]), 2)


def on_find_valid_interface(match, state, logger):
    """It happens when a valid interface is found."""
    logger.cfg("Valid interface: %s" % match[0])


def on_get_valid_interface(match, state, logger):
    """It happens when a valid interface is queried."""
    if match[2] == "1":
        multicast = "with" if match[3] == "1" else "no"
        logger.cfg("Valid interface: %s (%s multicast)"
                   % (match[1], multicast))


def on_skipped_interface(match, state, logger):
    """It happens when an interface is skipped."""
    logger.event("Skipped interface: %s" % match[0], 2)


# --------------------------------------------------------------------------- #
# -- Create or delete entities                                             -- #
# --------------------------------------------------------------------------- #
def on_create_participant(match, state, logger):
    """It happens for new participants."""
    logger.event("Created participant, domain: %3s index: %s" %
                 (match[0], match[1]))


def on_delete_participant(match, state, logger):
    """It happens for deleted participants."""
    logger.event("Deleted participant, domain: %3s index: %s" %
                 (match[0], match[1]))


def on_create_topic(match, state, logger):
    """It happens for new topics."""
    topic = get_topic_name(match[0], state)
    typ = get_type_name(match[1], state)
    logger.event("Created topic, name: '%s', type: '%s'" %
                 (topic, typ))


def on_create_cft(match, state, logger):
    """It happens for new CFT."""
    topic = get_topic_name(match[0], state)
    logger.event("Created ContentFilteredTopic, name: '%s'" % topic)


def on_delete_topic(match, state, logger):
    """It happens for deleted topics."""
    topic = get_topic_name(match[0], state)
    typ = get_type_name(match[1], state)
    logger.event("Deleted topic, name: '%s', type: '%s'" % (topic, typ), 1)


def on_create_writer(match, state, logger):
    """It happens for new DataWriters."""
    topic = get_topic_name(match[0], state)
    logger.event("Created writer for topic '%s'" % topic)


def on_create_reader(match, state, logger):
    """It happens for new DataReader."""
    topic = get_topic_name(match[0], state)
    logger.event("Created reader for topic '%s'" % topic)


def on_delete_writer(match, state, logger):
    """It happens for deleted DataWriters."""
    topic = get_topic_name(match[0], state)
    logger.event("Deleted writer for topic '%s'" % topic)


def on_delete_reader(match, state, logger):
    """It happens for deleted DataReaders."""
    topic = get_topic_name(match[0], state)
    logger.event("Deleted reader for topic '%s'" % topic)


def on_duplicate_topic_name_error(match, state, logger):
    """It happens when there is a topic name duplication."""
    topic = get_topic_name(match[0], state)
    logger.event("[LP-2] Topic name already in use by another topic: %s"
                 % topic)


def on_delete_topic_before_cft(match, state, logger):
    """It happens when deleting a topic before its CFT."""
    num_cft = match[0]
    logger.error("[LP-7] Cannot delete topic before its %s" % num_cft +
                 "ContentFilteredTopics")


def on_fail_delete_flowcontrollers(match, state, logger):
    """It happens when delete FC fails."""
    num_flowcontrol = match[0]
    logger.error("[LP-15] Cannot delete %s " % (num_flowcontrol) +
                 "FlowControllers from delete_contained_entities")


# pylint: disable=W0613
def on_inconsistent_transport_discovery_configuration(match, state, logger):
    """It happens for inconsistencies in the discovery configuration."""
    logger.error("Inconsistent transport/discovery configuration")


# --------------------------------------------------------------------------- #
# -- Discover remote or local entities                                     -- #
# --------------------------------------------------------------------------- #
def on_discover_participant(match, state, logger):
    """It happens for discovered participants."""
    local_address = parse_guid(state, match[0], match[1])
    full_addr = parse_guid(state, match[0], match[1], match[2])
    full_addr = " ".join(full_addr.split())
    logger.process(local_address, "", "Discovered new participant (%s)" %
                   full_addr, state)


def on_update_remote_participant(match, state, logger):
    """It happens when updating remote participant."""
    local_address = parse_guid(state, match[0], match[1])
    full_addr = parse_guid(state, match[0], match[1], match[2])
    full_addr = " ".join(full_addr.split())
    part_oid = get_oid(match[3])
    logger.process(local_address, "",
                   "Discovered/Updated participant (%s - %s)"
                   % (full_addr, part_oid), 1)


def on_announce_local_participant(match, state, logger):
    """It happens when announcing participant."""
    guid = hex2ip(match[0]) + " " + str(int(match[1], 16)).zfill(5)
    set_local_address(guid, state, logger)


def on_discover_publication(match, state, logger):
    """It happens for discovered writers."""
    remote_addr = parse_guid(state, match[0], match[1], match[2])
    pub_oid = get_oid(match[3])
    logger.process(remote_addr, "",
                   "Discovered new publication %s" % pub_oid,
                   state)


def on_update_endpoint(match, state, logger):
    """It happens when updating an endpoint."""
    remote_addr = parse_guid(state, match[0], match[1], match[2])
    pub_oid = get_oid(match[3])
    logger.process(remote_addr, "",
                   "Discovered/Updated publication %s" % pub_oid, 1)


def on_announce_local_publication(match, state, logger):
    """It happens when announcing a writer."""
    local_addr = parse_guid(state, match[0], match[1], match[2])
    pub_oid = get_oid(match[3])
    logger.process(local_addr, "", "Announcing new writer %s" % pub_oid)


def on_announce_local_subscription(match, state, logger):
    """It happens when announcing a reader."""
    local_addr = parse_guid(state, match[0], match[1], match[2])
    sub_oid = get_oid(match[3])
    logger.process(local_addr, "", "Announcing new reader %s" % sub_oid)


# pylint: disable=W0613
def on_participant_ignore_itself(match, state, logger):
    """It happens when ignoring itself."""
    logger.process("", "", "Participant is ignoring itself")


def on_lose_discovery_samples(match, state, logger):
    """It happens when losing discovery samples."""
    entity_type = match[0]
    entity_oid = get_oid(match[1])
    total = match[2]
    delta = match[3]
    logger.warning("%s discovery samples lost for %s %s (%s in total)" %
                   (delta, entity_type, entity_oid, total), state)


# --------------------------------------------------------------------------- #
# -- Match remote or local entities                                        -- #
# --------------------------------------------------------------------------- #
def on_match_entity(entity2, kind):
    """It happens when an entity is matched."""
    def match_entity(match, state, logger):
        """It happens when a specific entity is matched."""
        entity2_addr = parse_guid(state, match[0], match[1], match[2])
        entity2_oid = get_oid(match[3])
        entity1_oid = get_oid(match[4])
        verb = 1 if is_builtin_entity(match[4]) else 0
        reliable = match[5]  # Best-Effort or Reliable
        logger.process(entity2_addr, entity1_oid, "Discovered %s %s %s %s" %
                       (kind, reliable, entity2, entity2_oid),
                       verb)
    return match_entity


def on_different_type_names(match, state, logger):
    """It happens when there isn't TypeObject and type names are different."""
    topic = get_topic_name(match[0], state)
    type1 = get_type_name(match[1], state)
    type2 = get_type_name(match[2], state)
    logger.error("[LP-18] Cannot match remote entity in topic '%s': "
                 % (topic) + "Different type names found ('%s', '%s')"
                 % (type1, type2))


def on_typeobject_received(match, state, logger):
    """It happens for discovered entities when comparing TypeObjects."""
    logger.process("", "", "TypeObject %s" % match[0], 2)


# --------------------------------------------------------------------------- #
# -- Bad usage of the API                                                  -- #
# --------------------------------------------------------------------------- #
# pylint: disable=W0613
def on_register_unkeyed_instance(match, state, logger):
    """It happens when registering unkeyed instances."""
    logger.warning("[LP-4] Try to register instance with no key field.")


# pylint: disable=W0613
def on_get_unkeyed_key(match, state, logger):
    """It happens when getting key from unkeyed sample."""
    logger.error("[LP-5] Try to get key from unkeyed type.",)


def on_unregister_unkeyed_instance(match, state, logger):
    """It happens when unregistering unkeyed sample."""
    logger.warning("[LP-6] Try to unregister instance with no key field.")


# --------------------------------------------------------------------------- #
# -- General information                                                   -- #
# --------------------------------------------------------------------------- #
def on_library_version(match, state, logger):
    """It happens for the library version."""
    logger.cfg("Version of %s is %s" % (match[0], match[1]))


def on_participant_initial_peers(match, state, logger):
    """It happens for the initial peers."""
    initial_peers = [get_locator(peer, state) for peer in match[0].split(",")]
    state['initial_peers'] = initial_peers
    logger.cfg("Initial peers: %s" % ", ".join(initial_peers))


def on_envvar_file_not_found(match, state, logger):
    """It happens when the middleware cannot find an env var or file."""
    logger.cfg("%s %s not found" % (match[0].capitalize(), match[1]))


def on_envvar_file_found(match, state, logger):
    """It happens when the middleware found an env var or file."""
    logger.cfg("%s %s found" % (match[0].capitalize(), match[1]))