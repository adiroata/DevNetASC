from ncclient import manager
from devnet_sandbox import devnet_sandbox

devnet_connection = manager.connect(
    host=devnet_sandbox["HOST"],
    port=devnet_sandbox["PORT"],
    username=devnet_sandbox["USERNAME"],
    password=devnet_sandbox["PASSWORD"],
    hostkey_verify=False,
    # I set the below args to 'False' to avoid "SSHException('No existing session')" error.
    allow_agent=False,
    look_for_keys=False
    )