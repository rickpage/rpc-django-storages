AWS_S3_ACCESS_KEY_ID = 'Get this from Amazon'
AWS_S3_SECRET_ACCESS_KEY = 'This as well'
AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'

# TODO Watch out we dont really need or want static yet
# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'base.storages.MediaStorage'
