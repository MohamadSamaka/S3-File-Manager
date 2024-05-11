import boto3
import logging

class S3FileManager:
    def __init__(self, bucket_name, source_prefix, destination_prefix, sns_topic_arn):
        self.bucket_name = bucket_name
        self.source_prefix = source_prefix
        self.destination_prefix = destination_prefix
        self.sns_topic_arn = sns_topic_arn
        self.s3_client = boto3.client('s3')
        self.sns_client = boto3.client('sns')

        # Setting up logging
        logging.basicConfig(filename='s3_file_move.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def move_files(self):
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=self.source_prefix)

        if 'Contents' not in response:
            logging.info("No files found to move.")
            return

        for obj in response['Contents']:
            key = obj['Key']

            try:
                # Moving the object to the destination folder
                self.s3_client.copy_object(
                    Bucket=self.bucket_name,
                    CopySource={'Bucket': self.bucket_name, 'Key': key},
                    Key=self.destination_prefix + key.split('/')[-1]
                )

                # Deleting the object from the source folder
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)

                # Log the operation
                logging.info(f"Moved file {key} to {self.destination_prefix} folder and deleted from {self.source_prefix}.")

            except Exception as e:
                logging.error(f"An error occurred while copying/deleting file {key}: {str(e)}")

        self.send_notification()

    def send_notification(self):
        try:
            self.sns_client.publish(
                TopicArn=self.sns_topic_arn,
                Subject='S3 - File Move Notification',
                Message=f'Files have been moved to {self.destination_prefix} folder and deleted from {self.source_prefix}.'
            )
            logging.info('SNS notification sent.')
        except Exception as e:
            logging.error(f"An error occurred while sending SNS notification: {str(e)}")
