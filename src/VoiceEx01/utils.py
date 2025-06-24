import os
from azure.storage.blob import ContainerClient

def get_container_client_from_sas(sas_uri):
    """Get a container client directly from a container SAS URI."""
    return ContainerClient.from_container_url(sas_uri)

def download_blobs(container_client, prefix=None, suffix=None, local_folder="downloads"):
    """Download all blobs from a container with an optional prefix."""
    os.makedirs(local_folder, exist_ok=True)
    
    downloaded_files = []
    blob_list = list(container_client.list_blobs(
        name_starts_with=prefix if prefix else "", 
        name_ends_with=suffix if suffix else ""
    ))
    
    print(f"Found {len(blob_list)} blobs to download")
    
    for blob in blob_list:
        local_file_path = os.path.join(local_folder, os.path.basename(blob.name))
        print(f"Downloading {blob.name} to {local_file_path}")
        
        with open(local_file_path, "wb") as file:
            blob_data = container_client.download_blob(blob.name)
            file.write(blob_data.readall())
        
        downloaded_files.append({
            "blob_name": blob.name,
            "local_path": local_file_path
        })
    
    return downloaded_files

def upload_files(container_client, local_file_paths, folder=None):
    """Upload multiple files to the specified container."""

    uploaded_files = []

    for local_file_path in local_file_paths:
        file_name = os.path.basename(local_file_path)
        if folder:
            blob_name = f"{folder}/{file_name}"
        else:
            blob_name = file_name 

        print(f"Uploading {local_file_path}")
        with open(local_file_path, "rb") as data:
            container_client.upload_blob(
                name=blob_name, 
                data=data, 
                overwrite=True
            )

        uploaded_files.append(blob_name)

    return uploaded_files
