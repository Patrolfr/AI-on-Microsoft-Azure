# Azure Cognitive vision Services

The Face API provides features exposed as REST API that perform different analysis against given images containg faces. These features can be splitted into five categories:

- Verification: Check the likelihood that two faces belong to the same person.
- Detection: Detect human faces in an image.
- Identification: Search and identify faces. (Compare face to a persin group.)
- Similarity: Find similar faces. (Compare target face against face list)
- Grouping: Organize unidentified faces into groups, based on their visual similarity.

Algorithms base their conditions on so called face landmarks, which are a collection of detailed points on a face.

- Attributes
The Face API can identify and return following metrics based on face picture: 
Age, Gender, Smile intensity, Facial hair, Head pose, Emotion.



# Computer Vision service

Computer Vision API offers analysis of images. It has many features, containing drawing insights from images, extract text from images and generate high-quality thumbnails. It also has other features like estimating dominant and accent colors, categorizing the content of images, and describing an image with complete English sentences.

You can supply the image to be processed either as a raw image binary or an image URL.

Sample applications of the Computer Vision API (and corresponding resource type):

- Analyze images for insight (analyze)
- Extract printed text from images using optical character recognition (ocr)
- Recognize printed and handwritten text from images (recognizeText)
- Recognize celebrities and landmarks (analyze | describe)
- Analyze video
- Generate a thumbnail of an image (generateThumbnail)

Other resources: describe, models, tag.


# The Microsoft Custom Vision 

Service purpose is to create image classification models that "learn" from provided images. After training the model can be examined by REST API. Image to test can be profided as application/octet-stream or by direct url in body (application/json).
The Azure Custom Vision cognitive service combines artificial intelligence and machine learning to provide a sophisticated image classification and detection service.

There are two Project Types available:
- Classification
- Object Detection

Two classification types:
- Multilabel (Multiple tags per image)
- Multiclass (Single tag per image)

There is 4 basic domains:
- General
- Food
- Landmarks
- Retail



# Video Indexer service

You can use Video Indexer API to upload, index, retrieve insights, and search for content in video files.

Azure Video Indexer is a service to extract insights from media. It uses machine learning models that can be further customized and trained. The video insights include face identification, text recognition, object labels, scene segmentations, and more.

