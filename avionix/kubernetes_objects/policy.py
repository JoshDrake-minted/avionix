from typing import List, Optional

from avionix.kubernetes_objects.base_objects import KubernetesBaseObject
from avionix.kubernetes_objects.core import SELinuxOptions
from avionix.kubernetes_objects.meta import (DeleteOptions, LabelSelector,
                                             ListMeta, ObjectMeta)
from avionix.yaml.yaml_handling import HelmYaml


class PodDisruptionBudgetSpec(HelmYaml):
    """
    :param max_unavailable:An eviction is allowed if at most "maxUnavailable" pods \
        selected by "selector" are unavailable after the eviction, i.e. even in \
        absence of the evicted pod. For example, one can prevent all voluntary \
        evictions by specifying 0. This is a mutually exclusive setting with \
        "minAvailable".
    :type max_unavailable: str
    :param min_available:An eviction is allowed if at least "minAvailable" pods \
        selected by "selector" will still be available after the eviction, i.e. even \
        in the absence of the evicted pod.  So for example you can prevent all \
        voluntary evictions by specifying "100%".
    :type min_available: str
    :param selector:Label query over pods whose evictions are managed by the \
        disruption budget.
    :type selector: LabelSelector
    """

    def __init__(
        self, max_unavailable: str, min_available: str, selector: LabelSelector
    ):
        self.maxUnavailable = max_unavailable
        self.minAvailable = min_available
        self.selector = selector


class PodDisruptionBudget(KubernetesBaseObject):
    """
    :param metadata:None
    :type metadata: ObjectMeta
    :param spec:Specification of the desired behavior of the PodDisruptionBudget.
    :type spec: PodDisruptionBudgetSpec
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ObjectMeta,
        spec: PodDisruptionBudgetSpec,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.spec = spec


class PodDisruptionBudgetList(KubernetesBaseObject):
    """
    :param metadata:None
    :type metadata: ListMeta
    :param items:None
    :type items: List[PodDisruptionBudget]
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ListMeta,
        items: List[PodDisruptionBudget],
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.items = items


class AllowedHostPath(HelmYaml):
    """
    :param path_prefix:pathPrefix is the path prefix that the host volume must match. \
        It does not support `*`. Trailing slashes are trimmed when validating the path \
        prefix with a host path.  Examples: `/foo` would allow `/foo`, `/foo/` and \
        `/foo/bar` `/foo` would not allow `/food` or `/etc/foo`
    :type path_prefix: str
    :param read_only:when set to true, will allow host volumes matching the pathPrefix \
        only if all volume mounts are readOnly.
    :type read_only: bool
    """

    def __init__(self, path_prefix: str, read_only: bool):
        self.pathPrefix = path_prefix
        self.readOnly = read_only


class HostPortRange(HelmYaml):
    """
    :param max:max is the end of the range, inclusive.
    :type max: int
    :param min:min is the start of the range, inclusive.
    :type min: int
    """

    def __init__(self, max: int, min: int):
        self.max = max
        self.min = min


class RuntimeClassStrategyOptions(HelmYaml):
    """
    :param allowed_runtime_class_names:allowedRuntimeClassNames is a whitelist of \
        RuntimeClass names that may be specified on a pod. A value of "*" means that \
        any RuntimeClass name is allowed, and must be the only item in the list. An \
        empty list requires the RuntimeClassName field to be unset.
    :type allowed_runtime_class_names: List[str]
    :param default_runtime_class_name:defaultRuntimeClassName is the default \
        RuntimeClassName to set on the pod. The default MUST be allowed by the \
        allowedRuntimeClassNames list. A value of nil does not mutate the Pod.
    :type default_runtime_class_name: str
    """

    def __init__(
        self, allowed_runtime_class_names: List[str], default_runtime_class_name: str
    ):
        self.allowedRuntimeClassNames = allowed_runtime_class_names
        self.defaultRuntimeClassName = default_runtime_class_name


class AllowedFlexVolume(HelmYaml):
    """
    :param driver:driver is the name of the Flexvolume driver.
    :type driver: str
    """

    def __init__(self, driver: str):
        self.driver = driver


class IDRange(HelmYaml):
    """
    :param max:max is the end of the range, inclusive.
    :type max: int
    :param min:min is the start of the range, inclusive.
    :type min: int
    """

    def __init__(self, max: int, min: int):
        self.max = max
        self.min = min


class RunAsGroupStrategyOptions(HelmYaml):
    """
    :param ranges:ranges are the allowed ranges of gids that may be used. If you would \
        like to force a single gid then supply a single range with the same start and \
        end. Required for MustRunAs.
    :type ranges: List[IDRange]
    :param rule:rule is the strategy that will dictate the allowable RunAsGroup values \
        that may be set.
    :type rule: str
    """

    def __init__(self, ranges: List[IDRange], rule: str):
        self.ranges = ranges
        self.rule = rule


class RunAsUserStrategyOptions(HelmYaml):
    """
    :param ranges:ranges are the allowed ranges of uids that may be used. If you would \
        like to force a single uid then supply a single range with the same start and \
        end. Required for MustRunAs.
    :type ranges: List[IDRange]
    :param rule:rule is the strategy that will dictate the allowable RunAsUser values \
        that may be set.
    :type rule: str
    """

    def __init__(self, ranges: List[IDRange], rule: str):
        self.ranges = ranges
        self.rule = rule


class AllowedCSIDriver(HelmYaml):
    """
    :param name:Name is the registered name of the CSI driver
    :type name: str
    """

    def __init__(self, name: str):
        self.name = name


class FSGroupStrategyOptions(HelmYaml):
    """
    :param ranges:ranges are the allowed ranges of fs groups.  If you would like to \
        force a single fs group then supply a single range with the same start and \
        end. Required for MustRunAs.
    :type ranges: List[IDRange]
    :param rule:rule is the strategy that will dictate what FSGroup is used in the \
        SecurityContext.
    :type rule: str
    """

    def __init__(self, ranges: List[IDRange], rule: str):
        self.ranges = ranges
        self.rule = rule


class SupplementalGroupsStrategyOptions(HelmYaml):
    """
    :param ranges:ranges are the allowed ranges of supplemental groups.  If you would \
        like to force a single supplemental group then supply a single range with the \
        same start and end. Required for MustRunAs.
    :type ranges: List[IDRange]
    :param rule:rule is the strategy that will dictate what supplemental groups is \
        used in the SecurityContext.
    :type rule: str
    """

    def __init__(self, ranges: List[IDRange], rule: str):
        self.ranges = ranges
        self.rule = rule


class SELinuxStrategyOptions(HelmYaml):
    """
    :param rule:rule is the strategy that will dictate the allowable labels that may \
        be set.
    :type rule: str
    :param se_linux_options:seLinuxOptions required to run as; required for MustRunAs \
        More info: \
        https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
    :type se_linux_options: SELinuxOptions
    """

    def __init__(self, rule: str, se_linux_options: SELinuxOptions):
        self.rule = rule
        self.seLinuxOptions = se_linux_options


class PodSecurityPolicySpec(HelmYaml):
    """
    :param allowed_csidrivers:AllowedCSIDrivers is a whitelist of inline CSI drivers \
        that must be explicitly set to be embedded within a pod spec. An empty value \
        indicates that any CSI driver can be used for inline ephemeral volumes. This \
        is an alpha field, and is only honored if the API server enables the \
        CSIInlineVolume feature gate.
    :type allowed_csidrivers: List[AllowedCSIDriver]
    :param allowed_capabilities:allowedCapabilities is a list of capabilities that can \
        be requested to add to the container. Capabilities in this field may be added \
        at the pod author's discretion. You must not list a capability in both \
        allowedCapabilities and requiredDropCapabilities.
    :type allowed_capabilities: List[str]
    :param allowed_flex_volumes:allowedFlexVolumes is a whitelist of allowed \
        Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This \
        parameter is effective only when the usage of the Flexvolumes is allowed in \
        the "volumes" field.
    :type allowed_flex_volumes: List[AllowedFlexVolume]
    :param allowed_host_paths:allowedHostPaths is a white list of allowed host paths. \
        Empty indicates that all host paths may be used.
    :type allowed_host_paths: List[AllowedHostPath]
    :param allowed_proc_mount_types:AllowedProcMountTypes is a whitelist of allowed \
        ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may \
        be used. This requires the ProcMountType feature flag to be enabled.
    :type allowed_proc_mount_types: List[str]
    :param default_add_capabilities:defaultAddCapabilities is the default set of \
        capabilities that will be added to the container unless the pod spec \
        specifically drops the capability.  You may not list a capability in both \
        defaultAddCapabilities and requiredDropCapabilities. Capabilities added here \
        are implicitly allowed, and need not be included in the allowedCapabilities \
        list.
    :type default_add_capabilities: List[str]
    :param default_allow_privilege_escalation:defaultAllowPrivilegeEscalation controls \
        the default setting for whether a process can gain more privileges than its \
        parent process.
    :type default_allow_privilege_escalation: bool
    :param fs_group:fsGroup is the strategy that will dictate what fs group is used by \
        the SecurityContext.
    :type fs_group: FSGroupStrategyOptions
    :param host_ipc:hostIPC determines if the policy allows the use of HostIPC in the \
        pod spec.
    :type host_ipc: bool
    :param host_pid:hostPID determines if the policy allows the use of HostPID in the \
        pod spec.
    :type host_pid: bool
    :param host_ports:hostPorts determines which host port ranges are allowed to be \
        exposed.
    :type host_ports: List[HostPortRange]
    :param privileged:privileged determines if a pod can request to be run as \
        privileged.
    :type privileged: bool
    :param read_only_root_filesystem:readOnlyRootFilesystem when set to true will \
        force containers to run with a read only root file system.  If the container \
        specifically requests to run with a non-read only root file system the PSP \
        should deny the pod. If set to false the container may run with a read only \
        root file system if it wishes but it will not be forced to.
    :type read_only_root_filesystem: bool
    :param required_drop_capabilities:requiredDropCapabilities are the capabilities \
        that will be dropped from the container.  These are required to be dropped and \
        cannot be added.
    :type required_drop_capabilities: List[str]
    :param run_as_group:RunAsGroup is the strategy that will dictate the allowable \
        RunAsGroup values that may be set. If this field is omitted, the pod's \
        RunAsGroup can take any value. This field requires the RunAsGroup feature gate \
        to be enabled.
    :type run_as_group: RunAsGroupStrategyOptions
    :param run_as_user:runAsUser is the strategy that will dictate the allowable \
        RunAsUser values that may be set.
    :type run_as_user: RunAsUserStrategyOptions
    :param runtime_class:runtimeClass is the strategy that will dictate the allowable \
        RuntimeClasses for a pod. If this field is omitted, the pod's runtimeClassName \
        field is unrestricted. Enforcement of this field depends on the RuntimeClass \
        feature gate being enabled.
    :type runtime_class: RuntimeClassStrategyOptions
    :param se_linux:seLinux is the strategy that will dictate the allowable labels \
        that may be set.
    :type se_linux: SELinuxStrategyOptions
    :param supplemental_groups:supplementalGroups is the strategy that will dictate \
        what supplemental groups are used by the SecurityContext.
    :type supplemental_groups: SupplementalGroupsStrategyOptions
    :param allow_privilege_escalation:allowPrivilegeEscalation determines if a pod can \
        request to allow privilege escalation. If unspecified, defaults to true.
    :type allow_privilege_escalation: Optional[bool]
    :param allowed_unsafe_sysctls:allowedUnsafeSysctls is a list of explicitly allowed \
        unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or \
        ends in "*" in which case it is considered as a prefix of allowed sysctls. \
        Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all \
        allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. "foo/*" \
        allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", \
        etc.
    :type allowed_unsafe_sysctls: Optional[List[str]]
    :param forbidden_sysctls:forbiddenSysctls is a list of explicitly forbidden \
        sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \
        "*" in which case it is considered as a prefix of forbidden sysctls. Single * \
        means all sysctls are forbidden.  Examples: e.g. "foo/*" forbids "foo/bar", \
        "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.
    :type forbidden_sysctls: Optional[List[str]]
    :param host_network:hostNetwork determines if the policy allows the use of \
        HostNetwork in the pod spec.
    :type host_network: Optional[bool]
    :param volumes:volumes is a white list of allowed volume plugins. Empty indicates \
        that no volumes may be used. To allow all volumes you may use '\\*'.
    :type volumes: Optional[List[str]]
    """

    def __init__(
        self,
        allowed_csidrivers: List[AllowedCSIDriver],
        allowed_capabilities: List[str],
        allowed_flex_volumes: List[AllowedFlexVolume],
        allowed_host_paths: List[AllowedHostPath],
        allowed_proc_mount_types: List[str],
        default_add_capabilities: List[str],
        default_allow_privilege_escalation: bool,
        fs_group: FSGroupStrategyOptions,
        host_ipc: bool,
        host_pid: bool,
        host_ports: List[HostPortRange],
        privileged: bool,
        read_only_root_filesystem: bool,
        required_drop_capabilities: List[str],
        run_as_group: RunAsGroupStrategyOptions,
        run_as_user: RunAsUserStrategyOptions,
        runtime_class: RuntimeClassStrategyOptions,
        se_linux: SELinuxStrategyOptions,
        supplemental_groups: SupplementalGroupsStrategyOptions,
        allow_privilege_escalation: Optional[bool] = None,
        allowed_unsafe_sysctls: Optional[List[str]] = None,
        forbidden_sysctls: Optional[List[str]] = None,
        host_network: Optional[bool] = None,
        volumes: Optional[List[str]] = None,
    ):
        self.allowedCSIDrivers = allowed_csidrivers
        self.allowedCapabilities = allowed_capabilities
        self.allowedFlexVolumes = allowed_flex_volumes
        self.allowedHostPaths = allowed_host_paths
        self.allowedProcMountTypes = allowed_proc_mount_types
        self.defaultAddCapabilities = default_add_capabilities
        self.defaultAllowPrivilegeEscalation = default_allow_privilege_escalation
        self.fsGroup = fs_group
        self.hostIPC = host_ipc
        self.hostPID = host_pid
        self.hostPorts = host_ports
        self.privileged = privileged
        self.readOnlyRootFilesystem = read_only_root_filesystem
        self.requiredDropCapabilities = required_drop_capabilities
        self.runAsGroup = run_as_group
        self.runAsUser = run_as_user
        self.runtimeClass = runtime_class
        self.seLinux = se_linux
        self.supplementalGroups = supplemental_groups
        self.allowPrivilegeEscalation = allow_privilege_escalation
        self.allowedUnsafeSysctls = allowed_unsafe_sysctls
        self.forbiddenSysctls = forbidden_sysctls
        self.hostNetwork = host_network
        self.volumes = volumes


class Eviction(KubernetesBaseObject):
    """
    :param metadata:ObjectMeta describes the pod that is being evicted.
    :type metadata: ObjectMeta
    :param delete_options:DeleteOptions may be provided
    :type delete_options: DeleteOptions
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ObjectMeta,
        delete_options: DeleteOptions,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.deleteOptions = delete_options


class PodSecurityPolicy(KubernetesBaseObject):
    """
    :param metadata:Standard object's metadata. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa
    :type metadata: ObjectMeta
    :param spec:spec defines the policy enforced.
    :type spec: PodSecurityPolicySpec
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ObjectMeta,
        spec: PodSecurityPolicySpec,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.spec = spec


class PodSecurityPolicyList(KubernetesBaseObject):
    """
    :param metadata:Standard list metadata. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata  # noqa
    :type metadata: ListMeta
    :param items:items is a list of schema objects.
    :type items: List[PodSecurityPolicy]
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ListMeta,
        items: List[PodSecurityPolicy],
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.items = items
