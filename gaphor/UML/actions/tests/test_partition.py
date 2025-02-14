import pytest

from gaphor import UML
from gaphor.diagram.tests.fixtures import copy_and_paste, copy_clear_and_paste
from gaphor.diagram.tools import new_item_factory
from gaphor.UML.actions.actionstoolbox import partition_config
from gaphor.UML.actions.partition import PartitionItem


@pytest.fixture
def partition_item_factory():
    return new_item_factory(
        PartitionItem,
        UML.ActivityPartition,
        config_func=partition_config,
    )


@pytest.fixture
def partition_item(partition_item_factory, diagram):
    return partition_item_factory(diagram)


def test_partition_placement_adds_two_partitions(partition_item: PartitionItem):

    assert partition_item.subject in partition_item.partition
    assert len(partition_item.partition) == 2


def test_copy_and_paste_partition_item(partition_item, diagram, element_factory):
    new_items = copy_and_paste({partition_item}, diagram, element_factory)

    (new_item,) = new_items

    assert new_item.subject is partition_item.subject
    assert new_item.partition[0] is partition_item.partition[0]
    assert new_item.partition[1] is partition_item.partition[1]


def test_copy_remove_and_paste_partition_item(partition_item, diagram, element_factory):
    copy_clear_and_paste({partition_item}, diagram, element_factory)

    new_item = diagram.ownedPresentation[0]

    assert new_item.subject in new_item.partition
    assert len(new_item.partition) == 2
