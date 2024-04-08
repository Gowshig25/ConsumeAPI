import boto3
s3=boto3.client('s3')
s3.delete_object(Bucket='boto3buck',Key='Product_data.xlsx')
s3.upload_file('C:/JavaProgramming/ConsumingAPI/resources/excel/product_data.xlsx','boto3buck','Product_data.xlsx')