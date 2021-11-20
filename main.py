from google.cloud import secretmanager
import os
import shutil

def access_secret_version(project_id, secret_id, version_id='latest'):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    parent_name = client.secret_version_path(project_id, secret_id)
    name = client.secret_version_path(project_id, secret_id, version_id)

    # Access the secret version.
    response = client.access_secret_version(name)

    # Print the secret payload.
    payload = response.payload.data.decode("UTF-8")
    print("Plaintext: {}".format(payload))

    # Update the secret payload
    new_payload = str(int(payload) + 1)
    response = client.destroy_secret_version(name)
    response = client.add_secret_version(parent_name, {'data': new_payload.encode('utf-8')})
    
    # Print the new secret version name.
    print('Added secret version: {}'.format(response.name))

def get_credential(event, context):
    GCP_PROJECT = os.getenv('GCP_PROJECT')
    SECRET_ID = os.getenv('SECRET_ID')

    access_secret_version(GCP_PROJECT, SECRET_ID)
