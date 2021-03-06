import boto3

s3_client = boto3.client('s3',
                         aws_access_key_id='aws_access_key_id',
                         aws_secret_access_key='aws_secret_access_key',
                         region_name='bucked region'
                         )


def uploadFile(file):
    s3_client.put_object(Body=file, Bucket='bucket name',
                         Key='path/filename')
    return True
