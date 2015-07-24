# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v2 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:45:43.343652.

"""
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_activity_package as activity




# Set type keys.
shared.Citation.type_key = 'cim.2.shared.Citation'
shared.CimLink.type_key = 'cim.2.shared.CimLink'
activity.EnsembleMember.type_key = 'cim.2.activity.EnsembleMember'
activity.ForcingConstraint.type_key = 'cim.2.activity.ForcingConstraint'
science.Tuning.type_key = 'cim.2.science.Tuning'
science.Extent.type_key = 'cim.2.science.Extent'
drs.DrsTemporalIdentifier.type_key = 'cim.2.drs.DrsTemporalIdentifier'
activity.EnsembleAxis.type_key = 'cim.2.activity.EnsembleAxis'
science.Algorithm.type_key = 'cim.2.science.Algorithm'
activity.OutputTemporalRequirement.type_key = 'cim.2.activity.OutputTemporalRequirement'
shared.Reference.type_key = 'cim.2.shared.Reference'
data.Dataset.type_key = 'cim.2.data.Dataset'
science.GridSummary.type_key = 'cim.2.science.GridSummary'
activity.Ensemble.type_key = 'cim.2.activity.Ensemble'
software.EntryPoint.type_key = 'cim.2.software.EntryPoint'
activity.Project.type_key = 'cim.2.activity.Project'
science.ScientificDomain.type_key = 'cim.2.science.ScientificDomain'
shared.DateTime.type_key = 'cim.2.shared.DateTime'
drs.DrsPublicationDataset.type_key = 'cim.2.drs.DrsPublicationDataset'
platform.Performance.type_key = 'cim.2.platform.Performance'
activity.TemporalConstraint.type_key = 'cim.2.activity.TemporalConstraint'
activity.MultiEnsemble.type_key = 'cim.2.activity.MultiEnsemble'
activity.Activity.type_key = 'cim.2.activity.Activity'
shared.Calendar.type_key = 'cim.2.shared.Calendar'
activity.NumericalRequirement.type_key = 'cim.2.activity.NumericalRequirement'
drs.DrsAtomicDataset.type_key = 'cim.2.drs.DrsAtomicDataset'
science.ProcessDetail.type_key = 'cim.2.science.ProcessDetail'
shared.Party.type_key = 'cim.2.shared.Party'
activity.SimulationPlan.type_key = 'cim.2.activity.SimulationPlan'
shared.Pid.type_key = 'cim.2.shared.Pid'
shared.StandaloneDocument.type_key = 'cim.2.shared.StandaloneDocument'
science.Resolution.type_key = 'cim.2.science.Resolution'
activity.Simulation.type_key = 'cim.2.activity.Simulation'
software.DevelopmentPath.type_key = 'cim.2.software.DevelopmentPath'
science.ConservationProperties.type_key = 'cim.2.science.ConservationProperties'
shared.MinimalMeta.type_key = 'cim.2.shared.MinimalMeta'
activity.DomainProperties.type_key = 'cim.2.activity.DomainProperties'
platform.ComputePool.type_key = 'cim.2.platform.ComputePool'
activity.MultiTimeEnsemble.type_key = 'cim.2.activity.MultiTimeEnsemble'
shared.Meta.type_key = 'cim.2.shared.Meta'
platform.ComponentPerformance.type_key = 'cim.2.platform.ComponentPerformance'
shared.OnlineResource.type_key = 'cim.2.shared.OnlineResource'
activity.UberEnsemble.type_key = 'cim.2.activity.UberEnsemble'
activity.AxisMember.type_key = 'cim.2.activity.AxisMember'
shared.KeyFloat.type_key = 'cim.2.shared.KeyFloat'
shared.IrregularDateset.type_key = 'cim.2.shared.IrregularDateset'
software.ComponentBase.type_key = 'cim.2.software.ComponentBase'
software.Model.type_key = 'cim.2.software.Model'
shared.TimesliceList.type_key = 'cim.2.shared.TimesliceList'
activity.NumericalExperiment.type_key = 'cim.2.activity.NumericalExperiment'
activity.Downscaling.type_key = 'cim.2.activity.Downscaling'
software.Composition.type_key = 'cim.2.software.Composition'
platform.Partition.type_key = 'cim.2.platform.Partition'
activity.EnsembleRequirement.type_key = 'cim.2.activity.EnsembleRequirement'
data.VariableCollection.type_key = 'cim.2.data.VariableCollection'
platform.StoragePool.type_key = 'cim.2.platform.StoragePool'
shared.TimePeriod.type_key = 'cim.2.shared.TimePeriod'
shared.NumberArray.type_key = 'cim.2.shared.NumberArray'
shared.RegularTimeset.type_key = 'cim.2.shared.RegularTimeset'
shared.Cimtext.type_key = 'cim.2.shared.Cimtext'
software.Gridspec.type_key = 'cim.2.software.Gridspec'
software.Variable.type_key = 'cim.2.software.Variable'
software.SoftwareComponent.type_key = 'cim.2.software.SoftwareComponent'
data.RelatedData.type_key = 'cim.2.data.RelatedData'
shared.Responsibility.type_key = 'cim.2.shared.Responsibility'
drs.DrsGeographicalIndicator.type_key = 'cim.2.drs.DrsGeographicalIndicator'
platform.StorageVolume.type_key = 'cim.2.platform.StorageVolume'
drs.DrsEnsembleIdentifier.type_key = 'cim.2.drs.DrsEnsembleIdentifier'
shared.DatetimeSet.type_key = 'cim.2.shared.DatetimeSet'
platform.Machine.type_key = 'cim.2.platform.Machine'
activity.ParentSimulation.type_key = 'cim.2.activity.ParentSimulation'
activity.Conformance.type_key = 'cim.2.activity.Conformance'
science.Process.type_key = 'cim.2.science.Process'
shared.VocabMember.type_key = 'cim.2.shared.VocabMember'


# Set type info (name, type, is_required, is_iterative).
shared.Citation.type_info = (
    ('abstract', str, False, False),
    ('context', shared.Cimtext, False, False),
    ('url', shared.OnlineResource, False, False),
    ('citation_str', shared.Cimtext, True, False),
    ('doi', str, False, False),
    ('title', str, False, False),
)

shared.CimLink.type_info = (
    ('remote_type', str, True, False),
)

activity.EnsembleMember.type_info = (
    ('had_performance', platform.Performance, False, False),
    ('simulation', activity.Simulation, True, False),
    ('ran_on', platform.Machine, True, False),
)

activity.ForcingConstraint.type_info = (
    ('forcing_type', str, True, False),
    ('origin', shared.Citation, False, False),
    ('additional_constraint', shared.Cimtext, False, False),
    ('category', shared.VocabMember, True, False),
    ('code', shared.VocabMember, True, False),
    ('group', shared.VocabMember, False, False),
    ('data_link', shared.OnlineResource, False, False),
)

science.Tuning.type_info = (
    ('regional_metrics_used', data.VariableCollection, False, False),
    ('trend_metrics_used', data.VariableCollection, False, False),
    ('description', shared.Cimtext, True, False),
    ('global_mean_metrics_used', data.VariableCollection, False, False),
)

science.Extent.type_info = (
    ('northern_boundary', float, False, False),
    ('region_known_as', str, False, True),
    ('is_global', bool, True, False),
    ('minimum_vertical_level', float, False, False),
    ('western_boundary', float, False, False),
    ('maximum_vertical_level', float, False, False),
    ('southern_boundary', float, False, False),
    ('eastern_boundary', float, False, False),
    ('z_units', str, True, False),
)

drs.DrsTemporalIdentifier.type_info = (
    ('end', str, False, False),
    ('suffix', str, False, False),
    ('start', str, True, False),
)

activity.EnsembleAxis.type_info = (
    ('extra_detail', shared.Cimtext, True, False),
    ('short_identifier', str, True, False),
    ('target_requirement', activity.NumericalRequirement, True, False),
    ('member', activity.AxisMember, True, True),
)

science.Algorithm.type_info = (
    ('prognostic_variables', data.VariableCollection, False, True),
    ('diagnostic_variables', data.VariableCollection, False, True),
    ('references', shared.Citation, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
    ('heading', str, True, False),
)

activity.OutputTemporalRequirement.type_info = (
    ('throughout', bool, True, False),
    ('continuous_subset', shared.TimePeriod, False, True),
    ('sliced_subset', shared.TimesliceList, False, False),
)

shared.Reference.type_info = (
)

data.Dataset.type_info = (
    ('meta', shared.Meta, True, False),
    ('references', shared.Citation, False, True),
    ('related_to_dataset', data.RelatedData, False, True),
    ('description', str, False, False),
    ('availability', shared.OnlineResource, False, True),
    ('dataset_author', shared.Party, False, True),
    ('produced_by', activity.Simulation, False, False),
    ('drs_datasets', drs.DrsPublicationDataset, False, True),
    ('name', str, True, False),
)

science.GridSummary.type_info = (
    ('grid_type', str, True, False),
    ('grid_extent', science.Extent, True, False),
    ('grid_layout', str, True, False),
)

activity.Ensemble.type_info = (
    ('part_of', activity.UberEnsemble, False, True),
    ('members', activity.EnsembleMember, True, True),
    ('supported', activity.NumericalExperiment, True, True),
    ('common_conformances', activity.Conformance, False, True),
    ('has_ensemble_axes', activity.EnsembleAxis, False, True),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

activity.Project.type_info = (
    ('previous_projects', activity.Project, False, True),
    ('sub_projects', activity.Project, False, True),
    ('requires_experiments', activity.NumericalExperiment, False, True),
)

science.ScientificDomain.type_info = (
    ('realm', str, False, False),
    ('meta', shared.Meta, True, False),
    ('simulates', science.Process, True, True),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('references', shared.Reference, False, True),
    ('grid', science.GridSummary, False, False),
    ('overview', shared.Cimtext, False, False),
    ('name', str, True, False),
    ('time_step', float, True, False),
    ('resolution', science.Resolution, True, False),
)

shared.DateTime.type_info = (
    ('offset', bool, False, False),
    ('value', str, True, False),
)

drs.DrsPublicationDataset.type_info = (
    ('model', str, True, False),
    ('version_number', int, False, False),
    ('product', str, True, False),
    ('activity', str, True, False),
    ('realm', str, False, False),
    ('frequency', str, False, False),
    ('experiment', str, True, False),
    ('institute', str, True, False),
)

platform.Performance.type_info = (
    ('chsy', float, False, False),
    ('compiler', str, False, False),
    ('memory_bloat', float, False, False),
    ('meta', shared.Meta, True, False),
    ('asypd', float, False, False),
    ('model', software.Model, True, False),
    ('subcomponent_performance', platform.ComponentPerformance, False, False),
    ('load_imbalance', float, False, False),
    ('platform', platform.Machine, True, False),
    ('sypd', float, False, False),
    ('coupler_load', float, False, False),
    ('io_load', float, False, False),
    ('total_nodes_used', int, False, False),
    ('name', str, False, False),
)

activity.TemporalConstraint.type_info = (
    ('start_date', shared.DateTime, False, False),
    ('start_flexibility', shared.TimePeriod, False, False),
    ('required_calendar', shared.Calendar, False, False),
    ('required_duration', shared.TimePeriod, False, False),
)

activity.MultiEnsemble.type_info = (
    ('ensemble_axis', activity.EnsembleRequirement, True, True),
)

activity.Activity.type_info = (
    ('canonical_name', str, False, False),
    ('name', str, True, False),
    ('keywords', str, False, True),
    ('description', shared.Cimtext, False, False),
    ('references', shared.Citation, False, True),
    ('meta', shared.Meta, True, False),
    ('duration', shared.TimePeriod, False, False),
    ('long_name', str, False, False),
    ('rationale', shared.Cimtext, False, False),
    ('responsible_parties', shared.Responsibility, False, True),
)

shared.Calendar.type_info = (
    ('cal_type', str, True, False),
    ('name', str, False, False),
    ('month_lengths', int, False, True),
    ('description', str, False, False),
)

activity.NumericalRequirement.type_info = (
    ('additional_requirements', activity.NumericalRequirement, False, True),
    ('conformance_is_requested', bool, True, False),
)

drs.DrsAtomicDataset.type_info = (
    ('temporal_constraint', drs.DrsTemporalIdentifier, False, False),
    ('mip_table', str, True, False),
    ('variable_name', str, True, False),
    ('ensemble_member', drs.DrsEnsembleIdentifier, True, False),
    ('geographical_constraint', drs.DrsGeographicalIndicator, False, False),
)

science.ProcessDetail.type_info = (
    ('content', shared.Cimtext, False, False),
    ('vocabulary', str, False, False),
    ('selection', str, False, True),
    ('properties', shared.KeyFloat, False, True),
    ('heading', str, False, False),
)

shared.Party.type_info = (
    ('address', str, False, False),
    ('name', str, False, False),
    ('email', str, False, False),
    ('url', shared.OnlineResource, False, False),
    ('meta', shared.MinimalMeta, True, False),
    ('organisation', bool, False, False),
)

activity.SimulationPlan.type_info = (
    ('expected_platform', platform.Machine, False, False),
    ('expected_model', software.Model, True, False),
    ('will_support_experiments', activity.NumericalExperiment, True, True),
    ('expected_performance_sypd', float, False, False),
)

shared.Pid.type_info = (
    ('id', str, True, False),
    ('resolution_service', shared.OnlineResource, True, False),
)

shared.StandaloneDocument.type_info = (
    ('name', str, True, False),
    ('responsible_parties', shared.Responsibility, False, True),
    ('references', shared.Citation, False, True),
    ('long_name', str, False, False),
    ('meta', shared.Meta, True, False),
)

science.Resolution.type_info = (
    ('number_of_xy_gridpoints', int, False, True),
    ('equivalent_horizontal_resolution', float, True, False),
    ('number_of_levels', int, False, True),
    ('name', str, True, False),
    ('is_adaptive_grid', bool, False, False),
)

activity.Simulation.type_info = (
    ('primary_ensemble', activity.Ensemble, False, False),
    ('part_of_project', activity.Project, True, True),
    ('ensemble_identifier', str, True, False),
    ('run_for_experiments', activity.NumericalExperiment, True, True),
    ('parent_simulation', activity.ParentSimulation, False, False),
    ('used', software.Model, True, False),
)

software.DevelopmentPath.type_info = (
    ('previous_version', str, False, False),
    ('developed_in_house', bool, True, False),
    ('funding_sources', shared.Responsibility, False, True),
    ('consortium_name', str, False, False),
    ('creators', shared.Responsibility, False, True),
)

science.ConservationProperties.type_info = (
    ('corrected_conserved_prognostic_variables', data.VariableCollection, False, False),
    ('flux_correction_was_used', bool, True, False),
    ('correction_methodology', shared.Cimtext, False, False),
)

shared.MinimalMeta.type_info = (
    ('document_version', int, False, False),
    ('uid', str, True, False),
    ('metadata_last_updated', datetime.datetime, True, False),
)

activity.DomainProperties.type_info = (
    ('required_extent', science.Extent, False, False),
    ('required_resolution', science.Resolution, False, False),
)

platform.ComputePool.type_info = (
    ('model_number', str, False, False),
    ('accelerators_per_node', int, False, False),
    ('operating_system', str, False, False),
    ('memory_per_node', platform.StorageVolume, False, False),
    ('compute_cores_per_node', int, False, False),
    ('description', shared.Cimtext, False, False),
    ('accelerator_type', str, False, False),
    ('interconnect', str, False, False),
    ('number_of_nodes', int, False, False),
    ('cpu_type', str, False, False),
    ('name', str, False, False),
)

activity.MultiTimeEnsemble.type_info = (
    ('ensemble_members', shared.DatetimeSet, True, False),
)

shared.Meta.type_info = (
    ('metadata_author', shared.Party, True, False),
    ('metadata_quality', str, False, False),
    ('metadata_reviewer', shared.Party, False, False),
    ('metadata_completeness', str, False, False),
)

platform.ComponentPerformance.type_info = (
    ('speed', float, True, False),
    ('cores_used', int, False, False),
    ('component', software.SoftwareComponent, False, False),
    ('nodes_used', int, False, False),
    ('component_name', str, True, False),
)

shared.OnlineResource.type_info = (
    ('protocol', str, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
    ('linkage', str, True, False),
)

activity.UberEnsemble.type_info = (
    ('child_ensembles', activity.Ensemble, True, True),
)

activity.AxisMember.type_info = (
    ('value', float, False, False),
    ('description', str, True, False),
    ('index', int, True, False),
)

shared.KeyFloat.type_info = (
    ('key', str, True, False),
    ('value', float, True, False),
)

shared.IrregularDateset.type_info = (
    ('date_set', str, True, False),
)

software.ComponentBase.type_info = (
    ('version', str, False, False),
    ('development_history', software.DevelopmentPath, False, False),
    ('release_date', datetime.datetime, False, False),
    ('documentation', shared.Citation, False, True),
    ('tuning_applied', science.Tuning, False, False),
    ('description', shared.Cimtext, False, False),
    ('long_name', str, False, False),
    ('name', str, True, False),
)

software.Model.type_info = (
    ('internal_software_components', software.SoftwareComponent, False, True),
    ('scientific_domain', science.ScientificDomain, False, True),
    ('category', str, True, False),
    ('extra_conservation_properties', science.ConservationProperties, False, False),
    ('coupler', str, False, False),
    ('coupled_software_components', software.Model, False, True),
    ('meta', shared.Meta, True, False),
)

shared.TimesliceList.type_info = (
    ('members', shared.NumberArray, True, False),
    ('units', str, True, False),
)

activity.NumericalExperiment.type_info = (
    ('requirements', activity.NumericalRequirement, False, True),
    ('related_experiments', activity.NumericalExperiment, False, True),
)

activity.Downscaling.type_info = (
    ('downscaled_from', activity.Simulation, True, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

platform.Partition.type_info = (
    ('when_used', shared.TimePeriod, False, False),
    ('name', str, True, False),
    ('vendor', shared.Party, False, False),
    ('storage_pools', platform.StoragePool, False, True),
    ('online_documentation', shared.OnlineResource, False, True),
    ('institution', shared.Party, True, False),
    ('description', shared.Cimtext, False, False),
    ('compute_pools', platform.ComputePool, True, True),
    ('model_number', str, False, False),
    ('partition', platform.Partition, False, True),
)

activity.EnsembleRequirement.type_info = (
    ('ensemble_member', activity.NumericalRequirement, False, True),
    ('minimum_size', int, True, False),
    ('ensemble_type', str, True, False),
)

data.VariableCollection.type_info = (
    ('collection_name', str, False, False),
    ('variables', str, True, True),
)

platform.StoragePool.type_info = (
    ('description', shared.Cimtext, False, False),
    ('volume_available', platform.StorageVolume, True, False),
    ('vendor', shared.Party, False, False),
    ('name', str, True, False),
    ('type', str, False, False),
)

shared.TimePeriod.type_info = (
    ('units', str, True, False),
    ('date_type', str, True, False),
    ('length', int, True, False),
    ('calendar', shared.Calendar, False, False),
    ('date', shared.DateTime, False, False),
)

shared.NumberArray.type_info = (
    ('values', str, True, False),
)

shared.RegularTimeset.type_info = (
    ('increment', shared.TimePeriod, True, False),
    ('length', int, True, False),
    ('start_date', shared.DateTime, True, False),
)

shared.Cimtext.type_info = (
    ('content', str, True, False),
    ('content_type', str, True, False),
)

software.Gridspec.type_info = (
    ('description', str, True, False),
)

software.Variable.type_info = (
    ('description', str, False, False),
    ('prognostic', bool, True, False),
    ('name', str, True, False),
)

software.SoftwareComponent.type_info = (
    ('grid', software.Gridspec, False, False),
    ('license', str, False, False),
    ('composition', software.Composition, False, False),
    ('sub_components', software.SoftwareComponent, False, True),
    ('coupling_framework', str, False, False),
    ('language', str, False, False),
    ('connection_points', software.Variable, False, True),
    ('dependencies', software.EntryPoint, False, True),
)

data.RelatedData.type_info = (
    ('relationship', str, True, False),
    ('other_dataset', data.Dataset, True, False),
)

shared.Responsibility.type_info = (
    ('when', shared.TimePeriod, False, False),
    ('party', shared.Party, True, True),
    ('role', str, True, False),
)

drs.DrsGeographicalIndicator.type_info = (
    ('spatial_domain', str, False, False),
    ('bounding_box', str, False, False),
    ('operator', str, False, False),
)

platform.StorageVolume.type_info = (
    ('units', str, True, False),
    ('volume', int, True, False),
)

drs.DrsEnsembleIdentifier.type_info = (
    ('realisation_number', int, True, False),
    ('initialisation_method_number', int, True, False),
    ('perturbation_number', int, True, False),
)

shared.DatetimeSet.type_info = (
    ('length', int, True, False),
)

platform.Machine.type_info = (
    ('meta', shared.Meta, True, False),
)

activity.ParentSimulation.type_info = (
    ('branch_time_in_child', shared.DateTime, False, False),
    ('parent', activity.Simulation, True, False),
    ('branch_time_in_parent', shared.DateTime, False, False),
)

activity.Conformance.type_info = (
    ('target_requirement', activity.NumericalRequirement, True, False),
)

science.Process.type_info = (
    ('algorithm_properties', science.Algorithm, False, True),
    ('name', str, True, False),
    ('time_step_in_process', float, False, False),
    ('detailed_properties', science.ProcessDetail, False, True),
    ('keywords', str, True, False),
    ('description', str, False, False),
    ('references', shared.Reference, False, True),
    ('implementation_overview', shared.Cimtext, True, False),
)

shared.VocabMember.type_info = (
    ('uri', str, False, False),
    ('vocab', shared.Citation, False, False),
    ('value', str, True, False),
)

