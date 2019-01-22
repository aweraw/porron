import boto3
from botocore.exceptions import ClientError

from response_models import Response, Fail

class S3Object(Response):

    client = boto3.client('s3')

    def __init__(self, bucket: str, key: str):
        try:
            obj = self.client(Bucket=bucket, Key=key)
        except ClientError as e:
            message = e.response['Error']['Code']
            code = e.response['HTTPStatusCode']
            raise Fail("{}: {}/{}".format(message, bucket, key), code)

        super(S3Object, self).__init__(obj['Body'].read())

        self.set_content_type(obj['ContentType'])
