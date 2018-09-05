## rpc django storages
A django project that uses django-storages.

TODO:

The following is demonstrated:

* setting up s3 boto3 via django-storages
* ImageField
* Models using multiple Images
* Captions, titles, and notes on 
**ImageData** model
* Deleting an image from the server when the photo is deleted

There are issues using JSON and DRF to upload a file.

https://stackoverflow.com/questions/28036404/django-rest-framework-upload-image-the-submitted-data-was-not-a-file

The solutions seem based on making an image data form endpoint -
sending the data as **form-data** or **binary** (is this in Postman)

https://stackoverflow.com/questions/26723467/what-is-the-difference-between-form-data-x-www-form-urlencoded-and-raw-in-the-p
"if you have to send non-ASCII text or large binary data, the form-data is for that."


Need something liek this android side

NOW POST THE DATA USING MULTIPART FORM DATA

HttpClient httpclient = new DefaultHttpClient();
HttpPost httppost = new HttpPost("LINK TO SERVER");
Multipart FORM DATA

MultipartEntity mpEntity = new MultipartEntity(HttpMultipartMode.BROWSER_COMPATIBLE);
if (filePath != null) {
    File file = new File(filePath);
    Log.d("EDIT USER PROFILE", "UPLOAD: file length = " + file.length());
    Log.d("EDIT USER PROFILE", "UPLOAD: file exist = " + file.exists());
    mpEntity.addPart("avatar", new FileBody(file, "application/octet"));
}

