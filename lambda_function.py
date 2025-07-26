import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Step 1: Get all EBS snapshots owned by the user
    snapshots_response = ec2.describe_snapshots(OwnerIds=['self'])

    # Step 2: Get all running EC2 instance IDs
    instances_response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    active_instance_ids = set()
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Step 3: Iterate over each snapshot and apply cleanup logic
    for snapshot in snapshots_response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # Case 1: Snapshot not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id}: Not attached to any volume.")
            continue

        try:
            # Case 2: Volume exists
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            volume = volume_response['Volumes'][0]
            attachments = volume.get('Attachments', [])

            if not attachments:
                # Case 2a: Volume is not attached to any instance
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id}: Volume not attached to any instance.")
            else:
                # Case 2b: Volume is attached to an instance, check if the instance is running
                instance_id = attachments[0]['InstanceId']
                if instance_id not in active_instance_ids:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted snapshot {snapshot_id}: Volume attached to non-running instance {instance_id}.")
                else:
                    print(f"Kept snapshot {snapshot_id}: Volume in use by running instance {instance_id}.")

        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                # Case 3: Volume no longer exists
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id}: Volume not found (likely deleted).")
            else:
                print(f"Error checking volume {volume_id}: {e}")
