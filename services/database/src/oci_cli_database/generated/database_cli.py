# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('db.db_root_group.command_name', 'db'), cls=CommandGroupWithAlias, help=cli_util.override('db.db_root_group.help', """The API for the Database Service."""), short_help=cli_util.override('db.db_root_group.short_help', """Database Service API"""))
@cli_util.help_option_group
def db_root_group():
    pass


@click.command(cli_util.override('db.autonomous_data_warehouse_group.command_name', 'autonomous-data-warehouse'), cls=CommandGroupWithAlias, help="""**Deprecated.** See [AutonomousDatabase] for reference information about Autonomous Databases with the warehouse workload type.""")
@cli_util.help_option_group
def autonomous_data_warehouse_group():
    pass


@click.command(cli_util.override('db.backup_group.command_name', 'backup'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def backup_group():
    pass


@click.command(cli_util.override('db.autonomous_container_database_group.command_name', 'autonomous-container-database'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def autonomous_container_database_group():
    pass


@click.command(cli_util.override('db.patch_group.command_name', 'patch'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def patch_group():
    pass


@click.command(cli_util.override('db.exadata_infrastructure_group.command_name', 'exadata-infrastructure'), cls=CommandGroupWithAlias, help="""ExadataInfrastructure""")
@cli_util.help_option_group
def exadata_infrastructure_group():
    pass


@click.command(cli_util.override('db.database_group.command_name', 'database'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def database_group():
    pass


@click.command(cli_util.override('db.db_system_shape_group.command_name', 'db-system-shape'), cls=CommandGroupWithAlias, help="""The shape of the DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. For a description of shapes, see [DB System Launch Options]. To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_system_shape_group():
    pass


@click.command(cli_util.override('db.data_guard_association_group.command_name', 'data-guard-association'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def data_guard_association_group():
    pass


@click.command(cli_util.override('db.autonomous_database_backup_group.command_name', 'autonomous-database-backup'), cls=CommandGroupWithAlias, help="""An Autonomous Database backup.""")
@cli_util.help_option_group
def autonomous_database_backup_group():
    pass


@click.command(cli_util.override('db.db_home_group.command_name', 'db-home'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def db_home_group():
    pass


@click.command(cli_util.override('db.autonomous_exadata_infrastructure_shape_group.command_name', 'autonomous-exadata-infrastructure-shape'), cls=CommandGroupWithAlias, help="""The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def autonomous_exadata_infrastructure_shape_group():
    pass


@click.command(cli_util.override('db.gi_version_group.command_name', 'gi-version'), cls=CommandGroupWithAlias, help="""The Oracle Grid Infrastructure (GI) version.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def gi_version_group():
    pass


@click.command(cli_util.override('db.external_backup_job_group.command_name', 'external-backup-job'), cls=CommandGroupWithAlias, help="""Provides all the details that apply to an external backup job.""")
@cli_util.help_option_group
def external_backup_job_group():
    pass


@click.command(cli_util.override('db.autonomous_exadata_infrastructure_group.command_name', 'autonomous-exadata-infrastructure'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def autonomous_exadata_infrastructure_group():
    pass


@click.command(cli_util.override('db.autonomous_data_warehouse_backup_group.command_name', 'autonomous-data-warehouse-backup'), cls=CommandGroupWithAlias, help="""**Deprecated.** See [AutonomousDatabaseBackup Reference] for reference information about Autonomous Data Warehouse backups.""")
@cli_util.help_option_group
def autonomous_data_warehouse_backup_group():
    pass


@click.command(cli_util.override('db.backup_destination_group.command_name', 'backup-destination'), cls=CommandGroupWithAlias, help="""Backup destination details.""")
@cli_util.help_option_group
def backup_destination_group():
    pass


@click.command(cli_util.override('db.maintenance_run_group.command_name', 'maintenance-run'), cls=CommandGroupWithAlias, help="""Details of a Maintenance Run.""")
@cli_util.help_option_group
def maintenance_run_group():
    pass


@click.command(cli_util.override('db.db_system_group.command_name', 'db-system'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def db_system_group():
    pass


@click.command(cli_util.override('db.autonomous_database_group.command_name', 'autonomous-database'), cls=CommandGroupWithAlias, help="""An Oracle Autonomous Database.""")
@cli_util.help_option_group
def autonomous_database_group():
    pass


@click.command(cli_util.override('db.db_version_group.command_name', 'db-version'), cls=CommandGroupWithAlias, help="""The Oracle Database software version.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_version_group():
    pass


@click.command(cli_util.override('db.patch_history_entry_group.command_name', 'patch-history-entry'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def patch_history_entry_group():
    pass


@click.command(cli_util.override('db.vm_cluster_network_group.command_name', 'vm-cluster-network'), cls=CommandGroupWithAlias, help="""The VM cluster network.""")
@cli_util.help_option_group
def vm_cluster_network_group():
    pass


@click.command(cli_util.override('db.autonomous_db_preview_version_group.command_name', 'autonomous-db-preview-version'), cls=CommandGroupWithAlias, help="""The Autonomous Database preview version. Note that preview version software is only available for [serverless deployments].""")
@cli_util.help_option_group
def autonomous_db_preview_version_group():
    pass


@click.command(cli_util.override('db.vm_cluster_group.command_name', 'vm-cluster'), cls=CommandGroupWithAlias, help="""Details of the VM cluster.""")
@cli_util.help_option_group
def vm_cluster_group():
    pass


@click.command(cli_util.override('db.backup_destination_summary_group.command_name', 'backup-destination-summary'), cls=CommandGroupWithAlias, help="""Backup destination details, including the list of databases using the backup destination.""")
@cli_util.help_option_group
def backup_destination_summary_group():
    pass


@click.command(cli_util.override('db.db_node_group.command_name', 'db-node'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def db_node_group():
    pass


db_root_group.add_command(autonomous_data_warehouse_group)
db_root_group.add_command(backup_group)
db_root_group.add_command(autonomous_container_database_group)
db_root_group.add_command(patch_group)
db_root_group.add_command(exadata_infrastructure_group)
db_root_group.add_command(database_group)
db_root_group.add_command(db_system_shape_group)
db_root_group.add_command(data_guard_association_group)
db_root_group.add_command(autonomous_database_backup_group)
db_root_group.add_command(db_home_group)
db_root_group.add_command(autonomous_exadata_infrastructure_shape_group)
db_root_group.add_command(gi_version_group)
db_root_group.add_command(external_backup_job_group)
db_root_group.add_command(autonomous_exadata_infrastructure_group)
db_root_group.add_command(autonomous_data_warehouse_backup_group)
db_root_group.add_command(backup_destination_group)
db_root_group.add_command(maintenance_run_group)
db_root_group.add_command(db_system_group)
db_root_group.add_command(autonomous_database_group)
db_root_group.add_command(db_version_group)
db_root_group.add_command(patch_history_entry_group)
db_root_group.add_command(vm_cluster_network_group)
db_root_group.add_command(autonomous_db_preview_version_group)
db_root_group.add_command(vm_cluster_group)
db_root_group.add_command(backup_destination_summary_group)
db_root_group.add_command(db_node_group)


@exadata_infrastructure_group.command(name=cli_util.override('db.activate_exadata_infrastructure.command_name', 'activate'), help=u"""Activates the specified Exadata infrastructure.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--activation-file', required=True, help=u"""The activation zip file.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExadataInfrastructure'})
@cli_util.wrap_exceptions
def activate_exadata_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, activation_file):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['activationFile'] = activation_file

    client = cli_util.build_client('database', ctx)
    result = client.activate_exadata_infrastructure(
        exadata_infrastructure_id=exadata_infrastructure_id,
        activate_exadata_infrastructure_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_exadata_infrastructure') and callable(getattr(client, 'get_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_exadata_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.change_autonomous_container_database_compartment.command_name', 'change-compartment'), help=u"""Move the Autonomous Container Database and its dependent resources to the specified compartment. For more information about moving Autonomous Container Databases, see [Moving Database Resources to a Different Compartment].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--autonomous-container-database-id', required=True, help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_autonomous_container_database_compartment(ctx, from_json, compartment_id, autonomous_container_database_id, if_match):

    if isinstance(autonomous_container_database_id, six.string_types) and len(autonomous_container_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-container-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_autonomous_container_database_compartment(
        autonomous_container_database_id=autonomous_container_database_id,
        change_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.change_autonomous_database_compartment.command_name', 'change-compartment'), help=u"""Move the Autonomous Database and its dependent resources to the specified compartment. For more information about moving Autonomous Databases, see [Moving Database Resources to a Different Compartment].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_autonomous_database_compartment(ctx, from_json, compartment_id, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_autonomous_database_compartment(
        autonomous_database_id=autonomous_database_id,
        change_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.change_autonomous_exadata_infrastructure_compartment.command_name', 'change-compartment'), help=u"""Move the Autonomous Exadata Infrastructure and its dependent resources to the specified compartment. For more information about moving Autonomous Exadata Infrastructures, see [Moving Database Resources to a Different Compartment].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--autonomous-exadata-infrastructure-id', required=True, help=u"""The Autonomous Exadata Infrastructure  [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_autonomous_exadata_infrastructure_compartment(ctx, from_json, compartment_id, autonomous_exadata_infrastructure_id, if_match):

    if isinstance(autonomous_exadata_infrastructure_id, six.string_types) and len(autonomous_exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_autonomous_exadata_infrastructure_compartment(
        autonomous_exadata_infrastructure_id=autonomous_exadata_infrastructure_id,
        change_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.change_backup_destination_compartment.command_name', 'change-compartment'), help=u"""Move the backup destination and its dependent resources to the specified compartment. For more information about moving backup destinations, see [Moving Database Resources to a Different Compartment].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--backup-destination-id', required=True, help=u"""The [OCID] of the backup destination.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_backup_destination_compartment(ctx, from_json, compartment_id, backup_destination_id, if_match):

    if isinstance(backup_destination_id, six.string_types) and len(backup_destination_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-destination-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_backup_destination_compartment(
        backup_destination_id=backup_destination_id,
        change_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.change_db_system_compartment.command_name', 'change-compartment'), help=u"""Move the DB system and its dependent resources to the specified compartment. For more information about moving DB systems, see [Moving Database Resources to a Different Compartment].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_db_system_compartment(ctx, from_json, compartment_id, db_system_id, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_db_system_compartment(
        db_system_id=db_system_id,
        change_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.change_exadata_infrastructure_compartment.command_name', 'change-compartment'), help=u"""To move an Exadata infrastructure and its dependent resources to another compartment, use the [ChangeExadataInfrastructureCompartment] operation.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the resource to.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_exadata_infrastructure_compartment(ctx, from_json, compartment_id, exadata_infrastructure_id, if_match):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_exadata_infrastructure_compartment(
        exadata_infrastructure_id=exadata_infrastructure_id,
        change_exadata_infrastructure_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.change_vm_cluster_compartment.command_name', 'change-compartment'), help=u"""To move a VM cluster and its dependent resources to another compartment, use the [ChangeVmClusterCompartment] operation.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the VM cluster to.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The VM cluster [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vm_cluster_compartment(ctx, from_json, compartment_id, vm_cluster_id, if_match):

    if isinstance(vm_cluster_id, six.string_types) and len(vm_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('database', ctx)
    result = client.change_vm_cluster_compartment(
        vm_cluster_id=vm_cluster_id,
        change_vm_cluster_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@external_backup_job_group.command(name=cli_util.override('db.complete_external_backup_job.command_name', 'complete'), help=u"""Changes the status of the standalone backup resource to `ACTIVE` after the backup is created from the on-premises database and placed in Oracle Cloud Infrastructure Object Storage.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--backup-id', required=True, help=u"""The backup [OCID].""")
@cli_util.option('--tde-wallet-path', help=u"""If the database being backed up is TDE enabled, this will be the path to the associated TDE wallet in Object Storage.""")
@cli_util.option('--cf-backup-handle', help=u"""The handle of the control file backup.""")
@cli_util.option('--spf-backup-handle', help=u"""The handle of the spfile backup.""")
@cli_util.option('--sql-patches', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of SQL patches that need to be applied to the backup during the restore.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-size', type=click.INT, help=u"""The size of the data in the database, in megabytes.""")
@cli_util.option('--redo-size', type=click.INT, help=u"""The size of the redo in the database, in megabytes.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-patches': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-patches': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def complete_external_backup_job(ctx, from_json, backup_id, tde_wallet_path, cf_backup_handle, spf_backup_handle, sql_patches, data_size, redo_size, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if tde_wallet_path is not None:
        details['tdeWalletPath'] = tde_wallet_path

    if cf_backup_handle is not None:
        details['cfBackupHandle'] = cf_backup_handle

    if spf_backup_handle is not None:
        details['spfBackupHandle'] = spf_backup_handle

    if sql_patches is not None:
        details['sqlPatches'] = cli_util.parse_json_parameter("sql_patches", sql_patches)

    if data_size is not None:
        details['dataSize'] = data_size

    if redo_size is not None:
        details['redoSize'] = redo_size

    client = cli_util.build_client('database', ctx)
    result = client.complete_external_backup_job(
        backup_id=backup_id,
        complete_external_backup_job_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.create_autonomous_container_database.command_name', 'create'), help=u"""Create a new Autonomous Container Database in the specified Autonomous Exadata Infrastructure.""")
@cli_util.option('--display-name', required=True, help=u"""The display name for the Autonomous Container Database.""")
@cli_util.option('--autonomous-exadata-infrastructure-id', required=True, help=u"""The OCID of the Autonomous Exadata Infrastructure.""")
@cli_util.option('--patch-model', required=True, type=custom_types.CliCaseInsensitiveChoice(["RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"]), help=u"""Database Patch model preference.""")
@cli_util.option('--service-level-agreement-type', type=custom_types.CliCaseInsensitiveChoice(["STANDARD"]), help=u"""The service level agreement type of the Autonomous Container Database. The default is STANDARD. For a Mission Critical Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment containing the Autonomous Container Database.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'backup-config': {'module': 'database', 'class': 'AutonomousContainerDatabaseBackupConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'backup-config': {'module': 'database', 'class': 'AutonomousContainerDatabaseBackupConfig'}}, output_type={'module': 'database', 'class': 'AutonomousContainerDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_container_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, autonomous_exadata_infrastructure_id, patch_model, service_level_agreement_type, compartment_id, freeform_tags, defined_tags, backup_config):

    kwargs = {}

    details = {}
    details['displayName'] = display_name
    details['autonomousExadataInfrastructureId'] = autonomous_exadata_infrastructure_id
    details['patchModel'] = patch_model

    if service_level_agreement_type is not None:
        details['serviceLevelAgreementType'] = service_level_agreement_type

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if backup_config is not None:
        details['backupConfig'] = cli_util.parse_json_parameter("backup_config", backup_config)

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_container_database(
        create_autonomous_container_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_container_database') and callable(getattr(client, 'get_autonomous_container_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_container_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.create_autonomous_data_warehouse.command_name', 'create'), help=u"""**Deprecated.** To create a new Autonomous Data Warehouse, use the [CreateAutonomousDatabase] operation and specify `DW` as the workload type.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment of the Autonomous Data Warehouse.""")
@cli_util.option('--db-name', required=True, help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help=u"""Size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--admin-password', required=True, help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def create_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, db_name, cpu_core_count, data_storage_size_in_tbs, admin_password, display_name, license_model, freeform_tags, defined_tags):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['dbName'] = db_name
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['adminPassword'] = admin_password

    if display_name is not None:
        details['displayName'] = display_name

    if license_model is not None:
        details['licenseModel'] = license_model

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_data_warehouse(
        create_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('db.create_autonomous_data_warehouse_backup.command_name', 'create'), help=u"""**Deprecated.** To create a new Autonomous Data Warehouse backup for a specified database, use the [CreateAutonomousDatabaseBackup] operation.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The [OCID] of the Autonomous Data Warehouse backup.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouseBackup'})
@cli_util.wrap_exceptions
def create_autonomous_data_warehouse_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, autonomous_data_warehouse_id):

    kwargs = {}

    details = {}
    details['displayName'] = display_name
    details['autonomousDataWarehouseId'] = autonomous_data_warehouse_id

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_data_warehouse_backup(
        create_autonomous_data_warehouse_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse_backup') and callable(getattr(client, 'get_autonomous_data_warehouse_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.create_autonomous_database.command_name', 'create'), help=u"""Creates a new Autonomous Database.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment of the autonomous database.""")
@cli_util.option('--db-name', required=True, help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help=u"""The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--admin-password', required=True, help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.""")
@cli_util.option('--db-workload', type=custom_types.CliCaseInsensitiveChoice(["OLTP", "DW"]), help=u"""The autonomous database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse. The default is OLTP.""")
@cli_util.option('--is-free-tier', type=click.BOOL, help=u"""Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB memory. For Always Free databases, memory and CPU cannot be scaled.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the Oracle Autonomous Database. The default for Autonomous Database using the [shared deployment] is BRING_YOUR_OWN_LICENSE. Note that when provisioning an Autonomous Database using the [dedicated deployment] option, this attribute must be null because the attribute is already set on Autonomous Exadata Infrastructure level.""")
@cli_util.option('--is-preview-version-with-service-terms-accepted', type=click.BOOL, help=u"""If set to true, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for [serverless deployments].""")
@cli_util.option('--is-auto-scaling-enabled', type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for [serverless deployments] only.""")
@cli_util.option('--is-dedicated', type=click.BOOL, help=u"""True if the database uses the [dedicated deployment] option.""")
@cli_util.option('--autonomous-container-database-id', help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DATABASE"]), help=u"""The source of the database: Use NONE for creating a new Autonomous Database. Use DATABASE for creating a new Autonomous Database by cloning an existing Autonomous Database.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, db_name, cpu_core_count, data_storage_size_in_tbs, admin_password, db_workload, is_free_tier, display_name, license_model, is_preview_version_with_service_terms_accepted, is_auto_scaling_enabled, is_dedicated, autonomous_container_database_id, freeform_tags, defined_tags, source):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['dbName'] = db_name
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['adminPassword'] = admin_password

    if db_workload is not None:
        details['dbWorkload'] = db_workload

    if is_free_tier is not None:
        details['isFreeTier'] = is_free_tier

    if display_name is not None:
        details['displayName'] = display_name

    if license_model is not None:
        details['licenseModel'] = license_model

    if is_preview_version_with_service_terms_accepted is not None:
        details['isPreviewVersionWithServiceTermsAccepted'] = is_preview_version_with_service_terms_accepted

    if is_auto_scaling_enabled is not None:
        details['isAutoScalingEnabled'] = is_auto_scaling_enabled

    if is_dedicated is not None:
        details['isDedicated'] = is_dedicated

    if autonomous_container_database_id is not None:
        details['autonomousContainerDatabaseId'] = autonomous_container_database_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database(
        create_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.create_autonomous_database_create_autonomous_database_clone_details.command_name', 'create-autonomous-database-create-autonomous-database-clone-details'), help=u"""Creates a new Autonomous Database.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment of the autonomous database.""")
@cli_util.option('--db-name', required=True, help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help=u"""The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--admin-password', required=True, help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.""")
@cli_util.option('--source-id', required=True, help=u"""The [OCID] of the source Autonomous Database that you will clone to create a new Autonomous Database.""")
@cli_util.option('--clone-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FULL", "METADATA"]), help=u"""The Autonomous Database clone type.""")
@cli_util.option('--db-workload', type=custom_types.CliCaseInsensitiveChoice(["OLTP", "DW"]), help=u"""The autonomous database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse. The default is OLTP.""")
@cli_util.option('--is-free-tier', type=click.BOOL, help=u"""Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB memory. For Always Free databases, memory and CPU cannot be scaled.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the Oracle Autonomous Database. The default for Autonomous Database using the [shared deployment] is BRING_YOUR_OWN_LICENSE. Note that when provisioning an Autonomous Database using the [dedicated deployment] option, this attribute must be null because the attribute is already set on Autonomous Exadata Infrastructure level.""")
@cli_util.option('--is-preview-version-with-service-terms-accepted', type=click.BOOL, help=u"""If set to true, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for [serverless deployments].""")
@cli_util.option('--is-auto-scaling-enabled', type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for [serverless deployments] only.""")
@cli_util.option('--is-dedicated', type=click.BOOL, help=u"""True if the database uses the [dedicated deployment] option.""")
@cli_util.option('--autonomous-container-database-id', help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_clone_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, db_name, cpu_core_count, data_storage_size_in_tbs, admin_password, source_id, clone_type, db_workload, is_free_tier, display_name, license_model, is_preview_version_with_service_terms_accepted, is_auto_scaling_enabled, is_dedicated, autonomous_container_database_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['dbName'] = db_name
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['adminPassword'] = admin_password
    details['sourceId'] = source_id
    details['cloneType'] = clone_type

    if db_workload is not None:
        details['dbWorkload'] = db_workload

    if is_free_tier is not None:
        details['isFreeTier'] = is_free_tier

    if display_name is not None:
        details['displayName'] = display_name

    if license_model is not None:
        details['licenseModel'] = license_model

    if is_preview_version_with_service_terms_accepted is not None:
        details['isPreviewVersionWithServiceTermsAccepted'] = is_preview_version_with_service_terms_accepted

    if is_auto_scaling_enabled is not None:
        details['isAutoScalingEnabled'] = is_auto_scaling_enabled

    if is_dedicated is not None:
        details['isDedicated'] = is_dedicated

    if autonomous_container_database_id is not None:
        details['autonomousContainerDatabaseId'] = autonomous_container_database_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    details['source'] = 'DATABASE'

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database(
        create_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.create_autonomous_database_create_autonomous_database_details.command_name', 'create-autonomous-database-create-autonomous-database-details'), help=u"""Creates a new Autonomous Database.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment of the autonomous database.""")
@cli_util.option('--db-name', required=True, help=u"""The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU Cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', required=True, type=click.INT, help=u"""The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.""")
@cli_util.option('--admin-password', required=True, help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.""")
@cli_util.option('--db-workload', type=custom_types.CliCaseInsensitiveChoice(["OLTP", "DW"]), help=u"""The autonomous database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse. The default is OLTP.""")
@cli_util.option('--is-free-tier', type=click.BOOL, help=u"""Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB memory. For Always Free databases, memory and CPU cannot be scaled.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the Oracle Autonomous Database. The default for Autonomous Database using the [shared deployment] is BRING_YOUR_OWN_LICENSE. Note that when provisioning an Autonomous Database using the [dedicated deployment] option, this attribute must be null because the attribute is already set on Autonomous Exadata Infrastructure level.""")
@cli_util.option('--is-preview-version-with-service-terms-accepted', type=click.BOOL, help=u"""If set to true, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for [serverless deployments].""")
@cli_util.option('--is-auto-scaling-enabled', type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for [serverless deployments] only.""")
@cli_util.option('--is-dedicated', type=click.BOOL, help=u"""True if the database uses the [dedicated deployment] option.""")
@cli_util.option('--autonomous-container-database-id', help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def create_autonomous_database_create_autonomous_database_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, db_name, cpu_core_count, data_storage_size_in_tbs, admin_password, db_workload, is_free_tier, display_name, license_model, is_preview_version_with_service_terms_accepted, is_auto_scaling_enabled, is_dedicated, autonomous_container_database_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['dbName'] = db_name
    details['cpuCoreCount'] = cpu_core_count
    details['dataStorageSizeInTBs'] = data_storage_size_in_tbs
    details['adminPassword'] = admin_password

    if db_workload is not None:
        details['dbWorkload'] = db_workload

    if is_free_tier is not None:
        details['isFreeTier'] = is_free_tier

    if display_name is not None:
        details['displayName'] = display_name

    if license_model is not None:
        details['licenseModel'] = license_model

    if is_preview_version_with_service_terms_accepted is not None:
        details['isPreviewVersionWithServiceTermsAccepted'] = is_preview_version_with_service_terms_accepted

    if is_auto_scaling_enabled is not None:
        details['isAutoScalingEnabled'] = is_auto_scaling_enabled

    if is_dedicated is not None:
        details['isDedicated'] = is_dedicated

    if autonomous_container_database_id is not None:
        details['autonomousContainerDatabaseId'] = autonomous_container_database_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    details['source'] = 'NONE'

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database(
        create_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('db.create_autonomous_database_backup.command_name', 'create'), help=u"""Creates a new Autonomous Database backup for the specified database based on the provided request parameters.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The [OCID] of the Autonomous Database backup.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabaseBackup'})
@cli_util.wrap_exceptions
def create_autonomous_database_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, autonomous_database_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['autonomousDatabaseId'] = autonomous_database_id

    client = cli_util.build_client('database', ctx)
    result = client.create_autonomous_database_backup(
        create_autonomous_database_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database_backup') and callable(getattr(client, 'get_autonomous_database_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db.create_backup.command_name', 'create'), help=u"""Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@cli_util.option('--database-id', required=True, help=u"""The [OCID] of the database.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the backup. The name does not have to be unique.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Backup'})
@cli_util.wrap_exceptions
def create_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, display_name):

    kwargs = {}

    details = {}
    details['databaseId'] = database_id
    details['displayName'] = display_name

    client = cli_util.build_client('database', ctx)
    result = client.create_backup(
        create_backup_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup') and callable(getattr(client, 'get_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.create_backup_destination.command_name', 'create'), help=u"""Creates a backup destination.""")
@cli_util.option('--display-name', required=True, help=u"""The user-provided name of the backup destination.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["NFS", "RECOVERY_APPLIANCE"]), help=u"""Type of the backup destination.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'BackupDestination'})
@cli_util.wrap_exceptions
def create_backup_destination(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, type, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['compartmentId'] = compartment_id
    details['type'] = type

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.create_backup_destination(
        create_backup_destination_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup_destination') and callable(getattr(client, 'get_backup_destination')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup_destination(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.create_backup_destination_create_nfs_backup_destination_details.command_name', 'create-backup-destination-create-nfs-backup-destination-details'), help=u"""Creates a backup destination.""")
@cli_util.option('--display-name', required=True, help=u"""The user-provided name of the backup destination.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--local-mount-point-path', required=True, help=u"""The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'BackupDestination'})
@cli_util.wrap_exceptions
def create_backup_destination_create_nfs_backup_destination_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, local_mount_point_path, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['compartmentId'] = compartment_id
    details['localMountPointPath'] = local_mount_point_path

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    details['type'] = 'NFS'

    client = cli_util.build_client('database', ctx)
    result = client.create_backup_destination(
        create_backup_destination_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup_destination') and callable(getattr(client, 'get_backup_destination')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup_destination(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.create_backup_destination_create_recovery_appliance_backup_destination_details.command_name', 'create-backup-destination-create-recovery-appliance-backup-destination-details'), help=u"""Creates a backup destination.""")
@cli_util.option('--display-name', required=True, help=u"""The user-provided name of the backup destination.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--connection-string', required=True, help=u"""The connection string for connecting to the Recovery Appliance.""")
@cli_util.option('--vpc-users', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'vpc-users': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'vpc-users': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'BackupDestination'})
@cli_util.wrap_exceptions
def create_backup_destination_create_recovery_appliance_backup_destination_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, connection_string, vpc_users, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['compartmentId'] = compartment_id
    details['connectionString'] = connection_string
    details['vpcUsers'] = cli_util.parse_json_parameter("vpc_users", vpc_users)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    details['type'] = 'RECOVERY_APPLIANCE'

    client = cli_util.build_client('database', ctx)
    result = client.create_backup_destination(
        create_backup_destination_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup_destination') and callable(getattr(client, 'get_backup_destination')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup_destination(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.create_data_guard_association.command_name', 'create'), help=u"""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.**""")
@cli_util.option('--protection-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help=u"""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.""")
@cli_util.option('--transport-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help=u"""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.""")
@cli_util.option('--creation-type', required=True, help=u"""Specifies whether to create the peer database in an existing DB system or in a new DB system. `ExistingDbSystem` is not supported for creating Data Guard associations for virtual machine DB system databases.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_admin_password, protection_mode, transport_type, creation_type):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type
    details['creationType'] = creation_type

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.create_data_guard_association_create_data_guard_association_with_new_db_system_details.command_name', 'create-data-guard-association-create-data-guard-association-with-new-db-system-details'), help=u"""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.**""")
@cli_util.option('--protection-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help=u"""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.""")
@cli_util.option('--transport-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help=u"""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.""")
@cli_util.option('--display-name', help=u"""The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.""")
@cli_util.option('--availability-domain', help=u"""The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".""")
@cli_util.option('--subnet-id', help=u"""The OCID of the subnet the DB system is associated with. **Subnet Restrictions:** - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-network-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules]. Applicable only to Exadata DB systems.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname', help=u"""The hostname for the DB node.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_create_data_guard_association_with_new_db_system_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_admin_password, protection_mode, transport_type, display_name, availability_domain, subnet_id, nsg_ids, backup_network_nsg_ids, hostname):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    if display_name is not None:
        details['displayName'] = display_name

    if availability_domain is not None:
        details['availabilityDomain'] = availability_domain

    if subnet_id is not None:
        details['subnetId'] = subnet_id

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if backup_network_nsg_ids is not None:
        details['backupNetworkNsgIds'] = cli_util.parse_json_parameter("backup_network_nsg_ids", backup_network_nsg_ids)

    if hostname is not None:
        details['hostname'] = hostname

    details['creationType'] = 'NewDbSystem'

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.create_data_guard_association_create_data_guard_association_to_existing_db_system_details.command_name', 'create-data-guard-association-create-data-guard-association-to-existing-db-system-details'), help=u"""Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the specified database and a peer database. For more information, see [Using Oracle Data Guard].

All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

The password must contain no fewer than nine characters and include:

* At least two uppercase characters.

* At least two lowercase characters.

* At least two numeric characters.

* At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

**The password MUST be the same as the primary admin password.**""")
@cli_util.option('--protection-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]), help=u"""The protection mode to set up between the primary and standby databases. For more information, see [Oracle Data Guard Protection Modes] in the Oracle Data Guard documentation.

**IMPORTANT** - The only protection mode currently supported by the Database service is MAXIMUM_PERFORMANCE.""")
@cli_util.option('--transport-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SYNC", "ASYNC", "FASTSYNC"]), help=u"""The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

* MAXIMUM_AVAILABILITY - SYNC or FASTSYNC * MAXIMUM_PERFORMANCE - ASYNC * MAXIMUM_PROTECTION - SYNC

For more information, see [Redo Transport Services] in the Oracle Data Guard documentation.

**IMPORTANT** - The only transport type currently supported by the Database service is ASYNC.""")
@cli_util.option('--peer-db-system-id', help=u"""The [OCID] of the DB system in which to create the standby database. You must supply this value if creationType is `ExistingDbSystem`.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def create_data_guard_association_create_data_guard_association_to_existing_db_system_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_admin_password, protection_mode, transport_type, peer_db_system_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['databaseAdminPassword'] = database_admin_password
    details['protectionMode'] = protection_mode
    details['transportType'] = transport_type

    if peer_db_system_id is not None:
        details['peerDbSystemId'] = peer_db_system_id

    details['creationType'] = 'ExistingDbSystem'

    client = cli_util.build_client('database', ctx)
    result = client.create_data_guard_association(
        database_id=database_id,
        create_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.create_db_home.command_name', 'create'), help=u"""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--display-name', help=u"""The user-provided name of the database home.""")
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DB_BACKUP", "VM_CLUSTER_NEW", "VM_CLUSTER_BACKUP"]), help=u"""The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, source):

    kwargs = {}

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.create_db_home_create_db_home_with_db_system_id_from_backup_details.command_name', 'create-db-home-create-db-home-with-db-system-id-from-backup-details'), help=u"""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--db-system-id', required=True, help=u"""The [OCID] of the DB system.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_db_system_id_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, database, display_name):

    kwargs = {}

    details = {}
    details['dbSystemId'] = db_system_id
    details['database'] = cli_util.parse_json_parameter("database", database)

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'DB_BACKUP'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.create_db_home_create_db_home_with_vm_cluster_id_from_backup_details.command_name', 'create-db-home-create-db-home-with-vm-cluster-id-from-backup-details'), help=u"""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The [OCID] of the VM cluster.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseFromBackupDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_vm_cluster_id_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vm_cluster_id, database, display_name):

    kwargs = {}

    details = {}
    details['vmClusterId'] = vm_cluster_id
    details['database'] = cli_util.parse_json_parameter("database", database)

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'VM_CLUSTER_BACKUP'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.create_db_home_create_db_home_with_db_system_id_details.command_name', 'create-db-home-create-db-home-with-db-system-id-details'), help=u"""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--db-system-id', required=True, help=u"""The [OCID] of the DB system.""")
@cli_util.option('--db-version', required=True, help=u"""A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions] operation.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_db_system_id_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, db_version, database, display_name):

    kwargs = {}

    details = {}
    details['dbSystemId'] = db_system_id
    details['dbVersion'] = db_version
    details['database'] = cli_util.parse_json_parameter("database", database)

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'NONE'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.create_db_home_create_db_home_with_vm_cluster_id_details.command_name', 'create-db-home-create-db-home-with-vm-cluster-id-details'), help=u"""Creates a new database home in the specified DB system based on the request parameters you provide.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The [OCID] of the VM cluster.""")
@cli_util.option('--db-version', required=True, help=u"""A valid Oracle Database version. To get a list of supported versions, use the [ListDbVersions] operation.""")
@cli_util.option('--database', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-provided name of the database home.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database': {'module': 'database', 'class': 'CreateDatabaseDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def create_db_home_create_db_home_with_vm_cluster_id_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vm_cluster_id, db_version, database, display_name):

    kwargs = {}

    details = {}
    details['vmClusterId'] = vm_cluster_id
    details['dbVersion'] = db_version
    details['database'] = cli_util.parse_json_parameter("database", database)

    if display_name is not None:
        details['displayName'] = display_name

    details['source'] = 'VM_CLUSTER_NEW'

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.create_exadata_infrastructure.command_name', 'create'), help=u"""Create Exadata infrastructure.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the Exadata infrastructure. The name does not need to be unique.""")
@cli_util.option('--shape', required=True, help=u"""The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.""")
@cli_util.option('--time-zone', required=True, help=u"""The time zone of the Exadata infrastructure. For details, see [Exadata Infrastructure Time Zones].""")
@cli_util.option('--cloud-control-plane-server1', required=True, help=u"""The IP address for the first control plane server.""")
@cli_util.option('--cloud-control-plane-server2', required=True, help=u"""The IP address for the second control plane server.""")
@cli_util.option('--netmask', required=True, help=u"""The netmask for the control plane network.""")
@cli_util.option('--gateway', required=True, help=u"""The gateway for the control plane network.""")
@cli_util.option('--admin-network-cidr', required=True, help=u"""The CIDR block for the Exadata administration network.""")
@cli_util.option('--infini-band-network-cidr', required=True, help=u"""The CIDR block for the Exadata InfiniBand interconnect.""")
@cli_util.option('--corporate-proxy', required=True, help=u"""The corporate network proxy for access to the control plane network.""")
@cli_util.option('--dns-server', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ntp-server', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NTP server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-server': {'module': 'database', 'class': 'list[string]'}, 'ntp-server': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-server': {'module': 'database', 'class': 'list[string]'}, 'ntp-server': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExadataInfrastructure'})
@cli_util.wrap_exceptions
def create_exadata_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, shape, time_zone, cloud_control_plane_server1, cloud_control_plane_server2, netmask, gateway, admin_network_cidr, infini_band_network_cidr, corporate_proxy, dns_server, ntp_server, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['shape'] = shape
    details['timeZone'] = time_zone
    details['cloudControlPlaneServer1'] = cloud_control_plane_server1
    details['cloudControlPlaneServer2'] = cloud_control_plane_server2
    details['netmask'] = netmask
    details['gateway'] = gateway
    details['adminNetworkCIDR'] = admin_network_cidr
    details['infiniBandNetworkCIDR'] = infini_band_network_cidr
    details['corporateProxy'] = corporate_proxy
    details['dnsServer'] = cli_util.parse_json_parameter("dns_server", dns_server)
    details['ntpServer'] = cli_util.parse_json_parameter("ntp_server", ntp_server)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.create_exadata_infrastructure(
        create_exadata_infrastructure_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_exadata_infrastructure') and callable(getattr(client, 'get_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_exadata_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@external_backup_job_group.command(name=cli_util.override('db.create_external_backup_job.command_name', 'create'), help=u"""Creates a new backup resource and returns the information the caller needs to back up an on-premises Oracle Database to Oracle Cloud Infrastructure.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--availability-domain', required=True, help=u"""The targeted availability domain for the backup.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where this backup should be created.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the backup. This name does not have to be unique.""")
@cli_util.option('--db-version', required=True, help=u"""A valid Oracle Database version.""")
@cli_util.option('--db-name', required=True, help=u"""The name of the database from which the backup is being taken.""")
@cli_util.option('--external-database-identifier', required=True, type=click.INT, help=u"""The `DBID` of the Oracle Database being backed up.""")
@cli_util.option('--character-set', required=True, help=u"""The character set for the database.""")
@cli_util.option('--ncharacter-set', required=True, help=u"""The national character set for the database.""")
@cli_util.option('--database-mode', required=True, type=custom_types.CliCaseInsensitiveChoice(["SI", "RAC"]), help=u"""The mode (single instance or RAC) of the database being backed up.""")
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help=u"""The Oracle Database edition to use for creating a database from this standalone backup. Note that 2-node RAC DB systems require Enterprise Edition - Extreme Performance.""")
@cli_util.option('--db-unique-name', help=u"""The `DB_UNIQUE_NAME` of the Oracle Database being backed up.""")
@cli_util.option('--pdb-name', help=u"""The pluggable database name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def create_external_backup_job(ctx, from_json, availability_domain, compartment_id, display_name, db_version, db_name, external_database_identifier, character_set, ncharacter_set, database_mode, database_edition, db_unique_name, pdb_name):

    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['dbVersion'] = db_version
    details['dbName'] = db_name
    details['externalDatabaseIdentifier'] = external_database_identifier
    details['characterSet'] = character_set
    details['ncharacterSet'] = ncharacter_set
    details['databaseMode'] = database_mode
    details['databaseEdition'] = database_edition

    if db_unique_name is not None:
        details['dbUniqueName'] = db_unique_name

    if pdb_name is not None:
        details['pdbName'] = pdb_name

    client = cli_util.build_client('database', ctx)
    result = client.create_external_backup_job(
        create_external_backup_job_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.create_vm_cluster.command_name', 'create'), help=u"""Creates a VM cluster.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the VM cluster. The name does not need to be unique.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The [OCID] of the Exadata infrastructure.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU cores to enable for the VM cluster.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of one or more key pairs used for SSH access to the VM cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The [OCID] of the VM cluster network.""")
@cli_util.option('--gi-version', required=True, help=u"""The Oracle Grid Infrastructure software version for the VM cluster.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--is-sparse-diskgroup-enabled', type=click.BOOL, help=u"""If true, the sparse disk group is configured for the VM cluster. If false, the sparse disk group is not created.""")
@cli_util.option('--is-local-backup-enabled', type=click.BOOL, help=u"""If true, database backup on local Exadata storage is configured for the VM cluster. If false, database backup on local Exadata storage is not available in the VM cluster.""")
@cli_util.option('--time-zone', help=u"""The time zone to use for the VM cluster. For details, see [DB System Time Zones].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'VmCluster'})
@cli_util.wrap_exceptions
def create_vm_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, exadata_infrastructure_id, cpu_core_count, ssh_public_keys, vm_cluster_network_id, gi_version, license_model, is_sparse_diskgroup_enabled, is_local_backup_enabled, time_zone, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['exadataInfrastructureId'] = exadata_infrastructure_id
    details['cpuCoreCount'] = cpu_core_count
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['vmClusterNetworkId'] = vm_cluster_network_id
    details['giVersion'] = gi_version

    if license_model is not None:
        details['licenseModel'] = license_model

    if is_sparse_diskgroup_enabled is not None:
        details['isSparseDiskgroupEnabled'] = is_sparse_diskgroup_enabled

    if is_local_backup_enabled is not None:
        details['isLocalBackupEnabled'] = is_local_backup_enabled

    if time_zone is not None:
        details['timeZone'] = time_zone

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.create_vm_cluster(
        create_vm_cluster_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster') and callable(getattr(client, 'get_vm_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vm_cluster(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.create_vm_cluster_network.command_name', 'create'), help=u"""Creates the VM cluster network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the VM cluster network. The name does not need to be unique.""")
@cli_util.option('--scans', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The SCAN details.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm-networks', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details of the client and backup networks.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ntp', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NTP server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'scans': {'module': 'database', 'class': 'list[ScanDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'vm-networks': {'module': 'database', 'class': 'list[VmNetworkDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scans': {'module': 'database', 'class': 'list[ScanDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'vm-networks': {'module': 'database', 'class': 'list[VmNetworkDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'VmClusterNetwork'})
@cli_util.wrap_exceptions
def create_vm_cluster_network(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, compartment_id, display_name, scans, vm_networks, dns, ntp, freeform_tags, defined_tags):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['scans'] = cli_util.parse_json_parameter("scans", scans)
    details['vmNetworks'] = cli_util.parse_json_parameter("vm_networks", vm_networks)

    if dns is not None:
        details['dns'] = cli_util.parse_json_parameter("dns", dns)

    if ntp is not None:
        details['ntp'] = cli_util.parse_json_parameter("ntp", ntp)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.create_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster_network') and callable(getattr(client, 'get_vm_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vm_cluster_network(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('db.db_node_action.command_name', 'db-node-action'), help=u"""Performs one of the following power actions on the specified DB node: - start - power on - stop - power off - softreset - ACPI shutdown and power on - reset - power off and power on

**Note:** Stopping a node affects billing differently, depending on the type of DB system: *Bare metal and Exadata DB systems* - The _stop_ state has no effect on the resources you consume. Billing continues for DB nodes that you stop, and related resources continue to apply against any relevant quotas. You must terminate the DB system ([TerminateDbSystem]) to remove its resources from billing and quotas. *Virtual machine DB systems* - Stopping a node stops billing for all OCPUs associated with that node, and billing resumes when you restart the node.""")
@cli_util.option('--db-node-id', required=True, help=u"""The database node [OCID].""")
@cli_util.option('--action', required=True, help=u"""The action to perform on the DB Node. Allowed values are: STOP, START, SOFTRESET, RESET""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def db_node_action(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_node_id, action, if_match):

    if isinstance(db_node_id, six.string_types) and len(db_node_id.strip()) == 0:
        raise click.UsageError('Parameter --db-node-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.db_node_action(
        db_node_id=db_node_id,
        action=action,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_node') and callable(getattr(client, 'get_db_node')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_node(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.delete_autonomous_data_warehouse.command_name', 'delete'), help=u"""**Deprecated.** To delete an Autonomous Data Warehouse, use the [DeleteAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.delete_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_data_warehouse(autonomous_data_warehouse_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.delete_autonomous_database.command_name', 'delete'), help=u"""Deletes the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_database(autonomous_database_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db.delete_backup.command_name', 'delete'), help=u"""Deletes a full backup. You cannot delete automatic backups using this API.""")
@cli_util.option('--backup-id', required=True, help=u"""The backup [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "RESTORING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backup_id, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.delete_backup(
        backup_id=backup_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup') and callable(getattr(client, 'get_backup')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_backup(backup_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.delete_backup_destination.command_name', 'delete'), help=u"""Deletes a backup destination.""")
@cli_util.option('--backup-destination-id', required=True, help=u"""The [OCID] of the backup destination.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backup_destination(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backup_destination_id, if_match):

    if isinstance(backup_destination_id, six.string_types) and len(backup_destination_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-destination-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_backup_destination(
        backup_destination_id=backup_destination_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup_destination') and callable(getattr(client, 'get_backup_destination')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_backup_destination(backup_destination_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.delete_db_home.command_name', 'delete'), help=u"""Deletes a DB Home. The DB Home and its database data are local to the DB system and will be lost when it is deleted. Oracle recommends that you back up any data in the DB system prior to deleting it.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--perform-final-backup', type=click.BOOL, help=u"""Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_home(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_home_id, if_match, perform_final_backup):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if perform_final_backup is not None:
        kwargs['perform_final_backup'] = perform_final_backup
    client = cli_util.build_client('database', ctx)
    result = client.delete_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_db_home(db_home_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.delete_exadata_infrastructure.command_name', 'delete'), help=u"""Deletes the Exadata infrastructure.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_exadata_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, if_match):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_exadata_infrastructure(
        exadata_infrastructure_id=exadata_infrastructure_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_exadata_infrastructure') and callable(getattr(client, 'get_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_exadata_infrastructure(exadata_infrastructure_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.delete_vm_cluster.command_name', 'delete'), help=u"""Deletes the specified VM cluster.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The VM cluster [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vm_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vm_cluster_id, if_match):

    if isinstance(vm_cluster_id, six.string_types) and len(vm_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_vm_cluster(
        vm_cluster_id=vm_cluster_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster') and callable(getattr(client, 'get_vm_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_vm_cluster(vm_cluster_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.delete_vm_cluster_network.command_name', 'delete'), help=u"""Deletes the specified VM cluster network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The VM cluster network [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vm_cluster_network(ctx, from_json, exadata_infrastructure_id, vm_cluster_network_id, if_match):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    if isinstance(vm_cluster_network_id, six.string_types) and len(vm_cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.delete_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_id=vm_cluster_network_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.download_exadata_infrastructure_config_file.command_name', 'download-exadata-infrastructure-config-file'), help=u"""Downloads the configuration file for the specified Exadata infrastructure.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def download_exadata_infrastructure_config_file(ctx, from_json, file, exadata_infrastructure_id):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.download_exadata_infrastructure_config_file(
        exadata_infrastructure_id=exadata_infrastructure_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@vm_cluster_network_group.command(name=cli_util.override('db.download_vm_cluster_network_config_file.command_name', 'download-vm-cluster-network-config-file'), help=u"""Downloads the configuration file for the specified VM Cluster Network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The VM cluster network [OCID].""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def download_vm_cluster_network_config_file(ctx, from_json, file, exadata_infrastructure_id, vm_cluster_network_id):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    if isinstance(vm_cluster_network_id, six.string_types) and len(vm_cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.download_vm_cluster_network_config_file(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_id=vm_cluster_network_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@data_guard_association_group.command(name=cli_util.override('db.failover_data_guard_association.command_name', 'failover'), help=u"""Performs a failover to transition the standby database identified by the `databaseId` parameter into the specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.

A failover might result in data loss depending on the protection mode in effect at the time of the primary database failure.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help=u"""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""The DB system administrator password.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def failover_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.failover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        failover_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.generate_autonomous_data_warehouse_wallet.command_name', 'generate-autonomous-data-warehouse-wallet'), help=u"""**Deprecated.** To create and download a wallet for an Autonomous Data Warehouse, use the [GenerateAutonomousDatabaseWallet] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--password', required=True, help=u"""The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_autonomous_data_warehouse_wallet(ctx, from_json, file, autonomous_data_warehouse_id, password):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['password'] = password

    client = cli_util.build_client('database', ctx)
    result = client.generate_autonomous_data_warehouse_wallet(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        generate_autonomous_data_warehouse_wallet_details=details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@autonomous_database_group.command(name=cli_util.override('db.generate_autonomous_database_wallet.command_name', 'generate-autonomous-database-wallet'), help=u"""Creates and downloads a wallet for the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--password', required=True, help=u"""The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either 1 numeric character or 1 special character.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_autonomous_database_wallet(ctx, from_json, file, autonomous_database_id, password):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['password'] = password

    client = cli_util.build_client('database', ctx)
    result = client.generate_autonomous_database_wallet(
        autonomous_database_id=autonomous_database_id,
        generate_autonomous_database_wallet_details=details,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@exadata_infrastructure_group.command(name=cli_util.override('db.generate_recommended_vm_cluster_network.command_name', 'generate-recommended-vm-cluster-network'), help=u"""Generates a recommended VM cluster network configuration.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly name for the VM cluster network. The name does not need to be unique.""")
@cli_util.option('--networks', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of parameters for generation of the client and backup networks.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ntp', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NTP server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'networks': {'module': 'database', 'class': 'list[InfoForNetworkGenDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'networks': {'module': 'database', 'class': 'list[InfoForNetworkGenDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'VmClusterNetworkDetails'})
@cli_util.wrap_exceptions
def generate_recommended_vm_cluster_network(ctx, from_json, exadata_infrastructure_id, compartment_id, display_name, networks, dns, ntp, freeform_tags, defined_tags):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['networks'] = cli_util.parse_json_parameter("networks", networks)

    if dns is not None:
        details['dns'] = cli_util.parse_json_parameter("dns", dns)

    if ntp is not None:
        details['ntp'] = cli_util.parse_json_parameter("ntp", ntp)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.generate_recommended_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        generate_recommended_network_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.get_autonomous_container_database.command_name', 'get'), help=u"""Gets information about the specified Autonomous Container Database.""")
@cli_util.option('--autonomous-container-database-id', required=True, help=u"""The Autonomous Container Database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousContainerDatabase'})
@cli_util.wrap_exceptions
def get_autonomous_container_database(ctx, from_json, autonomous_container_database_id):

    if isinstance(autonomous_container_database_id, six.string_types) and len(autonomous_container_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-container-database-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_container_database(
        autonomous_container_database_id=autonomous_container_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.get_autonomous_data_warehouse.command_name', 'get'), help=u"""**Deprecated.** To get the details of an Autonomous Data Warehouse, use the [GetAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def get_autonomous_data_warehouse(ctx, from_json, autonomous_data_warehouse_id):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('db.get_autonomous_data_warehouse_backup.command_name', 'get'), help=u"""**Deprecated.** To get information about a specified Autonomous Data Warehouse backup, use the [GetAutonomousDatabaseBackup] operation.""")
@cli_util.option('--autonomous-data-warehouse-backup-id', required=True, help=u"""The [OCID] of the Autonomous Data Warehouse backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouseBackup'})
@cli_util.wrap_exceptions
def get_autonomous_data_warehouse_backup(ctx, from_json, autonomous_data_warehouse_backup_id):

    if isinstance(autonomous_data_warehouse_backup_id, six.string_types) and len(autonomous_data_warehouse_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_data_warehouse_backup(
        autonomous_data_warehouse_backup_id=autonomous_data_warehouse_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.get_autonomous_database.command_name', 'get'), help=u"""Gets the details of the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def get_autonomous_database(ctx, from_json, autonomous_database_id):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('db.get_autonomous_database_backup.command_name', 'get'), help=u"""Gets information about the specified Autonomous Database backup.""")
@cli_util.option('--autonomous-database-backup-id', required=True, help=u"""The [OCID] of the Autonomous Database backup.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabaseBackup'})
@cli_util.wrap_exceptions
def get_autonomous_database_backup(ctx, from_json, autonomous_database_backup_id):

    if isinstance(autonomous_database_backup_id, six.string_types) and len(autonomous_database_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-backup-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_database_backup(
        autonomous_database_backup_id=autonomous_database_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.get_autonomous_exadata_infrastructure.command_name', 'get'), help=u"""Gets information about the specified Autonomous Exadata Infrastructure.""")
@cli_util.option('--autonomous-exadata-infrastructure-id', required=True, help=u"""The Autonomous Exadata Infrastructure  [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousExadataInfrastructure'})
@cli_util.wrap_exceptions
def get_autonomous_exadata_infrastructure(ctx, from_json, autonomous_exadata_infrastructure_id):

    if isinstance(autonomous_exadata_infrastructure_id, six.string_types) and len(autonomous_exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_autonomous_exadata_infrastructure(
        autonomous_exadata_infrastructure_id=autonomous_exadata_infrastructure_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db.get_backup.command_name', 'get'), help=u"""Gets information about the specified backup.""")
@cli_util.option('--backup-id', required=True, help=u"""The backup [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Backup'})
@cli_util.wrap_exceptions
def get_backup(ctx, from_json, backup_id):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_backup(
        backup_id=backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.get_backup_destination.command_name', 'get'), help=u"""Gets information about the specified backup destination.""")
@cli_util.option('--backup-destination-id', required=True, help=u"""The [OCID] of the backup destination.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'BackupDestination'})
@cli_util.wrap_exceptions
def get_backup_destination(ctx, from_json, backup_destination_id):

    if isinstance(backup_destination_id, six.string_types) and len(backup_destination_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-destination-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_backup_destination(
        backup_destination_id=backup_destination_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.get_data_guard_association.command_name', 'get'), help=u"""Gets the specified Data Guard association's configuration information.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help=u"""The Data Guard association's [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def get_data_guard_association(ctx, from_json, database_id, data_guard_association_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('db.get_database.command_name', 'get'), help=u"""Gets information about a specific database.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def get_database(ctx, from_json, database_id):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_database(
        database_id=database_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.get_db_home.command_name', 'get'), help=u"""Gets information about the specified database home.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def get_db_home(ctx, from_json, db_home_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('db.get_db_home_patch.command_name', 'get-db-home'), help=u"""Gets information about a specified patch package.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--patch-id', required=True, help=u"""The [OCID] of the patch.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_db_home_patch(ctx, from_json, db_home_id, patch_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    if isinstance(patch_id, six.string_types) and len(patch_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home_patch(
        db_home_id=db_home_id,
        patch_id=patch_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('db.get_db_home_patch_history_entry.command_name', 'get-db-home'), help=u"""Gets the patch history details for the specified patchHistoryEntryId""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--patch-history-entry-id', required=True, help=u"""The [OCID] of the patch history entry.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PatchHistoryEntry'})
@cli_util.wrap_exceptions
def get_db_home_patch_history_entry(ctx, from_json, db_home_id, patch_history_entry_id):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    if isinstance(patch_history_entry_id, six.string_types) and len(patch_history_entry_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-history-entry-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home_patch_history_entry(
        db_home_id=db_home_id,
        patch_history_entry_id=patch_history_entry_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('db.get_db_node.command_name', 'get'), help=u"""Gets information about the specified database node.""")
@cli_util.option('--db-node-id', required=True, help=u"""The database node [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbNode'})
@cli_util.wrap_exceptions
def get_db_node(ctx, from_json, db_node_id):

    if isinstance(db_node_id, six.string_types) and len(db_node_id.strip()) == 0:
        raise click.UsageError('Parameter --db-node-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_node(
        db_node_id=db_node_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.get_db_system.command_name', 'get'), help=u"""Gets information about the specified DB system.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def get_db_system(ctx, from_json, db_system_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('db.get_db_system_patch.command_name', 'get-db-system'), help=u"""Gets information about a specified patch package.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--patch-id', required=True, help=u"""The [OCID] of the patch.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_db_system_patch(ctx, from_json, db_system_id, patch_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    if isinstance(patch_id, six.string_types) and len(patch_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system_patch(
        db_system_id=db_system_id,
        patch_id=patch_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('db.get_db_system_patch_history_entry.command_name', 'get-db-system'), help=u"""Gets the patch history details for the specified patchHistoryEntryId.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--patch-history-entry-id', required=True, help=u"""The [OCID] of the patch history entry.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'PatchHistoryEntry'})
@cli_util.wrap_exceptions
def get_db_system_patch_history_entry(ctx, from_json, db_system_id, patch_history_entry_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    if isinstance(patch_history_entry_id, six.string_types) and len(patch_history_entry_id.strip()) == 0:
        raise click.UsageError('Parameter --patch-history-entry-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system_patch_history_entry(
        db_system_id=db_system_id,
        patch_history_entry_id=patch_history_entry_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.get_exadata_infrastructure.command_name', 'get'), help=u"""Gets information about the specified Exadata infrastructure.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExadataInfrastructure'})
@cli_util.wrap_exceptions
def get_exadata_infrastructure(ctx, from_json, exadata_infrastructure_id):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_exadata_infrastructure(
        exadata_infrastructure_id=exadata_infrastructure_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.get_exadata_iorm_config.command_name', 'get-exadata-iorm-config'), help=u"""Gets `IORM` Setting for the requested Exadata DB System. The default IORM Settings is pre-created in all the Exadata DB System.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExadataIormConfig'})
@cli_util.wrap_exceptions
def get_exadata_iorm_config(ctx, from_json, db_system_id):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_exadata_iorm_config(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@external_backup_job_group.command(name=cli_util.override('db.get_external_backup_job.command_name', 'get'), help=u"""Gets information about the specified external backup job.

**Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud] for more information.""")
@cli_util.option('--backup-id', required=True, help=u"""The backup [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'ExternalBackupJob'})
@cli_util.wrap_exceptions
def get_external_backup_job(ctx, from_json, backup_id):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_external_backup_job(
        backup_id=backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@maintenance_run_group.command(name=cli_util.override('db.get_maintenance_run.command_name', 'get'), help=u"""Gets information about the specified Maintenance Run.""")
@cli_util.option('--maintenance-run-id', required=True, help=u"""The Maintenance Run OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'MaintenanceRun'})
@cli_util.wrap_exceptions
def get_maintenance_run(ctx, from_json, maintenance_run_id):

    if isinstance(maintenance_run_id, six.string_types) and len(maintenance_run_id.strip()) == 0:
        raise click.UsageError('Parameter --maintenance-run-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_maintenance_run(
        maintenance_run_id=maintenance_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.get_vm_cluster.command_name', 'get'), help=u"""Gets information about the specified VM cluster.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The VM cluster [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'VmCluster'})
@cli_util.wrap_exceptions
def get_vm_cluster(ctx, from_json, vm_cluster_id):

    if isinstance(vm_cluster_id, six.string_types) and len(vm_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_vm_cluster(
        vm_cluster_id=vm_cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.get_vm_cluster_network.command_name', 'get'), help=u"""Gets information about the specified VM cluster network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The VM cluster network [OCID].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'VmClusterNetwork'})
@cli_util.wrap_exceptions
def get_vm_cluster_network(ctx, from_json, exadata_infrastructure_id, vm_cluster_network_id):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    if isinstance(vm_cluster_network_id, six.string_types) and len(vm_cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.get_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_id=vm_cluster_network_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.launch_autonomous_exadata_infrastructure.command_name', 'launch'), help=u"""Launches a new Autonomous Exadata Infrastructure in the specified compartment and availability domain.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment the Autonomous Exadata Infrastructure belongs in.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain where the Autonomous Exadata Infrastructure is located.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet the Autonomous Exadata Infrastructure is associated with.

**Subnet Restrictions:** - For Autonomous Exadata Infrastructures, do not use a subnet that overlaps with 192.168.128.0/20

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.""")
@cli_util.option('--shape', required=True, help=u"""The shape of the Autonomous Exadata Infrastructure. The shape determines resources allocated to the Autonomous Exadata Infrastructure (CPU cores, memory and storage). To get a list of shapes, use the ListDbSystemShapes operation.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Exadata Infrastructure. It does not have to be unique.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--domain', help=u"""A domain name used for the Autonomous Exadata Infrastructure. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to all the databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--maintenance-window-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousExadataInfrastructure'})
@cli_util.wrap_exceptions
def launch_autonomous_exadata_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, availability_domain, subnet_id, shape, display_name, nsg_ids, domain, license_model, maintenance_window_details, freeform_tags, defined_tags):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['availabilityDomain'] = availability_domain
    details['subnetId'] = subnet_id
    details['shape'] = shape

    if display_name is not None:
        details['displayName'] = display_name

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if domain is not None:
        details['domain'] = domain

    if license_model is not None:
        details['licenseModel'] = license_model

    if maintenance_window_details is not None:
        details['maintenanceWindowDetails'] = cli_util.parse_json_parameter("maintenance_window_details", maintenance_window_details)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.launch_autonomous_exadata_infrastructure(
        launch_autonomous_exadata_infrastructure_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_exadata_infrastructure') and callable(getattr(client, 'get_autonomous_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_exadata_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.launch_db_system.command_name', 'launch'), help=u"""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain where the DB system is located.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--shape', required=True, help=u"""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname', required=True, help=u"""The hostname for the DB system. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata DB systems.

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--fault-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains.

If you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.

If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node.

To get a list of Fault Domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--backup-subnet-id', help=u"""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-network-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules]. Applicable only to Exadata DB systems.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-zone', help=u"""The time zone to use for the DB system. For details, see [DB System Time Zones].""")
@cli_util.option('--db-system-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sparse-diskgroup', type=click.BOOL, help=u"""If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.""")
@cli_util.option('--domain', help=u"""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--cluster-name', help=u"""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help=u"""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help=u"""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help=u"""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DB_BACKUP"]), help=u"""The source of the database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a backup. The default is NONE.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, availability_domain, subnet_id, shape, ssh_public_keys, hostname, cpu_core_count, fault_domains, display_name, backup_subnet_id, nsg_ids, backup_network_nsg_ids, time_zone, db_system_options, sparse_diskgroup, domain, cluster_name, data_storage_percentage, initial_data_storage_size_in_gb, node_count, freeform_tags, defined_tags, source):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['availabilityDomain'] = availability_domain
    details['subnetId'] = subnet_id
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['hostname'] = hostname
    details['cpuCoreCount'] = cpu_core_count

    if fault_domains is not None:
        details['faultDomains'] = cli_util.parse_json_parameter("fault_domains", fault_domains)

    if display_name is not None:
        details['displayName'] = display_name

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if backup_network_nsg_ids is not None:
        details['backupNetworkNsgIds'] = cli_util.parse_json_parameter("backup_network_nsg_ids", backup_network_nsg_ids)

    if time_zone is not None:
        details['timeZone'] = time_zone

    if db_system_options is not None:
        details['dbSystemOptions'] = cli_util.parse_json_parameter("db_system_options", db_system_options)

    if sparse_diskgroup is not None:
        details['sparseDiskgroup'] = sparse_diskgroup

    if domain is not None:
        details['domain'] = domain

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.launch_db_system_launch_db_system_details.command_name', 'launch-db-system-launch-db-system-details'), help=u"""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain where the DB system is located.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--shape', required=True, help=u"""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname', required=True, help=u"""The hostname for the DB system. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata DB systems.

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--db-home', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help=u"""The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.""")
@cli_util.option('--fault-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains.

If you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.

If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node.

To get a list of Fault Domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--backup-subnet-id', help=u"""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-network-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules]. Applicable only to Exadata DB systems.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-zone', help=u"""The time zone to use for the DB system. For details, see [DB System Time Zones].""")
@cli_util.option('--db-system-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sparse-diskgroup', type=click.BOOL, help=u"""If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.""")
@cli_util.option('--domain', help=u"""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--cluster-name', help=u"""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help=u"""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help=u"""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help=u"""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--disk-redundancy', type=custom_types.CliCaseInsensitiveChoice(["HIGH", "NORMAL"]), help=u"""The type of redundancy configured for the DB system. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_launch_db_system_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, availability_domain, subnet_id, shape, ssh_public_keys, hostname, cpu_core_count, db_home, database_edition, fault_domains, display_name, backup_subnet_id, nsg_ids, backup_network_nsg_ids, time_zone, db_system_options, sparse_diskgroup, domain, cluster_name, data_storage_percentage, initial_data_storage_size_in_gb, node_count, freeform_tags, defined_tags, disk_redundancy, license_model):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['availabilityDomain'] = availability_domain
    details['subnetId'] = subnet_id
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['hostname'] = hostname
    details['cpuCoreCount'] = cpu_core_count
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)
    details['databaseEdition'] = database_edition

    if fault_domains is not None:
        details['faultDomains'] = cli_util.parse_json_parameter("fault_domains", fault_domains)

    if display_name is not None:
        details['displayName'] = display_name

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if backup_network_nsg_ids is not None:
        details['backupNetworkNsgIds'] = cli_util.parse_json_parameter("backup_network_nsg_ids", backup_network_nsg_ids)

    if time_zone is not None:
        details['timeZone'] = time_zone

    if db_system_options is not None:
        details['dbSystemOptions'] = cli_util.parse_json_parameter("db_system_options", db_system_options)

    if sparse_diskgroup is not None:
        details['sparseDiskgroup'] = sparse_diskgroup

    if domain is not None:
        details['domain'] = domain

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if license_model is not None:
        details['licenseModel'] = license_model

    details['source'] = 'NONE'

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.launch_db_system_launch_db_system_from_backup_details.command_name', 'launch-db-system-launch-db-system-from-backup-details'), help=u"""Launches a new DB system in the specified compartment and availability domain. The Oracle Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment the DB system  belongs in.""")
@cli_util.option('--availability-domain', required=True, help=u"""The availability domain where the DB system is located.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet the DB system is associated with.

**Subnet Restrictions:** - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28. - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20.

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and the backup subnet.""")
@cli_util.option('--shape', required=True, help=u"""The shape of the DB system. The shape determines resources allocated to the DB system. - For virtual machine shapes, the number of CPU cores and memory - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage

To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@cli_util.option('--ssh-public-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--hostname', required=True, help=u"""The hostname for the DB system. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata DB systems.

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB system will fail to provision.""")
@cli_util.option('--cpu-core-count', required=True, type=click.INT, help=u"""The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:

- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52. - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336. - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92. - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184. - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape. For information about the number of cores for a virtual machine DB system shape, see [Virtual Machine DB Systems]""")
@cli_util.option('--db-home', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-edition', required=True, type=custom_types.CliCaseInsensitiveChoice(["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]), help=u"""The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.""")
@cli_util.option('--fault-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A Fault Domain is a grouping of hardware and infrastructure within an availability domain. Fault Domains let you distribute your instances so that they are not on the same physical hardware within a single availability domain. A hardware failure or maintenance that affects one Fault Domain does not affect DB systems in other Fault Domains.

If you do not specify the Fault Domain, the system selects one for you. To change the Fault Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.

If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into. The system assigns your nodes automatically to the Fault Domains you specify so that no Fault Domain contains more than one node.

To get a list of Fault Domains, use the [ListFaultDomains] operation in the Identity and Access Management Service API.

Example: `FAULT-DOMAIN-1`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB system. The name does not have to be unique.""")
@cli_util.option('--backup-subnet-id', help=u"""The [OCID] of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

**Subnet Restrictions:** See the subnet restrictions information for **subnetId**.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-network-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules]. Applicable only to Exadata DB systems.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-zone', help=u"""The time zone to use for the DB system. For details, see [DB System Time Zones].""")
@cli_util.option('--db-system-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sparse-diskgroup', type=click.BOOL, help=u"""If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.""")
@cli_util.option('--domain', help=u"""A domain name used for the DB system. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.option('--cluster-name', help=u"""The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@cli_util.option('--data-storage-percentage', type=click.INT, help=u"""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.""")
@cli_util.option('--initial-data-storage-size-in-gb', type=click.INT, help=u"""Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.""")
@cli_util.option('--node-count', type=click.INT, help=u"""The number of nodes to launch for a 2-node RAC virtual machine DB system.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--disk-redundancy', type=custom_types.CliCaseInsensitiveChoice(["HIGH", "NORMAL"]), help=u"""The type of redundancy configured for the DB system. NORMAL 2-way redundancy, recommended for test and development systems. HIGH is 3-way redundancy, recommended for production systems.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromBackupDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fault-domains': {'module': 'database', 'class': 'list[string]'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'db-system-options': {'module': 'database', 'class': 'DbSystemOptions'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'db-home': {'module': 'database', 'class': 'CreateDbHomeFromBackupDetails'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def launch_db_system_launch_db_system_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, availability_domain, subnet_id, shape, ssh_public_keys, hostname, cpu_core_count, db_home, database_edition, fault_domains, display_name, backup_subnet_id, nsg_ids, backup_network_nsg_ids, time_zone, db_system_options, sparse_diskgroup, domain, cluster_name, data_storage_percentage, initial_data_storage_size_in_gb, node_count, freeform_tags, defined_tags, disk_redundancy, license_model):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['availabilityDomain'] = availability_domain
    details['subnetId'] = subnet_id
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['hostname'] = hostname
    details['cpuCoreCount'] = cpu_core_count
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)
    details['databaseEdition'] = database_edition

    if fault_domains is not None:
        details['faultDomains'] = cli_util.parse_json_parameter("fault_domains", fault_domains)

    if display_name is not None:
        details['displayName'] = display_name

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if backup_network_nsg_ids is not None:
        details['backupNetworkNsgIds'] = cli_util.parse_json_parameter("backup_network_nsg_ids", backup_network_nsg_ids)

    if time_zone is not None:
        details['timeZone'] = time_zone

    if db_system_options is not None:
        details['dbSystemOptions'] = cli_util.parse_json_parameter("db_system_options", db_system_options)

    if sparse_diskgroup is not None:
        details['sparseDiskgroup'] = sparse_diskgroup

    if domain is not None:
        details['domain'] = domain

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if initial_data_storage_size_in_gb is not None:
        details['initialDataStorageSizeInGB'] = initial_data_storage_size_in_gb

    if node_count is not None:
        details['nodeCount'] = node_count

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if license_model is not None:
        details['licenseModel'] = license_model

    details['source'] = 'DB_BACKUP'

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.list_autonomous_container_databases.command_name', 'list'), help=u"""Gets a list of the Autonomous Container Databases in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--autonomous-exadata-infrastructure-id', help=u"""The Autonomous Exadata Infrastructure [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--availability-domain', help=u"""A filter to return only resources that match the given availability domain exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousContainerDatabaseSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_container_databases(ctx, from_json, all_pages, page_size, compartment_id, autonomous_exadata_infrastructure_id, limit, page, sort_by, sort_order, lifecycle_state, availability_domain, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if autonomous_exadata_infrastructure_id is not None:
        kwargs['autonomous_exadata_infrastructure_id'] = autonomous_exadata_infrastructure_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_container_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_container_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_container_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_backup_group.command(name=cli_util.override('db.list_autonomous_data_warehouse_backups.command_name', 'list'), help=u"""**Deprecated.** To get a list of Autonomous Data Warehouse backups, use the [ListAutonomousDatabaseBackups] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', help=u"""The database [OCID].""")
@cli_util.option('--compartment-id', help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDataWarehouseBackupSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_data_warehouse_backups(ctx, from_json, all_pages, page_size, autonomous_data_warehouse_id, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if autonomous_data_warehouse_id is not None:
        kwargs['autonomous_data_warehouse_id'] = autonomous_data_warehouse_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_data_warehouse_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_data_warehouse_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_autonomous_data_warehouse_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.list_autonomous_data_warehouses.command_name', 'list'), help=u"""**Deprecated.** To get a list of Autonomous Data Warehouses, use the [ListAutonomousDatabases] operation and specify `DW` as the workload type.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDataWarehouseSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_data_warehouses(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_data_warehouses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_data_warehouses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_data_warehouses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_database_backup_group.command(name=cli_util.override('db.list_autonomous_database_backups.command_name', 'list'), help=u"""Gets a list of Autonomous Database backups based on either the `autonomousDatabaseId` or `compartmentId` specified as a query parameter.""")
@cli_util.option('--autonomous-database-id', help=u"""The database [OCID].""")
@cli_util.option('--compartment-id', help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDatabaseBackupSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_database_backups(ctx, from_json, all_pages, page_size, autonomous_database_id, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if autonomous_database_id is not None:
        kwargs['autonomous_database_id'] = autonomous_database_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_database_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_database_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_autonomous_database_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.list_autonomous_databases.command_name', 'list'), help=u"""Gets a list of Autonomous Databases.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--autonomous-container-database-id', help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--db-workload', type=custom_types.CliCaseInsensitiveChoice(["OLTP", "DW"]), help=u"""A filter to return only autonomous database resources that match the specified workload type.""")
@cli_util.option('--is-free-tier', type=click.BOOL, help=u"""Filter on the value of the resource's 'isFreeTier' property. A value of `true` returns only Always Free resources. A value of `false` excludes Always Free resources from the returned results. Omitting this parameter returns both Always Free and paid resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDatabaseSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_databases(ctx, from_json, all_pages, page_size, compartment_id, autonomous_container_database_id, limit, page, sort_by, sort_order, lifecycle_state, db_workload, is_free_tier, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if autonomous_container_database_id is not None:
        kwargs['autonomous_container_database_id'] = autonomous_container_database_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if db_workload is not None:
        kwargs['db_workload'] = db_workload
    if is_free_tier is not None:
        kwargs['is_free_tier'] = is_free_tier
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_db_preview_version_group.command(name=cli_util.override('db.list_autonomous_db_preview_versions.command_name', 'list'), help=u"""Gets a list of supported Autonomous Database versions. Note that preview version software is only available for [serverless deployments].""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DBWORKLOAD"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for DBWORKLOAD is ascending.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousDbPreviewVersionSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_db_preview_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_db_preview_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_db_preview_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_db_preview_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_shape_group.command(name=cli_util.override('db.list_autonomous_exadata_infrastructure_shapes.command_name', 'list'), help=u"""Gets a list of the shapes that can be used to launch a new Autonomous Exadata Infrastructure DB system. The shape determines resources to allocate to the DB system (CPU cores, memory and storage).""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the Availability Domain.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousExadataInfrastructureShapeSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_exadata_infrastructure_shapes(ctx, from_json, all_pages, page_size, availability_domain, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_exadata_infrastructure_shapes,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_exadata_infrastructure_shapes,
            limit,
            page_size,
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_exadata_infrastructure_shapes(
            availability_domain=availability_domain,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.list_autonomous_exadata_infrastructures.command_name', 'list'), help=u"""Gets a list of the Autonomous Exadata Infrastructures in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

  **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--availability-domain', help=u"""A filter to return only resources that match the given availability domain exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[AutonomousExadataInfrastructureSummary]'})
@cli_util.wrap_exceptions
def list_autonomous_exadata_infrastructures(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, availability_domain, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_autonomous_exadata_infrastructures,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_autonomous_exadata_infrastructures,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_autonomous_exadata_infrastructures(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backup_destination_summary_group.command(name=cli_util.override('db.list_backup_destination.command_name', 'list-backup-destination'), help=u"""Gets a list of backup destinations in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--type', help=u"""A filter to return only resources that match the given type of the Backup Destination.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[BackupDestinationSummary]'})
@cli_util.wrap_exceptions
def list_backup_destination(ctx, from_json, all_pages, page_size, compartment_id, limit, page, type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if type is not None:
        kwargs['type'] = type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backup_destination,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backup_destination,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_backup_destination(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db.list_backups.command_name', 'list'), help=u"""Gets a list of backups based on the databaseId or compartmentId specified. Either one of the query parameters must be provided.""")
@cli_util.option('--database-id', help=u"""The [OCID] of the database.""")
@cli_util.option('--compartment-id', help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[BackupSummary]'})
@cli_util.wrap_exceptions
def list_backups(ctx, from_json, all_pages, page_size, database_id, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backups,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backups,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_backups(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.list_data_guard_associations.command_name', 'list'), help=u"""Lists all Data Guard associations for the specified database.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DataGuardAssociationSummary]'})
@cli_util.wrap_exceptions
def list_data_guard_associations(ctx, from_json, all_pages, page_size, database_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_guard_associations,
            database_id=database_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_guard_associations,
            limit,
            page_size,
            database_id=database_id,
            **kwargs
        )
    else:
        result = client.list_data_guard_associations(
            database_id=database_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('db.list_databases.command_name', 'list'), help=u"""Gets a list of the databases in the specified database home.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--db-home-id', required=True, help=u"""A database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DBNAME", "TIMECREATED"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DBNAME is ascending. The DBNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--db-name', help=u"""A filter to return only resources that match the entire database name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DatabaseSummary]'})
@cli_util.wrap_exceptions
def list_databases(ctx, from_json, all_pages, page_size, compartment_id, db_home_id, limit, page, sort_by, sort_order, lifecycle_state, db_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if db_name is not None:
        kwargs['db_name'] = db_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_databases,
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_databases(
            compartment_id=compartment_id,
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('db.list_db_home_patch_history_entries.command_name', 'list-db-home'), help=u"""Gets history of the actions taken for patches for the specified database home.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_db_home_patch_history_entries(ctx, from_json, all_pages, page_size, db_home_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_home_patch_history_entries,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_home_patch_history_entries,
            limit,
            page_size,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_db_home_patch_history_entries(
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('db.list_db_home_patches.command_name', 'list-db-home'), help=u"""Lists patches applicable to the requested database home.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_db_home_patches(ctx, from_json, all_pages, page_size, db_home_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_home_patches,
            db_home_id=db_home_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_home_patches,
            limit,
            page_size,
            db_home_id=db_home_id,
            **kwargs
        )
    else:
        result = client.list_db_home_patches(
            db_home_id=db_home_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.list_db_homes.command_name', 'list'), help=u"""Gets a list of database homes in the specified DB system and compartment. A database home is a directory where Oracle Database software is installed.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--db-system-id', help=u"""The [OCID] of the DB system.""")
@cli_util.option('--vm-cluster-id', help=u"""The [OCID] of the VM cluster.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbHomeSummary]'})
@cli_util.wrap_exceptions
def list_db_homes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, vm_cluster_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    if vm_cluster_id is not None:
        kwargs['vm_cluster_id'] = vm_cluster_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_homes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_homes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_homes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_node_group.command(name=cli_util.override('db.list_db_nodes.command_name', 'list'), help=u"""Gets a list of database nodes in the specified DB system and compartment. A database node is a server running database software.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--db-system-id', help=u"""The [OCID] of the DB system.""")
@cli_util.option('--vm-cluster-id', help=u"""The [OCID] of the VM cluster.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""Sort by TIMECREATED.  Default order for TIMECREATED is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbNodeSummary]'})
@cli_util.wrap_exceptions
def list_db_nodes(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, vm_cluster_id, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    if vm_cluster_id is not None:
        kwargs['vm_cluster_id'] = vm_cluster_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_nodes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_nodes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_nodes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_history_entry_group.command(name=cli_util.override('db.list_db_system_patch_history_entries.command_name', 'list-db-system'), help=u"""Gets the history of the patch actions performed on the specified DB system.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchHistoryEntrySummary]'})
@cli_util.wrap_exceptions
def list_db_system_patch_history_entries(ctx, from_json, all_pages, page_size, db_system_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_patch_history_entries,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_patch_history_entries,
            limit,
            page_size,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_system_patch_history_entries(
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@patch_group.command(name=cli_util.override('db.list_db_system_patches.command_name', 'list-db-system'), help=u"""Lists the patches applicable to the requested DB system.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_db_system_patches(ctx, from_json, all_pages, page_size, db_system_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_patches,
            db_system_id=db_system_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_patches,
            limit,
            page_size,
            db_system_id=db_system_id,
            **kwargs
        )
    else:
        result = client.list_db_system_patches(
            db_system_id=db_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_system_shape_group.command(name=cli_util.override('db.list_db_system_shapes.command_name', 'list'), help=u"""Gets a list of the shapes that can be used to launch a new DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--availability-domain', help=u"""The name of the Availability Domain.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbSystemShapeSummary]'})
@cli_util.wrap_exceptions
def list_db_system_shapes(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_system_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_system_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_system_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.list_db_systems.command_name', 'list'), help=u"""Gets a list of the DB systems in the specified compartment. You can specify a backupId to list only the DB systems that support creating a database using this backup in this compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--backup-id', help=u"""The [OCID] of the backup. Specify a backupId to list only the DB systems or DB homes that support creating a database using this backup in this compartment.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--availability-domain', help=u"""A filter to return only resources that match the given availability domain exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems(ctx, from_json, all_pages, page_size, compartment_id, limit, page, backup_id, sort_by, sort_order, lifecycle_state, availability_domain, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if backup_id is not None:
        kwargs['backup_id'] = backup_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if display_name is not None:
        kwargs['display_name'] = display_name
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_systems,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_systems,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_systems(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_version_group.command(name=cli_util.override('db.list_db_versions.command_name', 'list'), help=u"""Gets a list of supported Oracle Database versions.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--db-system-shape', help=u"""If provided, filters the results to the set of database versions which are supported for the given shape.""")
@cli_util.option('--db-system-id', help=u"""The DB system [OCID]. If provided, filters the results to the set of database versions which are supported for the DB system.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[DbVersionSummary]'})
@cli_util.wrap_exceptions
def list_db_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, db_system_shape, db_system_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if db_system_shape is not None:
        kwargs['db_system_shape'] = db_system_shape
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.list_exadata_infrastructures.command_name', 'list'), help=u"""Gets a list of the Exadata infrastructure in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[ExadataInfrastructureSummary]'})
@cli_util.wrap_exceptions
def list_exadata_infrastructures(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_exadata_infrastructures,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_exadata_infrastructures,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_exadata_infrastructures(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@gi_version_group.command(name=cli_util.override('db.list_gi_versions.command_name', 'list'), help=u"""Gets a list of supported GI versions for VM Cluster.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--shape', help=u"""If provided, filters the results for the given shape.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[GiVersionSummary]'})
@cli_util.wrap_exceptions
def list_gi_versions(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, shape):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if shape is not None:
        kwargs['shape'] = shape
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_gi_versions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_gi_versions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_gi_versions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@maintenance_run_group.command(name=cli_util.override('db.list_maintenance_runs.command_name', 'list'), help=u"""Gets a list of the Maintenance Runs in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--target-resource-id', help=u"""The target resource ID.""")
@cli_util.option('--target-resource-type', type=custom_types.CliCaseInsensitiveChoice(["AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE"]), help=u"""The type of the target resource.""")
@cli_util.option('--maintenance-type', type=custom_types.CliCaseInsensitiveChoice(["PLANNED", "UNPLANNED"]), help=u"""The maintenance type.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_SCHEDULED", "TIME_ENDED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIME_SCHEDULED and TIME_ENDED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--availability-domain', help=u"""A filter to return only resources that match the given availability domain exactly.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[MaintenanceRunSummary]'})
@cli_util.wrap_exceptions
def list_maintenance_runs(ctx, from_json, all_pages, page_size, compartment_id, target_resource_id, target_resource_type, maintenance_type, limit, page, sort_by, sort_order, lifecycle_state, availability_domain):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if target_resource_id is not None:
        kwargs['target_resource_id'] = target_resource_id
    if target_resource_type is not None:
        kwargs['target_resource_type'] = target_resource_type
    if maintenance_type is not None:
        kwargs['maintenance_type'] = maintenance_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_maintenance_runs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_maintenance_runs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_maintenance_runs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.list_vm_cluster_networks.command_name', 'list'), help=u"""Gets a list of the VM cluster networks in the specified compartment.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[VmClusterNetworkSummary]'})
@cli_util.wrap_exceptions
def list_vm_cluster_networks(ctx, from_json, all_pages, page_size, exadata_infrastructure_id, compartment_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vm_cluster_networks,
            exadata_infrastructure_id=exadata_infrastructure_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vm_cluster_networks,
            limit,
            page_size,
            exadata_infrastructure_id=exadata_infrastructure_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vm_cluster_networks(
            exadata_infrastructure_id=exadata_infrastructure_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.list_vm_clusters.command_name', 'list'), help=u"""Gets a list of the VM clusters in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--exadata-infrastructure-id', help=u"""If provided, filters the results for the given Exadata Infrastructure.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The pagination token to continue listing from.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state exactly.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'list[VmClusterSummary]'})
@cli_util.wrap_exceptions
def list_vm_clusters(ctx, from_json, all_pages, page_size, compartment_id, exadata_infrastructure_id, limit, page, sort_by, sort_order, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if exadata_infrastructure_id is not None:
        kwargs['exadata_infrastructure_id'] = exadata_infrastructure_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vm_clusters,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vm_clusters,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_vm_clusters(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.reinstate_data_guard_association.command_name', 'reinstate'), help=u"""Reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help=u"""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""The DB system administrator password.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def reinstate_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.reinstate_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        reinstate_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.restart_autonomous_container_database.command_name', 'restart'), help=u"""Rolling restarts the specified Autonomous Container Database.""")
@cli_util.option('--autonomous-container-database-id', required=True, help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousContainerDatabase'})
@cli_util.wrap_exceptions
def restart_autonomous_container_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_container_database_id, if_match):

    if isinstance(autonomous_container_database_id, six.string_types) and len(autonomous_container_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-container-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.restart_autonomous_container_database(
        autonomous_container_database_id=autonomous_container_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_container_database') and callable(getattr(client, 'get_autonomous_container_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_container_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.restore_autonomous_data_warehouse.command_name', 'restore'), help=u"""**Deprecated.** To restore an Autonomous Data Warehouse, use the [RestoreAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--timestamp', required=True, type=custom_types.CLI_DATETIME, help=u"""The time to restore the database to.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def restore_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, timestamp, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['timestamp'] = timestamp

    client = cli_util.build_client('database', ctx)
    result = client.restore_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        restore_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.restore_autonomous_database.command_name', 'restore'), help=u"""Restores an Autonomous Database based on the provided request parameters.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--timestamp', required=True, type=custom_types.CLI_DATETIME, help=u"""The time to restore the database to.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-scn', help=u"""Restores using the backup with the System Change Number (SCN) specified.""")
@cli_util.option('--latest', type=click.BOOL, help=u"""Restores to the last known good state with the least possible data loss.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def restore_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, timestamp, database_scn, latest, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['timestamp'] = timestamp

    if database_scn is not None:
        details['databaseSCN'] = database_scn

    if latest is not None:
        details['latest'] = latest

    client = cli_util.build_client('database', ctx)
    result = client.restore_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        restore_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('db.restore_database.command_name', 'restore'), help=u"""Restore a Database based on the request parameters you provide.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--database-scn', help=u"""Restores using the backup with the System Change Number (SCN) specified.""")
@cli_util.option('--timestamp', type=custom_types.CLI_DATETIME, help=u"""Restores to the timestamp specified.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--latest', type=click.BOOL, help=u"""Restores to the last known good state with the least possible data loss.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def restore_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, database_scn, timestamp, latest, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if database_scn is not None:
        details['databaseSCN'] = database_scn

    if timestamp is not None:
        details['timestamp'] = timestamp

    if latest is not None:
        details['latest'] = latest

    client = cli_util.build_client('database', ctx)
    result = client.restore_database(
        database_id=database_id,
        restore_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_database') and callable(getattr(client, 'get_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.start_autonomous_data_warehouse.command_name', 'start'), help=u"""**Deprecated.** To start an Autonomous Data Warehouse, use the [StartAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def start_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.start_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.start_autonomous_database.command_name', 'start'), help=u"""Starts the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def start_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.start_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.stop_autonomous_data_warehouse.command_name', 'stop'), help=u"""**Deprecated.** To stop an Autonomous Data Warehouse, use the [StopAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def stop_autonomous_data_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.stop_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.stop_autonomous_database.command_name', 'stop'), help=u"""Stops the specified Autonomous Database.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def stop_autonomous_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.stop_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_guard_association_group.command(name=cli_util.override('db.switchover_data_guard_association.command_name', 'switchover'), help=u"""Performs a switchover to transition the primary database of a Data Guard association into a standby role. The standby database associated with the `dataGuardAssociationId` assumes the primary database role.

A switchover guarantees no data loss.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--data-guard-association-id', required=True, help=u"""The Data Guard association's [OCID].""")
@cli_util.option('--database-admin-password', required=True, help=u"""The DB system administrator password.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'DataGuardAssociation'})
@cli_util.wrap_exceptions
def switchover_data_guard_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, data_guard_association_id, database_admin_password, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')

    if isinstance(data_guard_association_id, six.string_types) and len(data_guard_association_id.strip()) == 0:
        raise click.UsageError('Parameter --data-guard-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['databaseAdminPassword'] = database_admin_password

    client = cli_util.build_client('database', ctx)
    result = client.switchover_data_guard_association(
        database_id=database_id,
        data_guard_association_id=data_guard_association_id,
        switchover_data_guard_association_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_data_guard_association') and callable(getattr(client, 'get_data_guard_association')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_guard_association(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.terminate_autonomous_container_database.command_name', 'terminate'), help=u"""Terminates an Autonomous Container Database, which permanently deletes the container database and any databases within the container database. The database data is local to the Autonomous Exadata Infrastructure and will be lost when the container database is terminated. Oracle recommends that you back up any data in the Autonomous Container Database prior to terminating it.""")
@cli_util.option('--autonomous-container-database-id', required=True, help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_autonomous_container_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_container_database_id, if_match):

    if isinstance(autonomous_container_database_id, six.string_types) and len(autonomous_container_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-container-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.terminate_autonomous_container_database(
        autonomous_container_database_id=autonomous_container_database_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_container_database') and callable(getattr(client, 'get_autonomous_container_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_container_database(autonomous_container_database_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.terminate_autonomous_exadata_infrastructure.command_name', 'terminate'), help=u"""Terminates an Autonomous Exadata Infrastructure, which permanently deletes the Exadata Infrastructure and any container databases and databases contained in the Exadata Infrastructure. The database data is local to the Autonomous Exadata Infrastructure and will be lost when the system is terminated. Oracle recommends that you back up any data in the Autonomous Exadata Infrastructure prior to terminating it.""")
@cli_util.option('--autonomous-exadata-infrastructure-id', required=True, help=u"""The Autonomous Exadata Infrastructure  [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_autonomous_exadata_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_exadata_infrastructure_id, if_match):

    if isinstance(autonomous_exadata_infrastructure_id, six.string_types) and len(autonomous_exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-exadata-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.terminate_autonomous_exadata_infrastructure(
        autonomous_exadata_infrastructure_id=autonomous_exadata_infrastructure_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_exadata_infrastructure') and callable(getattr(client, 'get_autonomous_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_autonomous_exadata_infrastructure(autonomous_exadata_infrastructure_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.terminate_db_system.command_name', 'terminate'), help=u"""Terminates a DB system and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB system and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB system prior to terminating it.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.terminate_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_db_system(db_system_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_container_database_group.command(name=cli_util.override('db.update_autonomous_container_database.command_name', 'update'), help=u"""Updates the properties of an Autonomous Container Database, such as the CPU core count and storage size.""")
@cli_util.option('--autonomous-container-database-id', required=True, help=u"""The Autonomous Container Database [OCID].""")
@cli_util.option('--display-name', help=u"""The display name for the Autonomous Container Database.""")
@cli_util.option('--patch-model', type=custom_types.CliCaseInsensitiveChoice(["RELEASE_UPDATES", "RELEASE_UPDATE_REVISIONS"]), help=u"""Database Patch model preference.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'backup-config': {'module': 'database', 'class': 'AutonomousContainerDatabaseBackupConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'backup-config': {'module': 'database', 'class': 'AutonomousContainerDatabaseBackupConfig'}}, output_type={'module': 'database', 'class': 'AutonomousContainerDatabase'})
@cli_util.wrap_exceptions
def update_autonomous_container_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_container_database_id, display_name, patch_model, freeform_tags, defined_tags, backup_config, if_match):

    if isinstance(autonomous_container_database_id, six.string_types) and len(autonomous_container_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-container-database-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or backup_config:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and backup-config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if patch_model is not None:
        details['patchModel'] = patch_model

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if backup_config is not None:
        details['backupConfig'] = cli_util.parse_json_parameter("backup_config", backup_config)

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_container_database(
        autonomous_container_database_id=autonomous_container_database_id,
        update_autonomous_container_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_container_database') and callable(getattr(client, 'get_autonomous_container_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_container_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_data_warehouse_group.command(name=cli_util.override('db.update_autonomous_data_warehouse.command_name', 'update'), help=u"""**Deprecated.** To update the CPU core count and storage size of an Autonomous Data Warehouse, use the [UpdateAutonomousDatabase] operation.""")
@cli_util.option('--autonomous-data-warehouse-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The number of CPU cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', type=click.INT, help=u"""Size, in terabytes, of the data volume that will be attached to the database.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.""")
@cli_util.option('--admin-password', help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousDataWarehouse'})
@cli_util.wrap_exceptions
def update_autonomous_data_warehouse(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_data_warehouse_id, cpu_core_count, data_storage_size_in_tbs, display_name, admin_password, freeform_tags, defined_tags, if_match):

    if isinstance(autonomous_data_warehouse_id, six.string_types) and len(autonomous_data_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-data-warehouse-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_tbs is not None:
        details['dataStorageSizeInTBs'] = data_storage_size_in_tbs

    if display_name is not None:
        details['displayName'] = display_name

    if admin_password is not None:
        details['adminPassword'] = admin_password

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_data_warehouse(
        autonomous_data_warehouse_id=autonomous_data_warehouse_id,
        update_autonomous_data_warehouse_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_data_warehouse') and callable(getattr(client, 'get_autonomous_data_warehouse')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_data_warehouse(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_database_group.command(name=cli_util.override('db.update_autonomous_database.command_name', 'update'), help=u"""Updates the specified Autonomous Database with a new CPU core count and size.""")
@cli_util.option('--autonomous-database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The number of CPU cores to be made available to the database.""")
@cli_util.option('--data-storage-size-in-tbs', type=click.INT, help=u"""The size, in terabytes, of the data volume that will be attached to the database.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the Autonomous Database. The name does not have to be unique.""")
@cli_util.option('--is-free-tier', type=click.BOOL, help=u"""Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB memory. For Always Free databases, memory and CPU cannot be scaled.""")
@cli_util.option('--admin-password', help=u"""The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.""")
@cli_util.option('--db-name', help=u"""New name for this Autonomous Database. It must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted. This is valid only for dedicated databases.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the Oracle Autonomous Database. The default for Autonomous Database using the [shared deployment] is BRING_YOUR_OWN_LICENSE. Note that when provisioning an Autonomous Database using the [dedicated deployment] option, this attribute must be null because the attribute is already set on Autonomous Exadata Infrastructure level.""")
@cli_util.option('--whitelisted-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The client IP access control list (ACL). This feature is available for [serverless deployments] only. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet. To delete all the existing white listed IP\u2019s, use an array with a single empty string entry.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-auto-scaling-enabled', type=click.BOOL, help=u"""Indicates if auto scaling is enabled for the Autonomous Database CPU core count. The default value is false. Note that auto scaling is available for [serverless deployments] only.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'whitelisted-ips': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'AutonomousDatabase'})
@cli_util.wrap_exceptions
def update_autonomous_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_database_id, cpu_core_count, data_storage_size_in_tbs, display_name, is_free_tier, admin_password, db_name, freeform_tags, defined_tags, license_model, whitelisted_ips, is_auto_scaling_enabled, if_match):

    if isinstance(autonomous_database_id, six.string_types) and len(autonomous_database_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-database-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or whitelisted_ips:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and whitelisted-ips will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if data_storage_size_in_tbs is not None:
        details['dataStorageSizeInTBs'] = data_storage_size_in_tbs

    if display_name is not None:
        details['displayName'] = display_name

    if is_free_tier is not None:
        details['isFreeTier'] = is_free_tier

    if admin_password is not None:
        details['adminPassword'] = admin_password

    if db_name is not None:
        details['dbName'] = db_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if license_model is not None:
        details['licenseModel'] = license_model

    if whitelisted_ips is not None:
        details['whitelistedIps'] = cli_util.parse_json_parameter("whitelisted_ips", whitelisted_ips)

    if is_auto_scaling_enabled is not None:
        details['isAutoScalingEnabled'] = is_auto_scaling_enabled

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_database(
        autonomous_database_id=autonomous_database_id,
        update_autonomous_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_database') and callable(getattr(client, 'get_autonomous_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@autonomous_exadata_infrastructure_group.command(name=cli_util.override('db.update_autonomous_exadata_infrastructure.command_name', 'update'), help=u"""Updates the properties of an Autonomous Exadata Infrastructure, such as the CPU core count.""")
@cli_util.option('--autonomous-exadata-infrastructure-id', required=True, help=u"""The Autonomous Exadata Infrastructure  [OCID].""")
@cli_util.option('--display-name', help=u"""The display name is a user-friendly name for the Autonomous Exadata Infrastructure. The display name does not have to be unique.""")
@cli_util.option('--maintenance-window-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-window-details': {'module': 'database', 'class': 'MaintenanceWindow'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'AutonomousExadataInfrastructure'})
@cli_util.wrap_exceptions
def update_autonomous_exadata_infrastructure(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, autonomous_exadata_infrastructure_id, display_name, maintenance_window_details, nsg_ids, freeform_tags, defined_tags, if_match):

    if isinstance(autonomous_exadata_infrastructure_id, six.string_types) and len(autonomous_exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --autonomous-exadata-infrastructure-id cannot be whitespace or empty string')
    if not force:
        if maintenance_window_details or nsg_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to maintenance-window-details and nsg-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if maintenance_window_details is not None:
        details['maintenanceWindowDetails'] = cli_util.parse_json_parameter("maintenance_window_details", maintenance_window_details)

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_autonomous_exadata_infrastructure(
        autonomous_exadata_infrastructure_id=autonomous_exadata_infrastructure_id,
        update_autonomous_exadata_infrastructures_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_autonomous_exadata_infrastructure') and callable(getattr(client, 'get_autonomous_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_autonomous_exadata_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@backup_destination_group.command(name=cli_util.override('db.update_backup_destination.command_name', 'update'), help=u"""If no database is associated with the backup destination: - For a RECOVERY_APPLIANCE backup destination, updates the connection string and/or the list of VPC users. - For an NFS backup destination, updates the NFS location.""")
@cli_util.option('--backup-destination-id', required=True, help=u"""The [OCID] of the backup destination.""")
@cli_util.option('--vpc-users', type=custom_types.CLI_COMPLEX_TYPE, help=u"""For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-string', help=u"""For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.""")
@cli_util.option('--local-mount-point-path', help=u"""The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'vpc-users': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vpc-users': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'BackupDestination'})
@cli_util.wrap_exceptions
def update_backup_destination(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, backup_destination_id, vpc_users, connection_string, local_mount_point_path, freeform_tags, defined_tags, if_match):

    if isinstance(backup_destination_id, six.string_types) and len(backup_destination_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-destination-id cannot be whitespace or empty string')
    if not force:
        if vpc_users or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vpc-users and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if vpc_users is not None:
        details['vpcUsers'] = cli_util.parse_json_parameter("vpc_users", vpc_users)

    if connection_string is not None:
        details['connectionString'] = connection_string

    if local_mount_point_path is not None:
        details['localMountPointPath'] = local_mount_point_path

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_backup_destination(
        backup_destination_id=backup_destination_id,
        update_backup_destination_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_backup_destination') and callable(getattr(client, 'get_backup_destination')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_backup_destination(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_group.command(name=cli_util.override('db.update_database.command_name', 'update'), help=u"""Update a Database based on the request parameters you provide.""")
@cli_util.option('--database-id', required=True, help=u"""The database [OCID].""")
@cli_util.option('--db-backup-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-backup-config': {'module': 'database', 'class': 'DbBackupConfig'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'Database'})
@cli_util.wrap_exceptions
def update_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_id, db_backup_config, freeform_tags, defined_tags, if_match):

    if isinstance(database_id, six.string_types) and len(database_id.strip()) == 0:
        raise click.UsageError('Parameter --database-id cannot be whitespace or empty string')
    if not force:
        if db_backup_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to db-backup-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if db_backup_config is not None:
        details['dbBackupConfig'] = cli_util.parse_json_parameter("db_backup_config", db_backup_config)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_database(
        database_id=database_id,
        update_database_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_database') and callable(getattr(client, 'get_database')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_database(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_home_group.command(name=cli_util.override('db.update_db_home.command_name', 'update'), help=u"""Patches the specified dbHome.""")
@cli_util.option('--db-home-id', required=True, help=u"""The database home [OCID].""")
@cli_util.option('--db-version', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-version': {'module': 'database', 'class': 'PatchDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-version': {'module': 'database', 'class': 'PatchDetails'}}, output_type={'module': 'database', 'class': 'DbHome'})
@cli_util.wrap_exceptions
def update_db_home(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_home_id, db_version, if_match):

    if isinstance(db_home_id, six.string_types) and len(db_home_id.strip()) == 0:
        raise click.UsageError('Parameter --db-home-id cannot be whitespace or empty string')
    if not force:
        if db_version:
            if not click.confirm("WARNING: Updates to db-version will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if db_version is not None:
        details['dbVersion'] = cli_util.parse_json_parameter("db_version", db_version)

    client = cli_util.build_client('database', ctx)
    result = client.update_db_home(
        db_home_id=db_home_id,
        update_db_home_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_home') and callable(getattr(client, 'get_db_home')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_home(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.update_db_system.command_name', 'update'), help=u"""Updates the properties of a DB system, such as the CPU core count.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The new number of CPU cores to set for the DB system. Not applicable for virtual machine DB systems.""")
@cli_util.option('--version', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssh-public-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined keys cannot exceed 40,000 characters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help=u"""The size, in gigabytes, to scale the attached storage up to for this virtual machine DB system. This value must be greater than current storage size. Note that the resulting total storage size attached will be greater than the amount requested to allow for REDO/RECO space and software volume. Applies only to virtual machine DB systems.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--backup-network-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the [OCIDs] of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules]. Applicable only to Exadata DB systems.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'version': {'module': 'database', 'class': 'PatchDetails'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'version': {'module': 'database', 'class': 'PatchDetails'}, 'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'database', 'class': 'list[string]'}, 'backup-network-nsg-ids': {'module': 'database', 'class': 'list[string]'}}, output_type={'module': 'database', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def update_db_system(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, cpu_core_count, version, ssh_public_keys, data_storage_size_in_gbs, freeform_tags, defined_tags, nsg_ids, backup_network_nsg_ids, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    if not force:
        if version or ssh_public_keys or freeform_tags or defined_tags or nsg_ids or backup_network_nsg_ids:
            if not click.confirm("WARNING: Updates to version and ssh-public-keys and freeform-tags and defined-tags and nsg-ids and backup-network-nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if version is not None:
        details['version'] = cli_util.parse_json_parameter("version", version)

    if ssh_public_keys is not None:
        details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)

    if data_storage_size_in_gbs is not None:
        details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if nsg_ids is not None:
        details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if backup_network_nsg_ids is not None:
        details['backupNetworkNsgIds'] = cli_util.parse_json_parameter("backup_network_nsg_ids", backup_network_nsg_ids)

    client = cli_util.build_client('database', ctx)
    result = client.update_db_system(
        db_system_id=db_system_id,
        update_db_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_db_system') and callable(getattr(client, 'get_db_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_db_system(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@exadata_infrastructure_group.command(name=cli_util.override('db.update_exadata_infrastructure.command_name', 'update'), help=u"""Updates the Exadata infrastructure.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--cloud-control-plane-server1', help=u"""The IP address for the first control plane server.""")
@cli_util.option('--cloud-control-plane-server2', help=u"""The IP address for the second control plane server.""")
@cli_util.option('--netmask', help=u"""The netmask for the control plane network.""")
@cli_util.option('--gateway', help=u"""The gateway for the control plane network.""")
@cli_util.option('--admin-network-cidr', help=u"""The CIDR block for the Exadata administration network.""")
@cli_util.option('--infini-band-network-cidr', help=u"""The CIDR block for the Exadata InfiniBand interconnect.""")
@cli_util.option('--corporate-proxy', help=u"""The corporate network proxy for access to the control plane network.""")
@cli_util.option('--dns-server', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ntp-server', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NTP server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-zone', help=u"""The time zone of the Exadata infrastructure. For details, see [Exadata Infrastructure Time Zones].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-server': {'module': 'database', 'class': 'list[string]'}, 'ntp-server': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-server': {'module': 'database', 'class': 'list[string]'}, 'ntp-server': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'ExadataInfrastructure'})
@cli_util.wrap_exceptions
def update_exadata_infrastructure(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, cloud_control_plane_server1, cloud_control_plane_server2, netmask, gateway, admin_network_cidr, infini_band_network_cidr, corporate_proxy, dns_server, ntp_server, time_zone, freeform_tags, defined_tags, if_match):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')
    if not force:
        if dns_server or ntp_server or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to dns-server and ntp-server and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if cloud_control_plane_server1 is not None:
        details['cloudControlPlaneServer1'] = cloud_control_plane_server1

    if cloud_control_plane_server2 is not None:
        details['cloudControlPlaneServer2'] = cloud_control_plane_server2

    if netmask is not None:
        details['netmask'] = netmask

    if gateway is not None:
        details['gateway'] = gateway

    if admin_network_cidr is not None:
        details['adminNetworkCIDR'] = admin_network_cidr

    if infini_band_network_cidr is not None:
        details['infiniBandNetworkCIDR'] = infini_band_network_cidr

    if corporate_proxy is not None:
        details['corporateProxy'] = corporate_proxy

    if dns_server is not None:
        details['dnsServer'] = cli_util.parse_json_parameter("dns_server", dns_server)

    if ntp_server is not None:
        details['ntpServer'] = cli_util.parse_json_parameter("ntp_server", ntp_server)

    if time_zone is not None:
        details['timeZone'] = time_zone

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_exadata_infrastructure(
        exadata_infrastructure_id=exadata_infrastructure_id,
        update_exadata_infrastructure_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_exadata_infrastructure') and callable(getattr(client, 'get_exadata_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_exadata_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db.update_exadata_iorm_config.command_name', 'update-exadata-iorm-config'), help=u"""Update `IORM` Settings for the requested Exadata DB System.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB system [OCID].""")
@cli_util.option('--objective', type=custom_types.CliCaseInsensitiveChoice(["LOW_LATENCY", "HIGH_THROUGHPUT", "BALANCED", "AUTO", "BASIC"]), help=u"""Value for the IORM objective Default is \"Auto\"""")
@cli_util.option('--db-plans', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of IORM Setting for all the database in this Exadata DB System

This option is a JSON list with items of type DbIormConfigUpdateDetail.  For documentation on dbIormConfigUpdateDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/database/20160918/datatypes/DbIormConfigUpdateDetail.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["BOOTSTRAPPING", "ENABLED", "DISABLED", "UPDATING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'db-plans': {'module': 'database', 'class': 'list[DbIormConfigUpdateDetail]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'db-plans': {'module': 'database', 'class': 'list[DbIormConfigUpdateDetail]'}}, output_type={'module': 'database', 'class': 'ExadataIormConfig'})
@cli_util.wrap_exceptions
def update_exadata_iorm_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, objective, db_plans, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    if not force:
        if db_plans:
            if not click.confirm("WARNING: Updates to db-plans will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if objective is not None:
        details['objective'] = objective

    if db_plans is not None:
        details['dbPlans'] = cli_util.parse_json_parameter("db_plans", db_plans)

    client = cli_util.build_client('database', ctx)
    result = client.update_exadata_iorm_config(
        db_system_id=db_system_id,
        exadata_iorm_config_update_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_exadata_iorm_config') and callable(getattr(client, 'get_exadata_iorm_config')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_exadata_iorm_config(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@maintenance_run_group.command(name=cli_util.override('db.update_maintenance_run.command_name', 'update'), help=u"""Updates the properties of a Maintenance Run, such as the state of a Maintenance Run.""")
@cli_util.option('--maintenance-run-id', required=True, help=u"""The Maintenance Run OCID.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""If set to false, skips the Maintenance Run.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'MaintenanceRun'})
@cli_util.wrap_exceptions
def update_maintenance_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, maintenance_run_id, is_enabled, if_match):

    if isinstance(maintenance_run_id, six.string_types) and len(maintenance_run_id.strip()) == 0:
        raise click.UsageError('Parameter --maintenance-run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    client = cli_util.build_client('database', ctx)
    result = client.update_maintenance_run(
        maintenance_run_id=maintenance_run_id,
        update_maintenance_run_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_maintenance_run') and callable(getattr(client, 'get_maintenance_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_maintenance_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_group.command(name=cli_util.override('db.update_vm_cluster.command_name', 'update'), help=u"""Updates the specified VM cluster.""")
@cli_util.option('--vm-cluster-id', required=True, help=u"""The VM cluster [OCID].""")
@cli_util.option('--cpu-core-count', type=click.INT, help=u"""The number of CPU cores to enable for the VM cluster.""")
@cli_util.option('--license-model', type=custom_types.CliCaseInsensitiveChoice(["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]), help=u"""The Oracle license model that applies to the VM cluster. The default is BRING_YOUR_OWN_LICENSE.""")
@cli_util.option('--ssh-public-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The public key portion of one or more key pairs used for SSH access to the VM cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ssh-public-keys': {'module': 'database', 'class': 'list[string]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'VmCluster'})
@cli_util.wrap_exceptions
def update_vm_cluster(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vm_cluster_id, cpu_core_count, license_model, ssh_public_keys, freeform_tags, defined_tags, if_match):

    if isinstance(vm_cluster_id, six.string_types) and len(vm_cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-id cannot be whitespace or empty string')
    if not force:
        if ssh_public_keys or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to ssh-public-keys and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if license_model is not None:
        details['licenseModel'] = license_model

    if ssh_public_keys is not None:
        details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_vm_cluster(
        vm_cluster_id=vm_cluster_id,
        update_vm_cluster_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster') and callable(getattr(client, 'get_vm_cluster')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vm_cluster(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.update_vm_cluster_network.command_name', 'update'), help=u"""Updates the specified VM cluster network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The VM cluster network [OCID].""")
@cli_util.option('--scans', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The SCAN details.

This option is a JSON list with items of type ScanDetails.  For documentation on ScanDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/database/20160918/datatypes/ScanDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dns', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of DNS server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ntp', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of NTP server IP addresses. Maximum of 3 allowed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vm-networks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Details of the client and backup networks.

This option is a JSON list with items of type VmNetworkDetails.  For documentation on VmNetworkDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/database/20160918/datatypes/VmNetworkDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'scans': {'module': 'database', 'class': 'list[ScanDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'vm-networks': {'module': 'database', 'class': 'list[VmNetworkDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scans': {'module': 'database', 'class': 'list[ScanDetails]'}, 'dns': {'module': 'database', 'class': 'list[string]'}, 'ntp': {'module': 'database', 'class': 'list[string]'}, 'vm-networks': {'module': 'database', 'class': 'list[VmNetworkDetails]'}, 'freeform-tags': {'module': 'database', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'database', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'database', 'class': 'VmClusterNetwork'})
@cli_util.wrap_exceptions
def update_vm_cluster_network(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, vm_cluster_network_id, scans, dns, ntp, vm_networks, freeform_tags, defined_tags, if_match):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    if isinstance(vm_cluster_network_id, six.string_types) and len(vm_cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-network-id cannot be whitespace or empty string')
    if not force:
        if scans or dns or ntp or vm_networks or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to scans and dns and ntp and vm-networks and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if scans is not None:
        details['scans'] = cli_util.parse_json_parameter("scans", scans)

    if dns is not None:
        details['dns'] = cli_util.parse_json_parameter("dns", dns)

    if ntp is not None:
        details['ntp'] = cli_util.parse_json_parameter("ntp", ntp)

    if vm_networks is not None:
        details['vmNetworks'] = cli_util.parse_json_parameter("vm_networks", vm_networks)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('database', ctx)
    result = client.update_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_id=vm_cluster_network_id,
        update_vm_cluster_network_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster_network') and callable(getattr(client, 'get_vm_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vm_cluster_network(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@vm_cluster_network_group.command(name=cli_util.override('db.validate_vm_cluster_network.command_name', 'validate'), help=u"""Validates the specified VM cluster network.""")
@cli_util.option('--exadata-infrastructure-id', required=True, help=u"""The Exadata infrastructure [OCID].""")
@cli_util.option('--vm-cluster-network-id', required=True, help=u"""The VM cluster network [OCID].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database', 'class': 'VmClusterNetwork'})
@cli_util.wrap_exceptions
def validate_vm_cluster_network(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_infrastructure_id, vm_cluster_network_id):

    if isinstance(exadata_infrastructure_id, six.string_types) and len(exadata_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-infrastructure-id cannot be whitespace or empty string')

    if isinstance(vm_cluster_network_id, six.string_types) and len(vm_cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --vm-cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database', ctx)
    result = client.validate_vm_cluster_network(
        exadata_infrastructure_id=exadata_infrastructure_id,
        vm_cluster_network_id=vm_cluster_network_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_vm_cluster_network') and callable(getattr(client, 'get_vm_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vm_cluster_network(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
