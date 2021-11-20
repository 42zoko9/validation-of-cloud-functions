# validation-of-cloud-functions
cloud functionosの検証  

## Usage
事前にcloud functionsとsecret managerを取り扱う権限を持ったサービスアカウントを用意する

デプロイ用のコマンド  
```
gcloud functions deploy デプロイ名 \
    --entry-point 実行するmain.pyの関数 \
    --region asia-northeast1 \
    --runtime python37 \
    --memory 128MB \
    --trigger-resource 任意のトピック \
    --trigger-event google.pubsub.topic.publish \
    --service-account cloudfunctionsとsecretmanagerのaccess権限を持ったサービスアカウント \
    --set-env-vars SECRET_ID=呼び出すシークレット名
```

## Reference
- [Python Client for Secret Manager API](https://googleapis.dev/python/secretmanager/latest/index.html)
- [Python Client for Secret Manager API (Beta)](https://googleapis.dev/python/secretmanager/0.1.1/index.html)
- [Secret Manager に保存した機密情報を、Cloud Functions の Python コードから取得してみた。](https://dev.classmethod.jp/articles/secret-manager-access-from-cloudfunctions-python/)
- [Secret Managerの使い方](https://mahito.hatenablog.com/entry/2020/06/16/093140)