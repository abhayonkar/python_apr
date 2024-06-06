import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def create_upload(request):
    # Create the API client
    api_service_name = "youtube"
    api_version = "v3"
    client = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=request.user.credentials)

    # Create the API request
    insert_request = client.videos().insert(
        part="snippet,status,contentDetails",
        body=dict(
            snippet=dict(
                title="Test Video",
                description="Test Video Description",
                tags=["test", "video"]
            ),
            status=dict(
                privacyStatus="private"
            ),
            contentDetails=dict(
                file_size=1234,
                mime_type="video/mp4"
            )
        ),
        media_body=request.FILES['file']
    )

    # Execute the request
    response = insert_request.execute()

    print(response)
