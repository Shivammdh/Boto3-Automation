import boto3

aws_session=boto3.session.Session(profile_name="root")
ec2_con=aws_session.client(service_name="ec2",region_name="us-east-1")
all_regions=[]
for each_region in ec2_con.describe_regions()['Regions']:
    all_regions.append(each_region.get('RegionName'))

print(all_regions)
for region_name in all_regions:
    print(f"Create snapshot for rigion {region_name}")
    ec2_cli = aws_session.client(service_name="ec2", region_name=region_name)
    volume_ids = []
    f1 = {'Name': "tag:Prod", 'Values': ['backup', "Backup"]}
    # for each_vol in ec2_cli.describe_volumes(Filters=[f1])["Volumes"]:
    #     volume_ids.append(each_vol['VolumeId'])
    paginator_obj = ec2_cli.get_paginator("describe_volumes")
    for each_page in paginator_obj.paginate(Filters=[f1]):
        for each_volume in each_page['Volumes']:
            volume_ids.append(each_volume['VolumeId'])
    snap_ids = []
    for each_id in volume_ids:
        print(f"Taking Snap of: {each_id}")
        response = ec2_cli.create_snapshot(
            Description='Taking snapshot for each volumes',
            VolumeId=each_id,
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'delete on',
                            'Value': '90 days'
                        },
                    ],
                },
            ],
        )
        snap_ids.append(response['SnapshotId'])

    print(snap_ids)
    if snap_ids:
        # Creating waiter using client
        print("=================Snapshot creating started=================")
        # ec2_cli = aws_session.client(service_name="ec2", region_name="us-east-1")
        waiter = ec2_cli.get_waiter('snapshot_completed')
        waiter.wait(SnapshotIds=snap_ids)
        print(f"Successfully cretae snapshot for {region_name}")
    else:
        continue