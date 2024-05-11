# S3 File Manager

This Python project automates the process of moving files within an AWS S3 bucket and sends notifications using AWS SNS. The scripts are part of a system that leverages AWS services to manage S3 file operations efficiently.

## Project Structure

- **se_manager.py**: Contains the `S3FileManager` class responsible for all operations related to moving and deleting files within S3.
- **main.py**: The entry point for running the file operations.
- **keys.py**: Stores AWS credentials securely.
- **create_session.py**: Establishes a session with AWS using credentials from `keys.py`.

## Features

- Move specified files from one directory to another within an S3 bucket.
- Delete the original files after moving.
- Send notifications via SNS after operations are completed.
- Log all operations and errors.

## Setup

### Prerequisites

- AWS account
- Python 3.x
- Boto3 library
- Proper IAM permissions for S3 and SNS operations

### Installation

1. **Clone the repository:**
   git clone https://your-repository-url.git
   cd your-repository-directory

2. **Install required packages:**
   pip install boto3

3. **Configure your AWS credentials in `keys.py`:**
   AWS_ACCESS_KEY_ID = 'your-access-key-id'
   AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
   AWS_SESSION_TOKEN = 'your-session-token'  # if applicable
   AWS_DEFAULT_REGION = 'your-default-region'

4. **Ensure logging directory exists or adjust logging configuration in `se_manager.py` to match your setup.**

## Usage

To use this script to manage your S3 files:

1. **Set up your bucket details and topic ARN in `main.py`:**
   bucket_name = 'your-bucket-name'
   source_prefix = 'your-source-prefix/'
   destination_prefix = 'your-destination-prefix/'
   sns_topic_arn = 'your-sns-topic-arn'

2. **Run the script:**
   python main.py

This will execute the file operations defined and log the process in `s3_file_move.log`.

## Logging

Logs are generated in `s3_file_move.log`, documenting each step taken by the script and any errors that occur.
