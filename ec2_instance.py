import boto3


""" Provisioning ec2 instance with python """

def create_ec2(image_id, instance_type, key_name):

    ec2_client = boto3.client('ec2')
    response = ec2_client.run_instances(ImageId=image_id,
                                        InstanceType=instance_type,
                                        KeyName=key_name,
                                        MinCount=1,
                                        MaxCount=1)
    
    
    instance_id = response['Instances'][0]['InstanceID']
    return instance_id

def main():

    image_id = 'ami-adbsihg'
    instance_type = 't2.micro'
    key_name = 'secret-keys.txt'

    instance_id = create_ec2(image_id=image_id, 
                             instance_type=instance_type,
                             key_name=key_name)
    
    print(f"EC2 instance created with instance ID: {instance_id}")


if __name__ == '__main__':
    main()

