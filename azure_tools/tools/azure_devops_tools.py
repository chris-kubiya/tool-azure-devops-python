from kubiya_sdk.tools import Arg
from .base import AzureCliTool
from kubiya_sdk.tools.registry import tool_registry

az_devops = AzureCliTool(
    name="az_devops",
    description=("""
        Logs in to Azure DevOps CLI and then runs the specified `devops` group command.
        Use the command flag `--help` when needed to determine the correct command to use.
        
        Group:
        - az devops : Manage Azure DevOps organization level operations.
        
        Subgroups:
        - admin            : Manage administration operations.
        - extension        : Manage extensions.
        - project          : Manage team projects.
        - security         : Manage security related operations.
        - service-endpoint : Manage service endpoints/connections.
        - team             : Manage teams.
        - user             : Manage users.
        - wiki             : Manage wikis.
        """),
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
    description=("""
        Logs in to Azure DevOps CLI and then runs the specified `pipelines` group command.
        Use the command flag `--help` when needed to determine the correct command to use.
        
        Group:
        - az pipelines : Manage Azure Pipelines.

        Subgroups:
        - agent          : Manage agents.
        - build          : Manage builds.
        - folder         : Manage folders for organizing pipelines.
        - pool           : Manage agent pools.
        - queue          : Manage agent queues.
        - release        : Manage releases.
        - runs           : Manage pipeline runs.
        - variable       : Manage pipeline variables.
        - variable-group : Manage variable groups.

        Commands:
        - create         : Create a new Azure Pipeline (YAML based).
        - delete         : Delete a pipeline.
        - list           : List pipelines.
        - run            : Queue (run) a pipeline.
        - show           : Get the details of a pipeline.
        - update         : Update a pipeline.
        """),
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
        Use the command flag `--help` when needed to determine the correct command to use.

        Group:
        - az artifacts : Manage Azure Artifacts.

        Subgroups:
        - universal : Manage Universal Packages.
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
    description=("""
        Logs in to Azure DevOps CLI and then runs the specified `boards` group command.
        Use the command flag `--help` when needed to determine the correct command to use.

        Group:
        - az boards : Manage Azure Boards.

        Subgroups:
        - area      : Manage area paths.
        - iteration : Manage iterations.
        - work-item : Manage work items.

        Commands:
        - query     : Query for a list of work items.
        """),
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
    description=("""
        Logs in to Azure DevOps CLI and then runs the specified `repos` group command.
        Use the command flag `--help` when needed to determine the correct command to use.

        Group:
        - az repos : Manage Azure Repos.

        Subgroups:
        - import : Manage Git repositories import.
        - policy : Manage branch policy.
        - pr     : Manage pull requests.
        - ref    : Manage Git references.

        Commands:
        - create : Create a Git repository in a team project.
        - delete : Delete a Git repository in a team project.
        - list   : List Git repositories of a team project.
        - show   : Get the details of a Git repository.
        - update : Update the Git repository.
        """),
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
