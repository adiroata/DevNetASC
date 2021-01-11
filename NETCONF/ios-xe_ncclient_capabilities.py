from devnet_connection import devnet_connection

# Write a function to establish the remote connection and get device capabilities
def get_capabilities():
    for capability in devnet_connection.server_capabilities:
        print(capability)

devnet_connection.close_session()

# Call function
if __name__=='__main__':
    get_capabilities()