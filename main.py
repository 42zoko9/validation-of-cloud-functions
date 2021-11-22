from google.cloud import secretmanager
import os

def access_secret_version(project_id, secret_id, version_id='latest'):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    parent = client.secret_path(project_id, secret_id)
    name = client.secret_version_path(project_id, secret_id, version_id)

    # Access the secret version.
    # NOTE: latestのversionがDISABLEの場合，コケる
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    payload = response.payload.data.decode("UTF-8")
    print("payload : {}".format(payload))

    # List up secret version
    for version in client.list_secret_versions(request={"parent": parent}):
        # NOTE: stateは1: ENABLE, 2: DISABLE, 3: DESTROYを指す
        print("Found secret version: {}, state: {}".format(version.name, version.state))

    # Add the secret payload
    new_payload = str(int(payload) + 1)
    v_response = client.get_secret_version(request={'name': name})
    response = client.disable_secret_version(request={'name': v_response.name})
    response = client.add_secret_version(request = {'parent': parent, 'payload': {'data': new_payload.encode('utf-8')}})

    # Print the new secret version name.
    print('Added secret version: {}'.format(response.name))

def get_credential(event, context):
    GCP_PROJECT = os.getenv('GCP_PROJECT')
    SECRET_ID = os.getenv('SECRET_ID')

    access_secret_version(GCP_PROJECT, SECRET_ID)
