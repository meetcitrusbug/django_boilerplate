# """
# Define generic AWS functions here.
# """

# import logging

# import boto3
# from botocore.exceptions import ClientError
# from django.conf import settings


# def boto_s3_client():
#     """This method is used to create a client of S3"""
#     client = boto3.client(
#         's3',
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=settings.AWS_S3_REGION_NAME
#     )
#     return client


# def boto_elastic_transcoder_client():
#     """This method is used to create a client of Elastic Transcoder"""
#     client = boto3.client(
#         'elastictranscoder',
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=settings.AWS_S3_REGION_NAME
#     )
#     return client


# def boto_s3_delete_image_object(client, obj):
#     """This method is used to delete an object of S3"""
#     response = client.delete_object(
#         Bucket=settings.AWS_STORAGE_BUCKET_NAME,
#         Key=obj.image.split('.com/')[1],
#     )
#     return response


# def boto_s3_update_image_object(client, img_name, obj):
#     """This method is used to update an object of S3"""
#     response = client.put_object(
#         Body=img_name,
#         Bucket=settings.AWS_STORAGE_BUCKET_NAME,
#         Key=obj.image.split('.com/')[1],
#     )
#     return response


# def create_presigned_url(bucket_name, object_name, expiration=21600):
#     """
#     Generate a presigned URL to share an S3 object

#     :param bucket_name: string
#     :param object_name: string
#     :param expiration: Time in seconds for the pre-signed URL to remain valid
#     :return: Pre-signed URL as string. If error, returns None.
#     """

#     # Generate a presigned URL for the S3 object
#     s3_client = boto3.client(
#         's3',
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=settings.AWS_S3_REGION_NAME
#     )
#     try:
#         response = s3_client.generate_presigned_url('get_object',
#                                                     Params={'Bucket': bucket_name, 'Key': object_name},
#                                                     ExpiresIn=expiration)
#     except ClientError as e:
#         logging.error(e)
#         return None

#     # The response contains the pre-signed URL
#     return response
