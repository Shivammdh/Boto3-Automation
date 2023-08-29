import os,sys
try:
    import boto3
    print("Successfully imported")
except Exception as e:
    print(e)
    sys.exit(1)
source_region="us-east-1"
dest_region="us-east-2"
session=boto3.session.Session(profile_name="root")
ec2_source_client=session.client(service_name="ec2",region_name=source_region)
sts_client=session.client(service_name="sts",region_name=source_region)
account_id=sts_client.get_caller_identity().get('Account')
snap_filter={"Name":'tag:backup',"Values":['yes']}
backup_snap=[]
for each_snap in ec2_source_client.describe_snapshots(Filters=[snap_filter],OwnerIds=[account_id]).get('Snapshots'):
    backup_snap.append(each_snap.get('SnapshotId'))
print(backup_snap)
ec2_dest_client=session.client(service_name="ec2",region_name=dest_region)

for bck_snap_id in backup_snap:
    print(f"Taking backup for id of {bck_snap_id} into {dest_region}")
    ec2_dest_client.copy_snapshot(
        Description='Discovery Backup',
        SourceRegion=source_region,
        SourceSnapshotId=bck_snap_id,
    )
print("Successfully backup the snapshots")

for each_snap_id in backup_snap:
    print("Tag are deleted....")
    ec2_source_client.delete_tags(
    Resources=[
        each_snap_id,
    ],
    Tags=[
        {
            'Key': 'backup',
            'Value': 'yes'
        },]
    )
    print("New Tag are created...")
    ec2_source_client.create_tags(
        Resources=[
            each_snap_id,
        ],
        Tags=[
            {
                'Key': 'backup',
                'Value': 'Completed'
            }, ]
    )
