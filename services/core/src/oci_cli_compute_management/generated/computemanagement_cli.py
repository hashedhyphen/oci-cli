# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.core.src.oci_cli_core.generated import core_service_cli


@click.command(cli_util.override('compute_management.compute_management_root_group.command_name', 'compute-management'), cls=CommandGroupWithAlias, help=cli_util.override('compute_management.compute_management_root_group.help', """API covering the [Networking](/iaas/Content/Network/Concepts/overview.htm),
[Compute](/iaas/Content/Compute/Concepts/computeoverview.htm), and
[Block Volume](/iaas/Content/Block/Concepts/overview.htm) services. Use this API
to manage resources such as virtual cloud networks (VCNs), compute instances, and
block storage volumes.
"""), short_help=cli_util.override('compute_management.compute_management_root_group.short_help', """Core Services API"""))
@cli_util.help_option_group
def compute_management_root_group():
    pass


@click.command(cli_util.override('compute_management.instance_pool_group.command_name', 'instance-pool'), cls=CommandGroupWithAlias, help="""An instance pool is a group of instances within the same region that are created based off of the same instance configuration. For more information about instance pools and instance configurations, see [Managing Compute Instances].""")
@cli_util.help_option_group
def instance_pool_group():
    pass


@click.command(cli_util.override('compute_management.instance_group.command_name', 'instance'), cls=CommandGroupWithAlias, help="""A compute host. The image used to launch the instance determines its operating system and other software. The shape specified during the launch process determines the number of CPUs and memory allocated to the instance. For more information, see [Overview of the Compute Service].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def instance_group():
    pass


@click.command(cli_util.override('compute_management.instance_configuration_group.command_name', 'instance-configuration'), cls=CommandGroupWithAlias, help="""An instance configuration is a template that defines the settings to use when creating Compute instances. For more information about instance configurations, see [Managing Compute Instances].""")
@cli_util.help_option_group
def instance_configuration_group():
    pass


@click.command(cli_util.override('compute_management.cluster_network_group.command_name', 'cluster-network'), cls=CommandGroupWithAlias, help="""Cluster Network""")
@cli_util.help_option_group
def cluster_network_group():
    pass


@click.command(cli_util.override('compute_management.instance_pool_load_balancer_attachment_group.command_name', 'instance-pool-load-balancer-attachment'), cls=CommandGroupWithAlias, help="""Represents a load balancer that is attached to an instance pool.""")
@cli_util.help_option_group
def instance_pool_load_balancer_attachment_group():
    pass


core_service_cli.core_service_group.add_command(compute_management_root_group)
compute_management_root_group.add_command(instance_pool_group)
compute_management_root_group.add_command(instance_group)
compute_management_root_group.add_command(instance_configuration_group)
compute_management_root_group.add_command(cluster_network_group)
compute_management_root_group.add_command(instance_pool_load_balancer_attachment_group)


@instance_pool_group.command(name=cli_util.override('compute_management.attach_load_balancer.command_name', 'attach'), help=u"""Attach a load balancer to the instance pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The OCID of the load balancer to attach to the instance pool.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set on the load balancer to add instances to.""")
@cli_util.option('--port', required=True, type=click.INT, help=u"""The port value to use when creating the backend set.""")
@cli_util.option('--vnic-selection', required=True, help=u"""Indicates which VNIC on each instance in the pool should be used to associate with the load balancer. Possible values are \"PrimaryVnic\" or the displayName of one of the secondary VNICs on the instance configuration that is associated with the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def attach_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, load_balancer_id, backend_set_name, port, vnic_selection, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['loadBalancerId'] = load_balancer_id
    details['backendSetName'] = backend_set_name
    details['port'] = port
    details['vnicSelection'] = vnic_selection

    client = cli_util.build_client('compute_management', ctx)
    result = client.attach_load_balancer(
        instance_pool_id=instance_pool_id,
        attach_load_balancer_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cluster_network_group.command(name=cli_util.override('compute_management.change_cluster_network_compartment.command_name', 'change-compartment'), help=u"""Change the compartment of a cluster network.""")
@cli_util.option('--cluster-network-id', required=True, help=u"""The OCID of the cluster network.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_cluster_network_compartment(ctx, from_json, cluster_network_id, compartment_id, if_match):

    if isinstance(cluster_network_id, six.string_types) and len(cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('compute_management', ctx)
    result = client.change_cluster_network_compartment(
        cluster_network_id=cluster_network_id,
        change_cluster_network_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_configuration_group.command(name=cli_util.override('compute_management.change_instance_configuration_compartment.command_name', 'change-compartment'), help=u"""Moves an instance configuration into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When you move an instance configuration to a different compartment, associated resources such as instance pools are not moved.

**Important:** Most of the properties for an existing instance configuration, including the compartment, cannot be modified after you create the instance configuration. Although you can move an instance configuration to a different compartment, you will not be able to use the instance configuration to manage instance pools in the new compartment. If you want to update an instance configuration to point to a different compartment, you should instead create a new instance configuration in the target compartment using [CreateInstanceConfiguration].""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the instance configuration to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_instance_configuration_compartment(ctx, from_json, instance_configuration_id, compartment_id, if_match):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('compute_management', ctx)
    result = client.change_instance_configuration_compartment(
        instance_configuration_id=instance_configuration_id,
        change_instance_configuration_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.change_instance_pool_compartment.command_name', 'change-compartment'), help=u"""Moves an instance pool into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When you move an instance pool to a different compartment, associated resources such as the instances in the pool, boot volumes, VNICs, and autoscaling configurations are not moved.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the instance pool to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_instance_pool_compartment(ctx, from_json, instance_pool_id, compartment_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id

    client = cli_util.build_client('compute_management', ctx)
    result = client.change_instance_pool_compartment(
        instance_pool_id=instance_pool_id,
        change_instance_pool_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_network_group.command(name=cli_util.override('compute_management.create_cluster_network.command_name', 'create'), help=u"""Create a cluster network.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the cluster network.""")
@cli_util.option('--instance-pools', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""the data to create the instance pools in the cluster network.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--placement-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""the placement data for the intance pools in the cluster network""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name.  Does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'instance-pools': {'module': 'core', 'class': 'list[CreateClusterNetworkInstancePoolDetails]'}, 'placement-configuration': {'module': 'core', 'class': 'ClusterNetworkPlacementConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'instance-pools': {'module': 'core', 'class': 'list[CreateClusterNetworkInstancePoolDetails]'}, 'placement-configuration': {'module': 'core', 'class': 'ClusterNetworkPlacementConfigurationDetails'}}, output_type={'module': 'core', 'class': 'ClusterNetwork'})
@cli_util.wrap_exceptions
def create_cluster_network(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, instance_pools, placement_configuration, defined_tags, display_name, freeform_tags):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['instancePools'] = cli_util.parse_json_parameter("instance_pools", instance_pools)
    details['placementConfiguration'] = cli_util.parse_json_parameter("placement_configuration", placement_configuration)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute_management', ctx)
    result = client.create_cluster_network(
        create_cluster_network_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cluster_network') and callable(getattr(client, 'get_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cluster_network(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_configuration_group.command(name=cli_util.override('compute_management.create_instance_configuration.command_name', 'create'), help=u"""Creates an instance configuration. An instance configuration is a template that defines the settings to use when creating Compute instances.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the instance configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the instance configuration.  Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "INSTANCE"]), help=u"""The source of the instance configuration. An instance configuration defines the settings to use when creating Compute instances, including details such as the base image, shape, and metadata. You can also specify the associated resources for the instance, such as block volume attachments and network configuration.

The following values are supported:

* `NONE`: Creates an instance configuration using the list of settings that you specify.

* `INSTANCE`: Creates an instance configuration using an existing instance as a template. The instance configuration uses the same settings as the instance.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConfiguration'})
@cli_util.wrap_exceptions
def create_instance_configuration(ctx, from_json, compartment_id, defined_tags, display_name, freeform_tags, source):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if source is not None:
        details['source'] = source

    client = cli_util.build_client('compute_management', ctx)
    result = client.create_instance_configuration(
        create_instance_configuration=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_configuration_group.command(name=cli_util.override('compute_management.create_instance_configuration_create_instance_configuration_details.command_name', 'create-instance-configuration-create-instance-configuration-details'), help=u"""Creates an instance configuration. An instance configuration is a template that defines the settings to use when creating Compute instances.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the instance configuration.""")
@cli_util.option('--instance-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the instance configuration.  Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'instance-details': {'module': 'core', 'class': 'InstanceConfigurationInstanceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'instance-details': {'module': 'core', 'class': 'InstanceConfigurationInstanceDetails'}}, output_type={'module': 'core', 'class': 'InstanceConfiguration'})
@cli_util.wrap_exceptions
def create_instance_configuration_create_instance_configuration_details(ctx, from_json, compartment_id, instance_details, defined_tags, display_name, freeform_tags):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['instanceDetails'] = cli_util.parse_json_parameter("instance_details", instance_details)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    details['source'] = 'NONE'

    client = cli_util.build_client('compute_management', ctx)
    result = client.create_instance_configuration(
        create_instance_configuration=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_configuration_group.command(name=cli_util.override('compute_management.create_instance_configuration_create_instance_configuration_from_instance_details.command_name', 'create-instance-configuration-create-instance-configuration-from-instance-details'), help=u"""Creates an instance configuration. An instance configuration is a template that defines the settings to use when creating Compute instances.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the instance configuration.""")
@cli_util.option('--instance-id', required=True, help=u"""The [OCID] of the instance to use to create the instance configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the instance configuration.  Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConfiguration'})
@cli_util.wrap_exceptions
def create_instance_configuration_create_instance_configuration_from_instance_details(ctx, from_json, compartment_id, instance_id, defined_tags, display_name, freeform_tags):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['instanceId'] = instance_id

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    details['source'] = 'INSTANCE'

    client = cli_util.build_client('compute_management', ctx)
    result = client.create_instance_configuration(
        create_instance_configuration=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.create_instance_pool.command_name', 'create'), help=u"""Create an instance pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the instance pool""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration associated with the instance pool.""")
@cli_util.option('--placement-configurations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The placement configurations for the instance pool. Provide one placement configuration for each availability domain.

To use the instance pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--size', required=True, type=click.INT, help=u"""The number of instances that should be in the instance pool.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the instance pool. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The load balancers to attach to the instance pool.

This option is a JSON list with items of type AttachLoadBalancerDetails.  For documentation on AttachLoadBalancerDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/AttachLoadBalancerDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'placement-configurations': {'module': 'core', 'class': 'list[CreateInstancePoolPlacementConfigurationDetails]'}, 'load-balancers': {'module': 'core', 'class': 'list[AttachLoadBalancerDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'placement-configurations': {'module': 'core', 'class': 'list[CreateInstancePoolPlacementConfigurationDetails]'}, 'load-balancers': {'module': 'core', 'class': 'list[AttachLoadBalancerDetails]'}}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def create_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, instance_configuration_id, placement_configurations, size, defined_tags, display_name, freeform_tags, load_balancers):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['instanceConfigurationId'] = instance_configuration_id
    details['placementConfigurations'] = cli_util.parse_json_parameter("placement_configurations", placement_configurations)
    details['size'] = size

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if load_balancers is not None:
        details['loadBalancers'] = cli_util.parse_json_parameter("load_balancers", load_balancers)

    client = cli_util.build_client('compute_management', ctx)
    result = client.create_instance_pool(
        create_instance_pool_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_configuration_group.command(name=cli_util.override('compute_management.delete_instance_configuration.command_name', 'delete'), help=u"""Deletes an instance configuration.""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_instance_configuration(ctx, from_json, instance_configuration_id, if_match):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.delete_instance_configuration(
        instance_configuration_id=instance_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.detach_load_balancer.command_name', 'detach'), help=u"""Detach a load balancer from the instance pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""The OCID of the load balancer to detach from the instance pool.""")
@cli_util.option('--backend-set-name', required=True, help=u"""The name of the backend set on the load balancer to detach from the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def detach_load_balancer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, load_balancer_id, backend_set_name, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['loadBalancerId'] = load_balancer_id
    details['backendSetName'] = backend_set_name

    client = cli_util.build_client('compute_management', ctx)
    result = client.detach_load_balancer(
        instance_pool_id=instance_pool_id,
        detach_load_balancer_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cluster_network_group.command(name=cli_util.override('compute_management.get_cluster_network.command_name', 'get'), help=u"""Gets the specified cluster network""")
@cli_util.option('--cluster-network-id', required=True, help=u"""The OCID of the cluster network.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'ClusterNetwork'})
@cli_util.wrap_exceptions
def get_cluster_network(ctx, from_json, cluster_network_id):

    if isinstance(cluster_network_id, six.string_types) and len(cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('compute_management', ctx)
    result = client.get_cluster_network(
        cluster_network_id=cluster_network_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_configuration_group.command(name=cli_util.override('compute_management.get_instance_configuration.command_name', 'get'), help=u"""Gets the specified instance configuration""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstanceConfiguration'})
@cli_util.wrap_exceptions
def get_instance_configuration(ctx, from_json, instance_configuration_id):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('compute_management', ctx)
    result = client.get_instance_configuration(
        instance_configuration_id=instance_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.get_instance_pool.command_name', 'get'), help=u"""Gets the specified instance pool""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def get_instance_pool(ctx, from_json, instance_pool_id):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('compute_management', ctx)
    result = client.get_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_load_balancer_attachment_group.command(name=cli_util.override('compute_management.get_instance_pool_load_balancer_attachment.command_name', 'get'), help=u"""Gets information about a load balancer that is attached to the specified instance pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--instance-pool-load-balancer-attachment-id', required=True, help=u"""The OCID of the load balancer attachment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePoolLoadBalancerAttachment'})
@cli_util.wrap_exceptions
def get_instance_pool_load_balancer_attachment(ctx, from_json, instance_pool_id, instance_pool_load_balancer_attachment_id):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    if isinstance(instance_pool_load_balancer_attachment_id, six.string_types) and len(instance_pool_load_balancer_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-load-balancer-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('compute_management', ctx)
    result = client.get_instance_pool_load_balancer_attachment(
        instance_pool_id=instance_pool_id,
        instance_pool_load_balancer_attachment_id=instance_pool_load_balancer_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute_management.launch_instance_configuration.command_name', 'launch-instance-configuration'), help=u"""Launches an instance from an instance configuration.

If the instance configuration does not include all of the parameters that are required to launch an instance, such as the availability domain and subnet ID, you must provide these parameters when you launch an instance from the instance configuration. For more information, see the [InstanceConfiguration] resource.""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@cli_util.option('--instance-type', required=True, help=u"""The type of instance details. Supported instanceType is compute""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance_configuration(ctx, from_json, instance_configuration_id, instance_type):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['instanceType'] = instance_type

    client = cli_util.build_client('compute_management', ctx)
    result = client.launch_instance_configuration(
        instance_configuration_id=instance_configuration_id,
        instance_configuration=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute_management.launch_instance_configuration_compute_instance_details.command_name', 'launch-instance-configuration-compute-instance-details'), help=u"""Launches an instance from an instance configuration.

If the instance configuration does not include all of the parameters that are required to launch an instance, such as the availability domain and subnet ID, you must provide these parameters when you launch an instance from the instance configuration. For more information, see the [InstanceConfiguration] resource.""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@cli_util.option('--block-volumes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type InstanceConfigurationBlockVolumeDetails.  For documentation on InstanceConfigurationBlockVolumeDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/InstanceConfigurationBlockVolumeDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--launch-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secondary-vnics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type InstanceConfigurationAttachVnicDetails.  For documentation on InstanceConfigurationAttachVnicDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/InstanceConfigurationAttachVnicDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'block-volumes': {'module': 'core', 'class': 'list[InstanceConfigurationBlockVolumeDetails]'}, 'launch-details': {'module': 'core', 'class': 'InstanceConfigurationLaunchInstanceDetails'}, 'secondary-vnics': {'module': 'core', 'class': 'list[InstanceConfigurationAttachVnicDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'block-volumes': {'module': 'core', 'class': 'list[InstanceConfigurationBlockVolumeDetails]'}, 'launch-details': {'module': 'core', 'class': 'InstanceConfigurationLaunchInstanceDetails'}, 'secondary-vnics': {'module': 'core', 'class': 'list[InstanceConfigurationAttachVnicDetails]'}}, output_type={'module': 'core', 'class': 'Instance'})
@cli_util.wrap_exceptions
def launch_instance_configuration_compute_instance_details(ctx, from_json, instance_configuration_id, block_volumes, launch_details, secondary_vnics):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}

    if block_volumes is not None:
        details['blockVolumes'] = cli_util.parse_json_parameter("block_volumes", block_volumes)

    if launch_details is not None:
        details['launchDetails'] = cli_util.parse_json_parameter("launch_details", launch_details)

    if secondary_vnics is not None:
        details['secondaryVnics'] = cli_util.parse_json_parameter("secondary_vnics", secondary_vnics)

    details['instanceType'] = 'compute'

    client = cli_util.build_client('compute_management', ctx)
    result = client.launch_instance_configuration(
        instance_configuration_id=instance_configuration_id,
        instance_configuration=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_network_group.command(name=cli_util.override('compute_management.list_cluster_network_instances.command_name', 'list-cluster-network-instances'), help=u"""List the instances in the specified cluster network.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--cluster-network-id', required=True, help=u"""The OCID of the cluster network.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InstanceSummary]'})
@cli_util.wrap_exceptions
def list_cluster_network_instances(ctx, from_json, all_pages, page_size, compartment_id, cluster_network_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(cluster_network_id, six.string_types) and len(cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('compute_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cluster_network_instances,
            compartment_id=compartment_id,
            cluster_network_id=cluster_network_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cluster_network_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            cluster_network_id=cluster_network_id,
            **kwargs
        )
    else:
        result = client.list_cluster_network_instances(
            compartment_id=compartment_id,
            cluster_network_id=cluster_network_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cluster_network_group.command(name=cli_util.override('compute_management.list_cluster_networks.command_name', 'list'), help=u"""Lists the cluster networks in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[ClusterNetworkSummary]'})
@cli_util.wrap_exceptions
def list_cluster_networks(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('compute_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cluster_networks,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cluster_networks,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cluster_networks(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_configuration_group.command(name=cli_util.override('compute_management.list_instance_configurations.command_name', 'list'), help=u"""Lists the instance configurations in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InstanceConfigurationSummary]'})
@cli_util.wrap_exceptions
def list_instance_configurations(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

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
    client = cli_util.build_client('compute_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_configurations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_configurations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_instance_configurations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_group.command(name=cli_util.override('compute_management.list_instance_pool_instances.command_name', 'list-instance-pool-instances'), help=u"""List the instances in the specified instance pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InstanceSummary]'})
@cli_util.wrap_exceptions
def list_instance_pool_instances(ctx, from_json, all_pages, page_size, compartment_id, instance_pool_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('compute_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_pool_instances,
            compartment_id=compartment_id,
            instance_pool_id=instance_pool_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_pool_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            instance_pool_id=instance_pool_id,
            **kwargs
        )
    else:
        result = client.list_instance_pool_instances(
            compartment_id=compartment_id,
            instance_pool_id=instance_pool_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.list_instance_pools.command_name', 'list'), help=u"""Lists the instance pools in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[InstancePoolSummary]'})
@cli_util.wrap_exceptions
def list_instance_pools(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('compute_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_instance_pools,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_instance_pools,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_instance_pools(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.reset_instance_pool.command_name', 'reset'), help=u"""Performs the reset (power off and power on) action on the specified instance pool, which performs the action on all the instances in the pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def reset_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.reset_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_pool_group.command(name=cli_util.override('compute_management.softreset_instance_pool.command_name', 'softreset'), help=u"""Performs the softreset (ACPI shutdown and power on) action on the specified instance pool, which performs the action on all the instances in the pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def softreset_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.softreset_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_pool_group.command(name=cli_util.override('compute_management.start_instance_pool.command_name', 'start'), help=u"""Performs the start (power on) action on the specified instance pool, which performs the action on all the instances in the pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def start_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.start_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_pool_group.command(name=cli_util.override('compute_management.stop_instance_pool.command_name', 'stop'), help=u"""Performs the stop (power off) action on the specified instance pool, which performs the action on all the instances in the pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def stop_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.stop_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cluster_network_group.command(name=cli_util.override('compute_management.terminate_cluster_network.command_name', 'terminate'), help=u"""Terminate the specified cluster network.""")
@cli_util.option('--cluster-network-id', required=True, help=u"""The OCID of the cluster network.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_cluster_network(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_network_id, if_match):

    if isinstance(cluster_network_id, six.string_types) and len(cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-network-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.terminate_cluster_network(
        cluster_network_id=cluster_network_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cluster_network') and callable(getattr(client, 'get_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_cluster_network(cluster_network_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@instance_pool_group.command(name=cli_util.override('compute_management.terminate_instance_pool.command_name', 'terminate'), help=u"""Terminate the specified instance pool.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def terminate_instance_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('compute_management', ctx)
    result = client.terminate_instance_pool(
        instance_pool_id=instance_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_instance_pool(instance_pool_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@cluster_network_group.command(name=cli_util.override('compute_management.update_cluster_network.command_name', 'update'), help=u"""Update the specified cluster network. The OCID of the cluster network remains the same.""")
@cli_util.option('--cluster-network-id', required=True, help=u"""The OCID of the cluster network.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The user-friendly name.  Does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'ClusterNetwork'})
@cli_util.wrap_exceptions
def update_cluster_network(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_network_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(cluster_network_id, six.string_types) and len(cluster_network_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-network-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute_management', ctx)
    result = client.update_cluster_network(
        cluster_network_id=cluster_network_id,
        update_cluster_network_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_cluster_network') and callable(getattr(client, 'get_cluster_network')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_cluster_network(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@instance_configuration_group.command(name=cli_util.override('compute_management.update_instance_configuration.command_name', 'update'), help=u"""Updates the free-form tags, defined tags, and display name of an instance configuration.""")
@cli_util.option('--instance-configuration-id', required=True, help=u"""The OCID of the instance configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

Example: `My instance configuration`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}}, output_type={'module': 'core', 'class': 'InstanceConfiguration'})
@cli_util.wrap_exceptions
def update_instance_configuration(ctx, from_json, force, instance_configuration_id, defined_tags, display_name, freeform_tags, if_match):

    if isinstance(instance_configuration_id, six.string_types) and len(instance_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-configuration-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('compute_management', ctx)
    result = client.update_instance_configuration(
        instance_configuration_id=instance_configuration_id,
        update_instance_configuration_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@instance_pool_group.command(name=cli_util.override('compute_management.update_instance_pool.command_name', 'update'), help=u"""Update the specified instance pool. The OCID of the instance pool remains the same.""")
@cli_util.option('--instance-pool-id', required=True, help=u"""The OCID of the instance pool.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the instance pool. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--instance-configuration-id', help=u"""The OCID of the instance configuration associated with the instance pool.""")
@cli_util.option('--placement-configurations', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The placement configurations for the instance pool. Provide one placement configuration for each availability domain.

To use the instance pool with a regional subnet, provide a placement configuration for each availability domain, and include the regional subnet in each placement configuration.

This option is a JSON list with items of type UpdateInstancePoolPlacementConfigurationDetails.  For documentation on UpdateInstancePoolPlacementConfigurationDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/iaas/20160918/datatypes/UpdateInstancePoolPlacementConfigurationDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--size', type=click.INT, help=u"""The number of instances that should be in the instance pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "SCALING", "STARTING", "STOPPING", "TERMINATING", "STOPPED", "TERMINATED", "RUNNING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'placement-configurations': {'module': 'core', 'class': 'list[UpdateInstancePoolPlacementConfigurationDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'core', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'core', 'class': 'dict(str, string)'}, 'placement-configurations': {'module': 'core', 'class': 'list[UpdateInstancePoolPlacementConfigurationDetails]'}}, output_type={'module': 'core', 'class': 'InstancePool'})
@cli_util.wrap_exceptions
def update_instance_pool(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, instance_pool_id, defined_tags, display_name, freeform_tags, instance_configuration_id, placement_configurations, size, if_match):

    if isinstance(instance_pool_id, six.string_types) and len(instance_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --instance-pool-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or placement_configurations:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and placement-configurations will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if instance_configuration_id is not None:
        details['instanceConfigurationId'] = instance_configuration_id

    if placement_configurations is not None:
        details['placementConfigurations'] = cli_util.parse_json_parameter("placement_configurations", placement_configurations)

    if size is not None:
        details['size'] = size

    client = cli_util.build_client('compute_management', ctx)
    result = client.update_instance_pool(
        instance_pool_id=instance_pool_id,
        update_instance_pool_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_instance_pool') and callable(getattr(client, 'get_instance_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_instance_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
