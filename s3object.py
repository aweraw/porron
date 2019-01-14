import boto3
from botocore.exceptions import ClientError

from response import Response
from response_models import HTTPFail

class S3Object(Response):

    client = boto3.client('s3')

    def __init__(self, bucket, key):
        try:
            obj = self.client(Bucket=bucket, Key=key)
        except ClientError as e:
            message = e.response['Error']['Code']
            code = e.response['HTTPStatusCode']
            raise HTTPFail("{}: {}/{}".format(message, bucket, key), code)

        super(S3Object, self).__init__(obj['Body'].read())

        self.set_content_type(obj['ContentType'])
