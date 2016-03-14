
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.type_keys.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology map of types to keys.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_designing_package as designing
import typeset_for_shared_package as shared
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform




# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    designing: "cim.2.designing",
    shared: "cim.2.shared",
    activity: "cim.2.activity",
    software: "cim.2.software",
    science: "cim.2.science",
    data: "cim.2.data",
    drs: "cim.2.drs",
    platform: "cim.2.platform",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------

    designing.NumericalExperiment: "cim.2.designing.NumericalExperiment",

    designing.Project: "cim.2.designing.Project",

    designing.ForcingConstraint: "cim.2.designing.ForcingConstraint",

    designing.MultiTimeEnsemble: "cim.2.designing.MultiTimeEnsemble",

    designing.TemporalConstraint: "cim.2.designing.TemporalConstraint",

    designing.NumericalRequirement: "cim.2.designing.NumericalRequirement",

    designing.EnsembleRequirement: "cim.2.designing.EnsembleRequirement",

    designing.OutputTemporalRequirement: "cim.2.designing.OutputTemporalRequirement",

    designing.MultiEnsemble: "cim.2.designing.MultiEnsemble",

    designing.SimulationPlan: "cim.2.designing.SimulationPlan",

    designing.DomainProperties: "cim.2.designing.DomainProperties",

    shared.Pid: "cim.2.shared.Pid",

    shared.NumberArray: "cim.2.shared.NumberArray",

    shared.OnlineResource: "cim.2.shared.OnlineResource",

    shared.Party: "cim.2.shared.Party",

    shared.KeyFloat: "cim.2.shared.KeyFloat",

    shared.DatetimeSet: "cim.2.shared.DatetimeSet",

    shared.DocReference: "cim.2.shared.DocReference",

    shared.DateTime: "cim.2.shared.DateTime",

    shared.TimesliceList: "cim.2.shared.TimesliceList",

    shared.DocMetaInfo: "cim.2.shared.DocMetaInfo",

    shared.TimePeriod: "cim.2.shared.TimePeriod",

    shared.RegularTimeset: "cim.2.shared.RegularTimeset",

    shared.ExternalDocument: "cim.2.shared.ExternalDocument",

    shared.QualityReview: "cim.2.shared.QualityReview",

    shared.Reference: "cim.2.shared.Reference",

    shared.Responsibility: "cim.2.shared.Responsibility",

    shared.Cimtext: "cim.2.shared.Cimtext",

    shared.Calendar: "cim.2.shared.Calendar",

    shared.IrregularDateset: "cim.2.shared.IrregularDateset",

    activity.Conformance: "cim.2.activity.Conformance",

    activity.Ensemble: "cim.2.activity.Ensemble",

    activity.UberEnsemble: "cim.2.activity.UberEnsemble",

    activity.EnsembleMember: "cim.2.activity.EnsembleMember",

    activity.ParentSimulation: "cim.2.activity.ParentSimulation",

    activity.EnsembleAxis: "cim.2.activity.EnsembleAxis",

    activity.Activity: "cim.2.activity.Activity",

    activity.AxisMember: "cim.2.activity.AxisMember",

    software.DevelopmentPath: "cim.2.software.DevelopmentPath",

    software.EntryPoint: "cim.2.software.EntryPoint",

    software.Variable: "cim.2.software.Variable",

    software.SoftwareComponent: "cim.2.software.SoftwareComponent",

    software.Composition: "cim.2.software.Composition",

    software.ComponentBase: "cim.2.software.ComponentBase",

    software.Gridspec: "cim.2.software.Gridspec",

    science.Extent: "cim.2.science.Extent",

    science.Grid: "cim.2.science.Grid",

    science.Process: "cim.2.science.Process",

    science.Algorithm: "cim.2.science.Algorithm",

    science.ScientificDomain: "cim.2.science.ScientificDomain",

    science.ConservationProperties: "cim.2.science.ConservationProperties",

    science.Resolution: "cim.2.science.Resolution",

    science.KeyProperties: "cim.2.science.KeyProperties",

    science.ScienceContext: "cim.2.science.ScienceContext",

    science.SubProcess: "cim.2.science.SubProcess",

    science.Detail: "cim.2.science.Detail",

    science.Tuning: "cim.2.science.Tuning",

    science.Model: "cim.2.science.Model",

    data.Dataset: "cim.2.data.Dataset",

    data.Simulation: "cim.2.data.Simulation",

    data.VariableCollection: "cim.2.data.VariableCollection",

    data.Downscaling: "cim.2.data.Downscaling",

    drs.DrsEnsembleIdentifier: "cim.2.drs.DrsEnsembleIdentifier",

    drs.DrsPublicationDataset: "cim.2.drs.DrsPublicationDataset",

    drs.DrsAtomicDataset: "cim.2.drs.DrsAtomicDataset",

    drs.DrsTemporalIdentifier: "cim.2.drs.DrsTemporalIdentifier",

    drs.DrsGeographicalIndicator: "cim.2.drs.DrsGeographicalIndicator",

    platform.StoragePool: "cim.2.platform.StoragePool",

    platform.StorageVolume: "cim.2.platform.StorageVolume",

    platform.Machine: "cim.2.platform.Machine",

    platform.ComputePool: "cim.2.platform.ComputePool",

    platform.ComponentPerformance: "cim.2.platform.ComponentPerformance",

    platform.Performance: "cim.2.platform.Performance",

    platform.Partition: "cim.2.platform.Partition",

    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------

    (designing.NumericalExperiment, 'related_experiments'): "cim.2.designing.NumericalExperiment.related_experiments",

    (designing.NumericalExperiment, 'requirements'): "cim.2.designing.NumericalExperiment.requirements",

    (designing.Project, 'previous_projects'): "cim.2.designing.Project.previous_projects",

    (designing.Project, 'sub_projects'): "cim.2.designing.Project.sub_projects",

    (designing.Project, 'requires_experiments'): "cim.2.designing.Project.requires_experiments",

    (designing.ForcingConstraint, 'group'): "cim.2.designing.ForcingConstraint.group",

    (designing.ForcingConstraint, 'code'): "cim.2.designing.ForcingConstraint.code",

    (designing.ForcingConstraint, 'data_link'): "cim.2.designing.ForcingConstraint.data_link",

    (designing.ForcingConstraint, 'additional_constraint'): "cim.2.designing.ForcingConstraint.additional_constraint",

    (designing.ForcingConstraint, 'origin'): "cim.2.designing.ForcingConstraint.origin",

    (designing.ForcingConstraint, 'forcing_type'): "cim.2.designing.ForcingConstraint.forcing_type",

    (designing.ForcingConstraint, 'category'): "cim.2.designing.ForcingConstraint.category",

    (designing.MultiTimeEnsemble, 'ensemble_members'): "cim.2.designing.MultiTimeEnsemble.ensemble_members",

    (designing.TemporalConstraint, 'start_date'): "cim.2.designing.TemporalConstraint.start_date",

    (designing.TemporalConstraint, 'required_calendar'): "cim.2.designing.TemporalConstraint.required_calendar",

    (designing.TemporalConstraint, 'start_flexibility'): "cim.2.designing.TemporalConstraint.start_flexibility",

    (designing.TemporalConstraint, 'required_duration'): "cim.2.designing.TemporalConstraint.required_duration",

    (designing.NumericalRequirement, 'additional_requirements'): "cim.2.designing.NumericalRequirement.additional_requirements",

    (designing.NumericalRequirement, 'conformance_is_requested'): "cim.2.designing.NumericalRequirement.conformance_is_requested",

    (designing.EnsembleRequirement, 'ensemble_type'): "cim.2.designing.EnsembleRequirement.ensemble_type",

    (designing.EnsembleRequirement, 'ensemble_member'): "cim.2.designing.EnsembleRequirement.ensemble_member",

    (designing.EnsembleRequirement, 'minimum_size'): "cim.2.designing.EnsembleRequirement.minimum_size",

    (designing.OutputTemporalRequirement, 'continuous_subset'): "cim.2.designing.OutputTemporalRequirement.continuous_subset",

    (designing.OutputTemporalRequirement, 'throughout'): "cim.2.designing.OutputTemporalRequirement.throughout",

    (designing.OutputTemporalRequirement, 'sliced_subset'): "cim.2.designing.OutputTemporalRequirement.sliced_subset",

    (designing.MultiEnsemble, 'ensemble_axis'): "cim.2.designing.MultiEnsemble.ensemble_axis",

    (designing.SimulationPlan, 'will_support_experiments'): "cim.2.designing.SimulationPlan.will_support_experiments",

    (designing.SimulationPlan, 'expected_platform'): "cim.2.designing.SimulationPlan.expected_platform",

    (designing.SimulationPlan, 'expected_model'): "cim.2.designing.SimulationPlan.expected_model",

    (designing.SimulationPlan, 'expected_performance_sypd'): "cim.2.designing.SimulationPlan.expected_performance_sypd",

    (designing.DomainProperties, 'required_extent'): "cim.2.designing.DomainProperties.required_extent",

    (designing.DomainProperties, 'required_resolution'): "cim.2.designing.DomainProperties.required_resolution",

    (shared.Pid, 'id'): "cim.2.shared.Pid.id",

    (shared.Pid, 'resolution_service'): "cim.2.shared.Pid.resolution_service",

    (shared.NumberArray, 'values'): "cim.2.shared.NumberArray.values",

    (shared.OnlineResource, 'description'): "cim.2.shared.OnlineResource.description",

    (shared.OnlineResource, 'name'): "cim.2.shared.OnlineResource.name",

    (shared.OnlineResource, 'protocol'): "cim.2.shared.OnlineResource.protocol",

    (shared.OnlineResource, 'linkage'): "cim.2.shared.OnlineResource.linkage",

    (shared.Party, 'meta'): "cim.2.shared.Party.meta",

    (shared.Party, 'name'): "cim.2.shared.Party.name",

    (shared.Party, 'email'): "cim.2.shared.Party.email",

    (shared.Party, 'orcid_id'): "cim.2.shared.Party.orcid_id",

    (shared.Party, 'url'): "cim.2.shared.Party.url",

    (shared.Party, 'organisation'): "cim.2.shared.Party.organisation",

    (shared.Party, 'address'): "cim.2.shared.Party.address",

    (shared.KeyFloat, 'key'): "cim.2.shared.KeyFloat.key",

    (shared.KeyFloat, 'value'): "cim.2.shared.KeyFloat.value",

    (shared.DatetimeSet, 'length'): "cim.2.shared.DatetimeSet.length",

    (shared.DocReference, 'id'): "cim.2.shared.DocReference.id",

    (shared.DocReference, 'type'): "cim.2.shared.DocReference.type",

    (shared.DocReference, 'relationship'): "cim.2.shared.DocReference.relationship",

    (shared.DocReference, 'constraint_vocabulary'): "cim.2.shared.DocReference.constraint_vocabulary",

    (shared.DocReference, 'context'): "cim.2.shared.DocReference.context",

    (shared.DocReference, 'version'): "cim.2.shared.DocReference.version",

    (shared.DateTime, 'offset'): "cim.2.shared.DateTime.offset",

    (shared.DateTime, 'value'): "cim.2.shared.DateTime.value",

    (shared.TimesliceList, 'members'): "cim.2.shared.TimesliceList.members",

    (shared.TimesliceList, 'units'): "cim.2.shared.TimesliceList.units",

    (shared.DocMetaInfo, 'type'): "cim.2.shared.DocMetaInfo.type",

    (shared.DocMetaInfo, 'institute'): "cim.2.shared.DocMetaInfo.institute",

    (shared.DocMetaInfo, 'source'): "cim.2.shared.DocMetaInfo.source",

    (shared.DocMetaInfo, 'type_sort_key'): "cim.2.shared.DocMetaInfo.type_sort_key",

    (shared.DocMetaInfo, 'drs_keys'): "cim.2.shared.DocMetaInfo.drs_keys",

    (shared.DocMetaInfo, 'sort_key'): "cim.2.shared.DocMetaInfo.sort_key",

    (shared.DocMetaInfo, 'drs_path'): "cim.2.shared.DocMetaInfo.drs_path",

    (shared.DocMetaInfo, 'create_date'): "cim.2.shared.DocMetaInfo.create_date",

    (shared.DocMetaInfo, 'type_display_name'): "cim.2.shared.DocMetaInfo.type_display_name",

    (shared.DocMetaInfo, 'language'): "cim.2.shared.DocMetaInfo.language",

    (shared.DocMetaInfo, 'source_key'): "cim.2.shared.DocMetaInfo.source_key",

    (shared.DocMetaInfo, 'update_date'): "cim.2.shared.DocMetaInfo.update_date",

    (shared.DocMetaInfo, 'author'): "cim.2.shared.DocMetaInfo.author",

    (shared.DocMetaInfo, 'project'): "cim.2.shared.DocMetaInfo.project",

    (shared.DocMetaInfo, 'version'): "cim.2.shared.DocMetaInfo.version",

    (shared.DocMetaInfo, 'id'): "cim.2.shared.DocMetaInfo.id",

    (shared.DocMetaInfo, 'external_ids'): "cim.2.shared.DocMetaInfo.external_ids",

    (shared.TimePeriod, 'units'): "cim.2.shared.TimePeriod.units",

    (shared.TimePeriod, 'date'): "cim.2.shared.TimePeriod.date",

    (shared.TimePeriod, 'length'): "cim.2.shared.TimePeriod.length",

    (shared.TimePeriod, 'calendar'): "cim.2.shared.TimePeriod.calendar",

    (shared.TimePeriod, 'date_type'): "cim.2.shared.TimePeriod.date_type",

    (shared.RegularTimeset, 'increment'): "cim.2.shared.RegularTimeset.increment",

    (shared.RegularTimeset, 'start_date'): "cim.2.shared.RegularTimeset.start_date",

    (shared.RegularTimeset, 'length'): "cim.2.shared.RegularTimeset.length",

    (shared.ExternalDocument, 'online_at'): "cim.2.shared.ExternalDocument.online_at",

    (shared.ExternalDocument, 'title'): "cim.2.shared.ExternalDocument.title",

    (shared.ExternalDocument, 'date'): "cim.2.shared.ExternalDocument.date",

    (shared.ExternalDocument, 'doi'): "cim.2.shared.ExternalDocument.doi",

    (shared.ExternalDocument, 'meta'): "cim.2.shared.ExternalDocument.meta",

    (shared.ExternalDocument, 'publication_detail'): "cim.2.shared.ExternalDocument.publication_detail",

    (shared.ExternalDocument, 'name'): "cim.2.shared.ExternalDocument.name",

    (shared.ExternalDocument, 'authorship'): "cim.2.shared.ExternalDocument.authorship",

    (shared.QualityReview, 'quality_description'): "cim.2.shared.QualityReview.quality_description",

    (shared.QualityReview, 'date'): "cim.2.shared.QualityReview.date",

    (shared.QualityReview, 'quality_status'): "cim.2.shared.QualityReview.quality_status",

    (shared.QualityReview, 'metadata_reviewer'): "cim.2.shared.QualityReview.metadata_reviewer",

    (shared.Reference, 'context'): "cim.2.shared.Reference.context",

    (shared.Reference, 'document'): "cim.2.shared.Reference.document",

    (shared.Responsibility, 'when'): "cim.2.shared.Responsibility.when",

    (shared.Responsibility, 'party'): "cim.2.shared.Responsibility.party",

    (shared.Responsibility, 'role'): "cim.2.shared.Responsibility.role",

    (shared.Cimtext, 'content'): "cim.2.shared.Cimtext.content",

    (shared.Cimtext, 'content_type'): "cim.2.shared.Cimtext.content_type",

    (shared.Calendar, 'description'): "cim.2.shared.Calendar.description",

    (shared.Calendar, 'name'): "cim.2.shared.Calendar.name",

    (shared.Calendar, 'standard_name'): "cim.2.shared.Calendar.standard_name",

    (shared.Calendar, 'month_lengths'): "cim.2.shared.Calendar.month_lengths",

    (shared.IrregularDateset, 'date_set'): "cim.2.shared.IrregularDateset.date_set",

    (activity.Conformance, 'target_requirement'): "cim.2.activity.Conformance.target_requirement",

    (activity.Ensemble, 'has_ensemble_axes'): "cim.2.activity.Ensemble.has_ensemble_axes",

    (activity.Ensemble, 'common_conformances'): "cim.2.activity.Ensemble.common_conformances",

    (activity.Ensemble, 'part_of'): "cim.2.activity.Ensemble.part_of",

    (activity.Ensemble, 'documentation'): "cim.2.activity.Ensemble.documentation",

    (activity.Ensemble, 'members'): "cim.2.activity.Ensemble.members",

    (activity.Ensemble, 'supported'): "cim.2.activity.Ensemble.supported",

    (activity.UberEnsemble, 'child_ensembles'): "cim.2.activity.UberEnsemble.child_ensembles",

    (activity.EnsembleMember, 'errata'): "cim.2.activity.EnsembleMember.errata",

    (activity.EnsembleMember, 'simulation'): "cim.2.activity.EnsembleMember.simulation",

    (activity.EnsembleMember, 'had_performance'): "cim.2.activity.EnsembleMember.had_performance",

    (activity.EnsembleMember, 'variant_id'): "cim.2.activity.EnsembleMember.variant_id",

    (activity.EnsembleMember, 'ran_on'): "cim.2.activity.EnsembleMember.ran_on",

    (activity.ParentSimulation, 'parent'): "cim.2.activity.ParentSimulation.parent",

    (activity.ParentSimulation, 'branch_time_in_child'): "cim.2.activity.ParentSimulation.branch_time_in_child",

    (activity.ParentSimulation, 'branch_time_in_parent'): "cim.2.activity.ParentSimulation.branch_time_in_parent",

    (activity.EnsembleAxis, 'extra_detail'): "cim.2.activity.EnsembleAxis.extra_detail",

    (activity.EnsembleAxis, 'short_identifier'): "cim.2.activity.EnsembleAxis.short_identifier",

    (activity.EnsembleAxis, 'target_requirement'): "cim.2.activity.EnsembleAxis.target_requirement",

    (activity.EnsembleAxis, 'member'): "cim.2.activity.EnsembleAxis.member",

    (activity.Activity, 'canonical_name'): "cim.2.activity.Activity.canonical_name",

    (activity.Activity, 'references'): "cim.2.activity.Activity.references",

    (activity.Activity, 'long_name'): "cim.2.activity.Activity.long_name",

    (activity.Activity, 'meta'): "cim.2.activity.Activity.meta",

    (activity.Activity, 'name'): "cim.2.activity.Activity.name",

    (activity.Activity, 'duration'): "cim.2.activity.Activity.duration",

    (activity.Activity, 'responsible_parties'): "cim.2.activity.Activity.responsible_parties",

    (activity.Activity, 'description'): "cim.2.activity.Activity.description",

    (activity.Activity, 'keywords'): "cim.2.activity.Activity.keywords",

    (activity.Activity, 'rationale'): "cim.2.activity.Activity.rationale",

    (activity.AxisMember, 'description'): "cim.2.activity.AxisMember.description",

    (activity.AxisMember, 'index'): "cim.2.activity.AxisMember.index",

    (activity.AxisMember, 'value'): "cim.2.activity.AxisMember.value",

    (activity.AxisMember, 'extra_detail'): "cim.2.activity.AxisMember.extra_detail",

    (software.DevelopmentPath, 'consortium_name'): "cim.2.software.DevelopmentPath.consortium_name",

    (software.DevelopmentPath, 'previous_version'): "cim.2.software.DevelopmentPath.previous_version",

    (software.DevelopmentPath, 'developed_in_house'): "cim.2.software.DevelopmentPath.developed_in_house",

    (software.DevelopmentPath, 'funding_sources'): "cim.2.software.DevelopmentPath.funding_sources",

    (software.DevelopmentPath, 'creators'): "cim.2.software.DevelopmentPath.creators",

    (software.EntryPoint, 'name'): "cim.2.software.EntryPoint.name",

    (software.Variable, 'prognostic'): "cim.2.software.Variable.prognostic",

    (software.Variable, 'description'): "cim.2.software.Variable.description",

    (software.Variable, 'name'): "cim.2.software.Variable.name",

    (software.SoftwareComponent, 'coupling_framework'): "cim.2.software.SoftwareComponent.coupling_framework",

    (software.SoftwareComponent, 'license'): "cim.2.software.SoftwareComponent.license",

    (software.SoftwareComponent, 'dependencies'): "cim.2.software.SoftwareComponent.dependencies",

    (software.SoftwareComponent, 'connection_points'): "cim.2.software.SoftwareComponent.connection_points",

    (software.SoftwareComponent, 'sub_components'): "cim.2.software.SoftwareComponent.sub_components",

    (software.SoftwareComponent, 'composition'): "cim.2.software.SoftwareComponent.composition",

    (software.SoftwareComponent, 'language'): "cim.2.software.SoftwareComponent.language",

    (software.SoftwareComponent, 'grid'): "cim.2.software.SoftwareComponent.grid",

    (software.Composition, 'couplings'): "cim.2.software.Composition.couplings",

    (software.Composition, 'description'): "cim.2.software.Composition.description",

    (software.ComponentBase, 'repository'): "cim.2.software.ComponentBase.repository",

    (software.ComponentBase, 'long_name'): "cim.2.software.ComponentBase.long_name",

    (software.ComponentBase, 'development_history'): "cim.2.software.ComponentBase.development_history",

    (software.ComponentBase, 'name'): "cim.2.software.ComponentBase.name",

    (software.ComponentBase, 'description'): "cim.2.software.ComponentBase.description",

    (software.ComponentBase, 'version'): "cim.2.software.ComponentBase.version",

    (software.ComponentBase, 'release_date'): "cim.2.software.ComponentBase.release_date",

    (software.ComponentBase, 'documentation'): "cim.2.software.ComponentBase.documentation",

    (software.Gridspec, 'description'): "cim.2.software.Gridspec.description",

    (science.Extent, 'bottom_vertical_level'): "cim.2.science.Extent.bottom_vertical_level",

    (science.Extent, 'z_units'): "cim.2.science.Extent.z_units",

    (science.Extent, 'southern_boundary'): "cim.2.science.Extent.southern_boundary",

    (science.Extent, 'western_boundary'): "cim.2.science.Extent.western_boundary",

    (science.Extent, 'eastern_boundary'): "cim.2.science.Extent.eastern_boundary",

    (science.Extent, 'is_global'): "cim.2.science.Extent.is_global",

    (science.Extent, 'northern_boundary'): "cim.2.science.Extent.northern_boundary",

    (science.Extent, 'top_vertical_level'): "cim.2.science.Extent.top_vertical_level",

    (science.Extent, 'region_known_as'): "cim.2.science.Extent.region_known_as",

    (science.Grid, 'name'): "cim.2.science.Grid.name",

    (science.Grid, 'vertical_grid_type'): "cim.2.science.Grid.vertical_grid_type",

    (science.Grid, 'horizontal_grid_layout'): "cim.2.science.Grid.horizontal_grid_layout",

    (science.Grid, 'horizontal_grid_type'): "cim.2.science.Grid.horizontal_grid_type",

    (science.Grid, 'additional_details'): "cim.2.science.Grid.additional_details",

    (science.Grid, 'vertical_grid_layout'): "cim.2.science.Grid.vertical_grid_layout",

    (science.Grid, 'meta'): "cim.2.science.Grid.meta",

    (science.Grid, 'grid_extent'): "cim.2.science.Grid.grid_extent",

    (science.Process, 'properties'): "cim.2.science.Process.properties",

    (science.Process, 'algorithms'): "cim.2.science.Process.algorithms",

    (science.Process, 'references'): "cim.2.science.Process.references",

    (science.Process, 'implementation_overview'): "cim.2.science.Process.implementation_overview",

    (science.Process, 'sub_processes'): "cim.2.science.Process.sub_processes",

    (science.Process, 'keywords'): "cim.2.science.Process.keywords",

    (science.Algorithm, 'implementation_overview'): "cim.2.science.Algorithm.implementation_overview",

    (science.Algorithm, 'diagnostic_variables'): "cim.2.science.Algorithm.diagnostic_variables",

    (science.Algorithm, 'prognostic_variables'): "cim.2.science.Algorithm.prognostic_variables",

    (science.Algorithm, 'references'): "cim.2.science.Algorithm.references",

    (science.Algorithm, 'forced_variables'): "cim.2.science.Algorithm.forced_variables",

    (science.ScientificDomain, 'meta'): "cim.2.science.ScientificDomain.meta",

    (science.ScientificDomain, 'overview'): "cim.2.science.ScientificDomain.overview",

    (science.ScientificDomain, 'name'): "cim.2.science.ScientificDomain.name",

    (science.ScientificDomain, 'simulates'): "cim.2.science.ScientificDomain.simulates",

    (science.ScientificDomain, 'differing_key_properties'): "cim.2.science.ScientificDomain.differing_key_properties",

    (science.ScientificDomain, 'id'): "cim.2.science.ScientificDomain.id",

    (science.ScientificDomain, 'realm'): "cim.2.science.ScientificDomain.realm",

    (science.ScientificDomain, 'references'): "cim.2.science.ScientificDomain.references",

    (science.ConservationProperties, 'flux_correction_was_used'): "cim.2.science.ConservationProperties.flux_correction_was_used",

    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): "cim.2.science.ConservationProperties.corrected_conserved_prognostic_variables",

    (science.ConservationProperties, 'correction_methodology'): "cim.2.science.ConservationProperties.correction_methodology",

    (science.Resolution, 'typical_x_degrees'): "cim.2.science.Resolution.typical_x_degrees",

    (science.Resolution, 'is_adaptive_grid'): "cim.2.science.Resolution.is_adaptive_grid",

    (science.Resolution, 'name'): "cim.2.science.Resolution.name",

    (science.Resolution, 'number_of_levels'): "cim.2.science.Resolution.number_of_levels",

    (science.Resolution, 'number_of_xy_gridpoints'): "cim.2.science.Resolution.number_of_xy_gridpoints",

    (science.Resolution, 'equivalent_resolution_km'): "cim.2.science.Resolution.equivalent_resolution_km",

    (science.Resolution, 'typical_y_degrees'): "cim.2.science.Resolution.typical_y_degrees",

    (science.KeyProperties, 'extra_conservation_properties'): "cim.2.science.KeyProperties.extra_conservation_properties",

    (science.KeyProperties, 'tuning_applied'): "cim.2.science.KeyProperties.tuning_applied",

    (science.KeyProperties, 'grid'): "cim.2.science.KeyProperties.grid",

    (science.KeyProperties, 'resolution'): "cim.2.science.KeyProperties.resolution",

    (science.KeyProperties, 'additional_detail'): "cim.2.science.KeyProperties.additional_detail",

    (science.KeyProperties, 'time_step'): "cim.2.science.KeyProperties.time_step",

    (science.ScienceContext, 'name'): "cim.2.science.ScienceContext.name",

    (science.ScienceContext, 'context'): "cim.2.science.ScienceContext.context",

    (science.ScienceContext, 'id'): "cim.2.science.ScienceContext.id",

    (science.SubProcess, 'references'): "cim.2.science.SubProcess.references",

    (science.SubProcess, 'implementation_overview'): "cim.2.science.SubProcess.implementation_overview",

    (science.SubProcess, 'properties'): "cim.2.science.SubProcess.properties",

    (science.Detail, 'from_vocab'): "cim.2.science.Detail.from_vocab",

    (science.Detail, 'with_cardinality'): "cim.2.science.Detail.with_cardinality",

    (science.Detail, 'content'): "cim.2.science.Detail.content",

    (science.Detail, 'select'): "cim.2.science.Detail.select",

    (science.Detail, 'detail_selection'): "cim.2.science.Detail.detail_selection",

    (science.Tuning, 'trend_metrics_used'): "cim.2.science.Tuning.trend_metrics_used",

    (science.Tuning, 'description'): "cim.2.science.Tuning.description",

    (science.Tuning, 'regional_metrics_used'): "cim.2.science.Tuning.regional_metrics_used",

    (science.Tuning, 'global_mean_metrics_used'): "cim.2.science.Tuning.global_mean_metrics_used",

    (science.Model, 'coupler'): "cim.2.science.Model.coupler",

    (science.Model, 'simulates'): "cim.2.science.Model.simulates",

    (science.Model, 'id'): "cim.2.science.Model.id",

    (science.Model, 'coupled_components'): "cim.2.science.Model.coupled_components",

    (science.Model, 'internal_software_components'): "cim.2.science.Model.internal_software_components",

    (science.Model, 'model_default_properties'): "cim.2.science.Model.model_default_properties",

    (science.Model, 'meta'): "cim.2.science.Model.meta",

    (science.Model, 'category'): "cim.2.science.Model.category",

    (data.Dataset, 'meta'): "cim.2.data.Dataset.meta",

    (data.Dataset, 'availability'): "cim.2.data.Dataset.availability",

    (data.Dataset, 'name'): "cim.2.data.Dataset.name",

    (data.Dataset, 'description'): "cim.2.data.Dataset.description",

    (data.Dataset, 'responsible_parties'): "cim.2.data.Dataset.responsible_parties",

    (data.Dataset, 'produced_by'): "cim.2.data.Dataset.produced_by",

    (data.Dataset, 'drs_datasets'): "cim.2.data.Dataset.drs_datasets",

    (data.Dataset, 'references'): "cim.2.data.Dataset.references",

    (data.Dataset, 'related_to_dataset'): "cim.2.data.Dataset.related_to_dataset",

    (data.Simulation, 'ran_for_experiments'): "cim.2.data.Simulation.ran_for_experiments",

    (data.Simulation, 'parent_simulation'): "cim.2.data.Simulation.parent_simulation",

    (data.Simulation, 'calendar'): "cim.2.data.Simulation.calendar",

    (data.Simulation, 'used'): "cim.2.data.Simulation.used",

    (data.Simulation, 'part_of_project'): "cim.2.data.Simulation.part_of_project",

    (data.Simulation, 'primary_ensemble'): "cim.2.data.Simulation.primary_ensemble",

    (data.Simulation, 'ensemble_identifier'): "cim.2.data.Simulation.ensemble_identifier",

    (data.VariableCollection, 'collection_name'): "cim.2.data.VariableCollection.collection_name",

    (data.VariableCollection, 'variables'): "cim.2.data.VariableCollection.variables",

    (data.Downscaling, 'downscaled_from'): "cim.2.data.Downscaling.downscaled_from",

    (drs.DrsEnsembleIdentifier, 'realisation_number'): "cim.2.drs.DrsEnsembleIdentifier.realisation_number",

    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): "cim.2.drs.DrsEnsembleIdentifier.initialisation_method_number",

    (drs.DrsEnsembleIdentifier, 'perturbation_number'): "cim.2.drs.DrsEnsembleIdentifier.perturbation_number",

    (drs.DrsPublicationDataset, 'institute'): "cim.2.drs.DrsPublicationDataset.institute",

    (drs.DrsPublicationDataset, 'experiment'): "cim.2.drs.DrsPublicationDataset.experiment",

    (drs.DrsPublicationDataset, 'model'): "cim.2.drs.DrsPublicationDataset.model",

    (drs.DrsPublicationDataset, 'realm'): "cim.2.drs.DrsPublicationDataset.realm",

    (drs.DrsPublicationDataset, 'product'): "cim.2.drs.DrsPublicationDataset.product",

    (drs.DrsPublicationDataset, 'activity'): "cim.2.drs.DrsPublicationDataset.activity",

    (drs.DrsPublicationDataset, 'frequency'): "cim.2.drs.DrsPublicationDataset.frequency",

    (drs.DrsPublicationDataset, 'version_number'): "cim.2.drs.DrsPublicationDataset.version_number",

    (drs.DrsAtomicDataset, 'ensemble_member'): "cim.2.drs.DrsAtomicDataset.ensemble_member",

    (drs.DrsAtomicDataset, 'temporal_constraint'): "cim.2.drs.DrsAtomicDataset.temporal_constraint",

    (drs.DrsAtomicDataset, 'geographical_constraint'): "cim.2.drs.DrsAtomicDataset.geographical_constraint",

    (drs.DrsAtomicDataset, 'variable_name'): "cim.2.drs.DrsAtomicDataset.variable_name",

    (drs.DrsAtomicDataset, 'mip_table'): "cim.2.drs.DrsAtomicDataset.mip_table",

    (drs.DrsTemporalIdentifier, 'suffix'): "cim.2.drs.DrsTemporalIdentifier.suffix",

    (drs.DrsTemporalIdentifier, 'end'): "cim.2.drs.DrsTemporalIdentifier.end",

    (drs.DrsTemporalIdentifier, 'start'): "cim.2.drs.DrsTemporalIdentifier.start",

    (drs.DrsGeographicalIndicator, 'bounding_box'): "cim.2.drs.DrsGeographicalIndicator.bounding_box",

    (drs.DrsGeographicalIndicator, 'spatial_domain'): "cim.2.drs.DrsGeographicalIndicator.spatial_domain",

    (drs.DrsGeographicalIndicator, 'operator'): "cim.2.drs.DrsGeographicalIndicator.operator",

    (platform.StoragePool, 'type'): "cim.2.platform.StoragePool.type",

    (platform.StoragePool, 'volume_available'): "cim.2.platform.StoragePool.volume_available",

    (platform.StoragePool, 'vendor'): "cim.2.platform.StoragePool.vendor",

    (platform.StoragePool, 'description'): "cim.2.platform.StoragePool.description",

    (platform.StoragePool, 'name'): "cim.2.platform.StoragePool.name",

    (platform.StorageVolume, 'units'): "cim.2.platform.StorageVolume.units",

    (platform.StorageVolume, 'volume'): "cim.2.platform.StorageVolume.volume",

    (platform.Machine, 'meta'): "cim.2.platform.Machine.meta",

    (platform.ComputePool, 'compute_cores_per_node'): "cim.2.platform.ComputePool.compute_cores_per_node",

    (platform.ComputePool, 'memory_per_node'): "cim.2.platform.ComputePool.memory_per_node",

    (platform.ComputePool, 'accelerator_type'): "cim.2.platform.ComputePool.accelerator_type",

    (platform.ComputePool, 'cpu_type'): "cim.2.platform.ComputePool.cpu_type",

    (platform.ComputePool, 'model_number'): "cim.2.platform.ComputePool.model_number",

    (platform.ComputePool, 'description'): "cim.2.platform.ComputePool.description",

    (platform.ComputePool, 'name'): "cim.2.platform.ComputePool.name",

    (platform.ComputePool, 'accelerators_per_node'): "cim.2.platform.ComputePool.accelerators_per_node",

    (platform.ComputePool, 'interconnect'): "cim.2.platform.ComputePool.interconnect",

    (platform.ComputePool, 'number_of_nodes'): "cim.2.platform.ComputePool.number_of_nodes",

    (platform.ComputePool, 'operating_system'): "cim.2.platform.ComputePool.operating_system",

    (platform.ComponentPerformance, 'cores_used'): "cim.2.platform.ComponentPerformance.cores_used",

    (platform.ComponentPerformance, 'component'): "cim.2.platform.ComponentPerformance.component",

    (platform.ComponentPerformance, 'speed'): "cim.2.platform.ComponentPerformance.speed",

    (platform.ComponentPerformance, 'nodes_used'): "cim.2.platform.ComponentPerformance.nodes_used",

    (platform.ComponentPerformance, 'component_name'): "cim.2.platform.ComponentPerformance.component_name",

    (platform.Performance, 'io_load'): "cim.2.platform.Performance.io_load",

    (platform.Performance, 'sypd'): "cim.2.platform.Performance.sypd",

    (platform.Performance, 'memory_bloat'): "cim.2.platform.Performance.memory_bloat",

    (platform.Performance, 'chsy'): "cim.2.platform.Performance.chsy",

    (platform.Performance, 'subcomponent_performance'): "cim.2.platform.Performance.subcomponent_performance",

    (platform.Performance, 'meta'): "cim.2.platform.Performance.meta",

    (platform.Performance, 'name'): "cim.2.platform.Performance.name",

    (platform.Performance, 'total_nodes_used'): "cim.2.platform.Performance.total_nodes_used",

    (platform.Performance, 'compiler'): "cim.2.platform.Performance.compiler",

    (platform.Performance, 'load_imbalance'): "cim.2.platform.Performance.load_imbalance",

    (platform.Performance, 'coupler_load'): "cim.2.platform.Performance.coupler_load",

    (platform.Performance, 'platform'): "cim.2.platform.Performance.platform",

    (platform.Performance, 'asypd'): "cim.2.platform.Performance.asypd",

    (platform.Performance, 'model'): "cim.2.platform.Performance.model",

    (platform.Partition, 'online_documentation'): "cim.2.platform.Partition.online_documentation",

    (platform.Partition, 'when_used'): "cim.2.platform.Partition.when_used",

    (platform.Partition, 'description'): "cim.2.platform.Partition.description",

    (platform.Partition, 'partition'): "cim.2.platform.Partition.partition",

    (platform.Partition, 'institution'): "cim.2.platform.Partition.institution",

    (platform.Partition, 'vendor'): "cim.2.platform.Partition.vendor",

    (platform.Partition, 'model_number'): "cim.2.platform.Partition.model_number",

    (platform.Partition, 'name'): "cim.2.platform.Partition.name",

    (platform.Partition, 'storage_pools'): "cim.2.platform.Partition.storage_pools",

    (platform.Partition, 'compute_pools'): "cim.2.platform.Partition.compute_pools",

    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------

    designing.ExperimentalRelationships: "cim.2.designing.ExperimentalRelationships",

    designing.EnsembleTypes: "cim.2.designing.EnsembleTypes",

    designing.ForcingTypes: "cim.2.designing.ForcingTypes",

    shared.TimeUnits: "cim.2.shared.TimeUnits",

    shared.TextCode: "cim.2.shared.TextCode",

    shared.PeriodDateTypes: "cim.2.shared.PeriodDateTypes",

    shared.RoleCode: "cim.2.shared.RoleCode",

    shared.CalendarTypes: "cim.2.shared.CalendarTypes",

    shared.QualityStatus: "cim.2.shared.QualityStatus",

    shared.DocumentTypes: "cim.2.shared.DocumentTypes",

    shared.SlicetimeUnits: "cim.2.shared.SlicetimeUnits",

    shared.NilReason: "cim.2.shared.NilReason",

    activity.ForcingTypes: "cim.2.activity.ForcingTypes",

    activity.EnsembleTypes: "cim.2.activity.EnsembleTypes",

    software.ProgrammingLanguage: "cim.2.software.ProgrammingLanguage",

    software.CouplingFramework: "cim.2.software.CouplingFramework",

    science.ModelTypes: "cim.2.science.ModelTypes",

    science.SelectionCardinality: "cim.2.science.SelectionCardinality",

    data.DataAssociationTypes: "cim.2.data.DataAssociationTypes",

    drs.DrsFrequencyTypes: "cim.2.drs.DrsFrequencyTypes",

    drs.DrsTimeSuffixes: "cim.2.drs.DrsTimeSuffixes",

    drs.DrsRealms: "cim.2.drs.DrsRealms",

    drs.DrsGeographicalOperators: "cim.2.drs.DrsGeographicalOperators",

    platform.StorageSystems: "cim.2.platform.StorageSystems",

    platform.VolumeUnits: "cim.2.platform.VolumeUnits",

    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------

    (designing.ExperimentalRelationships, 'initialisation_for'): "cim.2.designing.ExperimentalRelationships.initialisation_for",

    (designing.ExperimentalRelationships, 'provides_constraints'): "cim.2.designing.ExperimentalRelationships.provides_constraints",

    (designing.ExperimentalRelationships, 'control_for'): "cim.2.designing.ExperimentalRelationships.control_for",

    (designing.ExperimentalRelationships, 'is_sibling'): "cim.2.designing.ExperimentalRelationships.is_sibling",

    (designing.EnsembleTypes, 'Initialisation'): "cim.2.designing.EnsembleTypes.Initialisation",

    (designing.EnsembleTypes, 'Staggered Start'): "cim.2.designing.EnsembleTypes.Staggered-Start",

    (designing.EnsembleTypes, 'Forced'): "cim.2.designing.EnsembleTypes.Forced",

    (designing.EnsembleTypes, 'Resolution'): "cim.2.designing.EnsembleTypes.Resolution",

    (designing.EnsembleTypes, 'Perturbed Physics'): "cim.2.designing.EnsembleTypes.Perturbed-Physics",

    (designing.EnsembleTypes, 'Initialisation Method'): "cim.2.designing.EnsembleTypes.Initialisation-Method",

    (designing.ForcingTypes, 'another simulation'): "cim.2.designing.ForcingTypes.another-simulation",

    (designing.ForcingTypes, 'scenario'): "cim.2.designing.ForcingTypes.scenario",

    (designing.ForcingTypes, 'historical'): "cim.2.designing.ForcingTypes.historical",

    (designing.ForcingTypes, 'idealised'): "cim.2.designing.ForcingTypes.idealised",

    (shared.TimeUnits, 'years'): "cim.2.shared.TimeUnits.years",

    (shared.TimeUnits, 'months'): "cim.2.shared.TimeUnits.months",

    (shared.TimeUnits, 'days'): "cim.2.shared.TimeUnits.days",

    (shared.TimeUnits, 'seconds'): "cim.2.shared.TimeUnits.seconds",

    (shared.TextCode, 'plaintext'): "cim.2.shared.TextCode.plaintext",

    (shared.PeriodDateTypes, 'date is start'): "cim.2.shared.PeriodDateTypes.date-is-start",

    (shared.PeriodDateTypes, 'date is end'): "cim.2.shared.PeriodDateTypes.date-is-end",

    (shared.PeriodDateTypes, 'unused'): "cim.2.shared.PeriodDateTypes.unused",

    (shared.RoleCode, 'metadata_reviewer'): "cim.2.shared.RoleCode.metadata_reviewer",

    (shared.RoleCode, 'user'): "cim.2.shared.RoleCode.user",

    (shared.RoleCode, 'metadata_author'): "cim.2.shared.RoleCode.metadata_author",

    (shared.RoleCode, 'owner'): "cim.2.shared.RoleCode.owner",

    (shared.RoleCode, 'distributor'): "cim.2.shared.RoleCode.distributor",

    (shared.RoleCode, 'sponsor'): "cim.2.shared.RoleCode.sponsor",

    (shared.RoleCode, 'Principal Investigator'): "cim.2.shared.RoleCode.Principal-Investigator",

    (shared.RoleCode, 'publisher'): "cim.2.shared.RoleCode.publisher",

    (shared.RoleCode, 'originator'): "cim.2.shared.RoleCode.originator",

    (shared.RoleCode, 'author'): "cim.2.shared.RoleCode.author",

    (shared.RoleCode, 'resource provider'): "cim.2.shared.RoleCode.resource-provider",

    (shared.RoleCode, 'collaborator'): "cim.2.shared.RoleCode.collaborator",

    (shared.RoleCode, 'processor'): "cim.2.shared.RoleCode.processor",

    (shared.RoleCode, 'custodian'): "cim.2.shared.RoleCode.custodian",

    (shared.RoleCode, 'point of contact'): "cim.2.shared.RoleCode.point-of-contact",

    (shared.CalendarTypes, '365_day'): "cim.2.shared.CalendarTypes.365_day",

    (shared.CalendarTypes, 'all_leap'): "cim.2.shared.CalendarTypes.all_leap",

    (shared.CalendarTypes, 'gregorian'): "cim.2.shared.CalendarTypes.gregorian",

    (shared.CalendarTypes, '366_day'): "cim.2.shared.CalendarTypes.366_day",

    (shared.CalendarTypes, '360_day'): "cim.2.shared.CalendarTypes.360_day",

    (shared.CalendarTypes, 'julian'): "cim.2.shared.CalendarTypes.julian",

    (shared.CalendarTypes, 'none'): "cim.2.shared.CalendarTypes.none",

    (shared.CalendarTypes, 'proleptic_gregorian'): "cim.2.shared.CalendarTypes.proleptic_gregorian",

    (shared.CalendarTypes, 'noleap'): "cim.2.shared.CalendarTypes.noleap",

    (shared.CalendarTypes, 'standard'): "cim.2.shared.CalendarTypes.standard",

    (shared.QualityStatus, 'finalised'): "cim.2.shared.QualityStatus.finalised",

    (shared.QualityStatus, 'under_review'): "cim.2.shared.QualityStatus.under_review",

    (shared.QualityStatus, 'incomplete'): "cim.2.shared.QualityStatus.incomplete",

    (shared.QualityStatus, 'reviewed'): "cim.2.shared.QualityStatus.reviewed",

    (shared.DocumentTypes, 'Project'): "cim.2.shared.DocumentTypes.Project",

    (shared.DocumentTypes, 'ScientificDomain'): "cim.2.shared.DocumentTypes.ScientificDomain",

    (shared.DocumentTypes, 'Simulation'): "cim.2.shared.DocumentTypes.Simulation",

    (shared.DocumentTypes, 'SimulationPlan'): "cim.2.shared.DocumentTypes.SimulationPlan",

    (shared.DocumentTypes, 'TemporalConstraint'): "cim.2.shared.DocumentTypes.TemporalConstraint",

    (shared.DocumentTypes, 'UberEnsemble'): "cim.2.shared.DocumentTypes.UberEnsemble",

    (shared.DocumentTypes, 'Conformance'): "cim.2.shared.DocumentTypes.Conformance",

    (shared.DocumentTypes, 'Dataset'): "cim.2.shared.DocumentTypes.Dataset",

    (shared.DocumentTypes, 'DomainProperties'): "cim.2.shared.DocumentTypes.DomainProperties",

    (shared.DocumentTypes, 'Downscaling'): "cim.2.shared.DocumentTypes.Downscaling",

    (shared.DocumentTypes, 'Ensemble'): "cim.2.shared.DocumentTypes.Ensemble",

    (shared.DocumentTypes, 'EnsembleRequirement'): "cim.2.shared.DocumentTypes.EnsembleRequirement",

    (shared.DocumentTypes, 'ExternalDocument'): "cim.2.shared.DocumentTypes.ExternalDocument",

    (shared.DocumentTypes, 'ForcingConstraint'): "cim.2.shared.DocumentTypes.ForcingConstraint",

    (shared.DocumentTypes, 'Grid'): "cim.2.shared.DocumentTypes.Grid",

    (shared.DocumentTypes, 'Machine'): "cim.2.shared.DocumentTypes.Machine",

    (shared.DocumentTypes, 'Model'): "cim.2.shared.DocumentTypes.Model",

    (shared.DocumentTypes, 'MultiEnsemble'): "cim.2.shared.DocumentTypes.MultiEnsemble",

    (shared.DocumentTypes, 'MultiTimeEnsemble'): "cim.2.shared.DocumentTypes.MultiTimeEnsemble",

    (shared.DocumentTypes, 'NumericalExperiment'): "cim.2.shared.DocumentTypes.NumericalExperiment",

    (shared.DocumentTypes, 'NumericalRequirement'): "cim.2.shared.DocumentTypes.NumericalRequirement",

    (shared.DocumentTypes, 'OutputTemporalRequirement'): "cim.2.shared.DocumentTypes.OutputTemporalRequirement",

    (shared.DocumentTypes, 'Party'): "cim.2.shared.DocumentTypes.Party",

    (shared.DocumentTypes, 'Performance'): "cim.2.shared.DocumentTypes.Performance",

    (shared.SlicetimeUnits, 'monthly'): "cim.2.shared.SlicetimeUnits.monthly",

    (shared.SlicetimeUnits, 'yearly'): "cim.2.shared.SlicetimeUnits.yearly",

    (shared.NilReason, 'nil:missing'): "cim.2.shared.NilReason.nil:missing",

    (shared.NilReason, 'nil:unknown'): "cim.2.shared.NilReason.nil:unknown",

    (shared.NilReason, 'nil:withheld'): "cim.2.shared.NilReason.nil:withheld",

    (shared.NilReason, 'nil:inapplicable'): "cim.2.shared.NilReason.nil:inapplicable",

    (shared.NilReason, 'nil:template'): "cim.2.shared.NilReason.nil:template",

    (activity.ForcingTypes, 'another simulation'): "cim.2.activity.ForcingTypes.another-simulation",

    (activity.ForcingTypes, 'scenario'): "cim.2.activity.ForcingTypes.scenario",

    (activity.ForcingTypes, 'historical'): "cim.2.activity.ForcingTypes.historical",

    (activity.ForcingTypes, 'idealised'): "cim.2.activity.ForcingTypes.idealised",

    (activity.EnsembleTypes, 'Perturbed Physics'): "cim.2.activity.EnsembleTypes.Perturbed-Physics",

    (activity.EnsembleTypes, 'Initialisation Method'): "cim.2.activity.EnsembleTypes.Initialisation-Method",

    (activity.EnsembleTypes, 'Initialisation'): "cim.2.activity.EnsembleTypes.Initialisation",

    (activity.EnsembleTypes, 'Staggered Start'): "cim.2.activity.EnsembleTypes.Staggered-Start",

    (activity.EnsembleTypes, 'Forced'): "cim.2.activity.EnsembleTypes.Forced",

    (activity.EnsembleTypes, 'Resolution'): "cim.2.activity.EnsembleTypes.Resolution",

    (software.ProgrammingLanguage, 'C'): "cim.2.software.ProgrammingLanguage.C",

    (software.ProgrammingLanguage, 'Python'): "cim.2.software.ProgrammingLanguage.Python",

    (software.ProgrammingLanguage, 'C++'): "cim.2.software.ProgrammingLanguage.C++",

    (software.ProgrammingLanguage, 'Fortran'): "cim.2.software.ProgrammingLanguage.Fortran",

    (software.CouplingFramework, 'OASIS'): "cim.2.software.CouplingFramework.OASIS",

    (software.CouplingFramework, 'OASIS3-MCT'): "cim.2.software.CouplingFramework.OASIS3-MCT",

    (software.CouplingFramework, 'ESMF'): "cim.2.software.CouplingFramework.ESMF",

    (software.CouplingFramework, 'NUOPC'): "cim.2.software.CouplingFramework.NUOPC",

    (software.CouplingFramework, 'Bespoke'): "cim.2.software.CouplingFramework.Bespoke",

    (software.CouplingFramework, 'Unknown'): "cim.2.software.CouplingFramework.Unknown",

    (software.CouplingFramework, 'None'): "cim.2.software.CouplingFramework.None",

    (science.ModelTypes, 'Atm Only'): "cim.2.science.ModelTypes.Atm-Only",

    (science.ModelTypes, 'Ocean Only'): "cim.2.science.ModelTypes.Ocean-Only",

    (science.ModelTypes, 'Planetary'): "cim.2.science.ModelTypes.Planetary",

    (science.ModelTypes, 'Regional'): "cim.2.science.ModelTypes.Regional",

    (science.ModelTypes, 'GCM'): "cim.2.science.ModelTypes.GCM",

    (science.ModelTypes, 'IGCM'): "cim.2.science.ModelTypes.IGCM",

    (science.ModelTypes, 'GCM-MLO'): "cim.2.science.ModelTypes.GCM-MLO",

    (science.ModelTypes, 'Mesoscale'): "cim.2.science.ModelTypes.Mesoscale",

    (science.ModelTypes, 'Process'): "cim.2.science.ModelTypes.Process",

    (science.SelectionCardinality, '1.N'): "cim.2.science.SelectionCardinality.1.N",

    (science.SelectionCardinality, '0.1'): "cim.2.science.SelectionCardinality.0.1",

    (science.SelectionCardinality, '0.N'): "cim.2.science.SelectionCardinality.0.N",

    (science.SelectionCardinality, '1.1'): "cim.2.science.SelectionCardinality.1.1",

    (data.DataAssociationTypes, 'isComposedOf'): "cim.2.data.DataAssociationTypes.isComposedOf",

    (data.DataAssociationTypes, 'partOf'): "cim.2.data.DataAssociationTypes.partOf",

    (data.DataAssociationTypes, 'revisonOf'): "cim.2.data.DataAssociationTypes.revisonOf",

    (drs.DrsFrequencyTypes, 'subhr'): "cim.2.drs.DrsFrequencyTypes.subhr",

    (drs.DrsFrequencyTypes, 'monClim'): "cim.2.drs.DrsFrequencyTypes.monClim",

    (drs.DrsFrequencyTypes, 'fx'): "cim.2.drs.DrsFrequencyTypes.fx",

    (drs.DrsFrequencyTypes, 'yr'): "cim.2.drs.DrsFrequencyTypes.yr",

    (drs.DrsFrequencyTypes, 'mon'): "cim.2.drs.DrsFrequencyTypes.mon",

    (drs.DrsFrequencyTypes, 'day'): "cim.2.drs.DrsFrequencyTypes.day",

    (drs.DrsFrequencyTypes, '6hr'): "cim.2.drs.DrsFrequencyTypes.6hr",

    (drs.DrsFrequencyTypes, '3hr'): "cim.2.drs.DrsFrequencyTypes.3hr",

    (drs.DrsTimeSuffixes, 'avg'): "cim.2.drs.DrsTimeSuffixes.avg",

    (drs.DrsTimeSuffixes, 'clim'): "cim.2.drs.DrsTimeSuffixes.clim",

    (drs.DrsRealms, 'atmosChem'): "cim.2.drs.DrsRealms.atmosChem",

    (drs.DrsRealms, 'ocnBgchem'): "cim.2.drs.DrsRealms.ocnBgchem",

    (drs.DrsRealms, 'atmos'): "cim.2.drs.DrsRealms.atmos",

    (drs.DrsRealms, 'ocean'): "cim.2.drs.DrsRealms.ocean",

    (drs.DrsRealms, 'land'): "cim.2.drs.DrsRealms.land",

    (drs.DrsRealms, 'landIce'): "cim.2.drs.DrsRealms.landIce",

    (drs.DrsRealms, 'seaIce'): "cim.2.drs.DrsRealms.seaIce",

    (drs.DrsRealms, 'aerosol'): "cim.2.drs.DrsRealms.aerosol",

    (drs.DrsGeographicalOperators, 'lnd-zonalavg'): "cim.2.drs.DrsGeographicalOperators.lnd-zonalavg",

    (drs.DrsGeographicalOperators, 'ocn-zonalavg'): "cim.2.drs.DrsGeographicalOperators.ocn-zonalavg",

    (drs.DrsGeographicalOperators, 'areaavg'): "cim.2.drs.DrsGeographicalOperators.areaavg",

    (drs.DrsGeographicalOperators, 'lnd-areaavg'): "cim.2.drs.DrsGeographicalOperators.lnd-areaavg",

    (drs.DrsGeographicalOperators, 'ocn-areaavg'): "cim.2.drs.DrsGeographicalOperators.ocn-areaavg",

    (drs.DrsGeographicalOperators, 'zonalavg'): "cim.2.drs.DrsGeographicalOperators.zonalavg",

    (platform.StorageSystems, 'Other Disk'): "cim.2.platform.StorageSystems.Other-Disk",

    (platform.StorageSystems, 'Tape - MARS'): "cim.2.platform.StorageSystems.Tape---MARS",

    (platform.StorageSystems, 'Tape - Other'): "cim.2.platform.StorageSystems.Tape---Other",

    (platform.StorageSystems, 'Tape - MASS'): "cim.2.platform.StorageSystems.Tape---MASS",

    (platform.StorageSystems, 'Tape - Castor'): "cim.2.platform.StorageSystems.Tape---Castor",

    (platform.StorageSystems, 'Lustre'): "cim.2.platform.StorageSystems.Lustre",

    (platform.StorageSystems, 'GPFS'): "cim.2.platform.StorageSystems.GPFS",

    (platform.StorageSystems, 'Unknown'): "cim.2.platform.StorageSystems.Unknown",

    (platform.StorageSystems, 'NFS'): "cim.2.platform.StorageSystems.NFS",

    (platform.StorageSystems, 'Panasas'): "cim.2.platform.StorageSystems.Panasas",

    (platform.StorageSystems, 'isilon'): "cim.2.platform.StorageSystems.isilon",

    (platform.VolumeUnits, 'PiB'): "cim.2.platform.VolumeUnits.PiB",

    (platform.VolumeUnits, 'EiB'): "cim.2.platform.VolumeUnits.EiB",

    (platform.VolumeUnits, 'GB'): "cim.2.platform.VolumeUnits.GB",

    (platform.VolumeUnits, 'TB'): "cim.2.platform.VolumeUnits.TB",

    (platform.VolumeUnits, 'PB'): "cim.2.platform.VolumeUnits.PB",

    (platform.VolumeUnits, 'EB'): "cim.2.platform.VolumeUnits.EB",

    (platform.VolumeUnits, 'TiB'): "cim.2.platform.VolumeUnits.TiB",

}