from google.cloud import secretmanager
import os
import shutil

def access_secret_version(project_id, secret_id, version_id='latest'):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    payload = response.payload.data.decode("UTF-8")
    print("Plaintext: {}".format(payload))

    # ファイル移動の検証
    shutil.copyfile('./sample.ini', '/tmp/copied_sample.ini') # /tmpへコピー
    shutil.move('./sample.ini', '/tmp') # 元ファイルを移動
    os.remove('/tmp/sample.ini') # 元ファイルを削除
    os.rename('/tmp/copied_sample.ini', '/tmp/sample.ini') # コピーしたファイル名を元ファイルと同じに
    shutil.move('/tmp/sample.ini', __file__) # コピーしたファイルを移動

def get_credential(event, context):
    GCP_PROJECT = os.getenv('GCP_PROJECT')
    SECRET_ID = os.getenv('SECRET_ID')

    access_secret_version(GCP_PROJECT, SECRET_ID)
