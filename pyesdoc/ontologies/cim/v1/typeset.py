
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_grids_package import *
from typeset_for_quality_package import *
from typeset_for_data_package import *
from typeset_for_activity_package import *
from typeset_for_misc_package import *


import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc



# Module exports.
__all__ = [
    # Packages
    shared,
    software,
    grids,
    quality,
    data,
    activity,
    misc,
    # Classes
    MachineCompilerUnit,
    Coupling,
    Experiment,
    Change,
    Timing,
    DataRestriction,
    EntryPoint,
    OutputRequirement,
    CimQuality,
    OpenDateRange,
    GridProperty,
    DateRange,
    VerticalCoordinateList,
    ChangeProperty,
    ProcessorComponent,
    RealCalendar,
    LateralBoundaryCondition,
    InitialCondition,
    DataDistribution,
    GridExtent,
    SpatialRegriddingUserMethod,
    Evaluation,
    ExperimentRelationship,
    DataExtentTemporal,
    ComponentLanguageProperty,
    NumericalRequirement,
    SpatialRegriddingProperty,
    ComponentProperty,
    ClosedDateRange,
    GridSpec,
    SimulationRelationshipTarget,
    Component,
    EnsembleMember,
    SpatialRegridding,
    SpatioTemporalConstraint,
    PerpetualPeriod,
    GridTileResolutionType,
    TimeLag,
    BoundaryCondition,
    DocumentSet,
    DataStorageIp,
    Parallelisation,
    ExperimentRelationshipTarget,
    NumericalActivity,
    ConnectionEndpoint,
    Calendar,
    GridMosaic,
    CoordinateList,
    DataExtentTimeInterval,
    StandardName,
    Ensemble,
    SimulationRun,
    DocRelationship,
    DataExtent,
    Compiler,
    Platform,
    Rank,
    Property,
    DocRelationshipTarget,
    PhysicalModification,
    Connection,
    GridTile,
    DocReference,
    ResponsibleParty,
    DataTopic,
    License,
    Activity,
    DataObject,
    CouplingProperty,
    Report,
    DataStorage,
    SimulationRelationship,
    ComponentLanguage,
    ConnectionProperty,
    Citation,
    Simulation,
    DataExtentGeographical,
    NumericalRequirementOption,
    Machine,
    DataSource,
    DataHierarchyLevel,
    StatisticalModelComponent,
    TimeTransformation,
    CouplingEndpoint,
    Deployment,
    Standard,
    DocGenealogy,
    ModelComponent,
    NumericalExperiment,
    Measure,
    DataProperty,
    Conformance,
    DataStorageDb,
    MeasurementCampaign,
    SimpleGridGeometry,
    Relationship,
    DocMetaInfo,
    DataContent,
    Daily360,
    SimulationComposite,
    DownscalingSimulation,
    DataStorageFile,
    Composition,
    # Enums
    CimResultType,
    FeatureTypeEnum,
    DocRelationshipDirectionType,
    FrequencyType,
    ProjectType,
    InterconnectType,
    ResolutionType,
    MachineType,
    QualitySeverityType,
    SimulationType,
    VerticalCsEnum,
    ModelComponentType,
    ChangePropertyType,
    SpatialRegriddingDimensionType,
    GridNodePositionEnum,
    SpatialRegriddingStandardMethodType,
    GridTypeEnum,
    CimScopeCodeType,
    DataPurpose,
    SimulationRelationshipType,
    DiscretizationEnum,
    CompilerType,
    ProcessorType,
    ConformanceType,
    DataHierarchyType,
    GeometryTypeEnum,
    DataStatusType,
    ArcTypeEnum,
    HorizontalCsEnum,
    CimFeatureType,
    OperatingSystemType,
    DocRelationshipType,
    CouplingFrameworkType,
    StatisticalModelComponentType,
    QualityStatusType,
    TimingUnits,
    EnsembleType,
    DownscalingType,
    ExperimentRelationshipType,
    DocStatusType,
    ConnectionType,
    QualityIssueType,
    UnitType,
    MachineVendorType,
    RefinementTypeEnum,
    DocType,
    ComponentPropertyIntentType,
    TimeMappingType,
]

# Set type keys.
# TODO deprecate
misc.DocumentSet.type_key = u"cim.1.misc.DocumentSet"
data.DataProperty.type_key = u"cim.1.data.DataProperty"
data.DataContent.type_key = u"cim.1.data.DataContent"
data.DataRestriction.type_key = u"cim.1.data.DataRestriction"
data.DataDistribution.type_key = u"cim.1.data.DataDistribution"
data.DataStorage.type_key = u"cim.1.data.DataStorage"
data.DataExtent.type_key = u"cim.1.data.DataExtent"
data.DataStorageDb.type_key = u"cim.1.data.DataStorageDb"
data.DataExtentGeographical.type_key = u"cim.1.data.DataExtentGeographical"
data.DataStorageFile.type_key = u"cim.1.data.DataStorageFile"
data.DataExtentTemporal.type_key = u"cim.1.data.DataExtentTemporal"
data.DataStorageIp.type_key = u"cim.1.data.DataStorageIp"
data.DataExtentTimeInterval.type_key = u"cim.1.data.DataExtentTimeInterval"
data.DataTopic.type_key = u"cim.1.data.DataTopic"
data.DataHierarchyLevel.type_key = u"cim.1.data.DataHierarchyLevel"
data.DataObject.type_key = u"cim.1.data.DataObject"
software.ModelComponent.type_key = u"cim.1.software.ModelComponent"
software.ConnectionProperty.type_key = u"cim.1.software.ConnectionProperty"
software.ProcessorComponent.type_key = u"cim.1.software.ProcessorComponent"
software.SpatialRegriddingUserMethod.type_key = u"cim.1.software.SpatialRegriddingUserMethod"
software.Component.type_key = u"cim.1.software.Component"
software.ComponentLanguageProperty.type_key = u"cim.1.software.ComponentLanguageProperty"
software.SpatialRegriddingProperty.type_key = u"cim.1.software.SpatialRegriddingProperty"
software.ComponentProperty.type_key = u"cim.1.software.ComponentProperty"
software.Deployment.type_key = u"cim.1.software.Deployment"
software.StatisticalModelComponent.type_key = u"cim.1.software.StatisticalModelComponent"
software.Composition.type_key = u"cim.1.software.Composition"
software.Connection.type_key = u"cim.1.software.Connection"
software.Parallelisation.type_key = u"cim.1.software.Parallelisation"
software.Timing.type_key = u"cim.1.software.Timing"
software.ConnectionEndpoint.type_key = u"cim.1.software.ConnectionEndpoint"
software.ComponentLanguage.type_key = u"cim.1.software.ComponentLanguage"
software.TimeTransformation.type_key = u"cim.1.software.TimeTransformation"
software.TimeLag.type_key = u"cim.1.software.TimeLag"
software.Coupling.type_key = u"cim.1.software.Coupling"
software.CouplingEndpoint.type_key = u"cim.1.software.CouplingEndpoint"
software.CouplingProperty.type_key = u"cim.1.software.CouplingProperty"
software.EntryPoint.type_key = u"cim.1.software.EntryPoint"
software.Rank.type_key = u"cim.1.software.Rank"
software.SpatialRegridding.type_key = u"cim.1.software.SpatialRegridding"
quality.CimQuality.type_key = u"cim.1.quality.CimQuality"
quality.Evaluation.type_key = u"cim.1.quality.Evaluation"
quality.Report.type_key = u"cim.1.quality.Report"
quality.Measure.type_key = u"cim.1.quality.Measure"
grids.GridTile.type_key = u"cim.1.grids.GridTile"
grids.GridExtent.type_key = u"cim.1.grids.GridExtent"
grids.GridTileResolutionType.type_key = u"cim.1.grids.GridTileResolutionType"
grids.GridMosaic.type_key = u"cim.1.grids.GridMosaic"
grids.SimpleGridGeometry.type_key = u"cim.1.grids.SimpleGridGeometry"
grids.GridProperty.type_key = u"cim.1.grids.GridProperty"
grids.VerticalCoordinateList.type_key = u"cim.1.grids.VerticalCoordinateList"
grids.GridSpec.type_key = u"cim.1.grids.GridSpec"
grids.CoordinateList.type_key = u"cim.1.grids.CoordinateList"
activity.Conformance.type_key = u"cim.1.activity.Conformance"
activity.OutputRequirement.type_key = u"cim.1.activity.OutputRequirement"
activity.MeasurementCampaign.type_key = u"cim.1.activity.MeasurementCampaign"
activity.PhysicalModification.type_key = u"cim.1.activity.PhysicalModification"
activity.SimulationComposite.type_key = u"cim.1.activity.SimulationComposite"
activity.NumericalActivity.type_key = u"cim.1.activity.NumericalActivity"
activity.Ensemble.type_key = u"cim.1.activity.Ensemble"
activity.Simulation.type_key = u"cim.1.activity.Simulation"
activity.Activity.type_key = u"cim.1.activity.Activity"
activity.NumericalExperiment.type_key = u"cim.1.activity.NumericalExperiment"
activity.EnsembleMember.type_key = u"cim.1.activity.EnsembleMember"
activity.NumericalRequirement.type_key = u"cim.1.activity.NumericalRequirement"
activity.Experiment.type_key = u"cim.1.activity.Experiment"
activity.SimulationRelationship.type_key = u"cim.1.activity.SimulationRelationship"
activity.NumericalRequirementOption.type_key = u"cim.1.activity.NumericalRequirementOption"
activity.ExperimentRelationship.type_key = u"cim.1.activity.ExperimentRelationship"
activity.SimulationRelationshipTarget.type_key = u"cim.1.activity.SimulationRelationshipTarget"
activity.BoundaryCondition.type_key = u"cim.1.activity.BoundaryCondition"
activity.ExperimentRelationshipTarget.type_key = u"cim.1.activity.ExperimentRelationshipTarget"
activity.SimulationRun.type_key = u"cim.1.activity.SimulationRun"
activity.DownscalingSimulation.type_key = u"cim.1.activity.DownscalingSimulation"
activity.InitialCondition.type_key = u"cim.1.activity.InitialCondition"
activity.LateralBoundaryCondition.type_key = u"cim.1.activity.LateralBoundaryCondition"
activity.SpatioTemporalConstraint.type_key = u"cim.1.activity.SpatioTemporalConstraint"
shared.Change.type_key = u"cim.1.shared.Change"
shared.PerpetualPeriod.type_key = u"cim.1.shared.PerpetualPeriod"
shared.Platform.type_key = u"cim.1.shared.Platform"
shared.Standard.type_key = u"cim.1.shared.Standard"
shared.Compiler.type_key = u"cim.1.shared.Compiler"
shared.RealCalendar.type_key = u"cim.1.shared.RealCalendar"
shared.DocRelationshipTarget.type_key = u"cim.1.shared.DocRelationshipTarget"
shared.Machine.type_key = u"cim.1.shared.Machine"
shared.Relationship.type_key = u"cim.1.shared.Relationship"
shared.ResponsibleParty.type_key = u"cim.1.shared.ResponsibleParty"
shared.StandardName.type_key = u"cim.1.shared.StandardName"
shared.ChangeProperty.type_key = u"cim.1.shared.ChangeProperty"
shared.DocRelationship.type_key = u"cim.1.shared.DocRelationship"
shared.DataSource.type_key = u"cim.1.shared.DataSource"
shared.MachineCompilerUnit.type_key = u"cim.1.shared.MachineCompilerUnit"
shared.DocMetaInfo.type_key = u"cim.1.shared.DocMetaInfo"
shared.Property.type_key = u"cim.1.shared.Property"
shared.DocGenealogy.type_key = u"cim.1.shared.DocGenealogy"
shared.Citation.type_key = u"cim.1.shared.Citation"
shared.Calendar.type_key = u"cim.1.shared.Calendar"
shared.DocReference.type_key = u"cim.1.shared.DocReference"
shared.ClosedDateRange.type_key = u"cim.1.shared.ClosedDateRange"
shared.Daily360.type_key = u"cim.1.shared.Daily360"
shared.DateRange.type_key = u"cim.1.shared.DateRange"
shared.OpenDateRange.type_key = u"cim.1.shared.OpenDateRange"
shared.License.type_key = u"cim.1.shared.License"
data.DataHierarchyType.type_key = u"cim.1.data.DataHierarchyType"
data.DataStatusType.type_key = u"cim.1.data.DataStatusType"
software.CouplingFrameworkType.type_key = u"cim.1.software.CouplingFrameworkType"
software.ModelComponentType.type_key = u"cim.1.software.ModelComponentType"
software.SpatialRegriddingDimensionType.type_key = u"cim.1.software.SpatialRegriddingDimensionType"
software.SpatialRegriddingStandardMethodType.type_key = u"cim.1.software.SpatialRegriddingStandardMethodType"
software.StatisticalModelComponentType.type_key = u"cim.1.software.StatisticalModelComponentType"
software.TimeMappingType.type_key = u"cim.1.software.TimeMappingType"
software.TimingUnits.type_key = u"cim.1.software.TimingUnits"
software.ComponentPropertyIntentType.type_key = u"cim.1.software.ComponentPropertyIntentType"
software.ConnectionType.type_key = u"cim.1.software.ConnectionType"
quality.QualitySeverityType.type_key = u"cim.1.quality.QualitySeverityType"
quality.CimScopeCodeType.type_key = u"cim.1.quality.CimScopeCodeType"
quality.CimFeatureType.type_key = u"cim.1.quality.CimFeatureType"
quality.QualityStatusType.type_key = u"cim.1.quality.QualityStatusType"
quality.QualityIssueType.type_key = u"cim.1.quality.QualityIssueType"
quality.CimResultType.type_key = u"cim.1.quality.CimResultType"
grids.VerticalCsEnum.type_key = u"cim.1.grids.VerticalCsEnum"
grids.GridNodePositionEnum.type_key = u"cim.1.grids.GridNodePositionEnum"
grids.DiscretizationEnum.type_key = u"cim.1.grids.DiscretizationEnum"
grids.GridTypeEnum.type_key = u"cim.1.grids.GridTypeEnum"
grids.FeatureTypeEnum.type_key = u"cim.1.grids.FeatureTypeEnum"
grids.RefinementTypeEnum.type_key = u"cim.1.grids.RefinementTypeEnum"
grids.HorizontalCsEnum.type_key = u"cim.1.grids.HorizontalCsEnum"
grids.GeometryTypeEnum.type_key = u"cim.1.grids.GeometryTypeEnum"
grids.ArcTypeEnum.type_key = u"cim.1.grids.ArcTypeEnum"
activity.EnsembleType.type_key = u"cim.1.activity.EnsembleType"
activity.ExperimentRelationshipType.type_key = u"cim.1.activity.ExperimentRelationshipType"
activity.FrequencyType.type_key = u"cim.1.activity.FrequencyType"
activity.ProjectType.type_key = u"cim.1.activity.ProjectType"
activity.ResolutionType.type_key = u"cim.1.activity.ResolutionType"
activity.SimulationType.type_key = u"cim.1.activity.SimulationType"
activity.DownscalingType.type_key = u"cim.1.activity.DownscalingType"
activity.SimulationRelationshipType.type_key = u"cim.1.activity.SimulationRelationshipType"
activity.ConformanceType.type_key = u"cim.1.activity.ConformanceType"
shared.ChangePropertyType.type_key = u"cim.1.shared.ChangePropertyType"
shared.CompilerType.type_key = u"cim.1.shared.CompilerType"
shared.DataPurpose.type_key = u"cim.1.shared.DataPurpose"
shared.InterconnectType.type_key = u"cim.1.shared.InterconnectType"
shared.MachineType.type_key = u"cim.1.shared.MachineType"
shared.MachineVendorType.type_key = u"cim.1.shared.MachineVendorType"
shared.OperatingSystemType.type_key = u"cim.1.shared.OperatingSystemType"
shared.ProcessorType.type_key = u"cim.1.shared.ProcessorType"
shared.UnitType.type_key = u"cim.1.shared.UnitType"
shared.DocRelationshipDirectionType.type_key = u"cim.1.shared.DocRelationshipDirectionType"
shared.DocRelationshipType.type_key = u"cim.1.shared.DocRelationshipType"
shared.DocStatusType.type_key = u"cim.1.shared.DocStatusType"
shared.DocType.type_key = u"cim.1.shared.DocType"

