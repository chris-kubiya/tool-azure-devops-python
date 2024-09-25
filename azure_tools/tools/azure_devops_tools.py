from kubiya_sdk.tools import Arg
from .base import AzureCliTool
from kubiya_sdk.tools.registry import tool_registry

az_devops = AzureCliTool(
    name="az_devops",
    description="Logs in to Azure DevOps CLI and then runs the specified `devops` group command.",
    content="az devops {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Azure DevOps CLI `devops` group command to run (example: `project`). Do not add
                `az devops` at the front.
            """,
            required=True),
    ],
)

az_pipelines = AzureCliTool(
    name="az_pipelines",
    description="""
        Logs in to Azure DevOps CLI and then runs the specified `pipelines` group command.
        """,
    content="az pipelines {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Azure DevOps CLI `pipelines` group command to run (example: `build`). Do not
                add `az pipelines` at the front.
                """,
            required=True),
    ],
)

az_artifacts = AzureCliTool(
    name="az_artifacts",
    description="""
        Logs in to Azure DevOps CLI and then runs the specified `artifacts` group command.
        """,
    content="az artifacts {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Azure DevOps CLI `artifacts` group command to run (example: `universal`). Do not
                add `az artifacts` at the front.
            """,
            required=True),
    ],
)

az_boards = AzureCliTool(
    name="az_boards",
    description="Logs in to Azure DevOps CLI and then runs the specified `boards` group command.",
    content="az boards {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Azure DevOps CLI `boards` group command to run (example: `work-item`). Do not
                add `az boards` at the front.
            """,
            required=True),
    ],
)

az_repos = AzureCliTool(
    name="az_repos",
    description="Logs in to Azure DevOps CLI and then runs the specified `repos` group command.",
    content="az repos {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Azure DevOps CLI `repos` group command to run (example: `create`). Do not add
                `az repos` at the front.
            """,
            required=True),
    ],
)

tool_registry.register("Azure", az_devops)
tool_registry.register("Azure", az_pipelines)
tool_registry.register("Azure", az_artifacts)
tool_registry.register("Azure", az_boards)
tool_registry.register("Azure", az_repos)
