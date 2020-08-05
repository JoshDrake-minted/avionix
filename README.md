# Avionix
Helm is a very useful tool that facilitates infrastructure releases to kubernetes. It's 
interface is written entirely in yaml which makes it hard to use and also has
 created a need for code to be repeated in many cases. The goal of avionix is to
  create an object oriented interface to make helm easy to use and reduce the
   repetition of code when possible.
   
# Installation

```bash
pip install avionix
```

# Usage

With avionix you can, build with the typical kubernetes components

## Simple Example

For example for a deployment:
```python
from avionix import ChartBuilder, ChartInfo, ObjectMeta
from avionix.kubernetes_objects.core import (
    PodSpec,
    LabelSelector,
    Container,
    ContainerPort,
    EnvVar,
)
from avionix.kubernetes_objects.apps import Deployment, DeploymentSpec, PodTemplateSpec

container = Container(
    name=f"test-container",
    image="k8s.gcr.io/echoserver:1.4",
    env=[EnvVar("test", "test-value")],
    ports=[ContainerPort(8080)],
)

deployment = Deployment(
    metadata=ObjectMeta(name=f"test-deployment", labels={"app": "my_app"}),
    spec=DeploymentSpec(
        replicas=1,
        template=PodTemplateSpec(
            ObjectMeta(labels={"app": "my_app"}),
            spec=PodSpec(containers=[container]),
        ),
        selector=LabelSelector(match_labels={"app": "my_app"}),
    ),
)

builder = ChartBuilder(
    ChartInfo(api_version="3.2.4", name="test", version="0.1.0", app_version="v1"),
    [deployment],
)
```
from there you either do 
```python
builder.install_chart()
```
if you want to install the chart directly and let avionix handle it
or
you can use 
```python
builder.generate_chart()
```
to view the chart.

Additionally there are methods for upgrade and uninstall charts.
These are all directly equivalent to the helm commands.

## Inheritance

The real power of avionix comes from it being object oriented. The one thing that
 helm is missing that avionix has is inheritance.
```python
from typing import List, Optional

from my_package import (
    AirflowLogVolumeGroup,
    AirflowOptions,
    RedisOptions,
    SqlOptions,
    ValueOrchestrator,
    AirflowDagVolumeGroup,
    ExternalStorageVolumeGroup,
)

from avionix.kubernetes_objects.core import (
    Container,
    ContainerPort,
    EnvFromSource,
    EnvVar,
    Probe,
    SecretEnvSource,
    HTTPGetAction,
)


class AvionixAirflowProbe(Probe):
    def __init__(self, path: str, port: int, host: Optional[str] = None):
        super().__init__(http_get=HTTPGetAction(path=path, port=port, host=host))


class CoreEnvVar(EnvVar):
    def __init__(self, name: str, value):
        super().__init__("AIRFLOW__CORE__" + name, value)


class AirflowContainer(Container):
    def __init__(
        self,
        name: str,
        sql_options: SqlOptions,
        redis_options: RedisOptions,
        airflow_options: AirflowOptions,
        ports: Optional[List[ContainerPort]] = None,
        readiness_probe: Optional[Probe] = None,
    ):
        values = ValueOrchestrator()
        self._sql_options = sql_options
        self._redis_options = redis_options
        self._airflow_options = airflow_options
        super().__init__(
            name=name,
            args=[name],
            image="airflow-image",
            image_pull_policy="Never",
            env=self._get_environment(),
            env_from=[
                EnvFromSource(
                    None, None, SecretEnvSource(values.secret_name, optional=False)
                )
            ],
            ports=ports,
            volume_mounts=self._get_volume_mounts(),
            readiness_probe=readiness_probe,
            command=["/entrypoint.sh"],
        )

    def _get_volume_mounts(self):
        return [
            AirflowLogVolumeGroup(self._airflow_options).volume_mount,
            AirflowDagVolumeGroup(self._airflow_options).volume_mount,
            ExternalStorageVolumeGroup(self._airflow_options).volume_mount,
        ]

    def _get_environment(self):
        env = (
            self._get_kubernetes_env()
            + self._get_airflow_env()
            + self._airflow_options.extra_env_vars
        )
        return env

    def _get_airflow_env(self):
        return [
            CoreEnvVar("EXECUTOR", self._airflow_options.core_executor),
            CoreEnvVar("DEFAULT_TIMEZONE", self._airflow_options.default_time_zone,),
            CoreEnvVar("LOAD_DEFAULT_CONNECTIONS", "False"),
            CoreEnvVar("LOAD_EXAMPLES", "False"),
            CoreEnvVar(
                "DAGS_ARE_PAUSED_AT_CREATION",
                str(self._airflow_options.dags_paused_at_creation),
            ),
        ]

    def _get_kubernetes_env(self):
        return [
            EnvVar("AIRFLOW__KUBERNETES__NAMESPACE", self._airflow_options.namespace),
            EnvVar(
                "AIRFLOW__KUBERNETES__DAGS_VOLUME_CLAIM",
                AirflowDagVolumeGroup(
                    self._airflow_options
                ).persistent_volume_claim.metadata.name,
            ),
            EnvVar(
                "AIRFLOW__KUBERNETES__LOGS_VOLUME_CLAIM",
                AirflowLogVolumeGroup(
                    self._airflow_options
                ).persistent_volume_claim.metadata.name,
            ),
            EnvVar(
                "AIRFLOW__KUBERNETES__WORKER_CONTAINER_REPOSITORY",
                self._airflow_options.worker_image,
            ),
            EnvVar(
                "AIRFLOW__KUBERNETES__WORKER_CONTAINER_IMAGE_PULL_POLICY",
                "IfNotPresent",
            ),
            EnvVar(
                "AIRFLOW__KUBERNETES__WORKER_CONTAINER_TAG",
                self._airflow_options.worker_image_tag,
            ),
        ]


class WebserverUI(AirflowContainer):
    def __init__(
        self,
        sql_options: SqlOptions,
        redis_options: RedisOptions,
        airflow_options: AirflowOptions,
    ):
        super().__init__(
            "webserver",
            sql_options,
            redis_options,
            airflow_options,
            ports=[ContainerPort(8080, host_port=8080)],
            readiness_probe=AvionixAirflowProbe("/airflow", 8080, "0.0.0.0"),
        )


class Scheduler(AirflowContainer):
    def __init__(
        self,
        sql_options: SqlOptions,
        redis_options: RedisOptions,
        airflow_options: AirflowOptions,
    ):
        super().__init__(
            "scheduler",
            sql_options,
            redis_options,
            airflow_options,
            [ContainerPort(8125, host_port=8125)],
        )


class FlowerUI(AirflowContainer):
    def __init__(
        self,
        sql_options: SqlOptions,
        redis_options: RedisOptions,
        airflow_options: AirflowOptions,
    ):
        super().__init__(
            "flower",
            sql_options,
            redis_options,
            airflow_options,
            readiness_probe=AvionixAirflowProbe("/flower/", 5555),
        )
```

# Development Environmnent

For development you will need
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) 
- [helm](https://helm.sh/docs/intro/install/)
- [docker](https://docs.docker.com/get-docker/)

# Starting the development environment

Be sure that docker is running, then run the following command
```bash
minikube start --driver=docker
```

## Warnings

Note that you currently cannot use public instance variables if subclassing one of the
 kubernetes components.
 
For example in the above inhertiance example code, this would break the helm output,

```python
class WebserverUI(AirflowContainer):
    def __init__(
        self,
        sql_options: SqlOptions,
        redis_options: RedisOptions,
        airflow_options: AirflowOptions,
    ):
        self.my_personal_variable = "I'm breaking helm!"
        super().__init__(
            "webserver",
            sql_options,
            redis_options,
            airflow_options,
            ports=[ContainerPort(8080, host_port=8080)],
            readiness_probe=AvionixAirflowProbe("/airflow", 8080, "0.0.0.0"),
        )
```