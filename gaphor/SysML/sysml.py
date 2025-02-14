# This file is generated by coder.py. DO NOT EDIT!
# isort: skip_file
# flake8: noqa F401,F811
# fmt: off

from __future__ import annotations

from gaphor.core.modeling.properties import (
    association,
    attribute as _attribute,
    derived,
    derivedunion,
    enumeration as _enumeration,
    redefine,
    relation_many,
    relation_one,
)


from gaphor.UML.uml import NamedElement
class AbstractRequirement(NamedElement):
    derived: relation_many[AbstractRequirement]
    derivedFrom: relation_many[AbstractRequirement]
    externalId: _attribute[str] = _attribute("externalId", str)
    master: relation_many[AbstractRequirement]
    refinedBy: relation_many[NamedElement]
    satisfiedBy: relation_many[NamedElement]
    text: _attribute[str] = _attribute("text", str)
    tracedTo: relation_many[NamedElement]
    verifiedBy: relation_many[NamedElement]


from gaphor.UML.uml import Class
class Requirement(AbstractRequirement, Class):
    pass


from gaphor.UML.uml import DirectedRelationship
class DirectedRelationshipPropertyPath(DirectedRelationship):
    sourceContext: relation_one[Classifier]
    sourcePropertyPath: relation_many[Property]
    targetContext: relation_one[Classifier]
    targetPropertyPath: relation_many[Property]


from gaphor.UML.uml import Dependency
class Trace(Dependency, DirectedRelationshipPropertyPath):
    pass


class Copy(Trace):
    pass


class Verify(Trace):
    pass


class DeriveReqt(Trace):
    pass


class Satisfy(Trace):
    pass


from gaphor.UML.uml import Behavior
class TestCase(Behavior):
    pass


class Block(Class):
    isEncapsulated: _attribute[int] = _attribute("isEncapsulated", int, default=False)


from gaphor.UML.uml import Property
class ConnectorProperty(Property):
    connector: relation_one[Connector]


class ParticipantProperty(Property):
    end_: relation_one[Property]


class DistributedProperty(Property):
    pass


from gaphor.UML.uml import DataType
class ValueType(DataType):
    quantityKind: relation_one[InstanceSpecification]
    unit: relation_one[InstanceSpecification]


from gaphor.UML.uml import InstanceSpecification
from gaphor.core.modeling.coremodel import Element
class ElementPropertyPath(Element):
    propertyPath: relation_many[Property]


from gaphor.UML.uml import Connector
class BindingConnector(Connector):
    pass


from gaphor.UML.uml import ConnectorEnd
class NestedConnectorEnd(ConnectorEnd, ElementPropertyPath):
    pass


from gaphor.UML.uml import Classifier
class PropertySpecificType(Classifier):
    pass


class EndPathMultiplicity(Property):
    pass


class BoundReference(EndPathMultiplicity):
    bindingPath: relation_many[Property]
    boundend: relation_many[ConnectorEnd]


class AdjuntProperty(Property):
    principal: relation_one[Element]


from gaphor.UML.uml import Port
class ProxyPort(Port):
    pass


class FullPort(Port):
    pass


class FlowProperty(Property):
    direction = _enumeration("direction", ("in", "inout", "out"), "in")


class InterfaceBlock(Block):
    pass


from gaphor.UML.uml import InvocationAction
from gaphor.UML.uml import Trigger
from gaphor.UML.uml import AddStructuralFeatureValueAction
class InvocationOnNestedPortAction(ElementPropertyPath, InvocationAction):
    onNestedPort: relation_many[Port]


class TriggerOnNestedPort(ElementPropertyPath, Trigger):
    onNestedPort: relation_many[Port]


class AddFlowPropertyValueOnNestedPortAction(AddStructuralFeatureValueAction, ElementPropertyPath):
    pass


from gaphor.UML.uml import ChangeEvent
class ChangeSructuralFeatureEvent(ChangeEvent):
    structuralFeature: relation_one[StructuralFeature]


from gaphor.UML.uml import StructuralFeature
from gaphor.UML.uml import AcceptEventAction
class AcceptChangeStructuralFeatureEventAction(AcceptEventAction):
    pass


from gaphor.UML.uml import Feature
class DirectedFeature(Feature):
    featureDirection = _enumeration("featureDirection", ("provided", "providedRequired", "required"), "provided")


from gaphor.UML.uml import Generalization
class Conform(Generalization):
    pass


class View(Class):
    stakeholder: relation_many[Stakeholder]
    viewpoint: relation_one[Viewpoint]


class Viewpoint(Class):
    concernList: relation_many[Comment]
    language: _attribute[str] = _attribute("language", str)
    method: relation_many[Behavior]
    presentation: _attribute[str] = _attribute("presentation", str)
    purpose: _attribute[str] = _attribute("purpose", str)
    stakeholder: relation_many[Stakeholder]


class Stakeholder(Classifier):
    concernList: relation_many[Comment]


class Expose(Dependency):
    pass


from gaphor.core.modeling.coremodel import Comment
class Rationale(Comment):
    pass


class Problem(Comment):
    pass


class ElementGroup(Comment):
    member: relation_many[Element]
    name: _attribute[str] = _attribute("name", str)
    orderedMember: relation_many[Element]


class ConstraintBlock(Block):
    pass


from gaphor.UML.uml import Parameter
from gaphor.UML.uml import ActivityEdge
from gaphor.UML.uml import ParameterSet
class Optional(Parameter):
    pass


class Rate(ActivityEdge, Parameter):
    rate: relation_many[InstanceSpecification]


class Probability(ActivityEdge, ParameterSet):
    probability: _attribute[str] = _attribute("probability", str)


class Continuous(Rate):
    pass


class Discrete(Rate):
    pass


from gaphor.UML.uml import Operation
from gaphor.UML.uml import ObjectNode
class ControlOperator(Behavior):
    pass


class NoBuffer(ObjectNode):
    pass


class Overwrite(ObjectNode):
    pass


from gaphor.UML.uml import Abstraction
class Allocate(Abstraction, DirectedRelationshipPropertyPath):
    pass


from gaphor.UML.uml import ActivityPartition
class AllocateActivityPartition(ActivityPartition):
    pass


class Refine(Dependency, DirectedRelationshipPropertyPath):
    pass


class Tagged(Property):
    nonunique: _attribute[int] = _attribute("nonunique", int)
    ordered: _attribute[int] = _attribute("ordered", int)
    subsets: _attribute[str] = _attribute("subsets", str)


class ClassifierBehaviorProperty(Property):
    pass



AbstractRequirement.derived = derivedunion("derived", AbstractRequirement)
AbstractRequirement.derivedFrom = derivedunion("derivedFrom", AbstractRequirement)
AbstractRequirement.master = derivedunion("master", AbstractRequirement)
AbstractRequirement.refinedBy = derivedunion("refinedBy", NamedElement)
AbstractRequirement.satisfiedBy = derivedunion("satisfiedBy", NamedElement)
AbstractRequirement.tracedTo = derivedunion("tracedTo", NamedElement)
AbstractRequirement.verifiedBy = derivedunion("verifiedBy", NamedElement)
DirectedRelationshipPropertyPath.targetContext = association("targetContext", Classifier, upper=1)
DirectedRelationshipPropertyPath.sourceContext = association("sourceContext", Classifier, upper=1)
DirectedRelationshipPropertyPath.sourcePropertyPath = association("sourcePropertyPath", Property)
DirectedRelationshipPropertyPath.targetPropertyPath = association("targetPropertyPath", Property)
ConnectorProperty.connector = association("connector", Connector, upper=1)
ParticipantProperty.end_ = association("end_", Property, upper=1)
ValueType.unit = association("unit", InstanceSpecification, upper=1)
ValueType.quantityKind = association("quantityKind", InstanceSpecification, upper=1)
ElementPropertyPath.propertyPath = association("propertyPath", Property, lower=1)
BoundReference.boundend = association("boundend", ConnectorEnd)
BoundReference.bindingPath = derivedunion("bindingPath", Property, lower=1)
AdjuntProperty.principal = association("principal", Element, upper=1)
InvocationOnNestedPortAction.onNestedPort = association("onNestedPort", Port, lower=1)
TriggerOnNestedPort.onNestedPort = association("onNestedPort", Port, lower=1)
ChangeSructuralFeatureEvent.structuralFeature = association("structuralFeature", StructuralFeature, upper=1)
View.stakeholder = derivedunion("stakeholder", Stakeholder)
View.viewpoint = derivedunion("viewpoint", Viewpoint, upper=1)
Viewpoint.concernList = association("concernList", Comment)
Viewpoint.method = derivedunion("method", Behavior)
Viewpoint.stakeholder = association("stakeholder", Stakeholder)
Stakeholder.concernList = association("concernList", Comment)
ElementGroup.member = derivedunion("member", Element)
ElementGroup.orderedMember = association("orderedMember", Element)
Rate.rate = association("rate", InstanceSpecification)
