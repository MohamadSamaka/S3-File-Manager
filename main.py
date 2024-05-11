from s3_manger import S3FileManager

if __name__ == "main":
    bucket_name = 'bucket-name'
    source_prefix = 'customer-details/sr1_'
    destination_prefix = 'sr1/'
    sns_topic_arn = 'your-sns-topic-arn'

    manager = S3FileManager(bucket_name, source_prefix, destination_prefix, sns_topic_arn)
    manager.move_files()