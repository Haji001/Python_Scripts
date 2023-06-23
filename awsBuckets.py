import boto3

""" SIMPLE PYTHON-BOTO3 SCRIPT 
TO DO THINGS WITH AWS S3 BUCKET """

def Create_S3_Bucket():

    s3 = boto3.client(aws_secret_access_key_id='aws access keys',
                    aws_access_key_id='aws secret access keys')

    s3 = boto3.resource("s3")

    
    
    bucketName = 'bucket-name'
    region = 'account region'
    response = s3.create_bucket(Bucket=bucketName)

    
    
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print('Bucket is created')
    else:
        print(f"Error: {bucketName} failed.")

    
    
    """ Upload file into the bucket """
    file = '/path/location/filename.txt'
    with open (file, 'rb') as f:
        s3.Bucket(bucketName).uploadfile_obj(f)

    
    """ LIST ALL OBJECTS IN S3 BUCKETS"""
    for objects in s3.Bucket(bucketName).objects.all():
        print(f"Here are the objects:\n{objects}")
    
    
    
    """ DELETE ALL ITEMS IN S3 BUCKETS."""
    for items in s3.Bucket(bucketName).objects.all():
        s = items
        s3.Object(bucketName, s).delete.all()

""" END. """