from kubiya_sdk.tools.models import Tool
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

AZURE_ICON_URL = "https://azure.microsoft.com/svghandler/azure-logo/?width=300&height=300"

# View https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops for Azure DevOps
# details
SCRIPT_LOGIN   = """
az extension add --name azure-devops
az devops login --organization $AZURE_DEVOPS_ORG_URL
az devops configure --defaults organization=$AZURE_DEVOPS_ORG_URL
"""

class AzureCliTool(Tool):
    def __init__(self, name, description, content, args, long_running=False, mermaid_diagram=None):
        # Combine the login and received content into a single script
        full_content = f"{SCRIPT_LOGIN}\n{content}"

        super().__init__(
            name=name,
            description=description,
            icon_url=AZURE_ICON_URL,
            type="docker",
            image="mcr.microsoft.com/azure-cli:latest",
            content=full_content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )

