import pytest
from gi.repository import Gtk

from gaphor import UML
from gaphor.UML.classes.classespropertypages import (
    AssociationPropertyPage,
    AttributesPage,
    ClassifierPropertyPage,
    DependencyPropertyPage,
    Folded,
    InterfacePropertyPage,
    NamedElementPropertyPage,
    OperationsPage,
)


def find(widget, name):
    if Gtk.Buildable.get_name(widget) == name:
        return widget
    if isinstance(widget, Gtk.Container):
        for child in widget.get_children():
            found = find(child, name)
            if found:
                return found
    return None


@pytest.fixture
def metaclass(element_factory):
    klass = element_factory.create(UML.Class)
    stereotype = element_factory.create(UML.Stereotype)
    UML.model.create_extension(klass, stereotype)
    return klass


def test_named_element_property_page(element_factory):
    subject = element_factory.create(UML.Class)
    property_page = NamedElementPropertyPage(subject)

    widget = property_page.construct()
    name_entry = find(widget, "name-entry")
    name_entry.set_text("Name")

    assert subject.name == "Name"


def test_no_named_element_property_page_for_metaclass(metaclass):
    property_page = NamedElementPropertyPage(metaclass)
    widget = property_page.construct()

    assert widget is None


def test_classifier_property_page(element_factory):
    subject = element_factory.create(UML.Class)
    property_page = ClassifierPropertyPage(subject)

    widget = property_page.construct()
    abstract = find(widget, "abstract")
    abstract.set_state(True)

    assert subject.isAbstract


def test_no_classifier_property_page_for_metaclass(metaclass):
    property_page = ClassifierPropertyPage(metaclass)
    widget = property_page.construct()

    assert widget is None


def test_interface_property_page(diagram, element_factory):
    item = diagram.create(
        UML.classes.InterfaceItem, subject=element_factory.create(UML.Interface)
    )
    property_page = InterfacePropertyPage(item)

    widget = property_page.construct()
    folded = find(widget, "folded")
    folded.set_state(True)

    assert item.folded == Folded.PROVIDED


def test_attributes_page(diagram, element_factory):
    item = diagram.create(
        UML.classes.InterfaceItem, subject=element_factory.create(UML.Interface)
    )
    property_page = AttributesPage(item)

    widget = property_page.construct()

    assert widget


def test_operations_page(diagram, element_factory):
    item = diagram.create(
        UML.classes.InterfaceItem, subject=element_factory.create(UML.Interface)
    )
    property_page = OperationsPage(item)

    widget = property_page.construct()

    assert widget


def test_dependency_property_page(diagram, element_factory):
    item = diagram.create(
        UML.classes.DependencyItem, subject=element_factory.create(UML.Dependency)
    )
    property_page = DependencyPropertyPage(item)

    widget = property_page.construct()

    assert widget


def test_dependency_property_page_without_subject(diagram, element_factory):
    item = diagram.create(UML.classes.DependencyItem)
    property_page = DependencyPropertyPage(item)

    widget = property_page.construct()

    assert widget


def test_association_property_page(diagram, element_factory):
    end1 = element_factory.create(UML.Class)
    end2 = element_factory.create(UML.Class)
    item = diagram.create(
        UML.classes.AssociationItem, subject=UML.model.create_association(end1, end2)
    )
    item.head_subject = item.subject.memberEnd[0]
    item.tail_subject = item.subject.memberEnd[1]
    property_page = AssociationPropertyPage(item)

    widget = property_page.construct()

    assert widget


def test_association_property_page_with_no_subject(diagram, element_factory):
    item = diagram.create(UML.classes.AssociationItem)
    property_page = AssociationPropertyPage(item)

    widget = property_page.construct()

    assert widget is None
