from google.oauth2 import service_account
from google.cloud import storage

# set this to your initials
project_id = "dscb230-info"
bucket_name = 'daily-results-dscb230' # replace the bucket name with yours

# the downloaded key filename which you uploaded to this Colab session
key_path = "gcp-key/dscb230-info-4ea2ec6f67df.json"

# create credentials
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# blob download
storage_client = storage.Client(credentials=credentials)

bucket = storage_client.bucket(bucket_name)  
for blob in storage_client.list_blobs(bucket_or_name=bucket_name):
    blob_name = blob.name
    blob = bucket.blob(blob_name=blob_name)
    blob.download_to_filename(f'data/gcp_april_may/{blob_name}')
    

print('Download complete!')
